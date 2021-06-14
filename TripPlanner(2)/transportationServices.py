# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'transport123.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import dbQueries as Db

class Ui_transportationWindow(object):
    def setupUi(self, transportationWindow,scity,dcity,parent):
        transportationWindow.setObjectName("transportationWindow")
        transportationWindow.setFixedSize(1360, 900)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(transportationWindow)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(transportationWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("ImageFile/bus.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.trainradio = QtWidgets.QRadioButton(transportationWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trainradio.sizePolicy().hasHeightForWidth())
        self.trainradio.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.trainradio.setFont(font)
        self.trainradio.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.trainradio.setChecked(True)
        self.trainradio.setObjectName("trainradio")
        self.horizontalLayout_2.addWidget(self.trainradio)
        self.busradio = QtWidgets.QRadioButton(transportationWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.busradio.sizePolicy().hasHeightForWidth())
        self.busradio.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.busradio.setFont(font)
        self.busradio.setObjectName("busradio")
        self.horizontalLayout_2.addWidget(self.busradio)
        self.planeradio = QtWidgets.QRadioButton(transportationWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.planeradio.sizePolicy().hasHeightForWidth())
        self.planeradio.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.planeradio.setFont(font)
        self.planeradio.setObjectName("planeradio")
        self.horizontalLayout_2.addWidget(self.planeradio)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.stackedWidget = QtWidgets.QStackedWidget(transportationWindow)
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.trainPage = QtWidgets.QWidget()
        self.trainPage.setObjectName("trainPage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.trainPage)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(7, 12, 0, -1)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.trainPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.source_label_train = QtWidgets.QLabel(self.trainPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.source_label_train.sizePolicy().hasHeightForWidth())
        self.source_label_train.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.source_label_train.setFont(font)
        self.source_label_train.setScaledContents(True)
        self.source_label_train.setWordWrap(True)
        self.source_label_train.setObjectName("source_label_train")
        self.horizontalLayout.addWidget(self.source_label_train)
        self.label_4 = QtWidgets.QLabel(self.trainPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.destination_label_train = QtWidgets.QLabel(self.trainPage)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.destination_label_train.setFont(font)
        self.destination_label_train.setScaledContents(True)
        self.destination_label_train.setWordWrap(True)
        self.destination_label_train.setObjectName("destination_label_train")
        self.horizontalLayout.addWidget(self.destination_label_train)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget_train = QtWidgets.QTableWidget(self.trainPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_train.sizePolicy().hasHeightForWidth())
        self.tableWidget_train.setSizePolicy(sizePolicy)
        self.tableWidget_train.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget_train.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_train.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget_train.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_train.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_train.setObjectName("tableWidget_train")
        self.tableWidget_train.setColumnCount(8)
        self.tableWidget_train.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_train.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_train.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_train.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_train.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_train.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_train.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_train.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_train.setHorizontalHeaderItem(7, item)
        self.verticalLayout.addWidget(self.tableWidget_train)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.stackedWidget.addWidget(self.trainPage)
        self.planePage = QtWidgets.QWidget()
        self.planePage.setObjectName("planePage")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.planePage)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.planePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.source_label_plane = QtWidgets.QLabel(self.planePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.source_label_plane.sizePolicy().hasHeightForWidth())
        self.source_label_plane.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.source_label_plane.setFont(font)
        self.source_label_plane.setScaledContents(True)
        self.source_label_plane.setWordWrap(True)
        self.source_label_plane.setObjectName("source_label_plane")
        self.horizontalLayout_4.addWidget(self.source_label_plane)
        self.label_7 = QtWidgets.QLabel(self.planePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.destination_label_plane = QtWidgets.QLabel(self.planePage)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.destination_label_plane.setFont(font)
        self.destination_label_plane.setScaledContents(True)
        self.destination_label_plane.setWordWrap(True)
        self.destination_label_plane.setObjectName("destination_label_plane")
        self.horizontalLayout_4.addWidget(self.destination_label_plane)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.tableWidget_plane = QtWidgets.QTableWidget(self.planePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_plane.sizePolicy().hasHeightForWidth())
        self.tableWidget_plane.setSizePolicy(sizePolicy)
        self.tableWidget_plane.setMinimumSize(QtCore.QSize(1056, 0))
        self.tableWidget_plane.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_plane.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget_plane.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_plane.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_plane.setObjectName("tableWidget_plane")
        self.tableWidget_plane.setColumnCount(7)
        self.tableWidget_plane.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_plane.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_plane.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_plane.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_plane.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_plane.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_plane.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_plane.setHorizontalHeaderItem(6, item)
        self.verticalLayout_4.addWidget(self.tableWidget_plane)
        self.stackedWidget.addWidget(self.planePage)
        self.busPage = QtWidgets.QWidget()
        self.busPage.setObjectName("busPage")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.busPage)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.busPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.source_label_bus = QtWidgets.QLabel(self.busPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.source_label_bus.sizePolicy().hasHeightForWidth())
        self.source_label_bus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.source_label_bus.setFont(font)
        self.source_label_bus.setScaledContents(True)
        self.source_label_bus.setWordWrap(True)
        self.source_label_bus.setObjectName("source_label_bus")
        self.horizontalLayout_5.addWidget(self.source_label_bus)
        self.label_11 = QtWidgets.QLabel(self.busPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_5.addWidget(self.label_11)
        self.destination_label_bus = QtWidgets.QLabel(self.busPage)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.destination_label_bus.setFont(font)
        self.destination_label_bus.setScaledContents(True)
        self.destination_label_bus.setWordWrap(True)
        self.destination_label_bus.setObjectName("destination_label_bus")
        self.horizontalLayout_5.addWidget(self.destination_label_bus)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.tableWidget_bus = QtWidgets.QTableWidget(self.busPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_bus.sizePolicy().hasHeightForWidth())
        self.tableWidget_bus.setSizePolicy(sizePolicy)
        self.tableWidget_bus.setMinimumSize(QtCore.QSize(1056, 0))
        self.tableWidget_bus.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_bus.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget_bus.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_bus.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_bus.setObjectName("tableWidget_bus")
        self.tableWidget_bus.setColumnCount(9)
        self.tableWidget_bus.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_bus.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_bus.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_bus.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_bus.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_bus.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_bus.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_bus.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_bus.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_bus.setHorizontalHeaderItem(8, item)
        self.verticalLayout_5.addWidget(self.tableWidget_bus)
        self.stackedWidget.addWidget(self.busPage)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(148, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.backbtn = QtWidgets.QPushButton(transportationWindow)
        self.backbtn.setObjectName("backbtn")
        self.horizontalLayout_3.addWidget(self.backbtn)
        spacerItem1 = QtWidgets.QSpacerItem(63, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.okbtn = QtWidgets.QPushButton(transportationWindow)
        self.okbtn.setObjectName("okbtn")
        self.horizontalLayout_3.addWidget(self.okbtn)
        spacerItem2 = QtWidgets.QSpacerItem(148, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(transportationWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(transportationWindow)
        self.source_label_bus.setText(scity)
        self.destination_label_bus.setText(dcity)
        self.source_label_train.setText(scity)
        self.destination_label_train.setText(dcity)
        self.source_label_plane.setText(scity)
        self.destination_label_plane.setText(dcity)

        self.tableWidget_train.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.tableWidget_plane.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.tableWidget_bus.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)



        self.tableWidget_train.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.header=self.tableWidget_train.horizontalHeader()
        self.header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        self.tableWidget_plane.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.header2=self.tableWidget_plane.horizontalHeader()
        self.header2.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.header2.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        self.tableWidget_bus.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.header3=self.tableWidget_bus.horizontalHeader()
        self.header3.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.header3.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        self.stackedWidget.setCurrentIndex(0)
        self.sourcecity=str(scity).upper()
        self.destinationcity=str(dcity).upper()

        self.banner=QtGui.QMovie('ImageFile/track.gif')
        self.label_2.setMovie(self.banner)
        self.banner.start()


        self.dbresult=Db.get_Train_info(self.sourcecity,self.destinationcity)
        self.tableWidget_train.setRowCount(len(self.dbresult))
        for index,val in enumerate(self.dbresult):
            for col in range(len(self.dbresult[0])):
                if col==4:
                    cell=QtWidgets.QTableWidgetItem(val[col].strftime("%d/%m/%Y"))
                else:
                    cell=QtWidgets.QTableWidgetItem(str(val[col]))
                self.tableWidget_train.setItem(index,col,cell)


        self.dbresult2=Db.get_Bus_info(self.sourcecity,self.destinationcity)
        self.tableWidget_bus.setRowCount(len(self.dbresult2))
        for index,val in enumerate(self.dbresult2):
            for col in range(len(self.dbresult2[0])):
                if col==5:
                    cell=QtWidgets.QTableWidgetItem(val[col].strftime("%d/%m/%Y"))
                else:
                    cell=QtWidgets.QTableWidgetItem(str(val[col]))
                self.tableWidget_bus.setItem(index,col,cell)

        self.dbresult3=Db.get_Plane_info(self.sourcecity,self.destinationcity)
        self.tableWidget_plane.setRowCount(len(self.dbresult3))
        for index,val in enumerate(self.dbresult3):
            for col in range(len(self.dbresult3[0])):
                if col==4:
                    cell=QtWidgets.QTableWidgetItem(val[col].strftime("%d/%m/%Y"))
                else:
                    cell=QtWidgets.QTableWidgetItem(str(val[col]))
                self.tableWidget_plane.setItem(index,col,cell)

        self.row=0
        self.tableWidget_train.clicked.connect(self.selectedVehicle)
        self.tableWidget_plane.clicked.connect(self.selectedVehicle)
        self.tableWidget_bus.clicked.connect(self.selectedVehicle)


        self.trainradio.toggled.connect(self.changePagetoTrain)
        self.busradio.toggled.connect(self.changePagetoBus)
        self.planeradio.toggled.connect(self.changePagetoPlane)

        self.okbtn.clicked.connect(self.extractSelectedRow)

        self.parent=parent
        self.duplicateForm=transportationWindow


    def selectedVehicle(self,clickedIndex):
        self.row=clickedIndex.row()
        print(self.row)

    def extractSelectedRow(self):
        try:
            x=[]
            self.parent.transportFlag=True
            if self.trainradio.isChecked():
                train=self.dbresult[int(self.row)]
                x.append(train[0])
                x.append(train[4])
                x.append(train[5])
                x.append(train[2])
                x.append('-Train')
            elif self.busradio.isChecked():
                bus=self.dbresult2[int(self.row)]
                x.append(bus[0])
                x.append(bus[5])
                x.append(bus[6])
                x.append(bus[2])
                x.append('-Bus')
            elif self.planeradio.isChecked():
                plane=self.dbresult3[int(self.row)]
                x.append(plane[0])
                x.append(plane[4])
                x.append(plane[5])
                x.append(plane[2])
                x.append('-Plane')
            x.append(self.sourcecity)
            x.append(self.destinationcity)
            self.parent.transportSelected=x
        except Exception as e:
            print(e)
        self.duplicateForm.close()

    def changePagetoTrain(self):
        self.stackedWidget.setCurrentIndex(0)
        self.banner=QtGui.QMovie('ImageFile/track.gif')
        self.label_2.setMovie(self.banner)
        self.banner.start()

    def changePagetoBus(self):
        self.stackedWidget.setCurrentIndex(2)
        self.banner=QtGui.QMovie('ImageFile/bus.gif')
        self.label_2.setMovie(self.banner)
        self.banner.start()

    def changePagetoPlane(self):
        self.stackedWidget.setCurrentIndex(1)
        self.banner=QtGui.QMovie('ImageFile/aeroplane.gif')
        self.label_2.setMovie(self.banner)
        self.banner.start()

    def retranslateUi(self, transportationWindow):
        _translate = QtCore.QCoreApplication.translate
        transportationWindow.setWindowTitle(_translate("transportationWindow", "Transportation Services"))
        self.trainradio.setText(_translate("transportationWindow", "TRAINS"))
        self.busradio.setText(_translate("transportationWindow", "BUSES"))
        self.planeradio.setText(_translate("transportationWindow", "PLANES"))
        self.label.setText(_translate("transportationWindow", "Upcoming Trains from "))
        self.source_label_train.setText(_translate("transportationWindow", "BENGALURU"))
        self.label_4.setText(_translate("transportationWindow", "to"))
        self.destination_label_train.setText(_translate("transportationWindow", "DELHI"))
        item = self.tableWidget_train.horizontalHeaderItem(0)
        item.setText(_translate("transportationWindow", "TRAIN NAME"))
        item = self.tableWidget_train.horizontalHeaderItem(1)
        item.setText(_translate("transportationWindow", "CLASS"))
        item = self.tableWidget_train.horizontalHeaderItem(2)
        item.setText(_translate("transportationWindow", "FARE"))
        item = self.tableWidget_train.horizontalHeaderItem(3)
        item.setText(_translate("transportationWindow", "JOURNEY HOURS"))
        item = self.tableWidget_train.horizontalHeaderItem(4)
        item.setText(_translate("transportationWindow", "DEPARTURE DATE"))
        item = self.tableWidget_train.horizontalHeaderItem(5)
        item.setText(_translate("transportationWindow", "DEPARTURE TIME"))
        item = self.tableWidget_train.horizontalHeaderItem(6)
        item.setText(_translate("transportationWindow", "AVAILABLE NO OF SEATS"))
        item = self.tableWidget_train.horizontalHeaderItem(7)
        item.setText(_translate("transportationWindow", "STATUS"))
        self.label_5.setText(_translate("transportationWindow", "Upcoming Planes from "))
        self.source_label_plane.setText(_translate("transportationWindow", "BENGALURU"))
        self.label_7.setText(_translate("transportationWindow", "to"))
        self.destination_label_plane.setText(_translate("transportationWindow", "DELHI"))
        item = self.tableWidget_plane.horizontalHeaderItem(0)
        item.setText(_translate("transportationWindow", "PLANE NAME"))
        item = self.tableWidget_plane.horizontalHeaderItem(1)
        item.setText(_translate("transportationWindow", "CLASS"))
        item = self.tableWidget_plane.horizontalHeaderItem(2)
        item.setText(_translate("transportationWindow", "FARE"))
        item = self.tableWidget_plane.horizontalHeaderItem(3)
        item.setText(_translate("transportationWindow", "JOURNEY HOURS"))
        item = self.tableWidget_plane.horizontalHeaderItem(4)
        item.setText(_translate("transportationWindow", "DEPARTURE DATE"))
        item = self.tableWidget_plane.horizontalHeaderItem(5)
        item.setText(_translate("transportationWindow", "DEPARTURE TIME"))
        item = self.tableWidget_plane.horizontalHeaderItem(6)
        item.setText(_translate("transportationWindow", "AVAILABLE NO. OF SEATS"))
        self.label_9.setText(_translate("transportationWindow", "Upcoming Buses from "))
        self.source_label_bus.setText(_translate("transportationWindow", "BENGALURU"))
        self.label_11.setText(_translate("transportationWindow", "to"))
        self.destination_label_bus.setText(_translate("transportationWindow", "DELHI"))
        item = self.tableWidget_bus.horizontalHeaderItem(0)
        item.setText(_translate("transportationWindow", "SERVICE PROVIDER"))
        item = self.tableWidget_bus.horizontalHeaderItem(1)
        item.setText(_translate("transportationWindow", "RATING"))
        item = self.tableWidget_bus.horizontalHeaderItem(2)
        item.setText(_translate("transportationWindow", "FARE"))
        item = self.tableWidget_bus.horizontalHeaderItem(3)
        item.setText(_translate("transportationWindow", "SEAT TYPE"))
        item = self.tableWidget_bus.horizontalHeaderItem(4)
        item.setText(_translate("transportationWindow", "is AC"))
        item = self.tableWidget_bus.horizontalHeaderItem(5)
        item.setText(_translate("transportationWindow", "DEPARTURE DATE"))
        item = self.tableWidget_bus.horizontalHeaderItem(6)
        item.setText(_translate("transportationWindow", "DEPARTURE TIME"))
        item = self.tableWidget_bus.horizontalHeaderItem(7)
        item.setText(_translate("transportationWindow", "JOURNEY HOURS"))
        item = self.tableWidget_bus.horizontalHeaderItem(8)
        item.setText(_translate("transportationWindow", "AVAILABLE NO. OF SEATS"))
        self.backbtn.setText(_translate("transportationWindow", "BACK"))
        self.okbtn.setText(_translate("transportationWindow", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    transportationWindow = QtWidgets.QWidget()
    ui = Ui_transportationWindow()
    ui.setupUi(transportationWindow,'DELHI','MUMBAI')
    transportationWindow.show()
    sys.exit(app.exec_())
