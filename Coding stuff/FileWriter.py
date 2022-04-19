# Example for Writing a (.txt) file


# At first you want to define a variable, which contains the open method. This is a built-in method of Python, so no need to install anything. The first parameter of the function will be the file path.
# In the second parameter you have to specify, what you want to do with the file. In our case it's the "w", which stands for "write"

# Als erstes definieren wir eine Variable welche die open Methode enthält. Diese Methode ist eine in Python eingebaute Methode, also muss für die Verwendung nichts installiert werden.
# Als ersten Parameter gibt man den Dateipfad an. Beim zweiten Parameter gibt man an, was man mit der Datei machen möchte. In unserem Fall geben wir "w" an, was für "write" steht, also schreiben.
file = open("writtenFile.txt", "w")

# Then you want to use the write method, which is also a built-in method of Python. Type in the variable name and then you'll call the write method.
# As the parameter of the method you simply type in the text you want to write in the file

# Als nächstes werden wir die write Methode benutzen, welche ebenfalls eine in Python eingebaute Methode ist. Gib den Namen deiner zuvor definierten Variable an, und rufe dann die write Methode auf.
# Als Parameter der Funktion gibst du einfach nur den Text an, der in die Datei geschrieben werden soll.

file.write("Written text in file")

# Execute to write file
# Ausführen um die Datei zu schreiben
