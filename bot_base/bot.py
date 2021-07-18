import irc.bot
import irc.strings

class TestBot(irc.bot.SingleServerIRCBot):

    def __init__(self, channel, nickname, server, port=6667):
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, nickname)
        self.channel = channel

    def on_nicknameinuse(self, c, e):
        c.nick(c.get_nickname() + "_")

    def on_welcome(self, c, e):
        c.join(self.channel)

    def on_privmsg(self, c, e):
        nick = e.source.nick
        command = e.arguments[0]
        c = self.connection
        if self.callbackPrivmsg is not None:
            response = self.callbackPrivmsg(nick, command)
            if response is not None:
                c.privmsg(nick, response)

    def setCallbackPrivmsg(self, callback):
        self.callbackPrivmsg = callback

    def on_pubmsg(self, c, e):
        parts = e.arguments[0].split(" ", 1)
        pingNick = parts[0].strip().replace(",", "")
        command = parts[1].strip()
        if len(pingNick) > 1 and irc.strings.lower(pingNick) == irc.strings.lower(
            self.connection.get_nickname()
        ):
            channel = e.target
            nick = e.source.nick
            c = self.connection
            if self.callbackPubmsg is not None:
                response = self.callbackPubmsg(nick, command, channel)
                if response is not None:
                    c.privmsg(channel, response)
        return

    def setCallbackPubmsg(self, callback):
        self.callbackPubmsg = callback

    def on_dccmsg(self, c, e):
        # non-chat DCC messages are raw bytes; decode as text
        text = e.arguments[0].decode('utf-8')
        # c.privmsg("You said: " + text)

    def on_dccchat(self, c, e):
        if len(e.arguments) != 2:
            return


def connectBot(server, port, channel, nickname):
    bot = TestBot(channel, nickname, server, port)
    bot.start()
    return bot

def onPrivmessage(bot, callback):
    bot.setCallbackPrivmsg(callback)

def onPubmessage(bot, callback):
    bot.setCallbackPubmsg(callback)

