## NeoLogger

NeoLogger makes command line log more detailed and meaningful.

The structure of the log for the basic form as follow:  
_timestamp - file >> function | log message_

### 1 - Usage

Import classes

```
from neologger import NeoLogger
```

Create an NeoLogger object, pass the name of the file where the object is created.

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

NeoLogger inclides the possibility to visually display labels that differentiate logs, currently as for version 1.1.0, you can add labels for OK, WARNING, COMPLETED, SUCCESS, and ERROR.   
To add a label to the output, just call the proper method, as follow:

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
Templates allow to display logs with predefined colours, to include a Template with NeoLogger you need to import the Template class from the neologger.core package as follows:

```
from neologger.core import Template
```

As in version 1.1.0, the following Templates are available: BASE, NORMAL, DARK

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