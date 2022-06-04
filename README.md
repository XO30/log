<h1>log: Logger for Python</h1>

<hr/>

<h2>What is log?</h2>

<p>The log module contains the Logging class, which is a lightweight logger for python. With the module it is possible to log at five different levels. Messages can be output to the console as well as written to a logfile. The class Logging offers some settings to make the usage as easy as possible.</p>

<hr/>

<h2>Quick Start</h2>

<p><b>Import and initialize Logging:</b></p>
<p>Do it this way.</p>

```python
import log
log = log.Logging('example', file_name='example.log', file_mode='w', logging_level='DEBUG', console_output=True)
```

<p>or this way.</p>

```python
from log import Logging
log = Logging('example', file_name='example.log', file_mode='w', logging_level='DEBUG', console_output=True)
```
<p>name is a designation of the logger. file_name contains the document name and path. file_name can also be initialized with None. in this case no logfile is created. file_mode designates the write mode. "a" means that entries are added to the document, "w" causes the old logfile to be overwritten when the class is reinitialized. logging_level determines which messages are added to the logfile. Debug means that all messages are also written to the logfile. console_output specifies whether the messages should also be output to the console.</p>


<p><b>Get some information about the logger:</b></p>
<p>This way you get some information about the logger and the current settings of it.</p>

```python
print(log)
```

<p><b>Write to log:</b></p>
<p>now you can start writing messages to the log. The messages are marked differently depending on the method used.</p>

```python
log.debug('hello')
log.info('this')
log.warning('is')
log.info('a')
log.critical('example')
```

<p><b>Get information of a function:</b></p>
<p>Use @func_log to decorate a function. The decorator can record when a function is called and terminated. furthermore, the description of a function is recorded. The most important function is the interception of error messages.</p>

```python
@log.func_log
def square(x):
    """
    function to square a int
    :param x: int: input nr.
    :return: int: output nr.
    """
    return x ** 2

square(5)
```
