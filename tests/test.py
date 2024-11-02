from neologger import NeoLogger, SlackNotification, Table
from neologger.core import Template

neologger = NeoLogger("test.py")
slack = SlackNotification()
table = Table()

def main():
    print("\nBasic example:\n")
    neologger.log_this("Starting NeoLogger")
    print("\n")
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


    table.set_title("Table Title")
    header = ["ID", "Name", "Value", "Status", "Last Check"]
    table.set_header(header)
    # table.enable_total()
    # table.enable_border()
    row = table.new_row()
    row.fill_row(["1", "host", "asterisk.big4.dev.local", "Active", "2024-10-12"])
    table.push_row(row)
    row = table.new_row()
    row.fill_row(["2", "host", "asterisk.ifl.dev.local", "Disabled", "2024-10-12"])
    table.push_row(row)
    table.calculate_sizes()
    table.draw_lines()

    slack.add_data("IP", "192.168.1.157")
    slack.add_data("Hostname", "neolink")
    slack.add_data("Date", "2024-11-02")
    slack.add_data("Type", "Demo")
    slack.add_data("User", "NeoLink")
    slack.assembly_notification("NeoLogger Rocks with emojis, again!", "Table has been created", icon="sparkles")
    response_ok, response_message = slack.send()
    print(response_message)


if __name__ == "__main__":
    main()