# First Time Setup Guide
This document provides a set of instructions to install and setup necessary packages to run the Python and Django web application.

## Side Note - Pip Installation 
If you do not have Django in your system yet, you can install it using the command below in your terminal if you have the **pip** package installer in your system.
```
pip install Django
```
If you have Python and Django installed in your system or virtual environment already and using the **pip** command to install packages, you can skip using the the **Installation (Anaconda Environment)** step below and run the following **pip** commands to install the packages/dependencies in your local environment/virtual environment to run the program.
```
pip install Pillow
pip install django-crispy-forms
```
Once the packages have been installed, skip past the **Installation (Anaconda Environment)** guide and move onto the **Running the application** step to run the django application.

## Installation (Anaconda Environment)
The development for this project was done in the Anaconda environment. To install anaconda please follow the link https://conda.io/projects/conda/en/latest/user-guide/install/download.html and follow the setup instructions depending on your OS system. 

Once you have installed anaconda, we will need to open the Anaconda Prompt through the start menu. The first step is to set up a virtual environment and then install the necessary packages to run the program. 

To create a virtual environment, run the following code in the Anaconda Prompt. Note djangoPoll is just the name we assigned for the created environment, you can replace it with any name you prefer.
```
conda create --name djangoPoll
```
After creating the environment, we activate it by running the following line
```
activate djangoPoll
```
Upon activating the environment, we need to install some packages starting with django
```
conda install -c anaconda django
```
Running this command will not only install django but also all other packages needed to work with django including our SQLite database that we are using in this project.

We also need to run the two commands below to install two other packages for our web application form to work with bootstrap and image files.
```
conda install -c anaconda pillow
conda install -c conda-forge django-crispy-forms
```

## Running the application
Once we have all the necessary packages installed, make a git pull request for this repository and navigate inside the **UNSW-Challenge** directory where you can find the **manage.py** file in the Anaconda Prompt or your system's terminal. And finally to run the application, run the following command:
```
python manage.py runserver
```

## Test Accounts
These are some active accounts created for testing purposes
```
Username: Jet
Password: polltest123
```
```
Username: Sam
Password: polltest123
```
```
Username: James
Password: polltest123
```
