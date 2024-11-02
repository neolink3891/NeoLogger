
## SlackNotification

```
from neologger import SlackNotification
import os

# Initialize the notification
slack_notification = SlackNotification()

# Set the Slack webhook URL (ensure this is stored securely)
slack_notification.set_hook(os.getenv("SLACK_WEBHOOK_URL"))

# Add data fields
slack_notification.add_data("Environment", "Production")
slack_notification.add_data("Status", "Operational")
slack_notification.add_data("Version", "1.0.0")

# Assemble the notification
slack_notification.assemble_notification(
    title="System Status Update",
    summary="All systems are running smoothly.",
    icon="white_check_mark"  # Use Slack emoji code without colons
)

# Send the notification
status, response = slack_notification.send()

if status:
    print("Notification sent successfully.")
else:
    print(f"Failed to send notification: {response}")
```

## Configuration

Environment Variables   
SLACK_WEBHOOK_URL: The webhook URL for sending Slack notifications. It is recommended to store this securely, such as in environment variables or a configuration file not checked into version control.
