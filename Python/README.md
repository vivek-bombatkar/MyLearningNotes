# Python-Basics
> its fun learning python (again!) :-)

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

## Deployment pipeline for python project

### A. test module

```make test```

- pull docker image from nexux   
- run docker container for test 

```python setup.py test```

- ***setup.py***

### B. build and release

```make compile```

- wheel ```setup.py bdist_wheel```

- create <>.zip

```make release```

- pipenv run pip install twine && pipenv run twine upload --config-file $(PYPIRC_PATH) -r nexus <>.zip

- ***Makefile*** 

- ***setup.py***


## pytest 


## Project setup

- makefile
    - make shell : This commands sets up the complete pipenv environment including the runtime dependencies you've defined in setup.py and enters this virtual environment. This is usually used for quick scripting tests in the python console.  
    - make notebook : Similar to make shell this creates a complete virtual environment and starts the jupyter notebook server in this environment.  
    - make install: Installs you modules into the local virtual environment using setuptools for testing purpose.  
    - make release: Creates a source distribution of your modules and releases it to nexus to share it with others. There is one constraint implemented on this release target.  
    
```bash
    #example make file
    
    
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

- Dockerfile
    - FROM
    - LABEL
    - RUN
- setup.py
- logging.yaml
- README.RST

## python packages
> https://docs.python.org/3/reference/import.html  

|Regular packages|Namespace packages|
| --- | --- |
| typically implemented as a directory containing an \__init__.py file |  is a composite of various portions, where each portion contributes a subpackage to the parent package|
| When imported, \__init__.py file is implicitly executed, and the objects it defines are bound to names in the package’s namespace. | there is no \__init__.py file |

***The \__init__.py file can contain the same Python code that any other module can contain, and Python will add some additional attributes to the module when it is imported.***


## python egg and wheel 
> https://packaging.python.org/discussions/wheel-vs-egg/  
> http://peak.telecommunity.com/DevCenter/PythonEggs  
> https://www.blog.pythonlibrary.org/2012/07/12/python-101-easy_install-or-how-to-create-eggs/  
> https://mrtopf.de/en/a-small-introduction-to-python-eggs/  
- Same concept as a .jar file in Java, it is a .zip file with some metadata files renamed .egg, for distributing code as bundles
- is a logical structure embodying the release of a specific version of a Python project, comprising its code, resources, and metadata.  

| wheel | egg |  
| --- | --- |  
| Wheel is a distribution format, i.e a packaging format. |  both a distribution format and a runtime installation format (if left zipped), and was designed to be importable. |  
| Wheel archives do not include .pyc files. | |  
| Wheel is internally organized by sysconfig path type, therefore making it easier to convert to other formats. | | 
  

## TypeError vs ValueError  
> https://www.datacamp.com/community/tutorials/exception-handling-python  

| TypeError | ValueError |
| --- | --- |
| Passing arguments of the wrong type (e.g. passing a list when an int is expected) should result in a TypeError | Raised when a built-in operation or function receives an argument that has the right type but an inappropriate value | 
| Whenever you see an error that include 'NoneType' that means that you have an operand or an object that is None when you were expecting something else. | |


## CONDA - environment manager
> https://medium.freecodecamp.org/why-you-need-python-environments-and-how-to-manage-them-with-conda-85f155f4353c  
> https://conda.io/docs/_downloads/conda-cheatsheet.pdf  

```bash
$ conda create MyEnv python=3.6 

$ source activate MyEnv
(MyEnv) $
```

### conda environments  
> https://conda.io/docs/user-guide/tasks/manage-environments.html#activating-an-environment

