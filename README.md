# Template for Python projects

Model for new projects in Python aiming to facilitate and standardize the
creation of projects with the [PyCharm](https://www.jetbrains.com/pycharm/)
IDE.

## Features

- Project configuration file [setup.py](setup.py).
- Compressed file of IDE settings ([settings.zip](settings.zip))
  File -> Manage IDE Settings -> Import Settings...
- Folder for documentation using [MkDocs](https://mkdocs.org/). Configuration
  file [mkdocs.yml](mkdocs.yml).
  - Theme for documentation using [mkdocs-material](https://squidfunk.github.io/mkdocs-material/).
- Log folder
  using  [Loguru](https://loguru.readthedocs.io/en/stable/index.html) for
  logging.
  Configuration file ([loguru_conf.py](logs/loguru_conf.py)).
- Folder for testing
  using [unittest](https://docs.python.org/3/library/unittest.html).
- .gitignore file generated
  by [Toptal](https://www.toptal.com/developers/gitignore/)
  with python and pycharm+all tags.
- [Prospector](https://prospector.readthedocs.io/) configuration file to
  improve code quality ([.prospector.yaml](.prospector.yaml)).
- Installation of the [Blue](https://blue.readthedocs.io/en/latest/) library to
  format the code according
  to [PEP8](https://www.python.org/dev/peps/pep-0008/).
- Installation of the [isort](https://isort.readthedocs.io/en/stable/) library
  to sort the imports, of the codes, in alphabetical order.

## Installing libraries and settings

### [MKDocs](https://mkdocs.org/)

* `pip install mkdocs` - Install MKDocs
* `mkdocs new .` - Create a new site
* `mkdocs serve` - Serve the site
* `mkdocs build` - Build the site
  * `pip install mkdocs-material` - Install the theme material

### [Loguru](https://loguru.readthedocs.io/en/stable/index.html)

* `pip install loguru` - Install Loguru
* `loguru_conf.py` - Configuration file for Loguru
* `logs` - Folder for logs

### [Prospector](https://prospector.readthedocs.io/)

* `pip install prospector` - Install Prospector
* `.prospector.yaml` - Configuration file for Prospector
* `prospector` - Command to run Prospector

### [Blue](https://blue.readthedocs.io/en/latest/)

* `pip install blue` - Install Blue
* `blue .` - Command to run Blue on the current folder

### [isort](https://isort.readthedocs.io/en/stable/)

* `pip install isort` - Install isort
* `isort .` - Command to run isort on the current folder