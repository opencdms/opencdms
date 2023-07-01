Flask doesn't implement a hierachy of static folders like it does with template folders.

Currently we've made a copy of the static folder in order to modify things like `img/logo.png`.

Instead of forking and maintaining the static files, in the long term we can switch to using Flask-Assets

https://flask-assets.readthedocs.io/en/latest/
