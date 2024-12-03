# Empty Python Flask App

This is a minimal setup for a Python Flask application.
The main goal of this app is to have a good starting point for a Flask application.


## DevContainers:

* Based on Debian image
* Exposing the app on port 5000
* Installing default VS Code extensions
* Setting the PYTHONPATH environment variable
* Running the following commands:
  * Install NPM dependencies
  * Build TypeScript
  * Create the Python venv .venv
  * Activate the Python venv .venv
  * Install Python dependencies


## Build & debug pipeline:

* Install NPM dependencies (every time, because of changes in package.json)
* Build Typescript
* Install Python dependencies (every time, because of changes in requirements.txt)
* Run PyLint on 'src' folder
* Run PyLint on 'tests' folder
* Run Python Unit Tests


## Supported IDEs:

* Visual Studio Code
* JetBrains PyCharm


## PyLint

* Support from all IDEs
* Support from command line "pylint src"
* Support from command line "pylint tests"


## Unit Tests

* Support from all IDEs
* Support from command line "python -m unittest"


## Others

* CleanAll.sh to clean all files produced from build
* Dockerfile


## License

This project is licensed under the MIT License.
