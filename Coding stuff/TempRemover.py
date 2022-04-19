# This program removes all the unneeded files in the temp folder
# Dieses Programm löscht alle unbrauchbaren Dateien im temp Ordner

# # # # # # #
#  imports  #
# # # # # # #
import time
import os
import shutil

# No installation for the libraries needed


print("_-_-_-_-_-_Temp files remover_-_-_-_-_-_")

# At first we're defining a variable, which contains the path of the temp folder, written in a String
# Als erstes definieren wir eine Variable, die den Pfad des temp Ordners, als String
folder = "PATH"

# Now we will use a for loop to list all the files which are in the folder, by calling the listdir method from os. As parameter we'll use the folder variable
# Jetzt benutzen wir eine For Schleife, um alle Dateien die in dem Ordner sind aufzulisten, in dem wir die listdir Methode von os benutzen. Als Parameter benutzen wir die folder Variable
for filename in os.listdir(folder):
    # Join one or more path components intelligently. The return value is the concatenation of path and any members of *paths with exactly one directory separator following each
    # non-empty part except the last,
    # meaning that the result will only end in a separator if the last part is empty

    # Verbindet eine oder mehrere Pfadkomponenten auf intelligente Weise. Der Rückgabewert ist die Verkettung von path und beliebigen Bestandteilen von *paths mit genau einem Verzeichnistrennzeichen nach jedem nicht leeren Teil,
    # außer dem letzten, was bedeutet, dass das Ergebnis nur dann mit einem Trennzeichen endet,
    # wenn der letzte Teil leer ist.
    file_path = os.path.join(folder, filename)

    # Since we're working with files, we'll try except
    try:
        # Here we're checking if file_path is an existing file
        # Hier überprüfen wir ob file_path eine existierende Datei ist
        if os.path.isfile(file_path) or os.path.islink(file_path):
            # If true, it will delete the file path
            # Wenn True, dann löscht es den Dateipfad
            os.unlink(file_path)

        # Here we're checking if file_path is an existing directory
        # Hier überprüfen wir, ob file_path ein existierendes Verzeichnis ist
        elif os.path.isdir(file_path):
            # If true, it deletes all the files in this directory (temp folder)
            # Wenn true, dann löscht es alle Dateien in diesem Verzeichnis (temp Ordner)
            shutil.rmtree(file_path)
            print("Deleted Files")
    # "except" catches erros and prints them output
    # "except" fängt Error ab und gibt sie in der Konsole aus
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))
