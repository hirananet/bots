from jaraco.stream import buffer
from irc import client

server = client.Reactor().server()
server.buffer_class = buffer.LenientDecodingLineBuffer
server.connect()