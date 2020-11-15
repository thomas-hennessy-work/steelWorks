# steelWorks

This application is a very simple flask web app which stores information about songs and user reviews of those songs. Songs can be added, viewed, edited and deleted. Reviews can be added to a song, viewed and deleted. Progress on the development of the project can be found on the steelWorks [trello](https://trello.com/b/p4Kncors/steel-works-product-backlog) board.
## Tools

This application has used the following tools during development:

 - Flask
 - Python
 - PYTest
 - WTForms
 - Google cloud platform
 - SQL
 - SQLAlchemy
 - Jenkins
 - Gunicorn

### Required installations
The dependencies required for the application can be installed using [pip](https://pip.pypa.io/en/stable/) in conjunction with the requirements document.
`pip install -r requierments.txt`

## Accessing the website

The website is accessible via Gunicorn via the IP address and port number of the virtual machine. The website is launched via a script within the repository.
`bash launchGunicorn.sh`
Once the script is run, the application will be accessible from the local host on port 5000.

## Testing
The application is tested using unit tests. The tests currently cover 86% of the code written by this application, as shown by the image at the bottom of this section. The environment setup for the unit tests allow them to connect to the same SQL server the live application connects to.
### Testing coverage
![Image of pytest coverage for the application](images/testing.jpg)

## Build server
The application is run on a Jenkins server obtaining the source code via GitHub. The server takes the source code, ensures it can be run and produces a software artefact in the form of a build of the software.
### Build server
![Build server producing builds](images/buildServer.jpg)
## Future improvements

 1. The website would benefit from CSS stylings to improve the layout and readability
 2. Adding sanitization to inputted video URL's would allow users to input the first URL to the video they find, making the website easier to use.
 3. Adding a user feature so that added reviews can be contributed to a person.
 4. After the build server ensures the application is able to run, it should automatically stop the application rather than needing manual intervention.


