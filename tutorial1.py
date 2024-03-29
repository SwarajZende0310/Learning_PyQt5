from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    # Set Size and label of window
    win.setGeometry(200,100,300,300) # xpos,ypos,width,height (origin = Top left corner) 
    win.setWindowTitle("Swaraj_learning_PyQt5")

    label = QtWidgets.QLabel(win)
    label.setText("Hello World!")
    label.move(50,50)

    win.show()

    sys.exit(app.exec_())#for clean exit and waiting for 'app' to exit

def main():
    window()

if __name__ == '__main__':
    main()
