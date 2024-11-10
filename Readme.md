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
    docker exec -it hackaton-prep-web-1 python manage.py shell
    ```
    * Inside of Django bash
        ```bash
        python manage.py shell
        python manage.py makemigrations --empty todo
        python manage.py createsuperuser
        python manage.py changepassword
        ```
        * Database management through `python manage.py shell` example: https://docs.djangoproject.com/en/5.1/intro/tutorial02/
            ```python
            from polls.models import Choice, Question
            Question.objects.all()
            q = Question(question_text="What's new?", pub_date=timezone.now())
            q.save()
            q = Question.objects.get(pk=1)
            q.choice_set.all()
            c = q.choice_set.create(choice_text="Just hacking again", votes=0)
            c.question
            q.choice_set.all()
            ```
* PostgreSQL container
    ```bash
    docker exec -it hackaton-prep-db-1 bash
    docker exec -it hackaton-prep-db-1 psql -U myuser -d mydatabase
    ```
    * Inside of PostgreSQL bash:
        ```
        psql -U myuser -d mydatabase
        ```
        * Inside of psql cmd:
            ```sql
            \dt
            select * from polls_question;
            ```

## Useful commands
...
