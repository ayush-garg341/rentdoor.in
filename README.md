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
