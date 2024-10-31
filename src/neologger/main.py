# neologger/main.py

from datetime import datetime
import time
import logging
from .core import FontColour, BackgroundColour, FontStyle, Icon, Template
import stomp
import json
import inspect
import requests

# Configure the logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class NeoLogger:
    """
    A custom logger class that provides advanced logging features with customizable
    colors, styles, and templates for log messages.
    """

    def __init__(self, initialized_by):
        """
        Initialize the NeoLogger with default styling.

        Args:
            initialized_by (str): The name of the module or script that initializes the logger.
        """
        self.initialized_by = initialized_by
        self.date_colour = FontColour.WHITE
        self.date_style = FontStyle.NORMAL
        self.file_colour = FontColour.WHITE
        self.file_style = FontStyle.NORMAL
        self.function_colour = FontColour.WHITE
        self.function_style = FontStyle.NORMAL
        self.text_colour = FontColour.WHITE
        self.text_style = FontStyle.NORMAL
        self.markers = {}

    def set_log_font_colour(self, date_colour, file_colour, function_colour, text_colour):
        """
        Set the font colors for different parts of the log message.

        Args:
            date_colour (str): ANSI escape code for the date color.
            file_colour (str): ANSI escape code for the file name color.
            function_colour (str): ANSI escape code for the function name color.
            text_colour (str): ANSI escape code for the log message text color.
        """
        self.date_colour = date_colour
        self.file_colour = file_colour
        self.function_colour = function_colour
        self.text_colour = text_colour

    def set_log_font_style(self, date_style, file_style, function_style, text_style):
        """
        Set the font styles for different parts of the log message.

        Args:
            date_style (str): ANSI escape code for the date style.
            file_style (str): ANSI escape code for the file name style.
            function_style (str): ANSI escape code for the function name style.
            text_style (str): ANSI escape code for the log message text style.
        """
        self.date_style = date_style
        self.file_style = file_style
        self.function_style = function_style
        self.text_style = text_style

    def set_template(self, template_name):
        """
        Apply a predefined template to the logger.

        Args:
            template_name (str): The name of the template to apply.
        """
        if template_name == Template.DARK:
            self.set_log_font_colour(
                FontColour.YELLOW, FontColour.GREEN, FontColour.CYAN, FontColour.GREY
            )
            self.set_log_font_style(
                FontStyle.BOLD, FontStyle.NORMAL, FontStyle.ITALIC, FontStyle.NORMAL
            )
        elif template_name == Template.BASE:
            self.set_log_font_colour(
                FontColour.CYAN, FontColour.YELLOW, FontColour.BLUE, FontColour.MAGENTA
            )
            self.set_log_font_style(
                FontStyle.BOLD, FontStyle.NORMAL, FontStyle.ITALIC, FontStyle.NORMAL
            )
        else:
            # Default template
            self.set_log_font_colour(
                FontColour.WHITE, FontColour.WHITE, FontColour.WHITE, FontColour.WHITE
            )
            self.set_log_font_style(
                FontStyle.NORMAL, FontStyle.NORMAL, FontStyle.NORMAL, FontStyle.NORMAL
            )

    def log_this(self, message):
        """
        Log a general information message with the current styling.

        Args:
            message (str): The message to log.
        """
        stack = inspect.stack()
        from_here = stack[1].function
        logging.info(
            self.date_colour
            + self.date_style
            + f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            + FontStyle.ENDC
            + " - "
            + self.file_colour
            + self.file_style
            + f"{self.initialized_by} >> "
            + FontStyle.ENDC
            + self.function_colour
            + self.function_style
            + f"{from_here} | "
            + FontStyle.ENDC
            + self.text_colour
            + self.text_style
            + f"{message}"
            + FontStyle.ENDC
        )

    def log_this_warning(self, message):
        """
        Log a warning message with a warning icon and styling.

        Args:
            message (str): The warning message to log.
        """
        stack = inspect.stack()
        from_here = stack[1].function
        logging.warning(
            FontColour.YELLOW
            + FontStyle.BOLD
            + "["
            + Icon.WARNING
            + " WARNING]"
            + FontColour.ENDC
            + self.date_colour
            + self.date_style
            + f" {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            + FontStyle.ENDC
            + " - "
            + self.file_colour
            + self.file_style
            + f"{self.initialized_by} >> "
            + FontStyle.ENDC
            + self.function_colour
            + self.function_style
            + f"{from_here} | "
            + FontStyle.ENDC
            + self.text_colour
            + self.text_style
            + f"{message}"
            + FontStyle.ENDC
        )

    def log_this_ok(self, message):
        """
        Log a success message indicating an operation was OK.

        Args:
            message (str): The success message to log.
        """
        stack = inspect.stack()
        from_here = stack[1].function
        logging.info(
            FontColour.GREEN
            + FontStyle.BOLD
            + "["
            + Icon.DONE
            + " OK]"
            + FontColour.ENDC
            + self.date_colour
            + self.date_style
            + f" {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            + FontStyle.ENDC
            + " - "
            + self.file_colour
            + self.file_style
            + f"{self.initialized_by} >> "
            + FontStyle.ENDC
            + self.function_colour
            + self.function_style
            + f"{from_here} | "
            + FontStyle.ENDC
            + self.text_colour
            + self.text_style
            + f"{message}"
            + FontStyle.ENDC
        )

    def log_this_error(self, message):
        """
        Log an error message with an error icon and styling.

        Args:
            message (str): The error message to log.
        """
        stack = inspect.stack()
        from_here = stack[1].function
        logging.error(
            FontColour.RED
            + FontStyle.BOLD
            + "["
            + Icon.ERROR
            + " ERROR]"
            + FontColour.ENDC
            + self.date_colour
            + self.date_style
            + f" {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            + FontStyle.ENDC
            + " - "
            + self.file_colour
            + self.file_style
            + f"{self.initialized_by} >> "
            + FontStyle.ENDC
            + self.function_colour
            + self.function_style
            + f"{from_here} | "
            + FontStyle.ENDC
            + self.text_colour
            + self.text_style
            + f"{message}"
            + FontStyle.ENDC
        )

    def log_this_completed(self, message):
        """
        Log a message indicating a task has been completed.

        Args:
            message (str): The completion message to log.
        """
        stack = inspect.stack()
        from_here = stack[1].function
        logging.info(
            FontColour.CYAN
            + FontStyle.BOLD
            + "["
            + Icon.BULLSEYE
            + " COMPLETED]"
            + FontColour.ENDC
            + self.date_colour
            + self.date_style
            + f" {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            + FontStyle.ENDC
            + " - "
            + self.file_colour
            + self.file_style
            + f"{self.initialized_by} >> "
            + FontStyle.ENDC
            + self.function_colour
            + self.function_style
            + f"{from_here} | "
            + FontStyle.ENDC
            + self.text_colour
            + self.text_style
            + f"{message}"
            + FontStyle.ENDC
        )

    def log_this_success(self, message):
        """
        Log a success message with a star icon.

        Args:
            message (str): The success message to log.
        """
        stack = inspect.stack()
        from_here = stack[1].function
        logging.info(
            FontColour.MAGENTA
            + FontStyle.BOLD
            + "["
            + Icon.STAR
            + " SUCCESS]"
            + FontColour.ENDC
            + self.date_colour
            + self.date_style
            + f" {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            + FontStyle.ENDC
            + " - "
            + self.file_colour
            + self.file_style
            + f"{self.initialized_by} >> "
            + FontStyle.ENDC
            + self.function_colour
            + self.function_style
            + f"{from_here} | "
            + FontStyle.ENDC
            + self.text_colour
            + self.text_style
            + f"{message}"
            + FontStyle.ENDC
        )

    def get_time_mark(self):
        """
        Get the current time in seconds since the Epoch.

        Returns:
            float: The current time in seconds.
        """
        return time.time()

    def log_with_elapsed_time(self, message, start_time):
        """
        Log a message along with the elapsed time since a given start time.

        Args:
            message (str): The message to log.
            start_time (float): The start time to calculate elapsed time from.

        Returns:
            str: A string indicating the elapsed time.
        """
        stack = inspect.stack()
        from_here = stack[1].function
        elapsed_time = time.time() - start_time
        logging.info(
            self.date_colour
            + self.date_style
            + f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            + FontStyle.ENDC
            + " - "
            + self.file_colour
            + self.file_style
            + f"{self.initialized_by} >> "
            + FontStyle.ENDC
            + self.function_colour
            + self.function_style
            + f"{from_here} | "
            + FontStyle.ENDC
            + self.text_colour
            + self.text_style
            + f"{message}"
            + FontStyle.ENDC
            + FontColour.GREY
            + FontStyle.ITALIC
            + f" [Elapsed time: {elapsed_time} seconds.]"
            + FontStyle.ENDC
        )
        return f"Elapsed time: {elapsed_time} seconds."

class StompBabbler:
    """
    A class to send messages over STOMP (Simple Text Oriented Messaging Protocol).
    """

    def __init__(self, userName, userPassword, queue, server, port):
        """
        Initialize the STOMP connection parameters.

        Args:
            userName (str): The username for the STOMP server.
            userPassword (str): The password for the STOMP server.
            queue (str): The destination queue to send messages to.
            server (str): The STOMP server address.
            port (int): The port number of the STOMP server.
        """
        self.stompUsername = userName
        self.stompPassword = userPassword
        self.stompQueue = queue
        self.stompServer = server
        self.stompPort = port

    def babble(self, message):
        """
        Send a message to the configured STOMP queue.

        Args:
            message (dict): The message payload to send.

        Returns:
            tuple: A tuple containing a boolean status and a message.
        """
        try:
            # Establish a connection to the STOMP server
            stompConnection = stomp.Connection([(self.stompServer, self.stompPort)])
            stompConnection.connect(self.stompUsername, self.stompPassword, wait=True)

            # Convert the message to JSON and send it
            json_message = json.dumps(message)
            stompConnection.send(body=json_message, destination=self.stompQueue)

            # Disconnect after sending the message
            stompConnection.disconnect()

            return True, "OK"
        except stomp.exception.ConnectFailedException as ex:
            return False, f"Connection failed: {str(ex)}"
        except Exception as ex:
            return False, str(ex)

class SlackNotification:
    """
    A class to assemble and send notifications to Slack via a webhook.
    """

    def __init__(self):
        """
        Initialize the SlackNotification with default values.
        """
        self.data = []
        self.hook = ""
        self.ready = False
        self.body = None

    def add_data(self, field_name, field_value):
        """
        Add a field to the notification data.

        Args:
            field_name (str): The name of the field.
            field_value (str): The value of the field.
        """
        self.data.append({"name": field_name, "value": field_value})

    def set_hook(self, hook):
        """
        Set the Slack webhook URL.

        Args:
            hook (str): The Slack webhook URL.
        """
        self.hook = hook
        self.ready = True

    def assembly_notification(self, title, summary, icon=""):
        """
        Assemble the notification payload to send to Slack.

        Args:
            title (str): The title of the notification.
            summary (str): A summary message.
            icon (str, optional): An emoji icon to include in the header. Defaults to "".
        """
        blocks = []

        # Add a header with optional icon
        if len(icon) > 0:
            blocks.append({
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": f":{icon}: - {title}",
                    "emoji": True
                }
            })
        else:
            blocks.append({
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": f"{title}",
                    "emoji": True
                }
            })

        blocks.append({"type": "divider"})

        # Add the summary section
        blocks.append({
            "type": "section",
            "text": {
                "type": "plain_text",
                "text": summary,
                "emoji": True
            }
        })

        # Add fields from the data list in pairs
        while self.data:
            row = {"type": "section"}
            row_fields = []

            # Pop the first item and add it to the fields
            item1 = self.data.pop()
            row_fields.append({
                "type": "mrkdwn",
                "text": f"*{item1['name']}:*\n{item1['value']}"
            })

            # Pop the second item if available and add it
            if len(self.data) > 0:
                item2 = self.data.pop()
                row_fields.append({
                    "type": "mrkdwn",
                    "text": f"*{item2['name']}:*\n{item2['value']}"
                })

            row['fields'] = row_fields
            blocks.append(row)

        blocks.append({"type": "divider"})

        # Set the assembled blocks as the message body
        self.body = {"blocks": blocks}

    def send(self):
        """
        Send the assembled notification to Slack.

        Returns:
            tuple: A tuple containing a boolean status and a message.
        """
        if self.ready:
            if self.body is not None:
                try:
                    response = requests.post(
                        self.hook,
                        data=json.dumps(self.body),
                        headers={'Content-Type': 'application/json'}
                    )

                    if response.status_code == 200:
                        return True, "OK"
                    else:
                        return False, f"HTTP Error: {response.status_code}"
                except requests.exceptions.RequestException as ex:
                    return False, f"Request error: {str(ex)}"
                except Exception as ex:
                    return False, str(ex)
            else:
                return False, "Empty Body"
        else:
            return False, "Not Ready"