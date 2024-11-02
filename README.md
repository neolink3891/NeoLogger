# NeoLogger

A collection of Python notification classes for enhanced logging, messaging, and Slack notifications.

## Overview

NeoNotifications provides a set of tools to improve logging output with customizable styles, send messages over STOMP protocol, and send Slack notifications with rich formatting.

## Features

- **NeoLogger**: Advanced logging with customizable colors, styles, and templates.
- **StompBabbler**: Send messages over STOMP protocol to a specified queue.
- **SlackNotification**: Assemble and send richly formatted notifications to Slack channels via webhooks.

## Installation

You can install NeoNotifications via pip:

```bash
pip install neologger
```

## Requirements

Python 3.6 or higher

## Dependencies:
stomp.py    
requests

## Usage

### NeoLogger

Basic Usage

```
from neologger import NeoLogger

# Initialize the logger
neologger = NeoLogger("your_script.py")

# Log messages
neologger.log_this("This is a general information message.")
neologger.log_this_warning("This is a warning message.")
neologger.log_this_error("This is an error message.")
```

## Customizing Styles and Templates

```
from neologger import NeoLogger, Template

# Initialize the logger
neologger = NeoLogger("your_script.py")

# Set a predefined template
neologger.set_template(Template.DARK)

# Log messages with the new style
neologger.log_this("This message uses the DARK template.")
```

## Measuring Elapsed Time

```
# Get a time mark
start_time = neologger.get_time_mark()

# ... perform some operations ...

# Log with elapsed time
neologger.log_with_elapsed_time("Operation completed.", start_time)
```

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

## Table Logging with NeoLogger

In addition to logging messages and notifications, NeoLogger now includes a Table class to help you format and display tabular data within your logs. This feature is ideal for displaying structured data in an easy-to-read format.

### Key Features
Set Table Headers: Define column headers for your table.
Customize Borders: Option to add borders around the table for clearer readability.
Display Row Counts: Option to display the total number of rows at the end of the table.
Auto-Adjust Column Widths: The table dynamically adjusts column widths based on the longest content in each column.
Usage
Here’s how to create and use a table with NeoLogger.

### Basic Table Example
```
from neologger import Table, TableRow

# Initialize the Table
table = Table()
table.set_title("User Information Table")

# Set table headers
table.set_header(["ID", "Name", "Role"])

# Add rows of data
row1 = table.new_row()
row1.add_data(["1", "Alice", "Developer"])
table.push_row(row1)

row2 = table.new_row()
row2.add_data(["2", "Bob", "Manager"])
table.push_row(row2)

row3 = table.new_row()
row3.add_data(["3", "Charlie", "Analyst"])
table.push_row(row3)

# Enable borders and row count display
table.enable_border()
table.enable_total()

# Calculate column sizes and draw the table
table.calculate_sizes()
table.draw_lines()
```

### Output Example

The above code would output something like:

```
USER INFORMATION TABLE
------------------------------
| ID  | Name     | Role      |
------------------------------
| 1   | Alice    | Developer |
| 2   | Bob      | Manager   |
| 3   | Charlie  | Analyst   |
------------------------------
TOTAL ROWS: 3
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

Inspired by the need for customizable logging and notification tools in Python applications.

Utilizes the stomp.py library for STOMP protocol messaging.     
Utilizes the requests library for HTTP requests to Slack webhooks.

## Contact

For questions or suggestions, please contact Pablo Martinez at neolink3891@gmail.com.