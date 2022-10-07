- .env, .env.template 파일은 COPY로 안들어가나?
- 이 파일들은 docker-compose.yml에서 처리하네. 
- Container안에서 env명령어 치면 나온드아. 이 파일 위치가 좀 헷갈림.


```bash
# execute in backend Container
alembic revision -m "create_main_tables"

# 수정 후
alembic upgrade head
```


```text
Here's a few psql commands that can be useful:

\l - list all databases
\d+ - list all tables (relations) in the current database
\c postgres - connect to the postgres database
\d cleanings - describe the cleanings table and the associated columns
```