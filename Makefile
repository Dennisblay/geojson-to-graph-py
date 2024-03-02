include .env
export


run:
	python3 main.py

postgres:
	 docker run --name $(PG_CONTAINER_NAME) -p $(PG_PORT_M5430APPING) -e POSTGRES_PASSWORD=$(PGPASSWORD) -e POSTGRES_USER=$(PGUSER) -d postgres:13.14-alpine3.19
#	 docker start $(DB_CONTAINER_NAME)

createdb:
	 docker exec -it $(PG_CONTAINER_NAME) createdb --username=$(PGUSER) --owner=$(PGUSER) $(PGDATABASE)

dropdb:
	 docker exec -it $(PG_CONTAINER_NAME) dropdb $(PGDATABASE) --username=$(PGUSER)


generate:
	npx pgtyped -c config.json

migrate_up:
	migrate -path ./src/database/sql/migrations -database "$(DATABASE_URL)" -verbose up


migrate_down:
	migrate -path ./src/database/sql/migrations -database "$(DATABASE_URL)" -verbose down

restart_db:
	$(MAKE) migrate_down
	$(MAKE) migrate_up

shuv:
	git add .
	git commit -a
	git push

migrate:
	ts-node ./src/database/migrate.ts

.PHONY: down, up, up-prod, server, createdb, dropdb, migrate_up, migrate_down, restart_db, generate
