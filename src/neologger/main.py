# neologger/main.py

from datetime import datetime
import time
import logging
from .core import FontColour, BackgroundColour, FontStyle, Icon, Template, Condition
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

    def __init__(self, initialized_by, alarm=None, teams=None, slack=None, stopwatch=None):
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
        self.stopwatch = stopwatch
        self.alarm = alarm
        self.slack = slack
        self.teams = teams

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

    def start_stopwatch(self, title=""):
        self.stopwatch = Stopwatch(title)

    def lap(self, label=""):
        self.stopwatch.lap(label, alarm=self.alarm)

    def log_this_with_trace(self, message):
        stopwatch_data = self.stopwatch.stop()

        self.log_this(message + "\n" + stopwatch_data)

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

        if self.alarm:
            self.alarm.check(elapsed_time, start_time, summary="Function " + from_here + " raised an Alarm", title="NeoLogger Alarm.")

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

class TeamsNotification:

    def __init__(self):
        self.webhook = ""
        self.type = "standard"
        self.title = ""
        self.theme_colour = "0076D7"
        self.summary = ""
        self.text = ""
        self.data = []
        self.teams_type = "MessageCard"
        self.profile_image = ""
        self.profile_name = ""
        self.teams_context = "http://schema.org/extensions"
        self.teams_content_type = "application/vnd.microsoft.card.adaptive"
        self.teams_schema = "http://adaptivecards.io/schemas/adaptive-card.json"
        self.hook_ready = False
        self.content_ready = False
        self.teams_version = "1.6"
    
    def set_hook(self, webhook):
        if len(webhook) > 0:
            self.webhook = webhook
            self.hook_ready = True

    def set_profile_image(self, image):
        self.profile_image = image
    
    def set_profile_name(self, name):
        self.profile_name = name
        
    def add_data(self, line):
        self.data.append({
            "type": "TextBlock",
            "text": line,
            "wrap": True
        })
    
    def assembly_teams_notification(self):
        notification_body = {}
        body = []
        body.append({"type": "TextBlock", "size": "Medium", "weight": "Bolder", "text": self.title})
        body_content = {}
        body_content["type"] = "ColumnSet"
        body_columns = []
        body_columns.append({"type": "Column", "items": [{"type": "Image", "style": "Person", "url": self.profile_image, "altText": self.profile_name, "size": "Small"}], "width": "auto"})
        body_columns.append({"type": "Column", "items": [{"type": "TextBlock", "weight": "Bolder", "text": self.profile_name, "wrap": True}, {"type": "TextBlock", "spacing": "None", "text": "Created on " + datetime.now().strftime('%d-%m-%Y at %H:%M'), "isSubtle": True, "wrap": True}], "width": "stretch"})
        body_content["columns"] = body_columns
        body.append(body_content)
        for dat in self.data:
            body.append(dat)
    
        notification_body["type"] = "AdaptiveCard"

        body_columns_data = {}
        body_columns_data["type"] = "ColumnSet"
        body_columns_data["columns"] = body_columns

        notification_body["body"] = body
        notification_body["$schema"] = self.teams_schema
        notification_body["version"] = self.teams_version

        attachments = []
        attachments_body = {}
        attachments_body["contentType"] = self.teams_content_type
        attachments_body["contentUrl"] = None
        attachments_body["content"] = notification_body
        attachments.append(attachments_body)

        notif = {}
        notif["type"] = "message"
        notif["attachments"] = attachments

        return notif
    
    def assembly_standard_notification(self, title, summary, text):
        self.type = "standard"
        self.data = []
        self.content_ready = True
        if len(title) > 0:
            self.title = title.upper()
        else:
            self.content_ready = False
        
        if len(summary) > 0:
            self.summary = summary
        else:
            self.content_ready = False

        if len(text) > 0:
            self.text = text
        else:
            self.content_ready = False
    
    def set_adaptative_notification(self, title):
        self.type = "AdaptiveCard"
        self.content_ready = True
        if len(title) > 0:
            self.title = title.upper()
        else:
            self.content_ready = False

    def send(self):
        result_ok = True
        result_message = ""

        if self.type == "standard":
            if self.content_ready == True and self.hook_ready == True:
                message = {
                    "@type": self.teams_type,
                    "@context": self.teams_context,
                    "summary": self.summary,
                    "themeColor": self.theme_colour,
                    "title": self.title,
                    "text": self.text
                }

                try:
                    response = requests.post(self.webhook, json=message)

                    if response.status_code == 200:
                        result_message = "OK"
                        self.summary = ""
                        self.title = ""
                        self.text = ""
                        self.content_ready = False
                    else:
                        result_ok = False
                        result_message = "Error" 
                except Exception as ex12:
                    result_ok = False
                    result_message = "Error: " + ex12

        elif self.type == "AdaptiveCard":
            if self.content_ready == True and self.hook_ready == True:

                message = self.assembly_teams_notification()

                try:
                    response = requests.post(self.webhook, json=message)

                    if response.status_code == 200:
                        result_message = "OK"
                        self.title = ""
                        self.text = ""
                        self.content_ready = False

                        self.data = []
                    else:
                        result_ok = False
                        result_message = "Error: " + str(response.status_code) 
                except Exception as ex12:
                    result_ok = False
                    result_message = "Error: " + ex12
        
        return result_ok, result_message


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

        self.data = []

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

class Table:
    """
    A class to display data in a table format.
    """

    def __init__(self):
        """
        Initialize the Table with default settings.
        """
        self.title = ""
        self.display_total = False
        self.display_border = False
        self.header = TableRow()
        self.data = []
        self.sizes = []
        self.size_format = ""
        self.table = ""
        self.table_width = 0

    def set_header(self, header):
        """
        Set the header row for the table.

        Args:
            header (list): A list of column headers.
        """
        self.header.add_data(header)

    def set_title(self, text):
        """
        Set the title of the table.

        Args:
            text (str): The title of the table.
        """
        self.title = text

    def enable_total(self):
        """Enable the display of the total number of rows."""
        self.display_total = True

    def enable_border(self):
        """Enable the display of a border around the table."""
        self.display_border = True

    def new_row(self):
        """
        Create a new row instance.

        Returns:
            TableRow: A new TableRow instance with the same number of columns as the header.
        """
        row = TableRow()
        row.total = self.header.total
        return row

    def push_row(self, row):
        """
        Add a row to the table's data.

        Args:
            row (TableRow): A TableRow instance to add to the table.
        """
        self.data.append(row)

    def from_json(self, data):
        if isinstance(data, list) and all(isinstance(item, dict) for item in data):
            try:
                all_keys = list(data[0].keys())
                
                all_rows_valid = all(set(all_keys) == set(row.keys()) for row in data)
                
                if all_rows_valid:
                    self.set_header(all_keys)  
                    
                    for dt in data:
                        row = self.new_row()
                        
                        row_content = [dt[key] for key in all_keys]
                        
                        row.fill_row(row_content)  
                        self.push_row(row) 

                    self.render()
                else:
                    self.table = "INCOMPLETED DATA"
            except TypeError:
                self.table = "INVALID JSON"
        else:
            self.table = "INVALID TYPE"
        
        return self.table

    def render(self):
        """
        Construct and print the table based on the current settings.
        """

        self.calculate_sizes()

        self.table = "\n\n"
        total_rows = 0

        # Title
        if self.title != "":
            self.table += FontStyle.BOLD + self.title.upper() + FontStyle.ENDC + "\n"
        # Border
        if self.display_border:
            self.table += "-" * self.table_width + "\n"
        # Header
        if len(self.header.rows):
            if self.display_border:
                self.table += "|" + self.size_format.format(*self.header.rows[0]) + "|\n"
            else:
                self.table += self.size_format.format(*self.header.rows[0]) + "\n"
        if self.display_border:
            self.table += "-" * self.table_width + "\n"
        # Data rows
        for dt in self.data:
            for rw in dt.rows:
                if self.display_border:
                    self.table += "|" + self.size_format.format(*rw) + "|\n"
                else:
                    self.table += self.size_format.format(*rw) + "\n"
                total_rows += 1
        # Border after rows
        if self.display_border:
            self.table += "-" * self.table_width + "\n"
        # Total row count
        if self.display_total:
            self.table += FontStyle.BOLD + FontStyle.ITALIC + "TOTAL ROWS: " + str(total_rows) + FontStyle.ENDC + "\n"
        
        self.table += "\n"
        
        return self.table

    def calculate_sizes(self):
        """
        Calculate column widths based on the longest content in each column.
        """
        max_size = 0
        self.sizes = []
        current_pos = 0
        self.size_format = ""
        self.table_width = 0

        # Calculate the max size for each column
        for hd in self.header.rows:
            for dt in hd:
                hd_col_len = len(dt)
                max_size = 0
                for rw in self.data:
                    col_len = len(str(rw.rows[0][current_pos]))
                    if col_len > max_size:
                        max_size = col_len
                current_pos += 1
                sel_max = hd_col_len
                if col_len > sel_max:
                    sel_max = col_len
                
                self.sizes.append(sel_max + 3)

        # Format specification
        for sz in self.sizes:
            self.size_format += "{:<" + str(sz) + "} "
            self.table_width += sz + 1
        self.table_width += 2

class TableRow:
    """
    A class to represent a row in a table.
    """

    def __init__(self):
        """Initialize the TableRow with default settings."""
        self.rows = []
        self.total = 0

    def add_data(self, data):
        """
        Add a list of data as a single row.

        Args:
            data (list): A list of values for the row.
        """
        self.total = 0
        self.rows = []
        tempo_row = []

        if len(data) > 0:
            for dt in data:
                self.total += 1
                tempo_row.append(str(dt))

        if self.total == len(data):
            self.rows.append(tempo_row)

    def fill_row(self, data):
        """
        Add additional rows of data.

        Args:
            data (list): A list of values to add as a new row.

        Returns:
            bool: True if the data length matches the header length, otherwise False.
        """
        if len(data) == self.total:
            self.rows.append(data)
            return True
        else:
            return False

class Stopwatch:
    def __init__(self, title=""):
        self.data = []
        self.title = title

    def lap(self, label="", alarm=None):
        current_epoch = time.time()
        current_timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S.%f')[:-3]
        difference = 0
        prev_epoch = None
        alarm_icon = ""
        if label == "":
            label = "Mark " + str(len(self.data) + 1)
        

        if len(self.data) > 0:
            prev = self.data[len(self.data) - 1]
            prev_epoch = float(prev["epoch"])
            difference = current_epoch - prev_epoch

            if alarm and len(self.data) > 0:
                alarm.check(prev_epoch, current_epoch, summary=label, title="New Alarm.")
                if alarm.last_result:
                    alarm_icon = "[*]"

        if label == "":
            self.data.append({"label": label, "timestamp": current_timestamp, "epoch": str(current_epoch), "difference": str(difference) + " Sec.", "alarm": alarm_icon})
        else:
            self.data.append({"label": label, "timestamp": current_timestamp, "epoch": str(current_epoch), "difference": str(difference) + " Sec.", "alarm": alarm_icon})

        
    def stop(self):
        if len(self.data) > 0:
            tbl_data = Table()
            if self.title != "":
                tbl_data.set_title(Icon.STOPWATCH + " " + self.title)
            else:
                tbl_data.set_title(Icon.STOPWATCH + " RESULTS:")
            tbl_data.enable_total()
            tbl_data.enable_border()

            output = tbl_data.from_json(self.data)

            self.data = {}

            return output
        else:
            return ""

class Alarm:
    def __init__(self, threshold, condition=Condition.ABOVE_OR_EQUAL, slack=None, teams=None):
        self.threshold = threshold
        self.condition = condition
        self.slack = slack
        self.teams = teams
        self.last_result = False

    def check(self, init_time, end_time, summary="New Alarm", title="An Alarm has been raced.", icon="loud_sound"):
        evaluation = False
        self.last_result = False

        difference = end_time - init_time
        
        if self.condition == Condition.ABOVE:
            if difference > self.threshold:
                evaluation = True
        elif self.condition == Condition.ABOVE_OR_EQUAL:
            if difference >= self.threshold:
                evaluation = True
        elif self.condition == Condition.EQUAL:
            if difference == self.threshold:
                evaluation = True
        elif self.condition == Condition.BELOW:
            if difference < self.threshold:
                evaluation = True
        elif self.condition == Condition.BELOW_OR_EQUAL:
            if difference <= self.threshold:
                evaluation = True
        
        if evaluation:
            self.last_result = True
            if self.slack:
                self.slack.add_data("Threshold", str(self.threshold) + " Sec.")
                self.slack.add_data("Value", str(difference) + " Sec.")
                self.slack.assembly_notification(
                    title=title, 
                    summary=summary,
                    icon=icon
                )
                status, response = self.slack.send()

            if self.teams:
                self.teams.set_adaptative_notification("AN ALARM HAS BEEN RACED")
                self.teams.add_data("Threshold: " + str(self.threshold) + " Sec.")
                self.teams.add_data("Value: " + str(difference) + " Sec.")
                result, message = self.teams.send()