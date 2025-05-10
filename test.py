from src.neologger import NeoLogger, DiscordNotification

neologger = NeoLogger("Tests")

DISCORD_WEBHOOK="https://discord.com/api/webhooks/1245327715012186173/gMmFuNBvqM7TQvlhk6W9aq9rmVyw-2QQRGsh9X6qFshavrpJ7QYLyNzFctpMz6HsNtSW"

discord_notification = DiscordNotification()

discord_notification.set_hook(DISCORD_WEBHOOK)
discord_notification.set_username("NeoLogger")
discord_notification.add_content("Hello world!")

# embed = discord_notification.create_embed()
# embed.set("Alert", "Something has gone wrong", "15539236")
# embed.add_author("NeoLogger", icon_url="https://icons.veryicon.com/png/o/cartoon/bicolor-icon/robot-9.png")
# discord_notification.add_embed(embed)

sent, result = discord_notification.send()
print(sent, result)