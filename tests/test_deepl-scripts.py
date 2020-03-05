import subprocess


def test_regression():
    subprocess.run("pytest 04_mini-projects/09_files/regression.py", shell=True)


def test_classification():
    subprocess.run("pytest 04_mini-projects/09_files/classification.py", shell=True)
