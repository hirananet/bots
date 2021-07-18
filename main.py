from ulises import ulises
# import penelope
import bot_base
import sys

if len(sys.argv) > 1:
    bot =  sys.argv[1]
else:
    bot = 'n/a'

if bot == "penelope":
    ulises.run_ulises()
elif bot == "ulises": 
    ulises.run_ulises()
else:
    print("debe utilizar python main.py nombre-del-bot")