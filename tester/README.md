# Mandrill Tester

Test rendering Mandrill templates.

## Install

1. Clone this repo. Ex: `git clone git://github.com/fictivekin/mandrill-tester.git`
2. `cd` into the local repo directory. Ex `cd mandrill-tester`
3. Set up a virtualenv. Ex: `virtualenv --no-site-packages ./venv`
4. Activate the virtualenv. Ex: `source ./venv/bin/activate`
5. Install the requirements with `pip install -r requirements.txt`
6. Copy the sample settings file. Ex: `cp tester/app_settings-sample.py tester/app_settings.py`
7. Edit `tester/app_settings.py` and fill in the `MANDRILL_API_KEY`
8. Start the server with `python runserver.py`
9. Open the app at [http://127.0.0.1:7102/](http://127.0.0.1:7102/)

## Use

1. Fill in the **Template slug** with an existing template slug on your Mandrill account
2. Fill in any **Template content** for editable sections. If none, leave as `[]`
3. Fill in any **Merge vars** as JSON
4. Hit **Render**