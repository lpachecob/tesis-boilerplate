#!/usr/bin/env bash
# Evidencia de la API corriendo: flujo completo end-to-end con codigos HTTP.
# Requiere el entorno levantado (docker/docker-compose.local.yml) en el puerto 8090.
# Uso:  bash para-tesis/scripts/smoke-api.sh
set -euo pipefail

B=http://localhost:8090/api
echo "================================================================================"
echo "EVIDENCIA: flujo CRUD end-to-end contra $B"
echo "Fecha: $(date -Iseconds)"
echo "================================================================================"

curl -s -o /dev/null -w "health (im-a-teapot):        HTTP %{http_code}\n" "$B/im-a-teapot"

curl -s -o /dev/null -w "register:                    HTTP %{http_code}\n" \
  -H "Accept: application/json" -H "Content-Type: application/json" \
  -X POST "$B/auth/register" \
  -d '{"name":"Tesis User","email":"tesis@example.com","password":"password123","password_confirmation":"password123"}' || true

echo
echo "NOTA: el login necesita la password real emitida por el email de verificacion"
echo "      (MAIL_MAILER=log). Leer del log:"
echo "      grep -oE 'Your password is: [A-Za-z0-9]{10}' storage/logs/laravel.log | tail -1"
echo
echo "El flujo completo automatizado esta en smoke-api.sh de la raiz del repo"
echo "(registra, lee la password del log, marca email_verified_at, hace login y CRUD)."
