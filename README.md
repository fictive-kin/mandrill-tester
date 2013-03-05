# Mandrill Tester

Test rendering Mandrill templates.

## Install

You'll need to install [`pip`](http://guide.python-distribute.org/installation.html) and [`virtualenv`](http://www.virtualenv.org/en/latest/) if you don't already have them. Probably these commands will work to install it on OS X:

	curl -O http://python-distribute.org/distribute_setup.py
	sudo python distribute_setup.py
	sudo easy_install pip
	sudo pip install virtualenv

You should now be able to install the Mandrill Tester application with the following steps:

1. Clone this repo.    
	`git clone git://github.com/fictivekin/mandrill-tester.git`
2. `cd` into the local repo directory.    
	`cd mandrill-tester`
3. Set up a virtualenv.    
	`virtualenv --no-site-packages ./venv`
4. Activate the virtualenv.    
	`source ./venv/bin/activate`
5. Install the requirements with    
	`pip install -r requirements.txt`
6. Copy the sample settings file.    
	`cp tester/app_settings-sample.py tester/app_settings.py`
7. Edit `tester/app_settings.py` and fill in the `MANDRILL_API_KEY`
8. Start the server with    
	`python runserver.py`
9. Open the app at [http://127.0.0.1:7102/](http://127.0.0.1:7102/)

## Use

### Rendering a template

1. Pick the **Template slug** with an existing template slug on your Mandrill account
2. Fill in any **Template content** for editable sections. If none, leave as `[]`
3. Fill in any **Merge vars** as JSON
4. Hit **Render**

### Sending an email through a template

1. Pick the **Template slug** with an existing template slug on your Mandrill account
2. Enter the to and from addresses, and the subject
3. Fill in any **Template content** for editable sections. If none, leave as `[]`
4. Fill in any **Merge vars** as JSON
5. Hit **Send**
