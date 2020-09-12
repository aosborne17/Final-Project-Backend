# Logging

- Logging is a good way to keep track of information overtime by storing it in a logging file

- To create a logging file we simply specify the name of a file in our logging method

- We could use print statements but loggings gives us a greater depth of information


## The five logging levels

- DEBUG --> 10
- INFO --> 20
- WARNING --> 30
- ERROR --> 40
- CRITICAL --> 50


## Changing login format

- By default logging only shows us the level name, the logger ('root' in our case) and lastly the message
- We can add many things such as the time of the log etc

## Creating seperate loggers

- For each module that we create we want to use different loggers so we can configure them seperately, we don;t want to
use root for everything

```python
"""
import logging
import boto3
import os

Here we are creating a new logger specific to this module
If ran from this file, the variable will be = main, else if ran elsewhere then the variable will be name of the module,
in this case that will be 'aws_upload'
"""
logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)

# we want the configurations to be same as it was for our root configuration, thus we do the following
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

# here we are specifying a file that will be contain our logs
file_handler = logging.FileHandler('upload_s3_new_logger.log')

# Here we are setting the file that we create to have the following formatting when showing the log messages
file_handler.setFormatter(formatter)

# here we are adding the file handler to our new logger
logger.addHandler(file_handler)

```

- This means that we would no longer need to use the basicConfig that we had for our root

```python
logging.basicConfig(filename='upload_s3.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
```

### We can then add a stream handler that will show the logs in the console

```python
# Here we are creating a stream handler that will log the statements in the console
stream_handler = logging.StreamHandler()

# We must then add the stream handler as we did for the life
logger.addHandler(stream_handler)

```