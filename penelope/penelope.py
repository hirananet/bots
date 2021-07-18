from bot_base.bot import connectBot, onPrivmessage, onPubmessage

def recibiMensajePrivado(nick, mensaje):
    print(nick, mensaje)

def recibiPingCanal(nick, mensaje, canal):
    print(nick, mensaje, canal)

def run_penelope(): 
    bot = connectBot("irc.hirana.net", 6667, "#BarmanTest", "Penelope")
    onPrivmessage(bot, recibiMensajePrivado)
    onPubmessage(bot, recibiPingCanal)
    bot.start()