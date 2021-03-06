# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bus_insert_update.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import dbQueries as Db
from transactionstatus import Ui_transactionSuccessful as transactionStatus


class Ui_busWindow(object):
    def setupUi(self, MainWindow,type):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.busInsertUpdateForm = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.busInsertUpdateForm.setFont(font)
        self.busInsertUpdateForm.setAlignment(QtCore.Qt.AlignCenter)
        self.busInsertUpdateForm.setObjectName("busInsertUpdateForm")
        self.verticalLayout_3.addWidget(self.busInsertUpdateForm)
        spacerItem = QtWidgets.QSpacerItem(20, 48, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.busId = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.busId.setFont(font)
        self.busId.setObjectName("busId")
        self.verticalLayout.addWidget(self.busId)
        self.busName = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.busName.setFont(font)
        self.busName.setObjectName("busName")
        self.verticalLayout.addWidget(self.busName)
        self.busSource = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.busSource.setFont(font)
        self.busSource.setObjectName("busSource")
        self.verticalLayout.addWidget(self.busSource)
        self.busDestination = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.busDestination.setFont(font)
        self.busDestination.setObjectName("busDestination")
        self.verticalLayout.addWidget(self.busDestination)
        self.busAcRating = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.busAcRating.setFont(font)
        self.busAcRating.setObjectName("busAcRating")
        self.verticalLayout.addWidget(self.busAcRating)
        self.Rating = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Rating.setFont(font)
        self.Rating.setObjectName("Rating")
        self.verticalLayout.addWidget(self.Rating)
        self.SeatType = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SeatType.setFont(font)
        self.SeatType.setObjectName("SeatType")
        self.verticalLayout.addWidget(self.SeatType)
        self.busFare = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.busFare.setFont(font)
        self.busFare.setObjectName("busFare")
        self.verticalLayout.addWidget(self.busFare)
        self.busNumberOfSeats = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.busNumberOfSeats.setFont(font)
        self.busNumberOfSeats.setObjectName("busNumberOfSeats")
        self.verticalLayout.addWidget(self.busNumberOfSeats)
        self.busJourneyHours = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.busJourneyHours.setFont(font)
        self.busJourneyHours.setObjectName("busJourneyHours")
        self.verticalLayout.addWidget(self.busJourneyHours)
        self.busServiceProvider = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.busServiceProvider.setFont(font)
        self.busServiceProvider.setObjectName("busServiceProvider")
        self.verticalLayout.addWidget(self.busServiceProvider)
        self.busDepartureDate = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.busDepartureDate.setFont(font)
        self.busDepartureDate.setObjectName("busDepartureDate")
        self.verticalLayout.addWidget(self.busDepartureDate)
        self.busDepartureTime = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.busDepartureTime.setFont(font)
        self.busDepartureTime.setObjectName("busDepartureTime")
        self.verticalLayout.addWidget(self.busDepartureTime)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.busIdLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.busIdLineEdit.setFont(font)
        self.busIdLineEdit.setObjectName("busIdLineEdit")
        self.verticalLayout_2.addWidget(self.busIdLineEdit)
        self.busNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.busNameLineEdit.setFont(font)
        self.busNameLineEdit.setObjectName("busNameLineEdit")
        self.verticalLayout_2.addWidget(self.busNameLineEdit)
        self.busSourceLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.busSourceLineEdit.setFont(font)
        self.busSourceLineEdit.setObjectName("busSourceLineEdit")
        self.verticalLayout_2.addWidget(self.busSourceLineEdit)
        self.busDestinationLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.busDestinationLineEdit.setFont(font)
        self.busDestinationLineEdit.setObjectName("busDestinationLineEdit")
        self.verticalLayout_2.addWidget(self.busDestinationLineEdit)
        self.busAcRatingLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.busAcRatingLineEdit.setFont(font)
        self.busAcRatingLineEdit.setObjectName("busAcRatingLineEdit")
        self.verticalLayout_2.addWidget(self.busAcRatingLineEdit)
        self.busRatingLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.busRatingLineEdit.setFont(font)
        self.busRatingLineEdit.setObjectName("busRatingLineEdit")
        self.verticalLayout_2.addWidget(self.busRatingLineEdit)
        self.busSeatTypeLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.busSeatTypeLineEdit.setFont(font)
        self.busSeatTypeLineEdit.setObjectName("busSeatTypeLineEdit")
        self.verticalLayout_2.addWidget(self.busSeatTypeLineEdit)
        self.busFareLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.busFareLineEdit.setFont(font)
        self.busFareLineEdit.setObjectName("busFareLineEdit")
        self.verticalLayout_2.addWidget(self.busFareLineEdit)
        self.busNumberOfSeatsLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.busNumberOfSeatsLineEdit.setFont(font)
        self.busNumberOfSeatsLineEdit.setObjectName("busNumberOfSeatsLineEdit")
        self.verticalLayout_2.addWidget(self.busNumberOfSeatsLineEdit)
        self.busJourneyHoursLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.busJourneyHoursLineEdit.setFont(font)
        self.busJourneyHoursLineEdit.setObjectName("busJourneyHoursLineEdit")
        self.verticalLayout_2.addWidget(self.busJourneyHoursLineEdit)
        self.busServiceProviderLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.busServiceProviderLineEdit.setObjectName("busServiceProviderLineEdit")
        self.verticalLayout_2.addWidget(self.busServiceProviderLineEdit)
        self.busDepartureDateLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.busDepartureDateLineEdit.setObjectName("busDepartureDateLineEdit")
        self.verticalLayout_2.addWidget(self.busDepartureDateLineEdit)
        self.busDepartureTimeLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.busDepartureTimeLineEdit.setObjectName("busDepartureTimeLineEdit")
        self.verticalLayout_2.addWidget(self.busDepartureTimeLineEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 48, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.busInsertUpdateOkButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.busInsertUpdateOkButton.setFont(font)
        self.busInsertUpdateOkButton.setObjectName("busInsertUpdateOkButton")
        self.horizontalLayout_3.addWidget(self.busInsertUpdateOkButton)
        self.busInsertUpdateBackButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.busInsertUpdateBackButton.setFont(font)
        self.busInsertUpdateBackButton.setObjectName("busInsertUpdateBackButton")
        self.horizontalLayout_3.addWidget(self.busInsertUpdateBackButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 806, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.type = type
        self.busInsertUpdateOkButton.clicked.connect(lambda: self.evaluate(type))
        self.busInsertUpdateBackButton.clicked.connect(lambda: MainWindow.close())

    def evaluate(self, type):
        if type == 'insert':
            if self.busRatingLineEdit.text()!='' and self.busSeatTypeLineEdit.text()!='' and self.busIdLineEdit.text() != '' \
                    and self.busNameLineEdit.text() != '' and self.busSourceLineEdit.text() != '' and self.busDestinationLineEdit.text() != ''\
                    and self.busAcRatingLineEdit.text() != '' and self.busFareLineEdit.text() != '' and self.busNumberOfSeatsLineEdit.text() != '' \
                    and self.busJourneyHoursLineEdit.text() != '' and self.busServiceProviderLineEdit.text() != '' and self.busDepartureDateLineEdit.text() != '' \
                    and self.busDepartureTimeLineEdit.text() != '':
                busId = self.busIdLineEdit.text()
                busName = self.busNameLineEdit.text()
                source = self.busSourceLineEdit.text()
                destination = self.busDestinationLineEdit.text()
                acRating = self.busAcRatingLineEdit.text()
                fare = self.busFareLineEdit.text()
                numberOfSeats = self.busNumberOfSeatsLineEdit.text()
                journeyHours = self.busJourneyHoursLineEdit.text()
                busServiceProvider = self.busServiceProviderLineEdit.text()
                departureDate = self.busDepartureDateLineEdit.text()
                departureTime = self.busDepartureTimeLineEdit.text()
                rating=self.busRatingLineEdit.text()
                seat_type=self.busSeatTypeLineEdit.text()

                res = Db.insertBus(busId, busName, source, destination, acRating, fare, numberOfSeats, journeyHours,
                                   busServiceProvider, departureDate, departureTime,rating,seat_type)
                if (res == 1):
                    self.tranForm = QtWidgets.QMainWindow()
                    self.tranUi = transactionStatus()
                    self.tranUi.setupUi(self.tranForm,1)
                    self.tranForm.show()
                else:
                    self.tranForm = QtWidgets.QMainWindow()
                    self.tranUi = transactionStatus()
                    self.tranUi.setupUi(self.tranForm,-1)
                    self.tranForm.show()
        elif type == 'update':
            if self.busRatingLineEdit.text()!='' and self.busSeatTypeLineEdit.text()!='' and self.busIdLineEdit.text() != '' and self.busNameLineEdit.text() != '' \
                    and self.busSourceLineEdit.text() != '' and self.busDestinationLineEdit.text() != '' and self.busAcRatingLineEdit.text() != '' and self.busFareLineEdit.text() != '' \
                    and self.busNumberOfSeatsLineEdit.text() != '' and self.busJourneyHoursLineEdit.text() != '' and self.busServiceProviderLineEdit.text() != '' \
                    and self.busDepartureDateLineEdit.text() != '' and self.busDepartureTimeLineEdit.text() != '':
                busId = self.busIdLineEdit.text()
                busName = self.busNameLineEdit.text()
                source = self.busSourceLineEdit.text()
                destination = self.busDestinationLineEdit.text()
                acRating = self.busAcRatingLineEdit.text()
                fare = self.busFareLineEdit.text()
                numberOfSeats = self.busNumberOfSeatsLineEdit.text()
                journeyHours = self.busJourneyHoursLineEdit.text()
                busServiceProvider = self.busServiceProviderLineEdit.text()
                departureDate = self.busDepartureDateLineEdit.text()
                departureTime = self.busDepartureTimeLineEdit.text()
                rating = self.busRatingLineEdit.text()
                seat_type = self.busSeatTypeLineEdit.text()
                res = Db.updateBus(busId, busName, source, destination, acRating, fare, numberOfSeats, journeyHours,
                                   busServiceProvider, departureDate, departureTime,rating,seat_type)
                if (res == 1):
                    self.tranForm = QtWidgets.QMainWindow()
                    self.tranUi = transactionStatus()
                    self.tranUi.setupUi(self.tranForm,1)
                    self.tranForm.show()
                else:
                    self.tranForm = QtWidgets.QMainWindow()
                    self.tranUi = transactionStatus()
                    self.tranUi.setupUi(self.tranForm,-1)
                    self.tranForm.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bus Details"))
        self.busInsertUpdateForm.setText(_translate("MainWindow", "BUS INSERT/ UPDATE FORM-"))
        self.busId.setText(_translate("MainWindow", "Bus ID"))
        self.busName.setText(_translate("MainWindow", "Bus Name"))
        self.busSource.setText(_translate("MainWindow", "Source"))
        self.busDestination.setText(_translate("MainWindow", "Destination"))
        self.busAcRating.setText(_translate("MainWindow", "AC Avaialbility"))
        self.Rating.setText(_translate("MainWindow", "Rating"))
        self.SeatType.setText(_translate("MainWindow", "Seat Type"))
        self.busFare.setText(_translate("MainWindow", "Fare"))
        self.busNumberOfSeats.setText(_translate("MainWindow", "Number of seats"))
        self.busJourneyHours.setText(_translate("MainWindow", "Jouney hours"))
        self.busServiceProvider.setText(_translate("MainWindow", "Bus Service Provider"))
        self.busDepartureDate.setText(_translate("MainWindow", "Departure Date"))
        self.busDepartureTime.setText(_translate("MainWindow", "Departure Time"))
        self.busInsertUpdateOkButton.setText(_translate("MainWindow", "Ok"))
        self.busInsertUpdateBackButton.setText(_translate("MainWindow", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_busWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
