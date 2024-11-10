# Usage

## Run
```
docker-compose up --build -d
```
it runs in dev mode 


## Containers Management
* Django container
    ```bash
    docker exec -it hackaton-prep-web-1 bash
    ```
    * Inside of Django bash
        ```bash
        python manage.py makemigrations --empty todo
        python manage.py createsuperuser
        python manage.py changepassword
        ```
* PostgreSQL container
    ```bash
    docker exec -it hackaton-prep-db-1 bash
    ```
    * Inside of PostgreSQL bash:
        ```
        psql -U myuser -d mydatabase
        ```
        * Inside of psql cmd:
            ```
            \dt
            ```

## Useful commands
...
