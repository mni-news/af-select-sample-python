# AlphaFlash Select Python Samples

[[_TOC_]]

This is a python sample for AlphaFlash select.

This was written using python 3.8.

## Running the code

The code can be run with 

    python selectsample.py xxx yyy

Where __xxx__ is your username and __yyy__ is your password. 

## About the code

[selectsample.py](selectsample.py) demonstrates logging in and interacting with 
REST apis.

[stompclient.py](stompclient.py) provides a basic stomp client for connectig to 
our real-time data service. 


## Third party STOMP library

This library contains a grounds up STOMP client which is **not intended for production use as-is**. 

There is an existing [STOMP client here](https://pypi.org/project/stomp.py/)
which may provide a more production ready alternative. 