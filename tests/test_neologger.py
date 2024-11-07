from neologger import NeoLogger, Table
from neologger.core import Template
from neologger.core import FontColour, FontStyle
import time

neologger = NeoLogger("test_neolloger.py")

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
    # time.sleep(1) # Adding delay
    neologger.log_with_elapsed_time("Function completed.", time_track)
    print("\n")

    print("\nExample of Table")
    table = Table()
    table.set_title("Last month sales report.")
    header = ["No", "Depto", "Name", "Top Product", "Total Sales", "Rank"]
    table.set_header(header)
    row = table.new_row()
    row_content = ["1", "IT", "Pablo Martinez", "Servers", "£12,500", "1sr"]
    row.fill_row(row_content)
    table.push_row(row)
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
    table.enable_total()
    table.enable_border()
    neologger.log_this(table.render())

    table = Table()
    jdata = [
        {"id": "1", "name": "ABC", "code": "LMN"},
        {"id": "2", "name": "CDE", "code": "OPQ"},
        {"id": "3", "name": "FGH", "code": "RST"},
        {"id": "4", "name": "IJK", "code": "UVW"}
    ]
    
    table.set_title("DATA FROM JSON")
    table.enable_total()
    table.enable_border()
    neologger.log_this(table.from_json(jdata))


if __name__ == "__main__":
    main()