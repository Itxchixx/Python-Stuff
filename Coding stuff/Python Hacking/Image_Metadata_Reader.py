# With this, you can read out metadata from an image such as:
#  Orientation, The software which was used, GPSInfo if given, size and some other info

# Mit diesem Programm kannst du Metadaten aus einem Bild lesen, wie zum Beispiel:
#  rientation, Die software die benutzt wurde, GPSInfo wenn angegeben, Bildgröße und andere Informationen

# # # # # # #
#  imports  #
# # # # # # #
from PIL import Image, ExifTags
# pip install pillow

# At first we'll define a variable which contains a file path. In this case we'll use an input, so the user can paste his own image path
# Als erstes definieren wir eine Variable, die den Dateipfad enthält. Wir benutzen hier einen input, damit der Benutzer selbst einen Dateipfad angeben kann
chooser = input("Image Path here: ")

# Next, we'll define a variable which contains the open method from the Image class from pillow. We'll use the variable for the file path as the parameter here
# Als nächstes definieren wir eine Variable, die die open Methode von der Image Klasse von pillow enthält. Als Parameter benutzen wir die Variable die wir für den Dateipfad benutzt haben.
img = Image.open(chooser)

# Now, to display the items (the info) in a good looking way, we'll use a for loop
# Um die items (die Informationen), in einem gut aussehendem Format auszugeben, benutzen wir eine For-Schleife
for i, j in img._getexif().items():  # in the -_getexif().items() Method we are getting all the info. # Mit der ._getexif().items() Methode bekommen wir die Informationen
    # Now we're checking if i is in the exifTags.
    # Jetzt überprüfen wir, ob i in den exifTags vorhanden ist.
    if i in ExifTags.TAGS:
        # If True, we'll print out the tags (information)
        # Wenn True, dann geben wir die Tags (Informationen) aus
        print(ExifTags.TAGS[i] + " - " + str(j))
