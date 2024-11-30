
# Stopwatch

The `Stopwatch` class is a utility for tracking elapsed time across multiple checkpoints or "laps", with optional alarm integration that can trigger notifications base on a threshold and condition.

Stopwatch can run as standalone object, and its also embeeded into neologger.

## Concept

The concept of the `Stopwatch` class is to provide a easy way to trace code execution within a function. Aditionally it offers a way to trigger an Alarm `from Alarm class` if the execution exceeds a condition and threshold.

The Stopwatch class implements `Table` class from NeoLogger package.

### Functionality
  - Records the current epoch time and formatted timestamp.
  - Calculates the time difference from the previous lap (if any).
  - Optionally checks and triggers alarms between laps.

### Stored Lap Data
  - `LABEL`: Label for the lap.
  - `TIMESTAMP`: Human-readable timestamp.
  - `EPOCH`: Epoch time with 3 decimal places.
  - `ELAPSED`: Elapsed time since the previous lap with 5 decimal places.
  - `ALARM`: Alarm status icon (`[*]` if triggered, otherwise empty).

## Tracking Execution Time

Import the required classes:

```
from neologger import Stopwatch
```

Initialise an object.

```
stopwatch = Stopwatch()
```

### Basic Trace

The basic `Stopwatch` initialising is designed to be a fast logging option, just add a _lap()_ method in any checkpoint you want to monitor, as follow:

```
stopwatch.lap()
time.sleep(1.25) # simulating delay.
stopwatch.lap()
time.sleep(2.55) # simulating delay.
stopwatch.lap()
time.sleep(0.35) # simulating delay.
stopwatch.lap()
```

After adding the desired checkpoints, the method _stop()_ generates a table with the tracked items.

Example of trace:
```
print(stopwatch.stop())
```

<p align="center">
  <img src="imgs/stopwatch_1.png" alt="NeoLogger Banner">
</p>

### Advanced Trace.

Stopwathc class allows you to use custom Titles, this is done by providing a title when creating the object.

Initialise an object.

```
stopwatch = Stopwatch("Testing NeoLogger's Stopwatch class.")
```

Then, each lap can also accept a label.

```
stopwatch1 = Stopwatch("Tracking checkpoints using labels.")
stopwatch1.lap("Starting.")
time.sleep(1.15)
stopwatch1.lap("Database connection with default driver")
time.sleep(3.25)
stopwatch1.lap("Post request completed. Call to SP defaultLoggingFunction")
time.sleep(2.3)
```

After adding the desired checkpoints, the method _stop()_ generates a table with the tracked items.

Example of trace:
```
print(stopwatch.stop())
```

<p align="center">
  <img src="imgs/stopwatch_2.png" alt="NeoLogger Banner">
</p>

### Code snipet

The followin is the completed code.

```
python
from datetime import datetime
import time

# Example of creating and using the Stopwatch class
stopwatch = Stopwatch("Example Stopwatch")

# Record laps
stopwatch.lap("Start")
time.sleep(1.5)  # Simulate time delay
stopwatch.lap("Middle")
time.sleep(1)  # Simulate time delay
stopwatch.lap("End")

# Stop and display results
results = stopwatch.stop()
print(results)
```

## Notes:
- The `Table` and `Icon` classes/functions are external dependencies and should be implemented or imported separately.
- The `alarm` parameter must have a `check` method and a `last_result` attribute to work correctly.

### Formatting:
- Epoch time is formatted with 3 decimal places.
- Elapsed time is formatted with 5 decimal places.
