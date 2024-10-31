from neologger import NeoLogger, SlackNotification
from neologger.core import Template

neologger = NeoLogger("test.py")
slack = SlackNotification()

def main():
    neologger.log_this("Starting NeoLogger")
    neologger.log_this_warning("Warning!")
    neologger.log_this_ok("OK!")
    neologger.log_this_error("Fail!")
    neologger.log_this_completed("Completed")
    neologger.log_this_success("Success")
    neologger.set_template(Template.BASE)
    neologger.log_this("Starting NeoLogger")
    position_1 = neologger.get_time_mark()
    neologger.log_with_elapsed_time("Starting NeoLogger", position_1)
    
    slack.set_hook("https://hooks.slack.com/services/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")
    slack.add_data("IP", "192.168.1.137")
    slack.add_data("Hostname", "neolink")
    slack.add_data("Date", "2024-09-12")
    slack.add_data("Type", "Demo")
    slack.add_data("User", "NeoLink")
    slack.assembly_notification("NeoLogger Rocks with emojis!", "This is an example of a summary within a Slack Notification with NeoLogger.", icon="sweat_smile")
    response_ok, response_message = slack.send()
    print(response_message)


if __name__ == "__main__":
    main()