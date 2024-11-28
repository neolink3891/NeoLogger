from neologger import Alarm, SlackNotification
from neologger.core import Condition
import time

slack = SlackNotification()
slack.set_hook("[SLACK_WEBHOOK_URL]")

alarm = Alarm(3, slack=slack)

def main():
    print("Testing NeoLogger's Alarm")

    print("Sleeping 2 Seconds")
    time_from = time.time()
    time.sleep(2)
    time_to = time.time()
    print("Awake after 2 Seconds")
    alarm.check(time_from, time_to)
    print("Sleeping 4 seconds")
    time_from = time.time()
    time.sleep(4)
    time_to = time.time()
    print("Awake after 4 seconds")
    alarm.check(time_from, time_to)

if __name__ == "__main__":
    main()