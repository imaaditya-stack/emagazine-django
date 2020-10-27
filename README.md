<h1 align="center"> Emagazine </h1> 
Emagazine is an Open Source Web Application Project made for Colleges to use to manage inforamation about different types of events and so in a smart way. Students can able to keep track of upcoming events in the College.

### Tech Stack 🛠️

1. Designing: Html5, CSS3, Bootstarp 4
2. Backend: Python, Django Framework
3. Containerization: Docker
4. Database: SQLite for Development/ PostgreSQL for Production
5. Web Server: Gunicorn for Production / Nginx Proxy Server to serve static files

### Sections 📚

✔️ Events
✔️ Achievements
✔️ Projects

### Clone and use 📋

```
git clone https://github.com/imaaditya-stack/emagazine-django.git
```

### Development

1) Use docker-compose 

```
docker-compose up -d --build
```

2) Create a superuser to access Django admin panel

```
docker-compose exec web python manage.py createsuperuser
```

4) View in browser ( Run in Port 8000 ) 

```
http://localhost:8000/
```

3) If you want to Recreate a fresh container

```
docker-compose down -v
```
```
docker-compose up -d --build
```

### Production

1) Use docker-compose 

```
docker-compose -f docker-compose.prod.yaml up -d --build
```

2) Create a superuser to access Django admin panel

```
docker-compose exec web python manage.py createsuperuser
```

3) Collect Static files so that nginx can serve Static files

```
docker-compose -f docker-compose.prod.yaml exec web python manage.py collectstatic --no-input --clear
```

4) View in browser ( Run in Port 1337 ) 

```
http://localhost:1337/
```
