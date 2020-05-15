---
noteId: "cf2a9d1096a811ea9e7f53bbf66be716"
tags: []

---

# pipenv

https://realpython.com/pipenv-guide/

## intro
I have no idea what pipenv is.

## why pipenv

current dependency management does not work well.

1. for one project, if you need the latest package of one lib which introduces the conflict with the other package.
2. dependency resolution: two packages require different version of a sub-dependency package. 

## how pipenv

```bash
pip install pipenv #install
pipenv shell #create a virtual environment
pipenv install flask==0.12.1 # and then pipfile and pipfile.locl will be created.
pipenv install pytest --dev #put the dependency in a special dev-packges locatioin in the pipfile.
pipenv lock #local the environment
pipenv install --ignore-pipfile #installthe last successful environment recorded. ignore-pipfile will use pipfile.lock.
pip install --dev #install the environment for development
pipenv graph --reverse # show the dependencies
```

## tips
1. pipenv install -e (editable) is required to do sub-dependency resolution
2. pipfile is like requirements.txt

