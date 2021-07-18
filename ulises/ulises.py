from bot_base.bot import connectBot, onPrivmessage, onPubmessage

def recibiMensajePrivado(nick, mensaje):
    print(nick, mensaje)
    if nick == "Gabriela-":
        return "hola"
    elif nick == "Alex":
        return "adios"

def recibiPingCanal(nick, mensaje, canal):
    print(nick, mensaje, canal)
    if mensaje == "hola":
        return "escribe algo o te mato"
def run_ulises(): 
    bot = connectBot("irc.hirana.net", 6667, "#BarmanTest", "Ulises")
    onPrivmessage(bot, recibiMensajePrivado)
    onPubmessage(bot, recibiPingCanal)
    bot.start()
