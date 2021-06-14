# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\insert_update_delete.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from busInsertUpdate import Ui_busWindow as busInsUpd
from hotelInsertUpdate import Ui_hotelWindow as hotInsUpd
from planeInsertUpdate import Ui_planeWindow as plaInsUpd
from trainInsertUpdate import Ui_trainWindow as traInsUpd
from deleteWindow import Ui_DeleteWindow as delWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow,uname):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(711, 605)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(11, 11, 691, 281))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(180, -1, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.welcomeInsertUpdateDelete = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.welcomeInsertUpdateDelete.sizePolicy().hasHeightForWidth())
        self.welcomeInsertUpdateDelete.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        self.welcomeInsertUpdateDelete.setFont(font)
        self.welcomeInsertUpdateDelete.setObjectName("welcomeInsertUpdateDelete")
        self.horizontalLayout_3.addWidget(self.welcomeInsertUpdateDelete)
        self.nameDisplayInInsertUpdateDelete = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameDisplayInInsertUpdateDelete.sizePolicy().hasHeightForWidth())
        self.nameDisplayInInsertUpdateDelete.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.nameDisplayInInsertUpdateDelete.setFont(font)
        self.nameDisplayInInsertUpdateDelete.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.nameDisplayInInsertUpdateDelete.setObjectName("nameDisplayInInsertUpdateDelete")
        self.horizontalLayout_3.addWidget(self.nameDisplayInInsertUpdateDelete)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.line_3 = QtWidgets.QFrame(self.widget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.insertRadioButton = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(22)
        self.insertRadioButton.setFont(font)
        self.insertRadioButton.setObjectName("insertRadioButton")
        self.horizontalLayout_2.addWidget(self.insertRadioButton)
        self.updateRadioButton = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(22)
        self.updateRadioButton.setFont(font)
        self.updateRadioButton.setObjectName("updateRadioButton")
        self.horizontalLayout_2.addWidget(self.updateRadioButton)
        self.deleteRadioButton = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(22)
        self.deleteRadioButton.setFont(font)
        self.deleteRadioButton.setObjectName("deleteRadioButton")
        self.horizontalLayout_2.addWidget(self.deleteRadioButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(11, 294, 691, 281))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.planeRadioButton = QtWidgets.QRadioButton(self.widget1)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        self.planeRadioButton.setFont(font)
        self.planeRadioButton.setObjectName("planeRadioButton")
        self.horizontalLayout.addWidget(self.planeRadioButton)
        self.trainRadioButton = QtWidgets.QRadioButton(self.widget1)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        self.trainRadioButton.setFont(font)
        self.trainRadioButton.setObjectName("trainRadioButton")
        self.horizontalLayout.addWidget(self.trainRadioButton)
        self.busRadioButton = QtWidgets.QRadioButton(self.widget1)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        self.busRadioButton.setFont(font)
        self.busRadioButton.setObjectName("busRadioButton")
        self.horizontalLayout.addWidget(self.busRadioButton)
        self.hotelsRadioButton = QtWidgets.QRadioButton(self.widget1)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        self.hotelsRadioButton.setFont(font)
        self.hotelsRadioButton.setObjectName("hotelsRadioButton")
        self.horizontalLayout.addWidget(self.hotelsRadioButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_2 = QtWidgets.QFrame(self.widget1)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.okPushButtonInsertUpdateDelete = QtWidgets.QPushButton(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.okPushButtonInsertUpdateDelete.setFont(font)
        self.okPushButtonInsertUpdateDelete.setObjectName("okPushButtonInsertUpdateDelete")
        self.horizontalLayout_4.addWidget(self.okPushButtonInsertUpdateDelete)
        self.logoutPushButtonInsertUpdateDelete = QtWidgets.QPushButton(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.logoutPushButtonInsertUpdateDelete.setFont(font)
        self.logoutPushButtonInsertUpdateDelete.setObjectName("logoutPushButtonInsertUpdateDelete")
        self.horizontalLayout_4.addWidget(self.logoutPushButtonInsertUpdateDelete)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.nameDisplayInInsertUpdateDelete.setText(str(uname).upper())

        self.logoutPushButtonInsertUpdateDelete.clicked.connect(lambda: MainWindow.close())
        self.okPushButtonInsertUpdateDelete.clicked.connect(self.transferControl)
        self.duplicateMain = MainWindow

    def transferControl(self):
        if self.insertRadioButton.isChecked() :
            self.type = 'insert'
            if self.planeRadioButton.isChecked():
                self.planeForm = QtWidgets.QMainWindow()
                self.planeUi = plaInsUpd()
                # Pass another parameter for insert update
                self.planeUi.setupUi(self.planeForm,self.type)
                self.planeForm.show()
                self.duplicateMain.close()
            elif self.trainRadioButton.isChecked():
                self.trainForm = QtWidgets.QMainWindow()
                self.trainUi = traInsUpd()
                self.trainUi.setupUi(self.trainForm,self.type)
                self.trainForm.show()
                self.duplicateMain.close()
            elif self.busRadioButton.isChecked():
                self.busForm = QtWidgets.QMainWindow()
                self.busUi = busInsUpd()
                self.busUi.setupUi(self.busForm,self.type)
                self.busForm.show()
                self.duplicateMain.close()
            elif self.hotelsRadioButton.isChecked():
                self.hotelsForm = QtWidgets.QMainWindow()
                self.hotelsUi = hotInsUpd()
                self.hotelsUi.setupUi(self.hotelsForm,self.type)
                self.hotelsForm.show()
                self.duplicateMain.close()
        elif self.updateRadioButton.isChecked():
            self.type='update'
            if self.planeRadioButton.isChecked():
                self.planeForm = QtWidgets.QMainWindow()
                self.planeUi = plaInsUpd()
                self.planeUi.setupUi(self.planeForm,self.type)
                self.planeForm.show()
                self.duplicateMain.close()
            elif self.trainRadioButton.isChecked():
                self.trainForm = QtWidgets.QMainWindow()
                self.trainUi = traInsUpd()
                self.trainUi.setupUi(self.trainForm,self.type)
                self.trainForm.show()
                self.duplicateMain.close()
            elif self.busRadioButton.isChecked():
                self.busForm = QtWidgets.QMainWindow()
                self.busUi = busInsUpd()
                self.busUi.setupUi(self.busForm,self.type)
                self.busForm.show()
                self.duplicateMain.close()
            elif self.hotelsRadioButton.isChecked():
                self.hotelsForm = QtWidgets.QMainWindow()
                self.hotelsUi = hotInsUpd()
                self.hotelsUi.setupUi(self.hotelsForm,self.type)
                self.hotelsForm.show()
                self.duplicateMain.close()

        elif self.deleteRadioButton.isChecked():
            if self.planeRadioButton.isChecked():
                self.type='plane'
            elif self.trainRadioButton.isChecked():
                self.type='train'
            elif self.busRadioButton.isChecked():
                self.type='bus'
            elif self.hotelsRadioButton.isChecked():
                self.type='hotel'

            self.delForm = QtWidgets.QMainWindow()
            self.delUi = delWindow()
            self.delUi.setupUi(self.delForm,self.type)
            self.delForm.show()
            self.duplicateMain.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add/Modify/Delete"))
        self.welcomeInsertUpdateDelete.setText(_translate("MainWindow", "WELCOME  "))
        self.nameDisplayInInsertUpdateDelete.setText(_translate("MainWindow", "NAME"))
        self.insertRadioButton.setText(_translate("MainWindow", "INSERT"))
        self.updateRadioButton.setText(_translate("MainWindow", "UPDATE"))
        self.deleteRadioButton.setText(_translate("MainWindow", "DELETE"))
        self.planeRadioButton.setText(_translate("MainWindow", "PLANE"))
        self.trainRadioButton.setText(_translate("MainWindow", "TRAIN"))
        self.busRadioButton.setText(_translate("MainWindow", "BUS"))
        self.hotelsRadioButton.setText(_translate("MainWindow", "HOTELS"))
        self.okPushButtonInsertUpdateDelete.setText(_translate("MainWindow", "Ok"))
        self.logoutPushButtonInsertUpdateDelete.setText(_translate("MainWindow", "Logout"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow,'vinod')
    MainWindow.show()
    sys.exit(app.exec_())
