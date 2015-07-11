# Pyramid Openshift starter
Pyramid Openshift starter is a build based upon:

1. [Openshift] by Red Hat as the server (SaaS).
2. [Postgresql] as database server.
3. [Sqlalchemy] as ORM.
4. [Alembic] as migrations manager.
5. [Pyramid] by Pylons Project as back end framework.
6. [Jinja2] as template engine.
7. [AngularJS] as front end framework.
8. [Bootstrap] as styling framework.
9. [Gulp] as automated tasks handler.

Getting all these ingredients to work together is a tidious task.
The goal is to create a build that can be copied to existing Openshift application, and will also work locally on development machine via Apache web server.

### Prerequisites
* Unix-like OS.
* python => 3.4
* Apache web server => 2.4

Packages (apt-get):
* python-dev
* libffi-dev

**Note**: This build was only tested in Debian Jessie machine. The installer won't work on Windows machine.


### Installation
For advanced users:

* Clone this builder to your machine.
* Delete .git folder in builder folder.
* Inside the build folder, clone openshift newly created app.
* Copy .git from app folder to build folder.
* Delete the app folder.
* Commit and push the changes.

Setting local development machine
* Configure Apache server to point to wsgi.py and serve static files from wsgi/static folder.
* Create virtual python3 environment in build folder
* Install setup.py file to python virtual environment.
* Install requirements.txt via pip from virtual environment.
* Run alembic upgrade to initialize the database.
* Use createuser script (available in the python virtual environment) to create superuser.

***Instead of doing it manually***, I made a small script managing the above instructions.

```sh
$ git clone https://github.com/rotemberger/pyramid_openshift_starter project-local-name
$ cd project-local-name
$ sudo python install.py ssh://somehash@app-domain.rhcloud.com/~/git/project.git/
```
**Note**: sudo is required only for writing Apache project.conf and adding local domain to /etc/hosts file. Check the source code of the installer. It is very short and simple.
**Trust only yourself when running scripts under sudo.**

You can then open browser and type in the url:
```code
http://project-local-name/
```

License
----
MIT

[AngularJS]:http://angularjs.org
[Gulp]:http://gulpjs.com
[Openshift]:https://www.openshift.com
[Pyramid]:http://www.pylonsproject.org
[Postgresql]:http://www.postgresql.org
[Bootstrap]:http://getbootstrap.com/css
[Sqlalchemy]:http://www.sqlalchemy.org
[Alembic]:https://code.google.com/p/alembic/
[Jinja2]:http://jinja.pocoo.org/