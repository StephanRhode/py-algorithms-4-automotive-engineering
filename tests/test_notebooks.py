import pytest
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.preprocessors.execute import CellExecutionError


def execute_notebook(notebook_file):
    """see this nbconvert docu
    http://nbconvert.readthedocs.io/en/latest/execute_api.html
    to understand this test"""
    print('---make jupyter test for ' + notebook_file)

    try:
        with open(notebook_file) as f:
            nb = nbformat.read(f, as_version=4)
        ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
        ep.preprocess(nb, {'metadata': {'path': ''}})
    except CellExecutionError:
        raise


@pytest.mark.parametrize("notebook", ["00_intro",
                                      "01_py-installation"])
def test_00_intro(notebook):
    execute_notebook(notebook_file="00_intro/" + notebook + ".ipynb")


@pytest.mark.parametrize("notebook", ["00_syntax",
                                      "01_semantics",
                                      "02_data-types",
                                      "03_conditions-and-loops",
                                      "04_functions",
                                      "05_classes",
                                      "06_modules"])
def test_01_basic_python(notebook):
    execute_notebook(notebook_file="01_basic-python/" + notebook + ".ipynb")


@pytest.mark.parametrize("notebook", ["00_tools-for-python",
                                      "01_plot-packages",
                                      "02_numpy",
                                      "03_scipy",
                                      "04_sympy",
                                      "05_sklearn",
                                      "06_additional-packages"])
def test_02_tools_and_packages(notebook):
    execute_notebook(notebook_file="02_tools-and-packages/" + notebook + ".ipynb")


@pytest.mark.parametrize("notebook", ["00_git-github",
                                      # ignore next line, this test does not terminate
                                      # "01_pytest",
                                      "02_sphinx",
                                      "03_continuous-integration",
                                      "04_clean-code"
                                      ])
def test_03_software_development(notebook):
    execute_notebook(notebook_file="03_software-development/" + notebook + ".ipynb")


@pytest.mark.parametrize("notebook", ["00_ode",
                                      "01_vehicle-model-calibration",
                                      "02_vehicle-state-estimation",
                                      "03_e-vehicle-powertrain-model",
                                      "09_deepl"
                                      ])
def test_04_mini_projects(notebook):
    execute_notebook(notebook_file="04_mini-projects/" + notebook + ".ipynb")
