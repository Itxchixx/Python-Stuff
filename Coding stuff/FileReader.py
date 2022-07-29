
# Here we are ONLY reading the file (which means we can't write anything in the file), because of the "r" which we have given as the second parameter, which stands for read
# Hier wird die Datei NUR bzw. ausschließlich gelesen (was bedeuted, dass man nichts in die Datei schreiben kann), da wir hier das "r" als zweites Parameter angegeben haben, was soviel wie read (überstetzt: lesen) bedeuted
file = open("writtenFile.txt", "r")

# Now we are defining a variable content, which has the read method from python stored in it
# Jetzt definieren wir eine Variable, die die read Methode von Python beinhaltet
content = file.read()
# With this method we are reading out the text (in this case it's a text) which is in the file
# Mit dieser Methode lesen wir den Text (in dem Fall ist es normaler Text), der in der Datei steht

# Now this is a simple example for what you could do with the content variable and the file
# Das ist jetzt ein simples Beispiel für das benutzen der content Variable und der Datei
try:

    if content == "Written text in file":
        # you can add your code in here. This is an easy example for writing a new text to the file
        # Du kannst hier deinen eigenen code hinzufügen. Das ist ein einfaches Beispiel um neuen Text in die Datei zu schreiben

        file = open("writtenFile.txt", "w")
        file.write("Fr")
        # Close the file
        file.close()
except Exception:
    print("Error occured")
    
# An easier way to do it
try:
    with open("writtenFile.txt", "r") as f:
        content = f.read()
        # Do stuff with the read text
        
except Exception:
    print("Error occured")

# FileWriter first has to be executed before running this program
# FileWriter muss erst ausgeführt werden, bevor dieses Programm ausgeführt wird
