
# Instructions

1. Copy `.env.example` to `.env` and modify the values
2. Run `docker-compose up` to build and start the containers
3. In the root folder of the project, open another terminal and run `docker-compose exec app python manage.py migrate` to run migrations
4. Access `http://localhost:8000/posts/` and test the endpoints
