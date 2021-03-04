1. list out all the virtual env packages: pip freeze

2. to see all django commands: django-admin help

3. we can get gitignore file from: https://www.toptal.com/developers/gitignore

4. install autopep8 in the venv with: pip install autopep8

5. we will create seperate urls.py file for each app.

6. the static contents of the site will be kept within the main project directory by creating a static named directory. Mostly css, js, webfonts and lightbox(if used) and img which are not inputed from server.

7. set STATIC_ROOT=os.path.join(BASE_DIR, 'assets') and STATICFILES_DIRS=[
    os.path.join(BASE_DIR, 'treesfarm/static')
] and run command: python manage.py collectstatic. As a result the static files inside the treesfarm directory will be created outside of the directory for global use. 

8. we have to gitignore the assets directory now. 
9. we will create the partials dir for navbar, sidebar, footer, topbar....
10. we have to create other required apps 
11. then have to install psycopg2 for postgres.
12. to work with images we must need to install pillow
13. to check the sql of a model after migrations: python manage.py sqlmigrate listings 0001
14. Inorder to change the styling of admin panel in django we will create a dir in templates called admin. Then we will create a base_site.html file. Then extends admin\base.html
15. Don't filter on a ForeignKey field itself in admin search.
16. pip install pylint-django and add in vscode settings "python.linting.pylintArgs": [
     "--load-plugins=pylint_django"
]," for removing dependency error with files. 

17. to add comma in the long int fields we can add 'django.contrib.humanize' in the settings.py file. and load it in the desired files. For more: "https://docs.djangoproject.com/en/3.1/ref/contrib/humanize/"