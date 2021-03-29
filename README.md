# AlphaFlash Select Python Samples

[[_TOC_]]

This is a python sample for AlphaFlash select.

This was written using python 3.8.

## Running the code

The code can be run with 

    python selectsample.py xxx yyy

Where __xxx__ is your username and __yyy__ is your password. This will use the included simple STOMP implementation 
to connect.  

### Using the [stomp.py](https://pypi.org/project/stomp.py/) library

This code also has a sample using the third party library [stomp.py](https://pypi.org/project/stomp.py/). 

To use this this library, the _stomp.py_ library will need to be installed on the host machine, either as a global
python package, or using [pipenv](https://pypi.org/project/pipenv/) and the included [Pipfile](Pipfile).

Once this is installed the _stomp.py_ sample can be run by passing in an additional argument, "stomp.py", to the
script. 

Example running with pipenv:

    pipenv run python selectsample.py xxx yyy stomp.py

Example running with _stomp.py_ installed as a global package:

    python selectsample.py xxx yyy stomp.py

## About the code

[selectsample.py](selectsample.py) demonstrates logging in and interacting with 
REST apis.

[stompclient.py](stompclient.py) provides a basic stomp client for connectig to 
our real-time data service. __This is intended as a demonstration and should not be used in production as-is!__


## Some useful snippets

Using the authentication service to get a token

```python

auth_response = requests.post(
    "https://api.alphaflash.com/api/auth/alphaflash-client/token", 
    json = { 'username':username, 'password':password } 
)

if auth_response.status_code != 200:
    print("Login failed")
    exit(1)

```

Getting calendar data

```python

calendar_data = requests.get(
    "https://api.alphaflash.com/api/select/calendar/events",
    headers = {"Authorization": "Bearer " + access_token}
)

```

Making a STOMP connection with [stomp.py](https://pypi.org/project/stomp.py/)

```python

# TODO - replace this with your message handling code
listener = stomp.PrintingListener()

c = stomp.Connection([("select.alphaflash.com",61614)],use_ssl=True,heartbeats=(0,30000))

c.set_listener('my_listener',listener)

c.connect(passcode=access_token, wait=True)

c.subscribe("/topic/observations",1)

```

