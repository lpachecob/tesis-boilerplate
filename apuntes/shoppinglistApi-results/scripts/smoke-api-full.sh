#!/usr/bin/env bash
# Full smoke test of the ShoppinglistApi (Laravel 7 / MVC pre-test).
# Reproduces: register -> login -> CRUD, capturing the real workflow quirks.
#
# Usage: ./smoke-api.sh [BASE_URL]   (default http://localhost:8090/api)
set -uo pipefail

B="${1:-http://localhost:8090/api}"
COMPOSE="docker compose -f docker/docker-compose.local.yml"
EMAIL="tesis@example.com"
OUT=/tmp/opencode/smoke

mkdir -p "$OUT"

echo "### 0. Clean user"
$COMPOSE exec -T db bash -c \
  "mysql -ushoppinglist -p9ffe1b01f6dea4aa3c183b5c shoppinglist -e \"DELETE FROM users WHERE email='$EMAIL';\"" 2>/dev/null

echo "### 1. Register (HTTP 201)"
$COMPOSE exec -T app bash -c ": > storage/logs/laravel.log"
curl -s -o /dev/null -w "  register: HTTP %{http_code}\n" -X POST "$B/auth/register" \
  -H 'Accept: application/json' -H 'Content-Type: application/json' \
  -d "{\"name\":\"Tesis User\",\"email\":\"$EMAIL\",\"password\":\"password123\",\"password_confirmation\":\"password123\"}"

# QUIRK: the repo's VerifyEmail notification REPLACES the password with a random
# 10-char string and mails it. With MAIL_MAILER=log we read it back from the log.
PASSWORD=$($COMPOSE exec -T app bash -c \
  "grep -oE 'Your password is: [A-Za-z0-9]{10}' storage/logs/laravel.log | tail -1 | awk '{print \$NF}'" | tr -d '\r')
echo "### 2. Password assigned by the verification email: $PASSWORD"

echo "### 3. Mark email verified (business routes require the 'verified' middleware)"
$COMPOSE exec -T db bash -c \
  "mysql -ushoppinglist -p9ffe1b01f6dea4aa3c183b5c shoppinglist -e \"UPDATE users SET email_verified_at=NOW() WHERE email='$EMAIL';\"" 2>/dev/null

echo "### 4. Login -> token"
TOKEN=$(curl -s -X POST "$B/auth/token" -H 'Accept: application/json' -H 'Content-Type: application/json' \
  -d "{\"email\":\"$EMAIL\",\"password\":\"$PASSWORD\",\"device_name\":\"smoke\"}" \
  | grep -oE '"token":"[^"]*"' | cut -d'"' -f4)
[ -z "$TOKEN" ] && { echo "  LOGIN FAILED"; exit 1; }
echo "  token: ${TOKEN:0:20}..."
echo "$TOKEN" > "$OUT/token.txt"

AUTH=(-H "Accept: application/json" -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json")

echo "### 5. GET /user"
curl -s "${AUTH[@]}" -w "  GET user: HTTP %{http_code}\n" "$B/user" -o "$OUT/user.json"

echo "### 6. POST /shopping-lists"
LIST_ID=$(curl -s "${AUTH[@]}" -X POST "$B/shopping-lists" -d '{"name":"Lista Tesis"}' \
  | grep -oE '"id":[0-9]+' | cut -d: -f2)
echo "  created list id=$LIST_ID"

echo "### 7. POST nested item (requires done + creator_email)"
curl -s -o /dev/null -w "  POST item: HTTP %{http_code}\n" "${AUTH[@]}" \
  -X POST "$B/shopping-lists/$LIST_ID/items" \
  -d "{\"product_name\":\"Leche\",\"amount\":2,\"unit_name\":\"litros\",\"done\":false,\"creator_email\":\"$EMAIL\"}"

echo "### 8. POST /products"
curl -s -o /dev/null -w "  POST product: HTTP %{http_code}\n" "${AUTH[@]}" \
  -X POST "$B/products" -d '{"name":"Leche Entera"}'

echo "### 9. GET /units"
curl -s "${AUTH[@]}" -w "  GET units: HTTP %{http_code}\n" "$B/units" -o "$OUT/units.json"

echo "### 10. PUT /shopping-lists/{id}"
curl -s -o /dev/null -w "  PUT list: HTTP %{http_code}\n" "${AUTH[@]}" \
  -X PUT "$B/shopping-lists/$LIST_ID" -d '{"name":"Lista Tesis Editada"}'

echo "### 11. DELETE list"
curl -s -o /dev/null -w "  DELETE list: HTTP %{http_code}\n" "${AUTH[@]}" \
  -X DELETE "$B/shopping-lists/$LIST_ID"

echo "### Done. Raw outputs in $OUT/"
