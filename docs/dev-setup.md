# Developer set-up guide

This guide describes how to set up and run a Django server locally to contribute and build features for this project.


## Prerequisites
- Windows subsystems for Linux (for windows users)
- Git
- Python 3
- pip

_NOTE: If you have both python 2 & 3 installed when following this guide you should be explicit and use `python3` instead of `python` & `pip3` instead of `pip`_



## Creating a Virtual Environment

   A virtual environment is used to isolate python projects from other python modules that you may have installed locally. 
   Using virtualenv lets you be explicit about what modules your project is dependent on ensuring all users are working in the same environment.

_NOTE: windows users will need to use 'bash-shell' by opening cmd and typing "bash"_   
1. Install virtualenv
`sudo pip install virtualenv`

2. Make a folder to store virtual environments
`mkdir ~/virtualenvironments`

3. Create new virtual environment
`virtualenv ~/virtualenvironments/<insert project name here>`

4. Activate a virtual environment
`source ~/virtualenvironments/<insert project name here>/bin/activate`

5. To exit virtualenv
`deactivate`


## Running django project

1. Create fork from this repository

2. Download repo to your local machine
`git clone https://github.com/<Your github username here>/competitive-programming.git`
`cd competitive-programming`

3. Activate your virtualenv (see above)

4. Install dependencies for project
`pip install -r requirements.txt`

5. Run server
`python manage.py runserver`


## Developing a feature 

1. Activate your virtualenv (see above)

2. Switch to your development branch 
`git checkout dev`
_alternatively you can create a new branch for each feature_
`git checkout -b <new branch name>`

3. Work on feature

4. `Push` new feature to your github

5. Open pull request on [this repo](https://github.com/johnpaulkiser/competitive-programming)'s `dev` branch

