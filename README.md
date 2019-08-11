# Python Algorithms for Automotive Engineering

This repository contains jupyter notebooks and python code for KIT course: *Python 
Algorithms for Automotive Engineering*. Please find the course syllabus 
[here](syllabus.md).

[![Build Status](https://travis-ci.com/StephanRhode/py-algorithms-4-automotive-engineering.svg?branch=master)](https://travis-ci.com/StephanRhode/py-algorithms-4-automotive-engineering)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/StephanRhode/py-algorithms-4-automotive-engineering/master)

## Getting Started

Please follow these steps to get a local copy of this project on your machine and to 
build, test, and deploy the lecture slides.

### Prerequisites

All notebooks can be used interactively via
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/StephanRhode/py-algorithms-4-automotive-engineering/master).

Hence, you can follow the lecture with your laptop and a web browser. However, if you
want to save your work and learn how to use tools like Pycharm, git and libraries like
Pytest, you should install the following software on your computer.

* [Anaconda](https://www.anaconda.com/distribution/)
* [Pycharm (community edition)](https://www.jetbrains.com/pycharm/download)
* [git](https://git-scm.com/downloads)

### Installing

First, clone this repository in a terminal with

```
git clone https://github.com/StephanRhode/py-algorithms-4-automotive-engineering.git
```

Second, navigate to the repository source folder and call this command to tell conda to
create a new virtual environment for python with packages defined in 
[requirements.txt](requirements.txt).

```
conda create -p ./_venv --file ./requirements.txt 
```

Third, test you installation with activated environment and a pytest call

```
conda activate ./_venv_
pytest
```

## Running the tests

This is very simple, just call
```
pytest
```

## Deployment

TODO: Add additional notes about how to deploy this on a live system if 
required.

## Contributing

TODO: add CONTRIBUTING.md file

Please read CONTRIBUTING.md for details on our code of conduct, and the process for
submitting pull requests to us.

## Maintainer

* [Stephan Rhode](https://github.com/StephanRhode)

## Contributors

* [awiawi](https://github.com/awiawi)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file 
for details

## Acknowledgments
