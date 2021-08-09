# sayollo
Test task for Sayollo.

Project is set up using Django, Postgres and Redis. I chose to use nosql db as it fits well for task of keeping track of number of visits for multiple users.
Project makes use of docker and docker-compose.

project does not make use of database, but if you want to set up database run project with <h6>docker-compose up</h6> and run migrations in separate tab with 
<h6>docker exec -it sayollo_backend python manage.py migrate</h6>

