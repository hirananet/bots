from jaraco.stream import buffer

server = irc.client.Reactor().server()
server.buffer_class = buffer.LenientDecodingLineBuffer
server.connect()