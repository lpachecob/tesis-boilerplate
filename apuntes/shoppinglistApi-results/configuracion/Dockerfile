FROM php:7.4-apache

# set the application folder as env variable
ENV APP_HOME /var/www/html

# Debian bullseye is EOL: deb.debian.org dropped the bullseye-security pool
# files (404 on every package), so point apt at the permanent archive.
RUN printf 'deb http://archive.debian.org/debian bullseye main\n\
deb http://archive.debian.org/debian-security bullseye-security main\n\
deb http://archive.debian.org/debian bullseye-updates main\n' > /etc/apt/sources.list \
    && echo 'Acquire::Check-Valid-Until "false";' > /etc/apt/apt.conf.d/99no-check-valid-until

# Install system dependencies
# Node 14 from NodeSource is EOL and its repos are gone; Debian bullseye ships
# Node 12, which is sufficient for laravel-mix 5.
RUN apt-get update && apt-get install -y \
    libzip-dev \
    libpng-dev \
    libonig-dev \
    libxml2-dev \
    nodejs \
    npm && apt-get clean && rm -rf /var/lib/apt/lists/*

# Clear cache
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Install PHP extensions
RUN docker-php-ext-install \
    zip \
    bcmath \
    pdo_mysql \
    intl \
    pcntl \
    opcache \
    exif \
    gd

# Get latest Composer
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

# change uid/gid of apache to docker user
RUN usermod -u 1000 www-data && groupmod -g 1000 www-data

# change the web_root to /var/www/html/public
RUN sed -i -e "s/html/html\/public/g" /etc/apache2/sites-enabled/000-default.conf

# enable apache module rewrite
RUN a2enmod rewrite

# copy source files and run composer
COPY . $APP_HOME

# Get init data
COPY docker/root /
RUN chmod a+x /usr/local/bin/init-shoppinglist.sh

# Install dependencies
RUN composer install --optimize-autoloader --no-dev
RUN npm install

# change ownership of our applications
RUN chown -R www-data:www-data $APP_HOME

ENTRYPOINT /usr/local/bin/init-shoppinglist.sh
