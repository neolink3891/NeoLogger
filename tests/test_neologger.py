from neologger import NeoLogger, Table
from neologger.core import Template
from neologger.core import FontColour, FontStyle
import time

neologger = NeoLogger("test_neolloger.py")
table = Table()

def main():
    print("\nBasic example:\n")
    neologger.log_this("Starting NeoLogger")
    print("\n")

    print("\nExample with OK label:\n")
    neologger.log_this_ok("Function completed Ok.")
    print("\n")

    print("\nExample with WARNING label:\n")
    neologger.log_this_warning("Data was sent uncompleted.")
    print("\n")

    print("\nExample with COMPLETED label:\n")
    neologger.log_this_completed("Data collection stage completed.")
    print("\n")

    print("\nExample with SUCCESS label:\n")
    neologger.log_this_success("Request has been completed successfuly")
    print("\n")
    
    print("\nExample with ERROR label:\n")
    neologger.log_this_error("Something went wrong!")
    print("\n")
    
    print("\nExample with BASE Template:\n")
    neologger.set_template(Template.BASE)
    neologger.log_this("NeoLogger has been set with BASE Template")
    print("\n")

    print("\nExample with NORMAL Template:\n")
    neologger.set_template(Template.NORMAL)
    neologger.log_this("NeoLogger has been set with NORMAL Template")
    print("\n")

    print("\nExample with DARK Template:\n")
    neologger.set_template(Template.DARK)
    neologger.log_this("NeoLogger has been set with DARK Template")
    print("\n")

    print("\nExample with FontStyle customisation\n")
    neologger.set_log_font_style(FontStyle.NORMAL, FontStyle.ITALIC, FontStyle.BOLD, FontStyle.UNDERLINE)
    neologger.log_this("Font style has been customised")
    print("\n")

    neologger.set_template(Template.BASE)
    print("\nExample with Elapsed Time display\n")
    time_track = neologger.get_time_mark()
    time.sleep(1) # Adding delay
    neologger.log_with_elapsed_time("Function completed.", time_track)
    print("\n")

    print("\nExample of Table")
    table.set_title("Last month sales report.")
    header = ["ID", "Name", "Sales", "Rank", "Last Check"]
    table.set_header(header)
    row = table.new_row()
    row_content = [1, "Pablo", "£12,500", "1st", "2024-10-12"]
    row.fill_row(row_content)
    table.push_row(row)
    row = table.new_row()
    row_content = ["2", "Orlando", "£22,750", "2st", "2024-10-11"]
    row.fill_row(row_content)
    table.push_row(row)
    row = table.new_row()
    row_content = ["3", "Beatriz", "£23,450", "3st", "2024-10-13"]
    row.fill_row(row_content)
    table.push_row(row)
    table.enable_total()
    table.enable_border()
    neologger.log_this(table.render())


if __name__ == "__main__":
    main()