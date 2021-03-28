
import requests
import stompclient
import sys

if len(sys.argv) < 3:
    print("Usage: python selectsample.py <user> <pass>")
    exit(1)

username=sys.argv[1]
password=sys.argv[2]

auth_response = requests.post(
    "https://api.alphaflash.com/api/auth/alphaflash-client/token", 
    json = { 'username':username, 'password':password } 
)

if auth_response.status_code != 200:
    print("Login failed")
    exit(1)

print("Login successful")

access_token = auth_response.json()['access_token']

calendar_data = calendar_data = requests.get(
    "https://api.alphaflash.com/api/select/calendar/events",
    headers = {"Authorization": "Bearer " + access_token}
)

if calendar_data.status_code != 200:
    print("Failed to fetch calendar data")
    exit(1)

print("Recevied calendar data")

stompConnection = stompclient.StompConnection(
    host="select.alphaflash.com",port=61614,access_token=access_token
    )

if stompConnection.connectResponse.type != "CONNECTED":
    print("STOMP connection failed")
    exit(1)

print("STOMP connection successful, waiting for data")


while True:
    message = stompConnection.recv_message()

    print("------- MESSAGE --------")
    print(message.type)
    for h in message.headers:
        print(h)
    print(message.body)
    print("---- END OF MESSAGE ----")


