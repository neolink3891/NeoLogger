from neologger import TeamsNotification

teams = TeamsNotification()

def main():
    print("\nStarting TeamsNotification")
    print("Setting Webhook")

    teams.set_hook("YOUR_WEBHOOK_URL")

    print("Standar Notification")

    print("Setting Data")
    teams.assembly_standard_notification("NOTIFICATION'S TITLE", "This is the summary.", "This is the text within the notification body, one single paragraph.")
    print("sending Standard Notification")
    teams.send()
    result, message = teams.send()
    print("Result: " + str(result))
    print("Response: " + message)

    print("Adaptative Notification")
    print("Setting Profile Image and Name")
    teams.set_profile_image("YOUR_PUBLIC_PROFILE_IMAGE_URL")
    teams.set_profile_name("profile Name")
    print("Setting Title and ")
    teams.set_adaptative_notification("THIS IS THE NOTIFICATION TITLE")
    print("Adding data rows")
    teams.add_data("Line 1")
    teams.add_data("Line 2")
    teams.add_data("Line 3")
    print("Sending Adaptative Notification")
    result, message = teams.send()
    print("Result: " + str(result))
    print("Response: " + message)

if __name__ == "__main__":
    main()
