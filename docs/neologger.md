## NeoLogger

NeoLogger makes command line log more detailed and meaningful.

The basic log structure is as follows: 
_timestamp - file >> function | log message_

### 1 - Usage

Import the necessary classes:

```
from neologger import NeoLogger
```

Create a NeoLogger object and pass the name of the file where the object is created:

```
neologger = NeoLogger("test_neolloger.py")
```

Call the basic logging method.

```
neologger.log_this("Starting NeoLogger")
```

Output:
<p align="center">
  <img src="imgs/neologger_1.png" alt="NeoLogger Banner">
</p>

### 2- Labels

NeoLogger allows you to visually display labels that differentiate logs. As of version 1.1.0, you can add labels for OK, WARNING, COMPLETED, SUCCESS, and ERROR.

To add a label to the output, call the appropriate method as follows:

* OK 
```
neologger.log_this_ok("Function completed Ok.")
```
Output:
<p align="center">
  <img src="imgs/neologger_2.png" alt="NeoLogger Banner">
</p>

* WARNING 
```
neologger.log_this_warning("Data was sent uncompleted")
```
Output:
<p align="center">
  <img src="imgs/neologger_3.png" alt="NeoLogger Banner">
</p>

* COMPLETED 
```
neologger.log_this_completed("Data collection stage completed.")
```
Output:
<p align="center">
  <img src="imgs/neologger_4.png" alt="NeoLogger Banner">
</p>

* SUCCESS 
```
neologger.log_this_success("Request has been completed successfuly")
```
Output:
<p align="center">
  <img src="imgs/neologger_5.png" alt="NeoLogger Banner">
</p>

* ERROR 
```
neologger.log_this_error("Something went wrong!")
```
Output:
<p align="center">
  <img src="imgs/neologger_6.png" alt="NeoLogger Banner">
</p>

### 3 - Templates
Templates allow you to display logs with predefined colours. To use a Template with NeoLogger, import the Template class from neologger.core.

Templates can be changed at any time during runtime.

```
from neologger.core import Template
```

Available Templates as of version 1.1.0: BASE, NORMAL, DARK

* BASE 
```
neologger.set_template(Template.BASE)
neologger.log_this("NeoLogger has been set with BASE Template")
```
Output:
<p align="center">
  <img src="imgs/neologger_7.png" alt="NeoLogger Banner">
</p>

* NORMAL 
```
neologger.set_template(Template.NORMAL)
neologger.log_this("NeoLogger has been set with NORMAL Template")
```
Output:
<p align="center">
  <img src="imgs/neologger_8.png" alt="NeoLogger Banner">
</p>

* DARK 
```
neologger.set_template(Template.DARK)
neologger.log_this("NeoLogger has been set with DARK Template")
```
Output:
<p align="center">
  <img src="imgs/neologger_9.png" alt="NeoLogger Banner">
</p>

### 4 - Customising Logs display
NeoLogger allows you to customize logs to match your style. Import the FontColour and FontStyle classes from the neologger.core package

```
from neologger.core import FontColour, FontStyle
```

NeoLogger provides two methods for customization:  

* Setting up Font Colour with _set_log_font_colour_

As in version 1.1.0, the folloging colours are available:
```
BLUE            # Light blue text
DARKBLUE        # Dark blue text
CYAN            # Light cyan text
DARKCYAN        # Dark cyan text
GREEN           # Light green text
DARKGREEN       # Dark green text
YELLOW          # Light yellow text
DARKYELLOW      # Dark yellow text
RED             # Light red text
DARKRED         # Dark red text
MAGENTA         # Light magenta text
DARKMAGENTA     # Dark magenta text
GREY            # Light grey text
DARKGREY        # Dark grey text
BLACK           # Black text
WHITE           # White text
```

Set custom font colours.

```
neologger.set_log_font_colour(FontColour.CYAN, FontColour.GREEN, FontColour.RED, FontColour.YELLOW)
neologger.log_this("Font colour has been customised")
```
Output:
<p align="center">
  <img src="imgs/neologger_10.png" alt="NeoLogger Banner">
</p>

* Setting up Font Style with _set_log_font_style_

As of version 1.1.0, the following styles are available:
```
BOLD                # Bold text
ITALIC              # Italic text
UNDERLINE           # Underlined text
DOUBLEUNDERLINE     # Double underlined text
DIM                 # Dim text
NORMAL              # Normal intensity text
```

Set custom font styles.

```
neologger.set_log_font_style(FontStyle.NORMAL, FontStyle.ITALIC, FontStyle.BOLD, FontStyle.UNDERLINE)
neologger.log_this("Font style has been customised")
```
Output:
<p align="center">
  <img src="imgs/neologger_11.png" alt="NeoLogger Banner">
</p>

### 5 - Tracking Elapsed Time

NeoLogger provides the option to display elapsed time in the log. To do this, capture the initial time and then pass it to the logging method.

Capture the initial time:
```
time_track = neologger.get_time_mark()
time.sleep(3) # Adding delay - import time
```

Then, use the method to display elapsed time:
```
neologger.log_with_elapsed_time("Function completed.", time_track)
```

Output:
<p align="center">
  <img src="imgs/neologger_12.png" alt="NeoLogger Banner">
</p>

### 6 - Displaying Data Tables

NeoLogger has the capability to display Data Tables in the logs, in order to use this feature, you need to import Table class from neologger package. The Tables created with NeoLogger will resize automatically.

```
from neologger import Table
```

Create a object of type Table

```
table = Table()
```

To display a Table you need to define the Header, which is a list of strings, and add it to the table object with method _set_header_

```
header = ["No", "Depto", "Name", "Top Product", "Total Sales", "Rank"]
table.set_header(header)
```

From this point, the Table object will expect each row with the same size of the Header.    
You can add rows by pulling a new row from the table with _new_row()_ method, then use the _fill_row_ method to add a collection of string containing the data for the row, and lastly use the method _push_row_ to add it to the Table, as follow:

```
row = table.new_row()
row_content = ["1", "IT", "Pablo Martinez", "Servers", "£12,500", "1sr"]
row.fill_row(row_content)
table.push_row(row)
```

Add as many rows as needed, and then use the method _render_ to show the table in the logs.

```
    row = table.new_row()
    row_content = ["2", "Marketing", "Beatriz Romero", "Campain", "£11,250", "2nd"]
    row.fill_row(row_content)
    table.push_row(row)
    row = table.new_row()
    row_content = ["3", "Automotive", "Gabriela Martinez", "Peugeot 3008", "£11,108", "3rd"]
    row.fill_row(row_content)
    table.push_row(row)
    row = table.new_row()
    row_content = ["4", "Robotics", "Aurora Martinez", "Robotic Arm", "£10,090", "4th"]
    row.fill_row(row_content)
    table.push_row(row)
```

When all rows are added, call the render method to display the table.

```
neologger.log_this(table.render())
```

Output:
<p align="center">
  <img src="imgs/neologger_13.png" alt="NeoLogger Banner">
</p>

#### 5.1 - Table Title

Tables created with NeoLogger's Table class can show a Title, use the method _set_title_ to provide it before calling the _render_ method. The title will be converted to upper case with a different colour.

```
table.set_title("Last month sales report.")
```

Output:
<p align="center">
  <img src="imgs/neologger_14.png" alt="NeoLogger Banner">
</p>

#### 5.2 - Displaying Row Count

NeoLogger Tables can also show the total number of rows at the botton, if you want to display it, use the method _enable_total_ before calling the _render_ method.

```
table.enable_total()
```

Output:
<p align="center">
  <img src="imgs/neologger_15.png" alt="NeoLogger Banner">
</p>

#### 5.3 - Display Borders

Optionally, you can show borders for the table by using the method _enable_border_ before calling the _render_ method.

```
table.enable_border()
```

Output:
<p align="center">
  <img src="imgs/neologger_16.png" alt="NeoLogger Banner">
</p>

#### 5.4 - Tables from JSON [from version 1.2.1]

Since version 1.2.1 NeoLogger's Table class can convert JSON objects to Tables with all Table's features. Thus, the JSON object must meet the following criteria:
- Type: _list_ of rows.
- Contain the same keys.
- The keys must be in the same order (otherwise data will not be displayed properly)

The following is an example of a proper JSON object that can be use to render a Table:

```
    jdata = [
        {"Id": "1011", "Code": "Ab99s0r", "Expiration": "13-10-2024", "Status": "ACTIVE", "Base": "https://endpoint.com/api/action"},
        {"Id": "1012", "Code": "12dLLd0", "Expiration": "12-11-2024", "Status": "ACTIVE", "Base": "https://endpoint.com/api/action"},
        {"Id": "1013", "Code": "5540xxD", "Expiration": "10-08-2024", "Status": "ACTIVE", "Base": "https://endpoint.com/api/action"},
        {"Id": "1014", "Code": "0dd9AsX", "Expiration": "08-05-2024", "Status": "INACTIVE", "Base": "https://endpoint.com/api/action"}
    ]
```

Then, call the method _from_json_ method, the following code shows this action.

```
    table.set_title("DATA FROM JSON")
    table.enable_total()
    table.enable_border()
    neologger.log_this(table.from_json(jdata))
```

Output:
<p align="center">
  <img src="imgs/neologger_18.png" alt="NeoLogger Banner">
</p>

### 6 - Testing
Please, refer to [test_neologger.py](../tests/test_neologger.py) to view the full source code for this example.