# WhensWipeDiscordBot
Respond to common question of "When's wipe?" in Rust Discords.

# Why?
![2599 people asking when's wipe](https://i.imgur.com/F05YoIJ.png)

# Installation
1. Install [Python 3.7 or newer](https://www.python.org/downloads/)
1. Install requirements by running `pip3 install -r requirements.txt`
1. Configure the `config.ini` and set the [bot token](https://discordapp.com/developers/applications)
1. Invite bot to your discord `https://discordapp.com/oauth2/authorize?client_id=CLIENT_ID_OF_THE_BOT_HERE&scope=bot`
1. Run the bot `python3 main.py`


# Configuration
* `token` - [bot's token](https://discordapp.com/developers/applications)
* `similarity_threshold` - How similar does the message have to be to get bot's reply, between 0.00 to 1.00
* `max_message_length` - If message is longer than this then it will be ignored and not checked
* `asking_phrase` - Most popular phrases asking when's wipe separated by comma
* `message_junk` - Junk in messages that should not count when checking if message is similiar to asking phrase
* `reply_message` - What bot should reply with when someone asking when's wipe. Use <#ChannelID> to mention a channel.


Made with :heartpulse: for [Rusticated.com](http://rusticated.com)
