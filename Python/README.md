# Python-Basics
> its fun learning python (again!) :-)


## IMP links / CheatSheets  
> https://www.cheatography.com/desmovalvo/cheat-sheets/python3-data-structures/pdf/  
> https://ehmatthes.github.io/pcc/cheatsheets/README.html  
> https://www.analyticsvidhya.com/blog/2015/06/quick-guide-text-data-cleaning-python/  
> https://www.analyticsvidhya.com/blog/2015/06/data-visualization-in-python-cheat-sheet/  
> https://www.analyticsvidhya.com/blog/2015/06/infographic-cheat-sheet-data-exploration-python/  




## global veriable 
> https://stackoverflow.com/questions/423379/using-global-variables-in-a-function-other-than-the-one-that-created-them
```python
glob_var=0

def set_1():
    global glob_var
    glob_var = 10

def set_2():
    glob_var = 20

print(glob_var)
set_1()
print(glob_var)
set_2()
print(glob_var)

0
10
10
```

## __init.py__
***The \__init__.py file can contain the same Python code that any other module can contain, and Python will add some additional attributes to the module when it is imported.***


## if __name__ == "__main__":
> https://stackoverflow.com/questions/419163/what-does-if-name-main-do
- The global variable, __name__, in the module that is the entry point to your program, is '__main__'. Otherwise, it's the name you import the module by.

- So, code under the if block will only run if the module is the entry point to your program.

- It allows the code in the module to be importable by other modules, without executing the code block beneath on import.

## yield
> https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
- yield is a keyword that is used like return, except the function will return a generator.
```python
def getGenerator():
    list = range(5)
    for i in list:
        yield i*i
myGen = getGenerator()
for i in myGen:
    print(i)
```
- Generators are iterators, a kind of iterable you can only iterate over once. Generators do not store all the values in memory, they generate the values on the fly:

## *args and **kwargs
> https://stackoverflow.com/questions/36901/what-does-double-star-asterisk-and-star-asterisk-do-for-parameters  
> http://sys-exit.blogspot.com/2013/07/python-positional-arguments-and-keyword.html

- The *args and **kwargs is a common idiom to allow arbitrary number of arguments to functions 
- The *args will give you all function parameters as a tuple
- The **kwargs will give you all keyword arguments except for those corresponding to a formal parameter as a dictionary

```python
def test(*args):
    for a in args:
        print(a)
test(1)
test(1,2,3,4,5)

def test_new(**kwargs):
    for a in kwargs:
        print(a,kwargs[a])
test_new(name="vb",age=27,sal=2000)

1
1
2
3
4
5
name vb
age 27
sal 2000
```

##  Python Scope LEGB Rule.
> https://stackoverflow.com/questions/291978/short-description-of-the-scoping-rules

- L, Local — Names assigned in any way within a function (def or lambda)), and not declared global in that function.
- E, Enclosing-function locals — Name in the local scope of any and all statically enclosing functions (def or lambda), from inner to outer.
- G, Global (module) — Names assigned at the top-level of a module file, or by executing a global statement in a def within the file.
- B, Built-in (Python) — Names preassigned in the built-in names module : open,range,SyntaxError,...

## The pipfile i.e. virtual environment
> https://robots.thoughtbot.com/how-to-manage-your-python-projects-with-pipenv

```commandline
pipenv install <abc>
pipenv install <xyz>
#OR
pipenv install requirments.txt
#this will create 'pipfile'
```

Once we have pipfile created run below to... 
 - automagically locate the Pipfiles
 - create a new virtual environment 
 - and install the necessary packag
```commandline
pipenv install
```


To activate virtual environment
```commandline
pipenv shell
```

Running code in the virtual environment
```commandline
pipenv run python <myCode>.py
```


And Finaly
```commandline
exit
```

> https://docs.pipenv.org/basics/
```markdown
- Generally, keep both Pipfile and Pipfile.lock in version control.
- Do not keep Pipfile.lock in version control if multiple versions of Python are being targeted.
- Specify your target Python version in your Pipfile’s [requires] section. Ideally, you should only have one target Python version, as this is a deployment tool.
- pipenv install is fully compatible with pip install syntax, for which the full documentation can be found here.
```

## Deployment pipeline for python project, with Makefile
> https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/index.html  

### A. test module  

```make test```  
```python setup.py test```
- pull docker image from nexux   
- run docker container for test  

### B. build and release

```make compile```
```setup.py bdist_wheel```
- this will create <>.whl

```make release```
```pipenv run pip install twine && pipenv run twine upload --config-file $(PYPIRC_PATH) -r nexus <>.zip```


## python packages management 
> https://docs.python.org/3/reference/import.html   
Need to understand below three things,
	- a. python egg and wheel   
	- b. Makefile  
	- c. setup.py  

- Package - A folder/directory that contains __init__.py file.  
- Module - A valid python file with .py extension.  
- Distribution - How one package relates to other packages and modules.  

|Regular packages|Namespace packages|
| --- | --- |
| typically implemented as a directory containing an \__init__.py file |  is a composite of various portions, where each portion contributes a subpackage to the parent package|
| When imported, \__init__.py file is implicitly executed, and the objects it defines are bound to names in the package’s namespace. | there is no \__init__.py file |


### a. python egg and wheel 
> https://packaging.python.org/discussions/wheel-vs-egg/  
> http://peak.telecommunity.com/DevCenter/PythonEggs  
> https://www.blog.pythonlibrary.org/2012/07/12/python-101-easy_install-or-how-to-create-eggs/  
> https://mrtopf.de/en/a-small-introduction-to-python-eggs/  
> https://stackoverflow.com/questions/46915070/wheel-files-what-is-the-meaning-of-none-any-in-protobuf-3-4-0-py2-py3-none-a

- Wheel is same concept as a .jar file in Java, it is a .zip file with some metadata files renamed .egg, for distributing code as bundles
- It is a logical structure embodying the release of a specific version of a Python project, comprising its code, resources, and metadata.  


| wheel | egg |  
| --- | --- |  
| Wheel is a distribution format, i.e a packaging format. |  both a distribution format and a runtime installation format (if left zipped), and was designed to be importable. |  
| Wheel archives do not include .pyc files. |  Eggs are to Pythons as Jars are to Java... |  
| Wheel is internally organized by sysconfig path type, therefore making it easier to convert to other formats. | Python eggs are a way of bundling additional information with a Python project, that allows the project's dependencies to be checked and satisfied at runtime, as well as allowing projects to provide plugins for other projects | 
| | .egg files are a "zero installation" format for a Python package; no build or install step is required, just put them on PYTHONPATH or sys.path and use them |
  
- for spark submit we rename .whl to .zip !!! 
 
- 'sample_project' project structure
```
	/sample_project
		/src
			main.py
			__inti__.py
	Pipfile
	README.md
	setup.py
```
- to build a ***wheel** for project 'sample_project'
 ```python setup.py bdist_wheel```  
	- this will create below files/folder
	- wheel will go to : dist/yourproject-<tags>.whl  
	- Ex: dist/example_pkg-0.0.1-py3-none-any.whl  
	- whl file package names by components : {distribution}-{version}(-{build tag})?-{python tag}-{abi tag}-{platform tag}.whl  
	- if 'abi tag; is 'noon' than that means it is 'sourse package'  
	- it creats ,.whl and egg-info directory 
```
	/sample_project
		/src
			main.py
			__inti__.py
		/example_pkg.egg-info
			top_level.txt
			SOURCES.txt
			PKG-INFO
			dependency_links.txt
		/dist
			example_pkg-0.0.1-py3-none-any.whl
		/build
			... # lib, etc
	Pipfile
	README.md
	setup.py
```
 
- to build a ***egg** for project 'sample_project'
``` python setup.py bdist_egg ```
	- three new folders: build, dist, and mymath.egg-info. 
	- The only one we care about is the dist folder in which you fill find your egg file, sample_project-0.1-py2.6.egg. 
	- The egg file itself is basically a zip file.
	- If you change the extension to “zip”, you can look inside it and see that it has two folders: mymath and EGG-INFO.
	- At this point, you should be able to point easy_install at your egg on your file system and have it install your package.

#### pipenv run pip wheel requirements.txt --only-binary all
- this will download all dependencies from requirements.txt file and create a single wheel file from it.



### b. Makefile 
> https://krzysztofzuraw.com/blog/2016/makefiles-in-python-projects.html  
> http://www.cs.colby.edu/maxwell/courses/tutorials/maketutor/  
> https://swcarpentry.github.io/make-novice/02-makefiles/  
- Makefiles are a simple way to organize code compilation.  
-  complicated shell commands- put them under a rule in the makefile.  
- This is a build file, which for Make is called a Makefile - a file executed by Make  
- Makefiles Do Not Have to be Called Makefile. if we call it something else we need to tell Make where to find it. This we can do using -f flag.  
- Additional things that you want to add is something called PHONY. By default, makefile operates on files so if there will be a file called clean-pyc it will try to use it instead of a command. To avoid this use ```.PHONY``` at the beginning of your makefile


- ```make -f MyOtherMakefile```  

    
```bash
    #example make file    
.PHONY: init clean wheel 
    
clean-build: 
	rm -rf build/
	
clean-dist: 
	rm -rf dist/

clean: clean-build clean-dist 
	rm -rf .eggs/
	rm -f Pipfile.*
	rm -f VERSION
	find . -name "*.egg-info" -exec rm -rf {} +
	find . -name "*.dist-info" -exec rm -rf {} +
	find . -name "*.egg" -exec rm -rf {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +

init: clean
	pipenv --python $(PYTHON_VERSION)
	pipenv run pip install pylint

bdist_wheel-depen: init
	mkdir -p build && cd build && pipenv run pip wheel -r ../requirements.txt --only-binary all

wheel: bdist_wheel-depen
	mkdir -p dist && mv build/*.whl dist && pipenv run python setup.py bdist_wheel
```

### c. setup.py
  > https://stackoverflow.com/questions/1471994/what-is-setup-py  
  > https://pythonhosted.org/an_example_pypi_project/setuptools.html  
  - setup.py  tells you that the module/package you are about to install has been packaged and distributed with Distutils, which is the standard for distributing Python Modules.
  - SETUP() - IS THE MAIN FUNCTIONS 
  - it used  setuptools lib : ```from setuptools import setup```
  - used to register python package with pipy
  - and distrubute / build package ( wheel the package )
  - using it is like 
  ```bash
  python setup.py <cmd>
  
  # python setup.py --help :  to get all the <cmd>
  ```

## Anaconda
> https://linuxhint.com/anaconda-python-tutorial/  
- Anaconda is data science and machine learning platform for the Python and R programming languages.  
- It is designed to make the process of creating and distributing projects simple, stable and reproducible across systems.  
- Anaconda is a Python based platform that curates major data science packages including pandas, scikit-learn, SciPy, NumPy and Google’s machine learning platform, TensorFlow.   
- It comes packaged with conda (a pip like install tool), Anaconda navigator for a GUI experience, and spyder for an IDE.  



## Conda - environment manager
> https://medium.freecodecamp.org/why-you-need-python-environments-and-how-to-manage-them-with-conda-85f155f4353c  
> https://conda.io/docs/_downloads/conda-cheatsheet.pdf   
> https://conda.io/docs/user-guide/tasks/manage-environments.html#activating-an-environment  
> https://community.hortonworks.com/articles/58418/running-pyspark-with-conda-env.html  
> https://www.slideshare.net/AaronMeurer/conda-a-binary-scipy2014  
- A conda environment is a directory that contains a specific collection of conda packages that you have installed.   
- On a machine the environment is made out of variables linking to different target folders containing executable or other resource files.  
- So if you execute a command it is either referenced from your PATH, PYTHON_LIBRARY, or any other defined variable.  
- These variables link to files in directories like /usr/bin, /usr/local/bin or any other referenced location.  
- They are called ***hard links or absolute reference*** as they start from root /.
- Environments using hard links are not easily transportable
- Therefor it is necessary to use relative links in a transportable/relocatable environment.
- This is especially true for conda env as it creates hard links by default. 
- By making the conda env relocatable it can be used in a application by referencing it from the application root .  
- You can also share your environment with someone by giving them a copy of your environment.yaml file  

```bash
$ conda create -n MyCondaEnv python=3.6 pandas


$ source activate MyCondaEnv
(MyEnv) $
```

- Cloning an environment  
> https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html  
``` conda create --name myclone --clone myenv ```


> https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/  

- Conda and pip
	- pip installs python packages within any environment; conda installs any package within conda environments.
	- If you want to, say, manage Python packages within an existing system Python installation, conda can't help you: by design, it can only install packages within conda environments. 

- Conda and Anaconda
	- Conda is a package manager; Anaconda is a distribution. 
	- A software distribution is a pre-built and pre-configured collection of packages that can be installed and used on a system. 
	- A package manager is a tool that automates the process of installing, updating, and removing packages. 

## pyspark with CONDA
> https://mapr.com/blog/python-pyspark-condas-pt1/  
> 
- PYSPARK_PYTHON : The variable controlling the python environment for python applications in Spark .


```bash
# client mode
export PYTHONPATH=/opt/cloudera/parcels/Anaconda/envs/<conda_env_name>
export PATH=${PYTHONPATH}/bin:$PATH 

spark2-submit --master yarn --deploy-mode client ...

# cluster mode
spark2-submit --master yarn --deploy-mode cluster \
--conf "spark.yarn.appMasterEnv.PYSPARK_PYTHON=/opt/cloudera/parcels/Anaconda/envs/<conda_env_name>/bin/python"  \
--conf "spark.yarn.appMasterEnv.PYSPARK_DRIVER_PYTHON=/opt/cloudera/parcels/Anaconda/envs/<conda_env_name>/bin/python" \
pySpark_script.py

```



## TypeError vs ValueError  
> https://www.datacamp.com/community/tutorials/exception-handling-python  

| TypeError | ValueError |
| --- | --- |
| Passing arguments of the wrong type (e.g. passing a list when an int is expected) should result in a TypeError | Raised when a built-in operation or function receives an argument that has the right type but an inappropriate value | 
| Whenever you see an error that include 'NoneType' that means that you have an operand or an object that is None when you were expecting something else. | |



## package management

|  pipenv  |  Docker  |  Conda  |
|  --  | --  |  --  |  
|  requirements.txt, setup.py, Makefile |  Dockerfile, setup.py, Makefile  |  setup.py, Makefile  | 


## Unit tests  [TODO]
> https://www.pythonsheets.com/notes/python-tests.html  
> https://python.g-node.org/python-summerschool-2009/_media/cheat_sheets.pdf    
> https://docs.python-guide.org/writing/tests/  

- mock.Mock vs mock.patch
    - patch replaces the class with a mock object and lets you work with the mock instance  
    - Once you patch a class, references to the class are completely replaced by the mock instance.
    - mock.patch is usually used when you are testing something that creates a new instance of a class inside of the test.  

- Mock vs MagicMock
    - Mock is use for replacing or mocking an object in python unittest while. 
    - MagicMock is a subclass of Mock with all the "magic methods" pre-created and ready to use.
    - Below  are the pre-created magic methods and its default values for MagicMock.
        ```python
        __lt__: NotImplemented
        __gt__: NotImplemented
        __le__: NotImplemented
        __ge__: NotImplemented
        __int__: 1
        __contains__: False
        __len__: 0
        __iter__: iter([])
        ...
        ```
- @pytest.fixture(autouse=True)
    - Autouse fixtures (xUnit setup on steroids)
The class-level transact fixture is marked with autouse=true which implies that all test methods in the class will use this fixture without a need to state it in the test function signature or with a class-level usefixtures decorator.
```python
@pytest.fixture(autouse=True)
def my_fixture():
    ...
```

    
    
### unittest
- Ex 1  
```python
import unittest

def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)
	
```

- Ex 2
```python
#Basic structure of a test suite
import unittest
class FirstTestCase(unittest.TestCase):
	 def setUp(self):
		 """setUp is called before every test"""
		 pass
	 def tearDown(self):
		 """tearDown is called at the end of every test"""
		 pass
	 def testtruisms(self):
		 """All methods beginning with ‘test’ are executed"""
		 self.assertTrue(True)
		 self.assertFalse(False)
class SecondTestCase(unittest.TestCase):
	 def testapproximation(self):
		 self.assertAlmostEqual(1.1, 1.15, 1)

if __name__ == '__main__':
	 # run all TestCase's in this module
	 unittest.main()

```

Assert methods in unittest.TestCase
Most assert methods accept an optional msg argument, which is used as an explanation for the error.

|  methon  |  result  |
|  --  |  --  |
|  assert_(expr[, msg) assertTrue(expr[, msg])  |   Fail if expr is False  |
|  assertFalse(expr[, msg])  |  Fail if expr is True  |
|  assertEqual(first, second[, msg])   |  Fail if first is not equal to second  |
|  assertNotEqual(first, second[, msg])  |  Fail if first is equal to second  |
|  assertAlmostEqual(first, second [, places[, msg]])  | Fail if first is equal to second up to the decimal place indicated by places  |
|  assertNotAlmostEqual(first, second [, places[, msg]])  |  Fail if first is not equal to second up to the decimal place indicated by places  |
|  assertRaises(exception, callable, ...)  |  Fail if the function callable does not raise an exception of class exception. If additional positional or keyword arguments are given, they are passed to callable.  |
|  fail([msg])  |  Always fail  |


### pytest
- By default, pytest runs tests in sequential order
- pytest provides us with an option to run tests in parallel.
For this, we need to first install the pytest-xdist plugin.
```shell script
pip install pytest-xdist
# pytest -n <num>
pytest -n 3
```

> https://pypi.org/project/pytest-runner/   
> https://stackoverflow.com/questions/38155169/how-do-i-get-pytest-to-run-all-functions-as-test  
> https://docs.pytest.org/en/latest/goodpractices.html

- Ex 1  
```python
import pytest 
def fun(x):
    return x+1

def test_fun():
    assert fun(5) == 7
```    

- Ex 2  
```python
import pytest 

def fun(x):
    try:
        return x+1
    except Exception as ex:
        raise

def test_fun():
    with pytest.raises(Exception) as exc_info:
        fun('5')
    assert exc_info.typename == "TypeError"
```

- Code coverage with pytest-cov package
```shell script
pip install pytest-cov

pytest \
--cov-report term-missing \
--cov=coverage_1 \
test_coverage_1.py
```

- Use coverage as a tool to find blind spots in the code, but not as a metric or target
goal.

- Pytest reusable features so that we can feed our tests with data or objects in
order to test more effectively and without repetition.

### Auto unit testing with setuptool



## Logging
> http://zyxue.github.io/2015/08/05/quick-setup-for-python-logging.html  

```python
import logging  
logging.basicConfig(
    level=logging.DEBUG, format='%(asctime)s|%(levelname)s|%(message)s')

logging.info('some message')
```

```python
import logging

def sample_function(secret_parameter):
    logger = logging.getLogger(__name__)  # __name__=projectA.moduleB
    logger.debug("Going to perform magic with '%s'",  secret_parameter)
    ...
    try:
        result = do_magic(secret_parameter)
    except IndexError:
        logger.exception("OMG it happened again, someone please tell Laszlo")
    except:
        logger.info("Unexpected exception", exc_info=True)
        raise
    else:
        logger.info("Magic with '%s' resulted in '%s'", secret_parameter, result, stack_info=True)

```

```python
# 1: logging.yaml  

version: 1
disable_existing_loggers: False
formatters:
    simple:
        format: "%(asctime)s - %(levelname)s -[%(name)s]  %(message)s"
handlers:
    console:
        class: logging.StreamHandler
        level: DEBUG
        formatter: simple
        stream: ext://sys.stdout

    file:
        class: logging.handlers.RotatingFileHandler
        level: INFO
        formatter: simple
        filename: app_test.log
        maxBytes: 10485760 # 10MB
        backupCount: 20
        encoding: utf8

loggers:
    <module name>.<py file>:
        level: DEBUG
        handlers: [console]
        propagate: no
    <module name>:
        level: DEBUG
        handlers: [console]
        propagate: no

root:
    level: INFO
    handlers: [console, file]


# 2: main.py

import logging
import logging.config

def setup_logging(default_path='logging.yaml', default_level=logging.INFO, env_key='LOG_CFG'):
    """Setup logging configuration
    """
    print("Path:")
    for i in os.listdir("."):
        print(i)
    config_path = default_path
    value = os.getenv(env_key, None)
    if value:
        config_path = value
    if os.path.exists(config_path):
        with open(config_path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
        logging.info("Logging successfully configured from {0}".format(config_path))
    else:
        logging.basicConfig(level=default_level)
        logging.warn("No logging configuration found. Using default configuration.")

# 3: test.py

import logging

def testF(abc):
    logger = logging.getLogger(__name__)
    try:
        logger.debug("Starting ...")
	...		
	logger.debug("...finished ")
        return result

    except Exception as e:
        logger.error("Error processing : {0}".format(e))

```

## CI vs CD in Python
> https://www.atlassian.com/continuous-delivery/principles/continuous-integration-vs-delivery-vs-deployment  



## code coverage
> https://coverage.readthedocs.io/en/v4.5.x/  

```
pip install coverage 

coverage run --source <PY PACKAGE FOLDER> -m pytest 	# find the py package 
coverage report -m --fail-under=80			# fail if less than 80% code coverage
coverage html						# generate html report

```

## style check
> https://realpython.com/python-code-quality/   

```
flake8 <PY PACKAGE FOLDER>
pylint <PY PACKAGE FOLDER> --ignore= <PY PACKAGE FOLDER>/tests

```

## tox
> https://tox.readthedocs.io/en/latest/  

- tox aims to automate and standardize testing in Python.  

-tox.ini  
```
[tox]
envlist = py36tox

[testenv]
setenv =
    PYTHONPATH={toxinidir}
    LC_ALL=en_US.UTF-8
    LANG=en_US.UTF-8
whitelist_externals =
    pytest
commands =
    pytest 

[testenv:abc]
whitelist_externals =
commands =
```

## Function channing  
> https://medium.com/@adamshort/python-gems-5-silent-function-chaining-a6501b3ef07e

## Resizing Jupyter notebook  
> https://medium.com/@1522933668924/using-matplotlib-in-jupyter-notebooks-comparing-methods-and-some-tips-python-c38e85b40ba1  

```
from IPython.display import display, HTML

display(HTML(data="""
<style>
    div#notebook-container    { width: 95%; }
    div#menubar-container     { width: 65%; }
    div#maintoolbar-container { width: 99%; }
</style>
"""))
``` 

# Python Anti-Patterns
> https://docs.quantifiedcode.com/python-anti-patterns/index.html   

 1. Correctness
 2. Maintainability
 3. Readability
 4. Security
 5. Performance
 
 
# Clean Code notes...

## The KeyWords
- DRY/OAOO
The ideas of Don't Repeat Yourself (DRY) and Once and Only Once (OAOO)

- YAGNI
YAGNI (short for You Ain't Gonna Need It) is an idea you might
want to keep in mind very often when writing a solution if you do
not want to over-engineer it.

- KIS
KIS (stands for Keep It Simple) relates very much to the previous
point. When you are designing a software component, avoid overengineering
it; ask yourself if your solution is the minimal one that
fits the problem.

- EAFP/LBYL
EAFP (stands for Easier to Ask Forgiveness than
Permission), while LBYL (stands for Look Before You Leap).

- Mixins
A mixin is a base class that encapsulates some common behavior
with the goal of reusing code. Typically, a mixin class is not useful
on its own, and extending this class alone will certainly not work,
because most of the time it depends on methods and properties that
are defined in other classes. The idea is to use mixin classes along
with other ones, through multiple inheritance, so that the methods
or properties used on the mixin will be available.

- SOLID principles
    - S: Single responsibility principle ; a class) must have only one responsibility.   Again, the smaller the class, the better.
    - O: Open/closed principle; open to extension but closed for modification.
    - L: Liskov's substitution principle; series of properties that an object type must hold to preserve reliability on its design.
    - I: Interface segregation principle; that interfaces (set of methods an object expose) should be small.
    - D: Dependency inversion principle; making it independent of things that are fragile, volatile, or out of our control

- Decorators : decorators wrap a function, modifying its behavior.
    - is a mechanism to simplify the way functions and methods are
defined when they have to be modified after their original definition.
    - Decorators are just syntax sugar for calling
whatever is after the decorator as a first parameter of the decorator
itself, and the result would be whatever the decorator returns.
    - original is the decorated function,
often also called a wrapped object.
    -   Use of decorators: Transforming parameters, Tracing code, Validate parameters, Implement retry operations, Simplify classes by moving some (repetitive) logic
        into decorators

## DockString vs Annotations

```python
class cls_no_use:
    def __init__(self, a, b):
        self.a = a
        self.b =b

        def _func_add(a: int = 10, b: int = 10) -> cls_no_use:
    """This func dose nothing but addition!"""
    return a+b
```

- DockString  
```python
_func_add.__doc__

'This func dose nothing but addition!'
```

- Annotations 
```python
_func_add.__annotations__

{'a': int, 'b': int, 'return': __main__.cls_no_use}
```

- doctest
The doctest module searches for pieces of text that look like interactive Python sessions, and then executes those sessions to verify that they work exactly as shown. 

```python
def my_fun():
    """
    this is my_fun
    Example:
    ::
        >>> assert my_fun() == None
        >>>
    """
```
- Finally  
```python
print(f'_func_add(): {_func_add()}')
print(f'_func_add(20): {_func_add(20)}')
print(f'_func_add(20,20): {_func_add(20,20)}')

_func_add(): 20
_func_add(20): 30
_func_add(20,20): 40
```

## Context managers  
- Using `with` is recomended!  

- General way  
```python
def _func_stop():
    print("Stop")

def _func_start():
    print("Start")
    
class DoNothing:
    def __enter__(self):
        _func_stop()
        return self
    
    def __exit__(self,str_type,str_value,str_traceback):
        _func_start()
        
def func_rolling():
    print("Lest get rolling!")
    

with DoNothing():
    func_rolling()
Stop
Lest get rolling!
Start
```

- Yet another way
```python
import contextlib
​
@contextlib.contextmanager
def func_do_nnothing():
    _func_stop()
    yield
    _func_start()
    
with func_do_nnothing():
    func_rolling()
    
Stop
Lest get rolling!
Start
```

## EAFP (stands for Easier to Ask Forgiveness than Permission), while LBYL (stands for Look Before You Leap).  
> https://docs.quantifiedcode.com/python-anti-patterns/readability/asking_for_permission_instead_of_forgiveness_when_working_with_files.html  


```python
if os.path.exists(filename):
with open(filename) as f:
```

Prefer EAFP over LBYL.  
```python
try:
with open(filename) as f:
...
except FileNotFoundError as e:
logger.error(e)
```


## Mutable default arguments  
Simply put, don't use mutable objects as the default arguments of
functions. If you use mutable objects as default arguments, you will
get results that are not the expected ones.

## How arguments are copied to functions  
The first rule in Python is that all arguments are passed by a value. Always.

```python 
def _func_test_agrs(arg):
    arg += " in func"
    return arg
​
immutable = " hello world"
print(_func_test_agrs(immutable))
print(immutable)
​
mutable = list(" hello world")
print(_func_test_agrs(mutable))
print(mutable)
 hello world in func
 hello world
[' ', 'h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', ' ', 'i', 'n', ' ', 'f', 'u', 'n', 'c']
[' ', 'h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', ' ', 'i', 'n', ' ', 'f', 'u', 'n', 'c']

```

> Don't mutate function arguments. In general, try to avoid side-effects in functions as much as possible.  


## Variable number of arguments  

we can use the packing mechanism and pass them all together in a single instruction:

```python
def _func_pack_args(arg1,arg2,arg3):
    print(arg1)
    print(arg2)
    print(arg3)
​
v1 = 10    
v2 = 20
v3 = 30
l = [v1,v2,v3]
# _func_pack_args(l)
#TypeError: _func_pack_args() missing 2 required positional arguments: 'arg2' and 'arg3'
​
_func_pack_args(*l)
10
20
30
```

Pass any # of args.
```python
def _func_veriable_args(*args):
    for arg in args:
        print(arg)
​
_func_veriable_args(10,20,30)        
10
20
30
```

## Static Type Checking in Python 3.6  

> https://medium.com/@ageitgey/learn-how-to-use-static-type-checking-in-python-3-6-in-10-minutes-12c86d72677b

## EDA with Seaborn and matplotlib  
```
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
```
> [sub plot management](https://jakevdp.github.io/PythonDataScienceHandbook/04.08-multiple-subplots.html)  
> https://www.kaggle.com/bombatkarvivek/pyspark-ml-pipeline-with-titanic-dataset-eda  


## Jupyter Notebook call from command line
This even can run the spark applications.
```
FILE_NAME=dummy3 jupyter nbconvert --to notebook --execute dummy_utility.ipynb 
[NbConvertApp] Converting notebook dummy_utility.ipynb to notebook
[NbConvertApp] Executing notebook with kernel: python3
...
```

- in notebook
```python
file_name = os.environ.get('FILE_NAME','dummy_default_name')
```
-  https://nbconvert.readthedocs.io/en/latest/execute_api.html  
-  https://pythonhosted.org/jupyter_runner/

## argparse
> https://docs.python.org/3/library/argparse.html

```python
parser = argparse.ArgumentParser(description='some description', 
			formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument('--arg1=', 
		help='what is arg1...',
		type=str, 
		default='Other', 
		dest='environment', 
		required=False)

args = parser.parse_args()
print(args.environment)
```

```bash
python test_argparse.py --arg1=="hello world!"
```

## structlog
> http://www.structlog.org/en/stable/getting-started.html . 

```python
chain = [
    structlog.stdlib.filter_by_level,
    structlog.stdlib.add_log_level,
    structlog.processors.StackInfoRenderer(),
    structlog.processors.format_exc_info,
    structlog.processors.JSONRenderer()
]

log_format = "%(filename)s:%(lineno)s %(funcName)10s %(message)s"


logging.basicConfig(level=log_level,
		stream=sys.stdout,
		format=log_format)

structlog.configure_once(
processors=chain,
context_class=dict,
logger_factory=structlog.stdlib.LoggerFactory(),
wrapper_class=structlog.stdlib.BoundLogger,
cache_logger_on_first_use=True,
)

logger = structlog.get_logger()

logger.info()
logger.degub()
...

```

## logdecorator
> https://pypi.org/project/logdecorator/ . 
```python
from logdecorator import log_on_start, log_on_end, log_on_error

logger = structlog.get_logger()

@log_on_start(logging.INFO, "start ...", logger=logger)
@log_on_end(logging.INFO, "finish ...", logger=logger)
@log_on_error(logging.ERROR, "Error ...",
              reraise=True)
def handle(*, country: int,
...
```

## DESIGN PATTERNS in PYTHON
> https://refactoring.guru/design-patterns/python
- video guides