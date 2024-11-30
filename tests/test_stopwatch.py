from neologger import Stopwatch
import time

print("Testing NeoLogger's Stopwatch class.")

stopwatch1 = Stopwatch("Tracking checkpoints using labels.")
stopwatch1.lap("Starting.")
time.sleep(1.15)
stopwatch1.lap("Database connection with default driver")
time.sleep(3.25)
stopwatch1.lap("Post request completed. Call to SP defaultLoggingFunction")
time.sleep(2.3)
stopwatch1.lap("Another process completed")
print(stopwatch1.stop())

# stopwatch2 = Stopwatch()
# stopwatch2.lap()
# time.sleep(1.25)
# stopwatch2.lap()
# time.sleep(2.55)
# stopwatch2.lap()
# time.sleep(0.35)
# stopwatch2.lap()
# print(stopwatch2.stop())