from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        MainWindow.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint)
        MainWindow.move(0,0)
        MainWindow.resize(600, 549)
        MainWindow.setMinimumSize(QtCore.QSize(200, 200))
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.settings_frame = QtWidgets.QFrame(self.centralwidget)
        self.settings_frame.setGeometry(QtCore.QRect(199, 0, 401, 168))
        self.settings_frame.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-style: solid;")
        self.settings_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.settings_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.settings_frame.setObjectName("settings_frame")
        self.settings_frame1 = QtWidgets.QFrame(self.settings_frame)
        self.settings_frame1.setGeometry(QtCore.QRect(0, 40, 400, 131))
        self.settings_frame1.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"border-width: 1px;\n"
"border-style: solid;")
        self.settings_frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.settings_frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.settings_frame1.setObjectName("settings_frame1")
        self.show_icon = QtWidgets.QCheckBox(self.settings_frame1)
        self.show_icon.setGeometry(QtCore.QRect(20, 40, 121, 17))
        self.show_icon.setStyleSheet("font: 700 7pt \"Tahoma\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: none;\n"
"border:none;")
        self.show_icon.setObjectName("show_icon")

        self.show_search_bar = QtWidgets.QCheckBox(self.settings_frame1)
        self.show_search_bar.setText("Show Search Bar")
        self.show_search_bar.setGeometry(QtCore.QRect(20, 70, 101, 17))
        self.show_search_bar.setStyleSheet("font: 700 7pt \"Tahoma\";\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "background-color: none;\n"
                                     "border:none;")
        self.show_search_bar.setObjectName("show_search_bar")


        self.settings_title = QtWidgets.QTextBrowser(self.settings_frame1)
        self.settings_title.setGeometry(QtCore.QRect(10, 10, 101, 21))
        self.settings_title.setStyleSheet("color: rgb(236, 18, 2);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"border:none;")
        self.settings_title.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.settings_title.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.settings_title.setObjectName("settings_title")
#         self.mute = QtWidgets.QCheckBox(self.settings_frame1)
#         self.mute.setGeometry(QtCore.QRect(20, 70, 101, 17))
#         self.mute.setStyleSheet("font: 700 7pt \"Tahoma\";\n"
# "color: rgb(255, 255, 255);\n"
# "background-color: none;\n"
# "border:none;")
#         self.mute.setObjectName("mute")

        self.show_terminal = QtWidgets.QCheckBox(self.settings_frame1)
        self.show_terminal.setGeometry(QtCore.QRect(20, 100, 111, 17))
        self.show_terminal.setStyleSheet("font: 700 7pt \"Tahoma\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: none;\n"
"border:none;")
        self.show_terminal.setObjectName("show_terminal")
        self.close_button = QtWidgets.QPushButton(self.settings_frame1)
        self.close_button.setGeometry(QtCore.QRect(378, 105, 21, 21))
        self.close_button.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border: none;")
        self.close_button.setObjectName("close_button")
        self.min_button = QtWidgets.QPushButton(self.settings_frame)
        self.min_button.setGeometry(QtCore.QRect(370, 0, 31, 23))
        self.min_button.setStyleSheet("background-color: transparent;\n"
                                      "border: none;\n"
                                      "font: 24pt \"MS Shell Dlg 2\";\n"
                                      "color: rgb(255, 255, 255);")
        self.min_button.setObjectName("min_button")
        self.name = QtWidgets.QLabel(self.settings_frame)
        self.name.setGeometry(QtCore.QRect(10, 7, 301, 31))
        self.name.setMaximumSize(QtCore.QSize(331, 241))
        font = QtGui.QFont()
        font.setFamily("Small Fonts")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.name.setFont(font)
        self.name.setStyleSheet("border: none;\n"
"color: rgb(255, 255, 255);")
        self.name.setText("")
        self.name.setPixmap(QtGui.QPixmap("RESOURCES/FRIDAY_TITLE.png"))
        self.name.setScaledContents(True)
        self.name.setWordWrap(False)
        self.name.setObjectName("name")
        self.input_frame = QtWidgets.QFrame(self.centralwidget)
        self.input_frame.setGeometry(QtCore.QRect(199, 168, 401, 31))
        self.input_frame.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-style: solid;")
        self.input_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.input_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.input_frame.setObjectName("input_frame")

        self.input_frame1 = QtWidgets.QFrame(self.centralwidget)
        self.input_frame1.setGeometry(QtCore.QRect(199, 168, 401, 31))
        self.input_frame1.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                       "border-color: rgb(255, 255, 255);\n"
                                       "border-width: 2px;\n"
                                       "border-style: solid;")
        self.input_frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.input_frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.input_frame1.setObjectName("input_frame1")

        self.input_box = QtWidgets.QLineEdit(self.input_frame)
        self.input_box.setGeometry(QtCore.QRect(0, 0, 351, 31))
        self.input_box.setStyleSheet("color: rgb(188, 120, 71);")
        self.input_box.setObjectName("input_box")
        self.input_box.setText("")
        self.input_box.setPlaceholderText("Enter your query here")



        self.send_button = QtWidgets.QPushButton(self.input_frame)
        self.send_button.setGeometry(QtCore.QRect(360, 4, 31, 23))
        self.send_button.setStyleSheet("border: none;\n"
                                  "color: transparent;\n"
                                  "background-color: transparent;\n"
                                       "opacity:0")
        self.send_button.setObjectName("send_button")

        self.name_2 = QtWidgets.QLabel(self.input_frame)
        self.name_2.setGeometry(QtCore.QRect(360, 4, 31, 23))
        # self.name_2.setMaximumSize(QtCore.QSize(331, 241))
        # font = QtGui.QFont()
        # font.setFamily("Small Fonts")
        # font.setPointSize(10)
        # font.setBold(True)
        # font.setWeight(75)
        # self.name_2.setFont(font)
        self.name_2.setStyleSheet("border: none;")
        # self.name_2.setText("")
        self.name_2.setPixmap(QtGui.QPixmap("RESOURCES/SEND_BUTTON.png"))
        self.name_2.setScaledContents(True)
        # self.name_2.setWordWrap(False)
        self.name_2.setObjectName("name_2")
        self.logo_button = QtWidgets.QPushButton(self.centralwidget)
        self.logo_button.setGeometry(QtCore.QRect(30, 30, 140, 140))
        self.logo_button.setStyleSheet("background-color: transparent;\n"
                                      "border: none;\n"
                                      "font: 0px \"MS Shell Dlg 2\";\n"
                                      "color: transparent;\n"
                                      "opacity: 0;")
        self.logo_button.setObjectName("logo_button")
        self.terminal_frame = QtWidgets.QFrame(self.centralwidget)
        self.terminal_frame.setGeometry(QtCore.QRect(0, 198, 600, 351))
        self.terminal_frame.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-style: solid;")
        self.terminal_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.terminal_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.terminal_frame.setObjectName("terminal_frame")
        self.terminal_title = QtWidgets.QTextEdit(self.terminal_frame)
        self.terminal_title.setGeometry(QtCore.QRect(0, 0, 600, 30))
        self.terminal_title.setReadOnly(True)
        self.terminal_title.setStyleSheet("color: rgb(255, 255, 255);\n"
"color: rgb(238, 0, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.terminal_title.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.terminal_title.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.terminal_title.setObjectName("terminal_title")
        self.terminal_box = QtWidgets.QPlainTextEdit(self.terminal_frame)
        self.terminal_box.setGeometry(QtCore.QRect(50, 60, 491, 211))
        self.terminal_box.setReadOnly(True)
        self.terminal_box.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "background-color:transparent;")
        self.terminal_box.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.terminal_box.setPlainText("")
        self.terminal_box.setObjectName("terminal_box")
        self.label = QtWidgets.QLabel(self.terminal_frame)
        self.label.setGeometry(QtCore.QRect(0, 28, 600, 321))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("RESOURCES/TERMINAL_FRAME.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.speaking = QtWidgets.QLabel(self.centralwidget)
        self.speaking.setGeometry(QtCore.QRect(0, 0, 200, 200))
        self.speaking.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-style: solid;")
        self.speaking.setText("")
        self.speaking.setPixmap(QtGui.QPixmap("RESOURCES/speaking.gif"))
        self.speaking.setScaledContents(True)
        self.speaking.setObjectName("speaking")

        self.listening = QtWidgets.QLabel(self.centralwidget)
        self.listening.setGeometry(QtCore.QRect(0, 0, 200, 200))
        self.listening.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-style: solid;")
        self.listening.setText("")
        self.listening.setPixmap(QtGui.QPixmap("RESOURCES/listening.gif"))
        self.listening.setScaledContents(True)
        self.listening.setObjectName("listening")

        self.loading = QtWidgets.QLabel(self.centralwidget)
        self.loading.setGeometry(QtCore.QRect(0, 0, 200, 200))
        self.loading.setStyleSheet("border-color: rgb(255, 255, 255);\n"
                                     "border-width: 2px;\n"
                                     "border-style: solid;")
        self.loading.setText("")
        self.loading.setPixmap(QtGui.QPixmap("RESOURCES/loading.gif"))
        self.loading.setScaledContents(True)
        self.loading.setObjectName("loading")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 200, 200))
        self.frame.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-style: solid;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.logo_label = QtWidgets.QLabel(self.frame)
        self.logo_label.setGeometry(QtCore.QRect(25, 25, 150, 150))
        self.logo_label.setStyleSheet("border:none")
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap("RESOURCES/logo1.gif"))
        self.logo_label.setScaledContents(True)
        self.logo_label.setObjectName("logo_label")

        self.settings_frame.raise_()
        self.input_frame.raise_()
        self.terminal_frame.raise_()


        self.logo_label.raise_()
        self.logo_button.raise_()

        self.terminal_box.raise_()
        # self.send_button.raise_()

        self.name_2.raise_()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.show_icon.setText(_translate("MainWindow", "Show Status Icon"))
        self.settings_title.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">SETTINGS</span></p></body></html>"))
        # self.mute.setText(_translate("MainWindow", "Mute FRIDAY"))
        self.show_terminal.setText(_translate("MainWindow", "Show Terminal"))
        self.close_button.setText(_translate("MainWindow", "x"))
        self.min_button.setText(_translate("MainWindow", "-"))
        self.send_button.setText(_translate("MainWindow", "PushButton"))
        self.logo_button.setText(_translate("MainWindow", "PushButton"))
        self.terminal_title.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">FRIDAY TERMINAL</span></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
