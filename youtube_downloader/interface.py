# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceNKHyBo.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(350, 489)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.directory_select = QPushButton(self.centralwidget)
        self.directory_select.setObjectName(u"directory_select")
        self.directory_select.setGeometry(QRect(20, 10, 301, 41))
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setPointSize(18)
        self.directory_select.setFont(font)
        self.directory_select.setIconSize(QSize(16, 16))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 60, 301, 31))
        font1 = QFont()
        font1.setPointSize(10)
        self.label.setFont(font1)
        self.url = QLineEdit(self.centralwidget)
        self.url.setObjectName(u"url")
        self.url.setGeometry(QRect(20, 130, 301, 22))
        self.url.setFont(font1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(150, 100, 31, 21))
        font2 = QFont()
        font2.setPointSize(17)
        font2.setBold(False)
        self.label_2.setFont(font2)
        self.format_mp4 = QRadioButton(self.centralwidget)
        self.format_mp4.setObjectName(u"format_mp4")
        self.format_mp4.setGeometry(QRect(90, 200, 51, 31))
        self.format_mp4.setSizeIncrement(QSize(0, 0))
        font3 = QFont()
        font3.setPointSize(12)
        self.format_mp4.setFont(font3)
        self.format_mp3 = QRadioButton(self.centralwidget)
        self.format_mp3.setObjectName(u"format_mp3")
        self.format_mp3.setGeometry(QRect(170, 200, 51, 31))
        self.format_mp3.setSizeIncrement(QSize(0, 0))
        self.format_mp3.setFont(font3)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(120, 160, 101, 31))
        font4 = QFont()
        font4.setPointSize(20)
        self.label_3.setFont(font4)
        self.download = QPushButton(self.centralwidget)
        self.download.setObjectName(u"download")
        self.download.setGeometry(QRect(20, 330, 301, 111))
        font5 = QFont()
        font5.setFamilies([u"Bahnschrift"])
        font5.setPointSize(34)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setUnderline(False)
        self.download.setFont(font5)
        self.download.setIconSize(QSize(16, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(100, 240, 141, 31))
        self.label_4.setFont(font4)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 280, 253, 28))
        self.res_block = QHBoxLayout(self.widget)
        self.res_block.setObjectName(u"res_block")
        self.res_block.setContentsMargins(0, 0, 0, 0)
        self.res_high = QRadioButton(self.widget)
        self.res_high.setObjectName(u"res_high")
        self.res_high.setSizeIncrement(QSize(0, 0))
        self.res_high.setFont(font3)

        self.res_block.addWidget(self.res_high)

        self.res_low = QRadioButton(self.widget)
        self.res_low.setObjectName(u"res_low")
        self.res_low.setSizeIncrement(QSize(0, 0))
        self.res_low.setFont(font3)

        self.res_block.addWidget(self.res_low)

        self.res_other = QRadioButton(self.widget)
        self.res_other.setObjectName(u"res_other")
        self.res_other.setSizeIncrement(QSize(0, 0))
        self.res_other.setFont(font3)

        self.res_block.addWidget(self.res_other)

        self.res_list = QComboBox(self.widget)
        self.res_list.setObjectName(u"res_list")
        self.res_list.setEnabled(False)

        self.res_block.addWidget(self.res_list)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 350, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.directory_select.setText(QCoreApplication.translate("MainWindow", u"Select directory", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"No directory selected", None))
        self.url.setText("")
        self.url.setPlaceholderText(QCoreApplication.translate("MainWindow", u"No url seletced", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Url:", None))
        self.format_mp4.setText(QCoreApplication.translate("MainWindow", u"MP4", None))
        self.format_mp3.setText(QCoreApplication.translate("MainWindow", u"MP3", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Format:", None))
        self.download.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Resolution:", None))
        self.res_high.setText(QCoreApplication.translate("MainWindow", u"High", None))
        self.res_low.setText(QCoreApplication.translate("MainWindow", u"Low", None))
        self.res_other.setText(QCoreApplication.translate("MainWindow", u"Other", None))
    # retranslateUi

