# drf-bootcamp-geek-uni
Python Django Rest Framework Bootcamp by Geek University from Udemy

This Bootcamp is intended to be a Recap for Django REST Framework where the topics are like:

- Create simple and also customized CRUD
- Utilize authentication
- Utilize permissions
- Utlize resquests limitations
- Utlize pagination
- Utilize API's test
- and so on...

## Console's input commands:

- $ python3 -m venv venv
- $ source venv/bin/activate
- $ django-admin startproject escola .
- $ django-admin startapp cursos
- $ python manage.py runserver
- $ python manage.py createsuperuser
- $ python manage.py makemigrations
- $ python manage.py migrate
- $ pip install -r requirements.txt
- $ python manage.py shell (
    - >>> from rest_framework.renderers import JSONRenderer
    - >>> from cursos.models import Curso
    - >>> from cursos.serializers import CursoSerializers
    - >>> curso = Curso.objects.latest('id')
    - >>> curso
    - >>> curso.titulo
    - >>> serializer = CursoSerializer(curso)
    - >>> serializer
    - >>> type(serializer)
    - >>> dir(serializer)
    - >>> serializer.data
    - >>> type(serializer.data)
    - >>> JSONRenderer()render(serializer.data)
)