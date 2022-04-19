# This is a little simple screenrecorder in just a few lines
# Das ist ein kleiner einfacher Screen recorder, in nur ein Paar Zeilen

# # # # # # #
#  imports  #
# # # # # # #
import cv2, numpy, pyautogui, keyboard # You will have to install these libraries first. You can do this with pip. # Du musst diese libraries zuerst installieren. Das kannst du mit pip tun.
# pip install opencv-python
# pip install numpy (numpy comes normally with opencv)
# pip install pyautogui
# pip install keyboard

# Here we're gonna define a variable with the file name of the output file (as a String)
# Hier werden wir eine Variable mit dem Dateinamen der Output-Datei definieren (Als String)
filename = "recorded"

# Here we're gonna define a variable with the screen size you want to use for the recording
# Hier definieren wir eine Variable, wo wir die Bildschirmgröße angeben, die wir für die Aufnahme verwenden wollen
screen_size = (1920, 1080)

# Every screen recorder needs a codec, for decoding the file. So we are gonna do this by defining a variable which contains the VideoWriter_fourcc Method of opencv
# The parameter will be the format of the file, so the format in which the file will be decoded. In this case we're using mp4

# Jeder screen recorder braucht einen codec, um die Aufnahme bzw. Datei in ein bestimmtes Format zu dekodieren. Das machen wir, indem wir eine Variable definieren die die VideoWriter_fourcc Methode von opencv enthält
# Der Parameter ist das Format der Datei, also in welches Format sie dekodiert wird. In unserem Fall benutzen wir mp4
codec = cv2.VideoWriter_fourcc(*'mp4v')

# Now we're "building" or video which we want to record, with the VideoWriter method and our variables as the parameters. 20.0 is the framerate for the video
# Jetzt "Bauen" wir unser Video zusammen, indem wir die VideoWriter Methode und unsere Variablen als Parameter. 20.0 ist die Framerate des Videos
vid = cv2.VideoWriter(filename + '.mp4', codec, 20.0, (screen_size))


print("Start")

# Here we are writing a while True loop, so it updates the frames every time
# Hier schreiben wir eine while True Schleife, damit die Bilder immer durchlaufen und sich die frames sozusagen updaten
while True:
    # Here we are using the screenshot method from pyautogui. Since it's in a while True loop, it takes a screenshot every time (because a video is just thousands of images)
    # Hier benutzen wir die screenshot Methode von pyautogui. Da es eine while True Schleife ist, macht es die ganze Zeit einen screenshot (Weil ein Video aus tausenden Bildern besteht)
    img = pyautogui.screenshot()

    # With this method from numpy, we convert the whole thing into a matrix, which can be easily processed by opencv
    # Mit dieser Methode von numpy, wandeln wir das ganze in eine von opencv leicht zu verarbeitende Matrix um
    numpy_frame = numpy.array(img)

    # With the cvtColor method, opencv turns an RGB image out of the screenshots
    # Mit der cvtColor Methode macht opencv aus den Screenshots ein RGB Bild
    frame = cv2.cvtColor(numpy_frame, cv2.COLOR_BGR2RGB)

    # After the Screenshots are set up we can write it in our video container by using the write method from opencv
    # Nachdem die Screenshots fertig aufbereitet wurden, schreiben wir diese in unseren Video-Container
    vid.write(frame)

    # Here we are using an if statement, to breakup the recording. In this example, we say, if x is pressed on the keyboard, then stop the loop
    # Hier benutzen wir ein if-statement, um  die Aufnahme zu beenden. In diesem Beispiel sagen wir, wenn x auf der Tastatur gedrückt wurde, dann stoppe die Schleife
    if keyboard.is_pressed('x'):
        print("Stop")
        break

# After the loop is stopped and finished, we'll destroy all Windows and finalize our video, so it'll be saved on our storage
# Nachdem die Schleife beendet wurde und fertig ist, zerstören wir alle Fenster und finalisieren das Video, sodass es auf die Festplatte gespeichert wird        
cv2.destroyAllWindows()
vid.release()
