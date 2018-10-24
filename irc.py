import socket
from irc_commands import *

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "irc.freenode.net" # Server
channel = "#ltch" # Channel
botnick = "eff3" # Your bots nick
adminname = "er3v" #Your IRC nickname. On IRC (and most other places) I go by OrderChaos so that’s what I am using for this example.

ircsock.connect((server, 6667)) # Here we connect to the server using the port 6667
ircsock.sendall(("NICK " + botnick + "\n").encode("utf8")) # assign the nick to the bot
ircsock.sendall(("USER " + botnick + " " + botnick + " " + botnick + " " + botnick + "\n").encode("utf8")) #We are basically filling out a form with this line and saying to set all the fields to the bot nickname.
ircsock.sendall(("/msg NickServ identify 90jM6KhMIPYU\n").encode("utf8"))

def joinchan(chan): # join channel(s).
  ircsock.sendall(("JOIN "+ chan +"\n").encode("utf8"))
  ircmsg = ""
  while ircmsg.find("End of /NAMES list.") == -1:
    ircmsg = ircsock.recv(2048).decode("UTF-8")
    ircmsg = ircmsg.strip('\n\r')
    print(ircmsg)

def ping(): # respond to server Pings.
    ircsock.sendall(("PONG :pingis\n", "UTF-8").encode("utf8"))

def sendmsg(msg, target=channel): # sends messages to the target.
    ircsock.sendall(("PRIVMSG "+ target +" :"+ msg +"\n").encode("utf8"))

