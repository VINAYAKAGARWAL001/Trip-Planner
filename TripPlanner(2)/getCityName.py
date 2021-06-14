# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secondselection.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import dbQueries as Db
city_list=Db.get_city_list()

class Ui_cityForm(object):
    def setupUi(self, cityForm, parent):
        cityForm.setObjectName("cityForm")
        cityForm.resize(621, 295)
        self.verticalLayout = QtWidgets.QVBoxLayout(cityForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(cityForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.srccombo = QtWidgets.QComboBox(cityForm)
        self.srccombo.setObjectName("srccombo")
        self.horizontalLayout.addWidget(self.srccombo)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.okbtn = QtWidgets.QPushButton(cityForm)
        self.okbtn.setObjectName("okbtn")
        self.horizontalLayout_2.addWidget(self.okbtn)
        self.cancelbtn = QtWidgets.QPushButton(cityForm)
        self.cancelbtn.setObjectName("cancelbtn")
        self.horizontalLayout_2.addWidget(self.cancelbtn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(cityForm)
        QtCore.QMetaObject.connectSlotsByName(cityForm)

        self.parent=parent
        self.srccombo.addItems(city_list)
        self.cancelbtn.clicked.connect(lambda:cityForm.close())
        self.okbtn.clicked.connect(self.showTransport)

    def showTransport(self):
        self.parent.execmethod()

    def retranslateUi(self, cityForm):
        _translate = QtCore.QCoreApplication.translate
        cityForm.setWindowTitle(_translate("cityForm", "Form"))
        self.label.setText(_translate("cityForm", "Select Your Nearest City"))
        self.okbtn.setText(_translate("cityForm", "Ok"))
        self.cancelbtn.setText(_translate("cityForm", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cityForm = QtWidgets.QWidget()
    ui = Ui_cityForm()
    ui.setupUi(cityForm)
    cityForm.show()
    sys.exit(app.exec_())
