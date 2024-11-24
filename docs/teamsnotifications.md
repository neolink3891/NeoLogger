## TeamsNotification

The TeamsNotification class allows you to send notifications to Microsoft Teams channels via incoming webhooks.

### Standard Notification

To send a standard notification import the required libraries.

```
from neologger import TeamsNotification
```

And create an object of the TeamsNotification.

```
# Initialize the TeamsNotification instance
teams = TeamsNotification()
```

Before sending any notification, you will need to add the webhook to send the notifications to.

```
# Set your Teams webhook URL
teams.set_hook("YOUR_WEBHOOK_URL")
```

Version 1.3.1 supports standar and adaptative notification types.

### Standard Notification

This is the default notification type, just add the Title, Summary, and the Text for the notification.

```
# Assemble the standard notification
teams.assembly_standard_notification(
    title="NOTIFICATION'S TITLE",
    summary="This is the summary.",
    text="This is the text within the notification body, one single paragraph."
)
```

Then just call the _send()_ method.

```
# Send the notification
result_ok, result_message = teams.send()


print("Result:", result_ok)
print("Response:", result_message)
```

<p align="center">
  <img src="imgs/teams_1.png" alt="NeoLogger Banner">
</p>

This method returns _result_ok:_ True if the notifcation was send, False if there was any problem. and _result_message:_ and string with OK if the notifaction was sent, otherwise it will retund a descritive message.

### Adaptative Notification

For richer content, you can send adaptive card notifications. This type allows to setup a profile name and image, as well as more detail messages.  
After setting the webhook url, to define it as Adaptative notification, set the image (public url) and name of the profile.

```
# Set profile image and name (optional)
teams.set_profile_image("YOUR_PUBLIC_PROFILE_IMAGE_URL")
teams.set_profile_name("Profile Name")
```

Set the Title if the notification, this is what will be shown on top.

```
# Assemble the adaptive card notification
teams.set_adaptative_notification("THIS IS THE NOTIFICATION TITLE")
```

You can add as many lines of content as you need.

```
# Add data lines to the adaptive card
teams.add_data("Line 1")
teams.add_data("Line 2")
teams.add_data("Line 3")
```

And, invoke the _send()_ method

```
# Send the notification
result_ok, result_message = teams.send()

print("Result:", result_ok)
print("Response:", result_message)
```

<p align="center">
  <img src="imgs/teams_2.png" alt="NeoLogger Banner">
</p>

### Bonus: Configuring a Teams Incoming Webhook

To send notifications to Microsoft Teams, set up an incoming webhook:

1. Navigate to the channel where you want to receive notifications.

2. Click on the "..." next to the channel name and select Connectors.

3. Search for Incoming Webhook and click Add.

4. Configure the webhook by providing a name and, optionally, an image.

5. Copy the generated webhook URL.

6. Use the webhook URL in your code.