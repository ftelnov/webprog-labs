CONTAINER_NAME := mysql-tst
DB_USER := username
DB_PASSWORD := password
DB_NAME := feedback-task

create-db:
	docker run --detach --name $(CONTAINER_NAME) --env MYSQL_DATABASE=$(DB_NAME) --env MYSQL_USER=$(DB_USER) --env MYSQL_PASSWORD=$(DB_PASSWORD) --env MYSQL_ROOT_PASSWORD=$(DB_PASSWORD) -p 18383:3808 mysql:latest --port 3808

rm-db:
	docker stop $(CONTAINER_NAME)
	docker rm $(CONTAINER_NAME)

