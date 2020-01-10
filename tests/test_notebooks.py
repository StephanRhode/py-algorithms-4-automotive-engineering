import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.preprocessors.execute import CellExecutionError


def execute_notebook(notebook_file):
    """see this nbconvert docu http://nbconvert.readthedocs.io/en/latest/execute_api.html
    to understand this test"""
    print('---make jupyter test for ' + notebook_file)

    try:
        with open(notebook_file) as f:
            nb = nbformat.read(f, as_version=4)
        ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
        ep.preprocess(nb, {'metadata': {'path': ''}})
    except CellExecutionError:
        raise


def test_intro_00():
    execute_notebook(notebook_file="00_intro/00_intro.ipynb")


def test_basic_python_00():
    execute_notebook(notebook_file="01_basic-python/00_syntax.ipynb")


def test_basic_python_01():
    execute_notebook(notebook_file="01_basic-python/01_semantics.ipynb")


def test_basic_python_02():
    execute_notebook(notebook_file="01_basic-python/02_data-types.ipynb")
