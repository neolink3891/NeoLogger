## StompBabbler

```
from neologger import StompBabbler

# Initialize the babbler
stomp_babbler = StompBabbler(
    user_name="username",
    user_password="password",
    queue="/queue/destination",
    server="stomp.server.com",
    port=61613
)

# Send a message
message = {"key": "value"}
status, response = stomp_babbler.babble(message)

if status:
    print("Message sent successfully.")
else:
    print(f"Failed to send message: {response}")
```