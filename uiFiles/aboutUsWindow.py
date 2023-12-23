from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_about_us_window_dialog(object):


    def setupUi(self, about_us_window_dialog):
        about_us_window_dialog.setObjectName("about_us_window_dialog")
        about_us_window_dialog.resize(780, 577)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(about_us_window_dialog.sizePolicy().hasHeightForWidth())
        about_us_window_dialog.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        about_us_window_dialog.setFont(font)
        about_us_window_dialog.setAutoFillBackground(False)
        about_us_window_dialog.setStyleSheet("font: 75 \"Verdana\";\n"
"background-color: rgb(255, 255, 255);")
        self.title_label = QtWidgets.QLabel(parent=about_us_window_dialog)
        self.title_label.setGeometry(QtCore.QRect(0, 0, 781, 131))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("font: 75 28pt \"Verdana\";\n"
"background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-bottom: 2px solid rgb(194, 194, 194);")
        self.title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title_label.setObjectName("title_label")

        self.gridLayoutWidget = QtWidgets.QWidget(parent=about_us_window_dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 150, 275, 207))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.image_label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.image_label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_label.sizePolicy().hasHeightForWidth())
        self.image_label.setSizePolicy(sizePolicy)
        self.image_label.setAutoFillBackground(False)
        self.image_label.setStyleSheet("border: 1px solid;\n"
                                       "border-color: rgb(85, 170, 255);")
        self.image_label.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.image_label.setText("")
        self.image_label.setPixmap(QtGui.QPixmap('../images/image.jpg'))
        # self.image_label.setPixmap(QtGui.QPixmap('image.jpg'))
        self.image_label.setScaledContents(False)
        self.image_label.setObjectName("image_label")
        self.gridLayout.addWidget(self.image_label, 0, 0, 1, 1)

        self.label_2 = QtWidgets.QLabel(parent=about_us_window_dialog)
        self.label_2.setGeometry(QtCore.QRect(330, 150, 421, 211))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(parent=about_us_window_dialog)
        self.label_3.setGeometry(QtCore.QRect(330, 385, 341, 71))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_6 = QtWidgets.QLabel(parent=about_us_window_dialog)
        self.label_6.setGeometry(QtCore.QRect(60, 500, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.label_5 = QtWidgets.QLabel(parent=about_us_window_dialog)
        self.label_5.setGeometry(QtCore.QRect(60, 380, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(about_us_window_dialog)
        QtCore.QMetaObject.connectSlotsByName(about_us_window_dialog)

    def retranslateUi(self, about_us_window_dialog):
        _translate = QtCore.QCoreApplication.translate
        about_us_window_dialog.setWindowTitle(_translate("about_us_window_dialog", "О нас"))
        self.title_label.setText(_translate("about_us_window_dialog", "Салон красоты\n"
                                                                      "\"Айнур\""))
        self.label_2.setText(_translate("about_us_window_dialog", "Мы представляем широкий выбор услуг для ухода \n"
                                                                  "за внешностью, включая стрижки и окрашивание\n"
                                                                  "волос, маникюр, массаж и различные косметические\n"
                                                                  "процедуры для лица и тела. Наша команда\n"
                                                                  "профессионалов готова помочь вам достигнуть\n"
                                                                  "любой цели — независимо от того, нужно ли вам\n"
                                                                  "просто расслабиться и отдохнуть, или вы ищете\n"
                                                                  "способ улучшить свой образ."))
        self.label_3.setText(_translate("about_us_window_dialog", "Наш адрес:\n"
                                                                  "      Астраханская область,\n"
                                                                  "      г. Знаменск, ул. Пионерская, д. 3"))
        self.label_6.setText(_translate("about_us_window_dialog", "Контактный телефон:\n"
                                                                  "    • 8 917 086 24 34"))
        self.label_5.setText(_translate("about_us_window_dialog", "График работы:\n"
                                                                  "    10.00-20.00\n"
                                                                  "    каждый день\n"
                                                                  "    (без выходных)"))
