import glob
import subprocess


for notebook in glob.glob("**/*.ipynb"):
    print("make slides for: ", notebook)
    command = "jupyter nbconvert " + notebook + " --to slides"
    subprocess.run(command, shell=True)
