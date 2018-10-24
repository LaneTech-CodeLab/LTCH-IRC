from irc import *
from command_decipher import *

def main():
    joinchan(channel)
    while True:
        ircmsg = ircsock.recv(2048).decode("UTF-8")
        ircmsg = ircmsg.strip('\n\r')
        print(ircmsg)

        check(ircmsg)

main()