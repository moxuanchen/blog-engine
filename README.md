# blog-engine
My awesome blog engine...

# Before the first run
$ python manage.py shell
>>> from core.models import db
>>> db.create_all()
