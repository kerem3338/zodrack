from tkinter import *
import os
import sys
import time
import threading
from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui,QtWidgets
import webbrowser

global run
global helpz


def helpz():
    webbrowser.open_new("https://github.com/kerem3338/")

def run(): 
    """Runs Minecraft Bedrock Edition"""   
    os.system(os.path.join(os.environ["userprofile"]+"\\Desktop\\Minecraft.lnk"))
    def wait_and_kill():
        time.sleep(12) 
        os.system("taskkill /F /IM RuntimeBroker.exe")  
    threading.Thread(target=wait_and_kill).start()





class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)

        self.play_button=self.findChild(QtWidgets.QPushButton, "pushButton")
        self.help_button=self.findChild(QtWidgets.QPushButton, "pushButton_2")
        self.status=self.findChild(QtWidgets.QStatusBar,"statusbar")

        self.status.showMessage("Launcher Started!")
        self.help_button.clicked.connect(helpz)
        self.play_button.clicked.connect(run)
        self.show()
try:
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
except KeyboardInterrupt:
    sys.exit()