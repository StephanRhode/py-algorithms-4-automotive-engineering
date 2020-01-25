![](https://www.python.org/static/community_logos/python-powered-w-140x56.png)

# Python Algorithms for Automotive Engineering

This repository contains jupyter notebooks and python code for KIT course: *Python 
Algorithms for Automotive Engineering*. Please find the course syllabus 
[here](syllabus.md).

[![Build Status](https://travis-ci.com/StephanRhode/py-algorithms-4-automotive-engineering.svg?branch=master)](https://travis-ci.com/StephanRhode/py-algorithms-4-automotive-engineering)

## Table of contents
1. [Introduction](00_intro/00_intro.ipynb)
2. [Basic python](01_basic-python) 
    1. [Syntax](01_basic-python/00_syntax.ipynb)
    2. [Semantics](01_basic-python/01_semantics.ipynb)
    3. [Data types](01_basic-python/02_data-types.ipynb)

## Getting Started

Please follow these steps to get a local copy of this project on your machine and to 
build, test, and deploy the lecture slides.

### Prerequisites

Please bring your laptop to class. All notebooks can be viewed directly in github or through 
[![nbviewer](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/StephanRhode/py-algorithms-4-automotive-engineering/tree/master/)
or, the notebooks ca be used interactively via
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/StephanRhode/py-algorithms-4-automotive-engineering/master).

Hence, you can follow the lecture with your laptop and a web browser. However, if you
want to save your work and learn how to use tools like Pycharm, git and libraries like
Pytest, you should install the following software on your computer.

* [Pycharm (community edition)](https://www.jetbrains.com/pycharm/download)
* [git](https://git-scm.com/downloads)
* [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

Add to this, you might want to store your results in your own github repository. 
Therefore, please create [a github account](https://github.com/).

### Installing

First, fork this repository to your github account. Than, clone this repository in a 
terminal with

```
git clone https://github.com/<YOUR USER>/py-algorithms-4-automotive-engineering.git
```

or go to Pycharm and click on `VCS/Get from Version Control...`. 

Second, open the project in Pycharm and create a new environment (right bottom corner
of Pycharm). Than open [requirements.txt](requirements.txt) in Project panel and click
on install missing packages.

Alternatively, you can install the virtual environment manually from command line
with [this pip manual](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

Third, test you installation with activated environment and a pytest call. You can 
check if you activated the environment by having a look at command prompt. If it 
starts with `(venv) user@computer:~/some/path`, you are in active environment
`(venv)`, if not you need to activate the environment with 

```
.\venv\Scripts\activate
```
on Windows and with 
```
source venv/bin/activate
```
on Linux and macOS. Now test your installation with
```
pytest
```

## Running the tests

This is very simple, just call
```
pytest
```

## Create presentation slides
You can convert the jupyter notebooks into slides with this command
```
python make_slides.py
```

## Create html or pdf script
You can join all jupyter notebooks into one file with `nbmerge` package 
and the command
```
nbmerge --recursive -o merged.ipynb
```
When this is done, you can use 
```
jupyter nbconvert merged.ipynb --to html
```
or 
```
jupyter nbconvert merged.ipynb --to pdf
```
to create all in one files of this course. Note that you need a 
`pandoc` installation on your computer. Curently, html option works,
pdf causes errors and the figures in pdf are missing.

## Maintainer

* [Stephan Rhode](https://github.com/StephanRhode)

## Contributors

* [awiawi](https://github.com/awiawi)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file 
for details

## Acknowledgments
