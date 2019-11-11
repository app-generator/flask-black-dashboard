# [Flask Dashboard Black](https://appseed.us/admin-dashboards/flask-dashboard-black)

**[Open-Source Admin Dashboard](https://appseed.us/admin-dashboards/flask-dashboard-black)** coded in **Flask Web Framework** on top of **Black Dashboard** design, crafted by Creative-Tim agency. **Dashboard** features:

- SQLite database
- SQLAlchemy ORM
- Session-Based authentication flow (login, register)

<br />

![Flask Dashboard Black - Open-Source Admin Panel](https://raw.githubusercontent.com/app-generator/flask-black-dashboard/master/screenshots/flask-black-dashboard-intro.gif)

<br />

## Build from sources

```bash
$ # clone the sources
$ git clone https://github.com/app-generator/flask-black-dashboard.git
$ cd flask-black-dashboard
$
$ # install modules using a virtualenv
$ virtualenv --no-site-packages env
$ source env/bin/activate
$
$ # install deps 
$ pip install -r requirements.txt
$
$ # Create SQLite database using the Flask console
$ flask shell
>> from app import db
>> db.create_all()
>> quit() 
$
$ # SQLite database.db should be created in the app folder:
$ # app\database.db
$
$ # Set the FLASK_APP environment variable
$ (Windows) set FLASK_APP=app.py
$ (Unix) export FLASK_APP=app.py
$ (Powershell) $env:FLASK_APP = ".\app.py"
$ 
$ flask app.py
$ # app is running on port 5000
```

<br />

## Want more? Go PRO!

<br />

| [Flask Dashboard Material](https://appseed.us/admin-dashboards/flask-dashboard-material-pro) | [Flask Dashboard Argon](https://appseed.us/admin-dashboards/flask-dashboard-argon-pro) | [Flask Dashboard Black](https://appseed.us/admin-dashboards/flask-dashboard-black-pro) |
| --- | --- | --- |
| [![Flask Dashboard Material PRO](https://raw.githubusercontent.com/app-generator/static/master/products/flask-dashboard-material-pro-intro.gif)](https://appseed.us/admin-dashboards/flask-dashboard-material-pro)  | [![Flask Dashboard Argon PRO](https://raw.githubusercontent.com/app-generator/static/master/products/flask-dashboard-argon-pro-intro.gif)](https://appseed.us/admin-dashboards/flask-dashboard-argon-pro) | [![Flask Dashboard Black PRO](https://raw.githubusercontent.com/app-generator/static/master/products/flask-dashboard-black-pro-intro.gif)](https://appseed.us/admin-dashboards/flask-dashboard-black-pro)

<br />

## Support
---

- Free support via eMail < [support @ appseed.us](https://appseed.us/support) > and [Github](https://github.com/app-generator/flask-black-dashboard/issues/)
- 24/7 Live Support via [Discord](https://discord.gg/fZC6hup) for paid plans and commercial products.

<br />

## Resources

- [Flask Dashboard Black](https://appseed.us/admin-dashboards/flask-dashboard-black) - Product page
- [Flask Dashboard Black](https://flask-black-dashboard.appseed.us/) - Live DEMO
- [Flask Dashboard Black](https://github.com/app-generator/flask-black-dashboard/) - Source code published on Github
- [Flask Framework](https://www.palletsprojects.com/p/flask/) - Offcial website
- [Flask Dashboard - Open-Source Boilerplates](https://dev.to/sm0ke/flask-dashboard-open-source-boilerplates-dkg) - A popular article published on Dev.to platform
- [Flask Dashboard](https://admin-dashboards.com/tags/flask-dashboard) - Index provided by **Admin-Dashboards.com**
 
<br />
 
---
[Flask Dashboard Black](https://appseed.us/admin-dashboards/flask-dashboard-black) - provided by **AppSeed**
