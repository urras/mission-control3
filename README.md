![GLADOS](http://i.imgur.com/126tjc6.png "Glados Logo")

Mission Control is a web interface application that is used for the Glint Analyzing Data Observation Satellite (GLADOS) to be launched in 2017. It's written in Flask, and contains numerous libraries to analyze satellite data, incuding self-executed autotests. Currently under work, planned features also include autonomous execution, push notifications, and console access.

##Installing
1. In a virtualenv, install the required python libraries with ```pip install -r requirements.txt```
2. Rename ```config_sample.py``` to ```config.py``` and replace ```'SECRET_KET'``` to a long, unguessable string.
3. Initialize the database by running ```./run.py db init```
4. Start the server with ```./run.py runserver <production|development>``` (default is development)
