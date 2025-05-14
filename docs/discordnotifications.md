
## DiscordNotification
The most basic notification requires the webhook URL and some content:
```
from neologger import NeoLogger, DiscordNotification

neologger = NeoLogger("Discord tests")

DISCORD_WEBHOOK="YOUR DISCORD WEBHOOK URL"

# Basic discord notification
discord_notification = DiscordNotification()
discord_notification.set_hook(DISCORD_WEBHOOK)
discord_notification.set_username("NeoLogger")
discord_notification.add_content("Hello world!")
sent, result = discord_notification.send()
print(sent, result)
```
However, the magic really happens when you use embeds. A simple embed can be created like this:
```
...
# Basic discord notification
discord_notification = DiscordNotification()
discord_notification.set_hook(DISCORD_WEBHOOK)
# First, create an embed object
embed = discord_notification.create_embed()
# The most basic embeds require only a title, a message and optionally a colour (decimal not hex!)
embed.set("Alert", "Something has gone wrong", "15539236")
# Finally, add the embed to the notification and send
discord_notification.add_embed(embed)
sent, result = discord_notification.send()
print(sent, result)
```
You can add multiple embeds, with fields, an author, a footer, a thumbnail or an image. See the example below!
```
...
discord_notification = DiscordNotification()
discord_notification.set_hook(DISCORD_WEBHOOK)
# Create first embed
embed1 = discord_notification.create_embed()
embed1.set("Alert 1", "Something has gone wrong", "15539236")
# Add an author
embed1.add_author("NeoLogger", icon_url="https://icons.veryicon.com/png/o/cartoon/bicolor-icon/robot-9.png")
# Add a field to the embed (the last argument is whether the field is inline or not)
embed1.add_field("Number", "1", True)
embed1.add_field("Letter", "A", True)
# Now add a thumbnail
embed1.add_thumbnail("https://icons.veryicon.com/png/o/cartoon/bicolor-icon/robot-9.png")
# Create second embed with image and footer
embed2 = discord_notification.create_embed()
embed2.set("Alert 2", "Something else has gone wrong", "15539236")
embed2.add_author("NeoLogger", icon_url="https://icons.veryicon.com/png/o/cartoon/bicolor-icon/robot-9.png")
embed2.add_field("Number", "1", False)
embed2.add_field("Letter", "A", False)
# Add an image to the embed
embed2.add_image("https://icons.veryicon.com/png/o/cartoon/bicolor-icon/robot-9.png")
# Add footer to embed
embed2.add_footer("Goodbye for now!")
# Add embeds to notification
discord_notification.add_embed(embed1)
discord_notification.add_embed(embed2)
sent, result = discord_notification.send()
print(sent, result)
```