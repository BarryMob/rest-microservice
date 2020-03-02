# Rest Microservice to fetch languages used in Github trending repositories. Python(Flask)
This is a small demonstration of how we can use Python (Flask) to create a rest microservice on one side, and on the other hand how to use the github API in order to fetch the most used languages in Github trends.

# Installation
The only main requirement is to use Python >= 3.6.9 and install then requirements.txt file's content.
One `pip install requirements.txt`, after creating a virtual environment, will do the trick.


# Usage
You can only perfom two kind of operations, get list of languages used by the 100 trending repos and the list of repos using a given language.

## EndPoints

* List of languages with the number of repos using them:
    * GET /trend/languages 
* List of repos using a given language:
    * GET /trend/languages/{laguage_name}

# Note
Since we are using the github API without authentication, we are only allowed 6O requests per hour, 10 per minute.