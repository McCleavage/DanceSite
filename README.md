# DanceSite
## Overview
This site catalogues the various dances I've been exposed to over my short ballroom dancing career. It was built using the Django python web app framework. It forms part of the project portfolio I developed during my hyperionDev software engineering course.
## Installation
If you're really interested in dancing, and my web dev coding skills (for some reason), simply clone this public repository. The webapp is stored as source.

The project requires python3 (tested with python 3.11) with the django and Pillow packages installed. After installing python make sure pip is installed by running:
```
 python -m pip install
```
To install venv:
```
pip install venv 
```
Assuming you've configured your venv path correctly, then creat new virtual env:
```
python -m venv /path/to/new/virtual/environment
/path/to/new/virtual/environment/Scripts/activate
```
Then, to install django and Pillow, run in root directory:
```
pip install -r "requirements.txt"
```
## Usage
To run the web server locally, open command prompt in the root directory of the project and run
```
python manage.py runserver
```
You should see:

![image](https://github.com/McCleavage/DanceSite/assets/137903276/869e8bbd-fd0b-413e-bdd6-17b96fac768d)

Simply click the link to open the web site in your browser:

![image](https://github.com/McCleavage/DanceSite/assets/137903276/265a44e5-58f9-4b5f-8dd9-634734ff8fa6)

## Docker Usage
Alternatively, you can use the Dockerfile to create a docker image to run the program.
Make sure you have Docker Desktop installed for this step, then in the root directory:
```
docker build -t dance-site ./
docker run -d -p 8000:8000 dance-site
```
Simply visit localhost:8000 to open the webpage
## Credits
This project was authored solely by [McCleavage (github.com)](https://github.com/McCleavage)
