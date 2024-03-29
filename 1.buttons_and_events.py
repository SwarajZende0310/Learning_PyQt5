from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setGeometry(200,100,300,300)
        self.setWindowTitle("Signals : Buttons and Events")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Hello World!")
        self.label.move(50,50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click me")
        self.b1.clicked.connect(self.b1_callback)

    def b1_callback(self):
        self.label.setText("You pressed the Button")
        self.update()
    
    def update(self):
        self.label.adjustSize() #Update the width according the lenght of sentence


def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()

    sys.exit(app.exec_())

def main():
    window()

if __name__ == '__main__':
    main()
