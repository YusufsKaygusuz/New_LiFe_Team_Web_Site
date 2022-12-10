# New_LiFe_Team_Web_Site


## Installation
```bash
docker-compose -f local.yml up
```

### Create super user ( admin )
#### You need to run docker to create admin user ( First command )
```bash
docker-compose -f local.yml run django python manage.py createsuperuser
```

### You can check 127.0.0.1:8000 or 0.0.0.0:8000

### Admin panel url path is 127.0.0.1:8000/admin BUT THIS IS JUST FOR DEBUG MODE
