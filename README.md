# steelWorks

This application is a very simple flask web app which stores information about songs and user reviews of those songs.

## Tools

This application has used the following tools during development:

 - Flask
 - Python
 - WTForms
 - Google cloud platform
 - SQL
 - SQLAlchemy
 - Jenkins
 - Gunicorn

The dependencies can be installed using [pip](https://pip.pypa.io/en/stable/) on the requirements document.
`pip install -r requierments.txt`

## Accessing the website

The website is accessible via Gunicorn via the IP address and port number of the virtual machine. The website is launched via a script within the repository (launchGunicorn.sh)

## Testing
The tests currently cover 86% of the code written by this application, as shown by the bellow image.![Image of pytest coverage for the application](images/testing.jpg)


