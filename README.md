![](https://www.python.org/static/community_logos/python-powered-w-140x56.png)

# Python Algorithms for Automotive Engineering

This repository contains jupyter notebooks and python code for KIT course: *Python 
Algorithms for Automotive Engineering*. Please find the course syllabus 
[here](syllabus.md).

[Build Status](https://travis-ci.com/StephanRhode/py-algorithms-4-automotive-engineering)
[![Build Status](https://travis-ci.com/StephanRhode/py-algorithms-4-automotive-engineering.svg?branch=master)](https://travis-ci.com/StephanRhode/py-algorithms-4-automotive-engineering)

## Table of contents
[**1. Introduction**](00_intro)

[1.1 Introduction;](00_intro/00_intro.ipynb)
[1.2. Python installation](00_intro/01_py-installation.ipynb)

[**2. Basic python**](01_basic-python) 

[2.1. Syntax;](01_basic-python/00_syntax.ipynb)
[2.2. Semantics;](01_basic-python/01_semantics.ipynb)
[2.3. Data types;](01_basic-python/02_data-types.ipynb)
[2.4. Conditions and loops;](01_basic-python/03_conditions-and-loops.ipynb)
[2.5. Functions;](01_basic-python/04_functions.ipynb)
[2.6. Classes;](01_basic-python/05_classes.ipynb)
[2.7. Modules](01_basic-python/06_modules.ipynb)

[**3. Tools and packages**](02_tools-and-packages)

[3.1. Tools for Python;](02_tools-and-packages/00_tools-for-python.ipynb)
[3.2. Plot packages;](02_tools-and-packages/01_plot-packages.ipynb)
[3.3. NumPy;](02_tools-and-packages/02_numpy.ipynb)
[3.4. SciPy;](02_tools-and-packages/03_scipy.ipynb)
[3.5. SymPy;](02_tools-and-packages/04_sympy.ipynb)
[3.6. Scikit-Learn;](02_tools-and-packages/05_sklearn.ipynb)
[3.7. Additional packages](02_tools-and-packages/06_additional-packages.ipynb)

[**4. Software development**](03_software-development)

[4.1. Git, Github;](03_software-development/00_git-github.ipynb)
[4.2. PyTest;](03_software-development/01_pytest.ipynb)
[4.3. Sphinx;](03_software-development/02_sphinx.ipynb)
[4.4. Continuous Integration;](03_software-development/03_continuous-integration.ipynb)
[4.5. Clean Code;](03_software-development/04_clean-code.ipynb)
[4.6. Workflows](03_software-development/05_workflows.ipynb)

[**5. Mini projects**](04_mini-projects)

[5.1. Ordinary Differential Equations;](04_mini-projects/00_ode.ipynb)
[5.2. Vehicle model calibration;](04_mini-projects/01_vehicle-model-calibration.ipynb)
[5.3. e-Vehicle powertrain modeling;](04_mini-projects/02_e-vehicle-powertrain-model.ipynb)
[5.4. Deep learning](04_mini-projects/09_deepl.ipynb)

## Video lectures
In addition to the course material above please find here links to [video lectures in 
German language](https://mediaservice.bibliothek.kit.edu/#/details/DIVA-2020-C16) 
(most videos are in preparation, therefore some links might not work yet).

**Lecture 01:** [Warm welcome;](http://dx.doi.org/10.5445/IR/1000118409) 
[1.1 Introduction;](https://doi.org/10.5445/IR/1000118403) [1.2. Python installation]()

**Lecture 02:** [2.1. Syntax;](https://doi.org/10.5445/IR/1000118466) [2.2. Semantics]()

**Lecture 03:** [2.3. Data types;]() [2.4. Conditions and loops]()

**Lecture 04:** [2.5. Functions;]() [2.6. Classes]()

**Lecture 05:** [2.7. Modules;]() [3.1. Tools for Python]()

**Lecture 06:** [3.2. Plot packages;]() [3.3. NumPy]()

**Lecture 07:** [3.4. SciPy;]() [3.5. SymPy]()

**Lecture 08:** [3.6. Scikit-Learn;]() [3.7. Additional packages]()

**Lecture 09:** [4.1. Git, Github;]() [4.2. PyTest]()

**Lecture 10:** [4.3. Sphinx;]() [4.4. Continuous Integration]()

**Lecture 11:** [4.5. Clean Code;]() [4.6. Workflows]()

**Lecture 12:** [5.1. Ordinary Differential Equations;]() [5.2. Vehicle model calibration;]()
[5.3. e-Vehicle powertrain modeling]()

**Lecture 13:** [5.4. Deep learning]()

## Getting Started

Please follow these steps to get a local copy of this project on your machine and to 
build, test, and deploy the lecture slides.

### Prerequisites

Please bring your laptop to class. All notebooks can be viewed directly in github or through 
[nbviewer](https://nbviewer.jupyter.org/github/StephanRhode/py-algorithms-4-automotive-engineering/tree/master/)
[![nbviewer](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/StephanRhode/py-algorithms-4-automotive-engineering/tree/master/)
or, the notebooks ca be used interactively via
[Binder](https://mybinder.org/v2/gh/StephanRhode/py-algorithms-4-automotive-engineering/master)
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

Third, test your installation with activated environment and a pytest call. You can 
check if you activated the environment by having a look at the command prompt. If it 
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
* [mauricio-fernandez-l](https://github.com/mauricio-fernandez-l)
* [FelixBleimund](https://github.com/FelixBleimund)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file 
for details

## Acknowledgments
