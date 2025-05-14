# This follows the examples described in https://birdie0.github.io/discord-webhooks-guide/discord_webhook.html

from src.neologger import NeoLogger, DiscordNotification

neologger = NeoLogger("Discord tests")

DISCORD_WEBHOOK="YOUR DISCORD WEBHOOK URL"

# Basic discord notification
discord_notification = DiscordNotification()
discord_notification.set_hook(DISCORD_WEBHOOK)
discord_notification.set_username("NeoLogger")
discord_notification.add_content("Hello world!")
sent, result = discord_notification.send()
print(sent, result)

# Testing a single, basic embed
discord_notification = DiscordNotification()
discord_notification.set_hook(DISCORD_WEBHOOK)
# Create embed
embed = discord_notification.create_embed()
embed.set("Alert", "Something has gone wrong", "15539236")
discord_notification.add_embed(embed)
sent, result = discord_notification.send()
print(sent, result)

# Testing a single, basic embed with an author
discord_notification = DiscordNotification()
discord_notification.set_hook(DISCORD_WEBHOOK)
# Create embed
embed = discord_notification.create_embed()
embed.set("Alert", "Something has gone wrong", "15539236")
embed.add_author("NeoLogger", icon_url="https://icons.veryicon.com/png/o/cartoon/bicolor-icon/robot-9.png")
# Add embed to notification
discord_notification.add_embed(embed)
sent, result = discord_notification.send()
print(sent, result)

# Testing multiple embeds with authors
discord_notification = DiscordNotification()
discord_notification.set_hook(DISCORD_WEBHOOK)
# Create first embed
embed1 = discord_notification.create_embed()
embed1.set("Alert 1", "Something has gone wrong", "15539236")
embed1.add_author("NeoLogger", icon_url="https://icons.veryicon.com/png/o/cartoon/bicolor-icon/robot-9.png")
# Create second embed
embed2 = discord_notification.create_embed()
embed2.set("Alert 2", "Something else has gone wrong", "15539236")
embed2.add_author("NeoLogger", icon_url="https://icons.veryicon.com/png/o/cartoon/bicolor-icon/robot-9.png")
# Add embeds to notification
discord_notification.add_embed(embed1)
discord_notification.add_embed(embed2)
sent, result = discord_notification.send()
print(sent, result)

# Testing multiple embeds with authors and fields
discord_notification = DiscordNotification()
discord_notification.set_hook(DISCORD_WEBHOOK)
# Create first embed
embed1 = discord_notification.create_embed()
embed1.set("Alert 1", "Something has gone wrong", "15539236")
embed1.add_author("NeoLogger", icon_url="https://icons.veryicon.com/png/o/cartoon/bicolor-icon/robot-9.png")
embed1.add_field("Number", "1", True)
embed1.add_field("Letter", "A", True)
# Create second embed
embed2 = discord_notification.create_embed()
embed2.set("Alert 2", "Something else has gone wrong", "15539236")
embed2.add_author("NeoLogger", icon_url="https://icons.veryicon.com/png/o/cartoon/bicolor-icon/robot-9.png")
embed2.add_field("Number", "1", False)
embed2.add_field("Letter", "A", False)
# Add embeds to notification
discord_notification.add_embed(embed1)
discord_notification.add_embed(embed2)
sent, result = discord_notification.send()
print(sent, result)

# Testing multiple embedw with authors and fields and a footer
discord_notification = DiscordNotification()
discord_notification.set_hook(DISCORD_WEBHOOK)
# Create first embed
embed1 = discord_notification.create_embed()
embed1.set("Alert 1", "Something has gone wrong", "15539236")
embed1.add_author("NeoLogger", icon_url="https://icons.veryicon.com/png/o/cartoon/bicolor-icon/robot-9.png")
embed1.add_field("Number", "1", True)
embed1.add_field("Letter", "A", True)
# Create second embed
embed2 = discord_notification.create_embed()
embed2.set("Alert 2", "Something else has gone wrong", "15539236")
embed2.add_author("NeoLogger", icon_url="https://icons.veryicon.com/png/o/cartoon/bicolor-icon/robot-9.png")
embed2.add_field("Number", "1", False)
embed2.add_field("Letter", "A", False)
# Add footer to embed
embed2.add_footer("Goodbye for now!")
# Add embeds to notification
discord_notification.add_embed(embed1)
discord_notification.add_embed(embed2)
sent, result = discord_notification.send()
print(sent, result)

# Testing multiple embeds with authors, fields, a footer, thumbnails and images
discord_notification = DiscordNotification()
discord_notification.set_hook(DISCORD_WEBHOOK)
# Create first embed with thumbnail
embed1 = discord_notification.create_embed()
embed1.set("Alert 1", "Something has gone wrong", "15539236")
embed1.add_author("NeoLogger", icon_url="https://icons.veryicon.com/png/o/cartoon/bicolor-icon/robot-9.png")
embed1.add_field("Number", "1", True)
embed1.add_field("Letter", "A", True)
embed1.add_thumbnail("https://icons.veryicon.com/png/o/cartoon/bicolor-icon/robot-9.png")
# Create second embed with image and footer
embed2 = discord_notification.create_embed()
embed2.set("Alert 2", "Something else has gone wrong", "15539236")
embed2.add_author("NeoLogger", icon_url="https://icons.veryicon.com/png/o/cartoon/bicolor-icon/robot-9.png")
embed2.add_field("Number", "1", False)
embed2.add_field("Letter", "A", False)
embed2.add_image("https://icons.veryicon.com/png/o/cartoon/bicolor-icon/robot-9.png")
# Add footer to embed
embed2.add_footer("Goodbye for now!")
# Add embeds to notification
discord_notification.add_embed(embed1)
discord_notification.add_embed(embed2)
sent, result = discord_notification.send()
print(sent, result)