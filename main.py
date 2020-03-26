import discord
import configparser
import difflib

config = configparser.ConfigParser()
config.read("config.ini")

token = config["SETTINGS"]["token"]
similarity_threshold = float(config["SETTINGS"]["similarity_threshold"])
max_message_length = int(config["SETTINGS"]["max_message_length"])
asking_phrases = config["SETTINGS"]["asking_phrases"].split(",")
message_junk = config["SETTINGS"]["message_junk"].split(",")
reply_message = config["SETTINGS"]["reply_message"]


def remove_junk(message):
    """
    Remove any junk contained in <message_junk> and trailing spaces
    """
    message = message.split()
    resultwords  = [word for word in message if word not in message_junk]
    message = ' '.join(resultwords)
    return message


def is_asking_whens_wipe(message):
    """
    Check if <message> is similar with any <asking_phrases> based on the <similarity_threshold>
    """
    highest_score = 0
    for asking_phrase in asking_phrases:
        current_score = difflib.SequenceMatcher(None, message, asking_phrase).ratio()
        if highest_score < current_score:
            highest_score = current_score
    # Debug: Print message and highest score detected
    # print(f"Message: {message}, highest score: {highest_score}")
    return highest_score >= similarity_threshold


class WhensWipeWatcher(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user.name}, ({self.user.id})\n')

    async def on_message(self, ctx):
        if ctx.author.bot:
            return
        message = ctx.content.lower()
        if len(message) >= max_message_length:
            return
        message = remove_junk(message)
        
        if is_asking_whens_wipe(message):
            await ctx.channel.send(reply_message)



if __name__ == "__main__":
    WhensWipeWatcher().run(token)