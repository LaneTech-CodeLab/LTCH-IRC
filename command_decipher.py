from irc import *
from irc_commands import *

def check(ircmsg):
    if ircmsg.find("PRIVMSG") != -1:
        name = ircmsg.split('!', 1)[0][1:]
        message = ircmsg.split('PRIVMSG', 1)[1].split(':', 1)[1]
        c = Commands(message, name)

        if len(name) < 17:
            if message.find('hi ' + botnick) != -1:
                sendmsg(c.hello(name))
            elif message.find('.vend') != -1:
                sendmsg(c.vend(message))
            elif message.find('.shoot') != -1:
                x = c.shoot(message, name)

                for i in range(len(x)):
                    sendmsg(x[i])
            elif message.find('.green') != -1:
                sendmsg(c.green(message, name))
            elif message.find(".rainbow") != -1:
                sendmsg(c.rainbow(message))
            elif message.find(".help") != -1 or message.find(".version") != -1:
                sendmsg(c.info())
    elif ircmsg.find("PING :") != -1:
                ping(ircmsg)
