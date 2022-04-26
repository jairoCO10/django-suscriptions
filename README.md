# soil study api

creamos un entorno virtual en python
para ello instalamos virtualenv

```sh
pip install virtualenv
```

creamos el entorno

```sh
python -m virtualenv env
```
activamos el entorno virtual 
```sh
env/Scritp/activate
```
instalamos las dependencias
```sh
pip install -r requirements.txt
```

hacemos las migraciones
```sh
python manage.py makemigrations
python manage.py migrate
```
creamos el superusuario
```sh
python manage.py createsuperuser
```
y lo corremos con el comando 
```sh
python manage.py runserver
```
