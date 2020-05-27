# shell command

## intro

reference:

[shell commands with Python](https://janakiev.com/blog/python-shell-commands/)
[stackoverflow question](https://stackoverflow.com/questions/89228/calling-an-external-command-from-python/89243#89243)
## implementation

### os.system 
- cannot get the results
- ipython will return return code: 0 for successful and -1 for unsuccessful

### os.popen()
example:

```python
stream = os.popen("echo hello")
output = stream.read()
```

### subprocess

```python
import subprocess
subprocess.run(["ls", "-l"])
```




