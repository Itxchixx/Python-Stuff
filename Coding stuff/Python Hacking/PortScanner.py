# This is a simple Port scanner, which scans for open ports
# Dies ist ein simpler Port Scanner, der für offene Ports scant

# # # # # # #
#  imports  #
# # # # # # #
import socket
import sys
from datetime import datetime
# no installation needed

# At first, we'll define a variable where we specify the target. Here we are using scanme.nmap.org because it's allowed to scan it (but not too much).
# Als erstes werden wir eine Variable definieren, wo wir die Zieladdresse angeben.
target = "scanme.nmap.org"

# Now we want to get the real ip from the site, which we can do with the getHostByName method from socket. We'll give the target variable as parameter here
# Jetzt möchten wir die IP Adresse dieser Seite haben, was wir mit der getHostByName Methode von socket machen können. Wir geben hier die target Variable als Parameter an
targetIP = socket.gethostbyname(target)

# This is to start a timer to see how long it took to scan the Ports
# Damit starten wir sozusagen einen Timer, um zu sehen, wie lange wir gebraucht haben, um die Ports zu scannen
tStart = datetime.now()

# Now we'll use a for in range loop to specify the amount of ports we want to scan
# Jetzt benutzen wir eine for in range Schleife, um die Menge der Ports die wir scannen möchten, anzugeben
try:

    for p in range(1, 800):
        # Here we will set up a connection
        # Hier bauen wir eine Verbindung auf
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        res = sock.connect_ex((targetIP, p))

        # Now we're checking if a port is open
        # Jetzt überprüfen wir ob ein Port offen ist
        if res == 0:
            print("Open connection at Port:" + str(p))
        sock.close()
except Exception:
    print("Error occured")
    sys.exit()

tend = datetime.now()

diff = tend - tStart
print("Scan completed in " + str(diff))
