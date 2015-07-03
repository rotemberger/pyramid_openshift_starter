# Pyramid Openshift starter
Pyramid Openshift starter is a build based upon:

1. [Openshift] by Red Hat as the server (SaaS).
2. [Postgresql] as database server.
3. [Sqlalchemy] as ORM.
4. [Alembic] as migrations manager.
5. [Pyramid] by Pylons Project as back end framework.
6. [AngularJS] as front end framework.
7. [Bootstrap] as styling framework.
8. [Gulp] as automated tasks handler.

Getting all these ingredients to work together is a tidious task.
The goal is to create a build that can be copied to existing Openshift application, and will also work locally on development machine via Apache web server.

### Installation
For advanced users:
* Clone your Openshift new app
* Merge this build as a remote branch.
* Configure Apache server to point to wsgi.py and serve static files from wsgi/static folder.
* Create virtual python3 environment and activate it
* Install setup.py file.
* Install requirements.txt via pip.
* Run alembic upgrade to initialize the database.
* Use createuser script (available in the activated python environment) to create superuser.
* Add "alembic upgrade head" command to .openshift action_hooks.

***Instead of doing it manually***, I made a small script managing the above instructions.

The installer is provided in [Pyramid Openshift starter installer]:
```sh
$ git clone https://github.com/rotemberger/pyramid_openshift_starter_installer installer
$ cd installer
$ sudo python install.py ssh://somehash@app-domain.rhcloud.com/~/git/project.git/ project-local-name owner-user owner-group
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
[Pyramid Openshift starter installer]:https://github.com/rotemberger/pyramid_openshift_starter_installer
[Sqlalchemy]:http://www.sqlalchemy.org
[Alembic]:https://code.google.com/p/alembic/