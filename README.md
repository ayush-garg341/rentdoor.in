- How to generate migrations ?
    - If we have models.py, then defining app name in INSTALLED_APPS and running the below command will create the one:
        - python3 manage.py makemigrations app_name
    - If we have models folder inside our app and then we have __init__.py and other model files, then we have to mention the name of model in __init__.py and run
        - python3 manage.py makemigrations app_name

- To generate the corresponding SQL from migrations, we can run the below command
    - python manage.py sqlmigrate app_name <migration_file_name_without_py>

- To get django models out of SQL tables
    - python manage.py inspectdb

- If there is an issue related to mysqlclient while installing and running django app, try to change the python version to >= 3.10

- When setting and deploying the app for the first time, need to follow below steps
    - Run `python manage.py migrate` to migrate django admin user model migrations.
    - Then run all the sql statements present in `setup/mysql/create_db.sql` inside mysql container

- Generate certificate using letsencrypt
    - First of all stop nginx server if it's already running
    - Now generate ssl for domain using below commands
        - docker-compose run --rm certbot certonly --webroot --webroot-path /var/www/certbot/ --dry-run -d housedoor.in
        - docker-compose run --rm certbot certonly --webroot --webroot-path /var/www/certbot/ -d housedoor.in
    - The above two commands will create necessary folders, now reload nginx
        - docker-compose restart
    - If you cannot afford the downtime the command above causes, execute the command below:
        - docker-compose exec nginx_rentdoor nginx -s reload
    - Renew Certificates
        - Let's Encrypt certificates last for three months, after which it is necessary to renew them:-
            - docker-compose run --rm certbot renew
        - Setup a cronjob for this, to renew automatically
