from ulises import ulises
from penelope import penelope
import sys

if len(sys.argv) > 1:
    bot =  sys.argv[1]
else:
    bot = 'n/a'

if bot == "penelope":
    penelope.run_penelope()
elif bot == "ulises": 
    ulises.run_ulises()
else:
    print("debe utilizar python main.py nombre-del-bot")