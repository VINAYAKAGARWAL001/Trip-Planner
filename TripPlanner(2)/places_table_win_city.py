# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'placesTable.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import dbQueries as Db
from placeInformation import Ui_Form as placeInformation


class Ui_Form(object):
    def setupUi(self, Form,source_city,city_name):
        Form.setObjectName("Form")
        Form.resize(1360, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../ImageFile/sunrise.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.DashLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.okbtn = QtWidgets.QPushButton(Form)
        self.okbtn.setMaximumSize(QtCore.QSize(1500000, 16777215))
        self.okbtn.setObjectName("okbtn")
        self.horizontalLayout.addWidget(self.okbtn)
        spacerItem = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancelbtn = QtWidgets.QPushButton(Form)
        self.cancelbtn.setObjectName("cancelbtn")
        self.horizontalLayout.addWidget(self.cancelbtn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.banner=QtGui.QMovie('ImageFile/sunrise.gif')
        self.label.setMovie(self.banner)
        self.banner.start()


        self.scity=source_city
        self.dcity=city_name

        #single row selection
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)

        #resize header to window size
        header=self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)


        #select row for mouse click on a row
        self.tableWidget.clicked.connect(self.selectPlace)
        self.cancelbtn.clicked.connect(lambda:Form.close())

        self.row=0
        self.okbtn.clicked.connect(self.openSelectedPlace)

        self.result=Db.get_places_city(city_name)

        self.tableWidget.setRowCount(len(self.result))
        for index,val in enumerate(self.result):
            for col in range(5):
                cell=QtWidgets.QTableWidgetItem(str(val[col]))
                self.tableWidget.setItem(index,col,cell)


    def selectPlace(self,clickedIndex):
        self.row=clickedIndex.row()


    def openSelectedPlace(self):
        placeInfo=Db.get_place_info(self.result[self.row][0])
        self.form5=QtWidgets.QWidget()
        self.placeInformation=placeInformation()
        self.placeInformation.setupUi(self.form5,placeInfo[0],self.scity,self.dcity,2)
        self.form5.show()


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Places"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "PLACE NAME"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "PLACE TYPE"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "LOCALITY"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "RATING"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "NEAR BY CITY"))
        self.okbtn.setText(_translate("Form", "OK"))
        self.cancelbtn.setText(_translate("Form", "back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
