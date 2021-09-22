from rivescript import RiveScript

chatBot = RiveScript(utf8=True)

chatBot.load_directory("brain")
chatBot.sort_replies()


def chat(message):
    if message == "":
        return -1, "No message found "
    else:
        responce = chatBot.reply("user", message)
    if responce:
        return 0, responce
    else:
        return -1, "No responce found"