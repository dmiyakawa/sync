# About this project

Something like an "echo" server with HTTP access.
When user accesses http://example.com/sync/hogehoge,
The user will obtain hogehoge for HTTP Response.

No security consideration.

# How to install

For Apache. Again, no security consideration.

> sudo chgrp www-data data
> sudo chmod 770 data
> ./manage.py syncdb
..
> sudo chgrp www-data data/sqlite3db
> sudo chmod 660 data/sqlite3db

(configure apache config)

    (For 2.2)
    WSGIScriptAlias /sync /opt/sync/sync/wsgi.py
    <Directory /opt/sync/sync>
        <Files wsgi.py>
            Order deny,allow
            Allow from all
        </Files>
    </Directory>

    (For 2.4)
    WSGIScriptAlias /sync /opt/sync/sync/wsgi.py
    <Directory /opt/sync/sync>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

