# logging

## Introduction

- resources: [real python tutorial](httpsL//realpython.com/python-logging)

## key takeaways

### level of serverity

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL


```python
import logging
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
```

note:
1. the default logger is named with `root`
2. by default, the logging module logs the messages with a severity level of WARNING or above.


### basic configuration

- set the logger level
```python
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug("This will get logged")
```

- set the logging file
```python
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')
```

filemode 'w' will rewrite the file at each run. The default mode is 'a', which is append.

**note**

-  calling basicConfig() to configure the root logger works only if the root logger has not been configured before. Basically, this function can only be called once.

### Logger class

**example**
```python
import logging

logger = logging.getLogger("example_logger")
logger.warning("This is a warning")
```

**note**
unlike the root logger, a custom logger can’t be configured using basicConfig(). You have to configure it using Handlers and Formatters

