# Developer set-up guide

This guide describes how to set up and run a Django server locally to contribute and build features for this project.


## Prerequisites
- Windows subsystems for Linux (for windows users)
- Git
- 🐍Python 3
- pip

_NOTE: If you have both python 2 & 3 installed when following this guide you should be explicit and use `python3` instead of `python` & `pip3` instead of `pip`_



## Creating a Virtual Environment

   A virtual environment is used to isolate python projects from other python modules that you may be installed locally. 
   Using `venv` lets you be explicit about what modules your project is dependent on ensuring all developers are working in the same environment.

_NOTE: windows users will need to use 'bash-shell' by opening cmd and typing "bash"_   

1. Make a folder to store virtual environments
`mkdir ~/virtualenvironments`

2. Create new virtual environment
`python -m venv ~/virtualenvironments/<insert project name here>`

3. Activate a virtual environment
`source ~/virtualenvironments/<insert project name here>/bin/activate`

4. To exit virtualenv
`deactivate`


## Running django project

1. Fork this repository

2. Clone the repo to your local machine
`git clone https://github.com/<Your github username here>/uni-code.git`
`cd competitive-programming`

3. Activate your virtualenv (see above)

4. Install dependencies for project
`pip install -r requirements.txt`

5. Run local development server on port 8000
`python manage.py runserver 8000`


## Developing a feature 

1. Activate your virtualenv (see above)

2. Switch to your development branch 
`git checkout dev`
_alternatively you can create a new branch for each feature_
`git checkout -b <new branch name>`

3. Work on feature

4. `Push` new feature to your fork on Github

5. Open pull request on [this repo](https://github.com/johnpaulkiser/uni-code)'s `dev` branch


## Quick Django commands
### Make database migrations
`python manage.py makemigrations` then `python manage.py migrate`

