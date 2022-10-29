
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QStyle
from PySide6.QtCore import QFile
from ui_interface import Ui_MainWindow

class Window(Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        for widget in self.ui.centralwidget.findChildren(QPushButton):
            print(widget.objectName())
            widget.setStyleSheet("QPushButton{	\
                                                border-radius:10px;	\
                                                background-color: rgb(203, 255, 222);\
                                            	border-style: solid;\
                                            	border-width: 1px;\
                                            	border-radius: 10px;\
                                            	border-color: rgb(63, 127, 94)}\
                                QPushButton:hover{ \
                                                background-color: rgb(255, 251, 133)};\
                                QPushButton:pressed{\
                                                background-color: rgb(255, 25, 48)};")

    #key event handle
    def keyPressEvent(self, event) -> None:
        print(event.text())
        # self.ui.pushButton_10

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    

    sys.exit(app.exec())
