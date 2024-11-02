from neologger import NeoLogger
from neologger.core import Template
from neologger.core import FontColour, FontStyle

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
    

if __name__ == "__main__":
    main()