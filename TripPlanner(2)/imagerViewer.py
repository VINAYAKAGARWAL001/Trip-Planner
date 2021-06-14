# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imageviewer.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import dbQueries as Db

class Ui_image_view(object):
    def setupUi(self, image_view,place_name):
        image_view.setObjectName("image_view")
        image_view.setFixedSize(1360, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(image_view.sizePolicy().hasHeightForWidth())
        image_view.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(image_view)
        self.verticalLayout.setObjectName("verticalLayout")
        self.place_name_label = QtWidgets.QLabel(image_view)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(20)
        font.setBold(True)
        self.place_name_label.setFont(font)
        self.place_name_label.setObjectName("place_name_label")
        self.verticalLayout.addWidget(self.place_name_label)
        self.image_panel = QtWidgets.QLabel(image_view)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_panel.sizePolicy().hasHeightForWidth())
        self.image_panel.setSizePolicy(sizePolicy)
        self.image_panel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image_panel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.image_panel.setLineWidth(10)
        self.image_panel.setMidLineWidth(12)
        self.image_panel.setText("")
        self.image_panel.setPixmap(QtGui.QPixmap("./ImageFile/imageViewerInitial.png"))
        self.image_panel.setScaledContents(True)
        self.image_panel.setObjectName("image_panel")
        self.verticalLayout.addWidget(self.image_panel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(120, 7, 120, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftbtn = QtWidgets.QPushButton(image_view)
        self.leftbtn.setAutoFillBackground(False)
        self.leftbtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ImageFile/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.leftbtn.setIcon(icon)
        self.leftbtn.setObjectName("leftbtn")
        self.horizontalLayout.addWidget(self.leftbtn)
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.rightbtn = QtWidgets.QPushButton(image_view)
        self.rightbtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ImageFile/forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rightbtn.setIcon(icon1)
        self.rightbtn.setObjectName("rightbtn")
        self.horizontalLayout.addWidget(self.rightbtn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(image_view)
        QtCore.QMetaObject.connectSlotsByName(image_view)

        self.place_name_label.setText("<font color=#990643>"+place_name+"</font>")
        self.imgIndex=0

        self.imagesAddress=Db.get_place_images(place_name)
        try:
            self.image_panel.setPixmap(QtGui.QPixmap(self.imagesAddress[0]))
        except:
            pass
        self.rightbtn.clicked.connect(self.shiftRight)
        self.leftbtn.clicked.connect(self.shiftLeft)


    def shiftRight(self):
        try:
            if self.imgIndex==3:
                self.image_panel.setPixmap(QtGui.QPixmap(self.imagesAddress[int(self.imgIndex)]))
            else:
                self.imgIndex+=1
                self.image_panel.setPixmap(QtGui.QPixmap(self.imagesAddress[int(self.imgIndex)]))
        except:
            pass


    def shiftLeft(self):
        try:
            if self.imgIndex==0:
                self.image_panel.setPixmap(QtGui.QPixmap(self.imagesAddress[int(self.imgIndex)]))
            else:
                self.imgIndex-=1
                self.image_panel.setPixmap(QtGui.QPixmap(self.imagesAddress[int(self.imgIndex)]))
        except:
            pass



    def retranslateUi(self, image_view):
        _translate = QtCore.QCoreApplication.translate
        image_view.setWindowTitle(_translate("image_view", "Image Viewer"))
        self.place_name_label.setText(_translate("image_view", "Place Name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    image_view = QtWidgets.QWidget()
    ui = Ui_image_view()
    ui.setupUi(image_view)
    image_view.show()
    sys.exit(app.exec_())
