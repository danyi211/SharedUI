# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_tooling.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1097, 705)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 131, 21))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.sbSensorToolID = QtWidgets.QSpinBox(Form)
        self.sbSensorToolID.setGeometry(QtCore.QRect(140, 10, 51, 21))
        self.sbSensorToolID.setMaximum(2147483647)
        self.sbSensorToolID.setObjectName("sbSensorToolID")
        self.listSensorToolComments = QtWidgets.QListWidget(Form)
        self.listSensorToolComments.setGeometry(QtCore.QRect(10, 100, 251, 121))
        self.listSensorToolComments.setObjectName("listSensorToolComments")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 80, 121, 21))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pbSensorToolDeleteComment = QtWidgets.QPushButton(Form)
        self.pbSensorToolDeleteComment.setGeometry(QtCore.QRect(130, 80, 131, 21))
        self.pbSensorToolDeleteComment.setObjectName("pbSensorToolDeleteComment")
        self.pteSensorToolWriteComment = QtWidgets.QPlainTextEdit(Form)
        self.pteSensorToolWriteComment.setGeometry(QtCore.QRect(10, 230, 251, 71))
        self.pteSensorToolWriteComment.setObjectName("pteSensorToolWriteComment")
        self.pbSensorToolAddComment = QtWidgets.QPushButton(Form)
        self.pbSensorToolAddComment.setGeometry(QtCore.QRect(10, 300, 111, 23))
        self.pbSensorToolAddComment.setObjectName("pbSensorToolAddComment")
        self.pbPcbToolAddComment = QtWidgets.QPushButton(Form)
        self.pbPcbToolAddComment.setGeometry(QtCore.QRect(10, 640, 111, 21))
        self.pbPcbToolAddComment.setObjectName("pbPcbToolAddComment")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 420, 121, 21))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.ptePcbToolWriteComment = QtWidgets.QPlainTextEdit(Form)
        self.ptePcbToolWriteComment.setGeometry(QtCore.QRect(10, 570, 251, 71))
        self.ptePcbToolWriteComment.setObjectName("ptePcbToolWriteComment")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 350, 131, 21))
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.sbPcbToolID = QtWidgets.QSpinBox(Form)
        self.sbPcbToolID.setGeometry(QtCore.QRect(140, 350, 51, 21))
        self.sbPcbToolID.setMaximum(2147483647)
        self.sbPcbToolID.setObjectName("sbPcbToolID")
        self.pbPcbToolDeleteComment = QtWidgets.QPushButton(Form)
        self.pbPcbToolDeleteComment.setGeometry(QtCore.QRect(130, 420, 131, 21))
        self.pbPcbToolDeleteComment.setObjectName("pbPcbToolDeleteComment")
        self.listPcbToolComments = QtWidgets.QListWidget(Form)
        self.listPcbToolComments.setGeometry(QtCore.QRect(10, 440, 251, 121))
        self.listPcbToolComments.setObjectName("listPcbToolComments")
        self.listPcbTrayComments = QtWidgets.QListWidget(Form)
        self.listPcbTrayComments.setGeometry(QtCore.QRect(310, 440, 291, 121))
        self.listPcbTrayComments.setObjectName("listPcbTrayComments")
        self.pbSensorTrayAddComment = QtWidgets.QPushButton(Form)
        self.pbSensorTrayAddComment.setGeometry(QtCore.QRect(310, 300, 111, 23))
        self.pbSensorTrayAddComment.setObjectName("pbSensorTrayAddComment")
        self.lineEdit_8 = QtWidgets.QLineEdit(Form)
        self.lineEdit_8.setGeometry(QtCore.QRect(310, 420, 161, 21))
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pteSensorTrayWriteComment = QtWidgets.QPlainTextEdit(Form)
        self.pteSensorTrayWriteComment.setGeometry(QtCore.QRect(310, 230, 291, 71))
        self.pteSensorTrayWriteComment.setObjectName("pteSensorTrayWriteComment")
        self.sbSensorTrayID = QtWidgets.QSpinBox(Form)
        self.sbSensorTrayID.setGeometry(QtCore.QRect(480, 10, 51, 21))
        self.sbSensorTrayID.setMaximum(2147483647)
        self.sbSensorTrayID.setObjectName("sbSensorTrayID")
        self.pbPcbTrayAddComment = QtWidgets.QPushButton(Form)
        self.pbPcbTrayAddComment.setGeometry(QtCore.QRect(310, 640, 111, 21))
        self.pbPcbTrayAddComment.setObjectName("pbPcbTrayAddComment")
        self.sbPcbTrayID = QtWidgets.QSpinBox(Form)
        self.sbPcbTrayID.setGeometry(QtCore.QRect(480, 350, 51, 21))
        self.sbPcbTrayID.setMaximum(2147483647)
        self.sbPcbTrayID.setObjectName("sbPcbTrayID")
        self.listSensorTrayComments = QtWidgets.QListWidget(Form)
        self.listSensorTrayComments.setGeometry(QtCore.QRect(310, 100, 291, 121))
        self.listSensorTrayComments.setObjectName("listSensorTrayComments")
        self.lineEdit_9 = QtWidgets.QLineEdit(Form)
        self.lineEdit_9.setGeometry(QtCore.QRect(310, 80, 161, 21))
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(Form)
        self.lineEdit_10.setGeometry(QtCore.QRect(310, 10, 171, 21))
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.pbSensorTrayDeleteComment = QtWidgets.QPushButton(Form)
        self.pbSensorTrayDeleteComment.setGeometry(QtCore.QRect(470, 80, 131, 21))
        self.pbSensorTrayDeleteComment.setObjectName("pbSensorTrayDeleteComment")
        self.pbPcbTrayDeleteComment = QtWidgets.QPushButton(Form)
        self.pbPcbTrayDeleteComment.setGeometry(QtCore.QRect(470, 420, 131, 21))
        self.pbPcbTrayDeleteComment.setObjectName("pbPcbTrayDeleteComment")
        self.ptePcbTrayWriteComment = QtWidgets.QPlainTextEdit(Form)
        self.ptePcbTrayWriteComment.setGeometry(QtCore.QRect(310, 570, 291, 71))
        self.ptePcbTrayWriteComment.setObjectName("ptePcbTrayWriteComment")
        self.lineEdit_12 = QtWidgets.QLineEdit(Form)
        self.lineEdit_12.setGeometry(QtCore.QRect(310, 350, 171, 21))
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(Form)
        self.lineEdit_13.setGeometry(QtCore.QRect(650, 80, 121, 21))
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.listAssemblyTrayComments = QtWidgets.QListWidget(Form)
        self.listAssemblyTrayComments.setGeometry(QtCore.QRect(650, 100, 251, 121))
        self.listAssemblyTrayComments.setObjectName("listAssemblyTrayComments")
        self.pbAssemblyTrayAddComment = QtWidgets.QPushButton(Form)
        self.pbAssemblyTrayAddComment.setGeometry(QtCore.QRect(650, 300, 111, 23))
        self.pbAssemblyTrayAddComment.setObjectName("pbAssemblyTrayAddComment")
        self.sbAssemblyTrayID = QtWidgets.QSpinBox(Form)
        self.sbAssemblyTrayID.setGeometry(QtCore.QRect(780, 10, 51, 21))
        self.sbAssemblyTrayID.setMaximum(2147483647)
        self.sbAssemblyTrayID.setObjectName("sbAssemblyTrayID")
        self.pbAssemblyTrayDeleteComment = QtWidgets.QPushButton(Form)
        self.pbAssemblyTrayDeleteComment.setGeometry(QtCore.QRect(770, 80, 131, 21))
        self.pbAssemblyTrayDeleteComment.setObjectName("pbAssemblyTrayDeleteComment")
        self.pteAssemblyTrayWriteComment = QtWidgets.QPlainTextEdit(Form)
        self.pteAssemblyTrayWriteComment.setGeometry(QtCore.QRect(650, 230, 251, 71))
        self.pteAssemblyTrayWriteComment.setObjectName("pteAssemblyTrayWriteComment")
        self.lineEdit_15 = QtWidgets.QLineEdit(Form)
        self.lineEdit_15.setGeometry(QtCore.QRect(650, 10, 131, 21))
        self.lineEdit_15.setReadOnly(True)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.pbSensorToolEditNew = QtWidgets.QPushButton(Form)
        self.pbSensorToolEditNew.setGeometry(QtCore.QRect(190, 10, 71, 21))
        self.pbSensorToolEditNew.setObjectName("pbSensorToolEditNew")
        self.pbSensorToolSave = QtWidgets.QPushButton(Form)
        self.pbSensorToolSave.setGeometry(QtCore.QRect(190, 30, 71, 21))
        self.pbSensorToolSave.setObjectName("pbSensorToolSave")
        self.pbSensorToolCancel = QtWidgets.QPushButton(Form)
        self.pbSensorToolCancel.setGeometry(QtCore.QRect(190, 50, 71, 21))
        self.pbSensorToolCancel.setObjectName("pbSensorToolCancel")
        self.pbPcbToolCancel = QtWidgets.QPushButton(Form)
        self.pbPcbToolCancel.setGeometry(QtCore.QRect(190, 390, 71, 21))
        self.pbPcbToolCancel.setObjectName("pbPcbToolCancel")
        self.pbPcbToolSave = QtWidgets.QPushButton(Form)
        self.pbPcbToolSave.setGeometry(QtCore.QRect(190, 370, 71, 21))
        self.pbPcbToolSave.setObjectName("pbPcbToolSave")
        self.pbPcbToolEditNew = QtWidgets.QPushButton(Form)
        self.pbPcbToolEditNew.setGeometry(QtCore.QRect(190, 350, 71, 21))
        self.pbPcbToolEditNew.setObjectName("pbPcbToolEditNew")
        self.pbPcbTrayEditNew = QtWidgets.QPushButton(Form)
        self.pbPcbTrayEditNew.setGeometry(QtCore.QRect(530, 350, 71, 21))
        self.pbPcbTrayEditNew.setObjectName("pbPcbTrayEditNew")
        self.pbPcbTraySave = QtWidgets.QPushButton(Form)
        self.pbPcbTraySave.setGeometry(QtCore.QRect(530, 370, 71, 21))
        self.pbPcbTraySave.setObjectName("pbPcbTraySave")
        self.pbPcbTrayCancel = QtWidgets.QPushButton(Form)
        self.pbPcbTrayCancel.setGeometry(QtCore.QRect(530, 390, 71, 21))
        self.pbPcbTrayCancel.setObjectName("pbPcbTrayCancel")
        self.pbSensorTrayCancel = QtWidgets.QPushButton(Form)
        self.pbSensorTrayCancel.setGeometry(QtCore.QRect(530, 50, 71, 21))
        self.pbSensorTrayCancel.setObjectName("pbSensorTrayCancel")
        self.pbSensorTraySave = QtWidgets.QPushButton(Form)
        self.pbSensorTraySave.setGeometry(QtCore.QRect(530, 30, 71, 21))
        self.pbSensorTraySave.setObjectName("pbSensorTraySave")
        self.pbSensorTrayEditNew = QtWidgets.QPushButton(Form)
        self.pbSensorTrayEditNew.setGeometry(QtCore.QRect(530, 10, 71, 21))
        self.pbSensorTrayEditNew.setObjectName("pbSensorTrayEditNew")
        self.pbAssemblyTrayEditNew = QtWidgets.QPushButton(Form)
        self.pbAssemblyTrayEditNew.setGeometry(QtCore.QRect(830, 10, 71, 21))
        self.pbAssemblyTrayEditNew.setObjectName("pbAssemblyTrayEditNew")
        self.pbAssemblyTrayCancel = QtWidgets.QPushButton(Form)
        self.pbAssemblyTrayCancel.setGeometry(QtCore.QRect(830, 50, 71, 21))
        self.pbAssemblyTrayCancel.setObjectName("pbAssemblyTrayCancel")
        self.pbAssemblyTraySave = QtWidgets.QPushButton(Form)
        self.pbAssemblyTraySave.setGeometry(QtCore.QRect(830, 30, 71, 21))
        self.pbAssemblyTraySave.setObjectName("pbAssemblyTraySave")
        self.leSensorToolLocation = QtWidgets.QLineEdit(Form)
        self.leSensorToolLocation.setGeometry(QtCore.QRect(80, 50, 111, 20))
        self.leSensorToolLocation.setObjectName("leSensorToolLocation")
        self.lineEdit_16 = QtWidgets.QLineEdit(Form)
        self.lineEdit_16.setGeometry(QtCore.QRect(10, 50, 71, 21))
        self.lineEdit_16.setReadOnly(True)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(Form)
        self.lineEdit_17.setGeometry(QtCore.QRect(310, 50, 71, 21))
        self.lineEdit_17.setReadOnly(True)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.leSensorTrayLocation = QtWidgets.QLineEdit(Form)
        self.leSensorTrayLocation.setGeometry(QtCore.QRect(380, 50, 151, 20))
        self.leSensorTrayLocation.setObjectName("leSensorTrayLocation")
        self.leAssemblyTrayLocation = QtWidgets.QLineEdit(Form)
        self.leAssemblyTrayLocation.setGeometry(QtCore.QRect(720, 50, 111, 20))
        self.leAssemblyTrayLocation.setObjectName("leAssemblyTrayLocation")
        self.lineEdit_18 = QtWidgets.QLineEdit(Form)
        self.lineEdit_18.setGeometry(QtCore.QRect(650, 50, 71, 21))
        self.lineEdit_18.setReadOnly(True)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.lineEdit_19 = QtWidgets.QLineEdit(Form)
        self.lineEdit_19.setGeometry(QtCore.QRect(10, 390, 71, 21))
        self.lineEdit_19.setReadOnly(True)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lePcbToolLocation = QtWidgets.QLineEdit(Form)
        self.lePcbToolLocation.setGeometry(QtCore.QRect(80, 390, 111, 20))
        self.lePcbToolLocation.setObjectName("lePcbToolLocation")
        self.lineEdit_20 = QtWidgets.QLineEdit(Form)
        self.lineEdit_20.setGeometry(QtCore.QRect(310, 390, 71, 21))
        self.lineEdit_20.setReadOnly(True)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.lePcbTrayLocation = QtWidgets.QLineEdit(Form)
        self.lePcbTrayLocation.setGeometry(QtCore.QRect(380, 390, 151, 20))
        self.lePcbTrayLocation.setObjectName("lePcbTrayLocation")
        self.lineEdit_21 = QtWidgets.QLineEdit(Form)
        self.lineEdit_21.setGeometry(QtCore.QRect(10, 30, 111, 21))
        self.lineEdit_21.setReadOnly(True)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.lineEdit_22 = QtWidgets.QLineEdit(Form)
        self.lineEdit_22.setGeometry(QtCore.QRect(310, 30, 151, 21))
        self.lineEdit_22.setReadOnly(True)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.lineEdit_23 = QtWidgets.QLineEdit(Form)
        self.lineEdit_23.setGeometry(QtCore.QRect(650, 30, 111, 21))
        self.lineEdit_23.setReadOnly(True)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.lineEdit_24 = QtWidgets.QLineEdit(Form)
        self.lineEdit_24.setGeometry(QtCore.QRect(10, 370, 111, 21))
        self.lineEdit_24.setReadOnly(True)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.lineEdit_25 = QtWidgets.QLineEdit(Form)
        self.lineEdit_25.setGeometry(QtCore.QRect(310, 370, 151, 21))
        self.lineEdit_25.setReadOnly(True)
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.cbSensorToolInstitution = QtWidgets.QComboBox(Form)
        self.cbSensorToolInstitution.setGeometry(QtCore.QRect(120, 30, 71, 21))
        self.cbSensorToolInstitution.setObjectName("cbSensorToolInstitution")
        self.cbSensorToolInstitution.addItem("")
        self.cbSensorToolInstitution.addItem("")
        self.cbSensorToolInstitution.addItem("")
        self.cbSensorToolInstitution.addItem("")
        self.cbSensorToolInstitution.addItem("")
        self.cbSensorToolInstitution.addItem("")
        self.cbSensorTrayInstitution = QtWidgets.QComboBox(Form)
        self.cbSensorTrayInstitution.setGeometry(QtCore.QRect(460, 30, 71, 21))
        self.cbSensorTrayInstitution.setObjectName("cbSensorTrayInstitution")
        self.cbSensorTrayInstitution.addItem("")
        self.cbSensorTrayInstitution.addItem("")
        self.cbSensorTrayInstitution.addItem("")
        self.cbSensorTrayInstitution.addItem("")
        self.cbSensorTrayInstitution.addItem("")
        self.cbSensorTrayInstitution.addItem("")
        self.cbAssemblyTrayInstitution = QtWidgets.QComboBox(Form)
        self.cbAssemblyTrayInstitution.setGeometry(QtCore.QRect(760, 30, 71, 21))
        self.cbAssemblyTrayInstitution.setObjectName("cbAssemblyTrayInstitution")
        self.cbAssemblyTrayInstitution.addItem("")
        self.cbAssemblyTrayInstitution.addItem("")
        self.cbAssemblyTrayInstitution.addItem("")
        self.cbAssemblyTrayInstitution.addItem("")
        self.cbAssemblyTrayInstitution.addItem("")
        self.cbAssemblyTrayInstitution.addItem("")
        self.cbPcbToolInstitution = QtWidgets.QComboBox(Form)
        self.cbPcbToolInstitution.setGeometry(QtCore.QRect(120, 370, 71, 21))
        self.cbPcbToolInstitution.setObjectName("cbPcbToolInstitution")
        self.cbPcbToolInstitution.addItem("")
        self.cbPcbToolInstitution.addItem("")
        self.cbPcbToolInstitution.addItem("")
        self.cbPcbToolInstitution.addItem("")
        self.cbPcbToolInstitution.addItem("")
        self.cbPcbToolInstitution.addItem("")
        self.cbPcbTrayInstitution = QtWidgets.QComboBox(Form)
        self.cbPcbTrayInstitution.setGeometry(QtCore.QRect(460, 370, 71, 21))
        self.cbPcbTrayInstitution.setObjectName("cbPcbTrayInstitution")
        self.cbPcbTrayInstitution.addItem("")
        self.cbPcbTrayInstitution.addItem("")
        self.cbPcbTrayInstitution.addItem("")
        self.cbPcbTrayInstitution.addItem("")
        self.cbPcbTrayInstitution.addItem("")
        self.cbPcbTrayInstitution.addItem("")

        self.retranslateUi(Form)
        self.cbSensorToolInstitution.setCurrentIndex(-1)
        self.cbSensorTrayInstitution.setCurrentIndex(-1)
        self.cbAssemblyTrayInstitution.setCurrentIndex(-1)
        self.cbPcbToolInstitution.setCurrentIndex(-1)
        self.cbPcbTrayInstitution.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setText(_translate("Form", "Sensor tool"))
        self.lineEdit_3.setText(_translate("Form", "Comments"))
        self.pbSensorToolDeleteComment.setText(_translate("Form", "delete selected"))
        self.pbSensorToolAddComment.setText(_translate("Form", "add comment"))
        self.pbPcbToolAddComment.setText(_translate("Form", "add comment"))
        self.lineEdit_4.setText(_translate("Form", "Comments"))
        self.lineEdit_5.setText(_translate("Form", "PCB tool"))
        self.pbPcbToolDeleteComment.setText(_translate("Form", "delete selected"))
        self.pbSensorTrayAddComment.setText(_translate("Form", "add comment"))
        self.lineEdit_8.setText(_translate("Form", "Comments"))
        self.pbPcbTrayAddComment.setText(_translate("Form", "add comment"))
        self.lineEdit_9.setText(_translate("Form", "Comments"))
        self.lineEdit_10.setText(_translate("Form", "Sensor Component Tray"))
        self.pbSensorTrayDeleteComment.setText(_translate("Form", "delete selected"))
        self.pbPcbTrayDeleteComment.setText(_translate("Form", "delete selected"))
        self.lineEdit_12.setText(_translate("Form", "PCB Component Tray"))
        self.lineEdit_13.setText(_translate("Form", "Comments"))
        self.pbAssemblyTrayAddComment.setText(_translate("Form", "add comment"))
        self.pbAssemblyTrayDeleteComment.setText(_translate("Form", "delete selected"))
        self.lineEdit_15.setText(_translate("Form", "Assembly Tray"))
        self.pbSensorToolEditNew.setText(_translate("Form", "edit/new"))
        self.pbSensorToolSave.setText(_translate("Form", "save"))
        self.pbSensorToolCancel.setText(_translate("Form", "cancel"))
        self.pbPcbToolCancel.setText(_translate("Form", "cancel"))
        self.pbPcbToolSave.setText(_translate("Form", "save"))
        self.pbPcbToolEditNew.setText(_translate("Form", "edit/new"))
        self.pbPcbTrayEditNew.setText(_translate("Form", "edit/new"))
        self.pbPcbTraySave.setText(_translate("Form", "save"))
        self.pbPcbTrayCancel.setText(_translate("Form", "cancel"))
        self.pbSensorTrayCancel.setText(_translate("Form", "cancel"))
        self.pbSensorTraySave.setText(_translate("Form", "save"))
        self.pbSensorTrayEditNew.setText(_translate("Form", "edit/new"))
        self.pbAssemblyTrayEditNew.setText(_translate("Form", "edit/new"))
        self.pbAssemblyTrayCancel.setText(_translate("Form", "cancel"))
        self.pbAssemblyTraySave.setText(_translate("Form", "save"))
        self.lineEdit_16.setText(_translate("Form", "Location"))
        self.lineEdit_17.setText(_translate("Form", "Location"))
        self.lineEdit_18.setText(_translate("Form", "Location"))
        self.lineEdit_19.setText(_translate("Form", "Location"))
        self.lineEdit_20.setText(_translate("Form", "Location"))
        self.lineEdit_21.setText(_translate("Form", "Institution"))
        self.lineEdit_22.setText(_translate("Form", "Institution"))
        self.lineEdit_23.setText(_translate("Form", "Institution"))
        self.lineEdit_24.setText(_translate("Form", "Institution"))
        self.lineEdit_25.setText(_translate("Form", "Institution"))
        self.cbSensorToolInstitution.setItemText(0, _translate("Form", "CERN"))
        self.cbSensorToolInstitution.setItemText(1, _translate("Form", "FNAL"))
        self.cbSensorToolInstitution.setItemText(2, _translate("Form", "UCSB"))
        self.cbSensorToolInstitution.setItemText(3, _translate("Form", "UMN"))
        self.cbSensorToolInstitution.setItemText(4, _translate("Form", "HEPHY"))
        self.cbSensorToolInstitution.setItemText(5, _translate("Form", "HPK"))
        self.cbSensorTrayInstitution.setItemText(0, _translate("Form", "CERN"))
        self.cbSensorTrayInstitution.setItemText(1, _translate("Form", "FNAL"))
        self.cbSensorTrayInstitution.setItemText(2, _translate("Form", "UCSB"))
        self.cbSensorTrayInstitution.setItemText(3, _translate("Form", "UMN"))
        self.cbSensorTrayInstitution.setItemText(4, _translate("Form", "HEPHY"))
        self.cbSensorTrayInstitution.setItemText(5, _translate("Form", "HPK"))
        self.cbAssemblyTrayInstitution.setItemText(0, _translate("Form", "CERN"))
        self.cbAssemblyTrayInstitution.setItemText(1, _translate("Form", "FNAL"))
        self.cbAssemblyTrayInstitution.setItemText(2, _translate("Form", "UCSB"))
        self.cbAssemblyTrayInstitution.setItemText(3, _translate("Form", "UMN"))
        self.cbAssemblyTrayInstitution.setItemText(4, _translate("Form", "HEPHY"))
        self.cbAssemblyTrayInstitution.setItemText(5, _translate("Form", "HPK"))
        self.cbPcbToolInstitution.setItemText(0, _translate("Form", "CERN"))
        self.cbPcbToolInstitution.setItemText(1, _translate("Form", "FNAL"))
        self.cbPcbToolInstitution.setItemText(2, _translate("Form", "UCSB"))
        self.cbPcbToolInstitution.setItemText(3, _translate("Form", "UMN"))
        self.cbPcbToolInstitution.setItemText(4, _translate("Form", "HEPHY"))
        self.cbPcbToolInstitution.setItemText(5, _translate("Form", "HPK"))
        self.cbPcbTrayInstitution.setItemText(0, _translate("Form", "CERN"))
        self.cbPcbTrayInstitution.setItemText(1, _translate("Form", "FNAL"))
        self.cbPcbTrayInstitution.setItemText(2, _translate("Form", "UCSB"))
        self.cbPcbTrayInstitution.setItemText(3, _translate("Form", "UMN"))
        self.cbPcbTrayInstitution.setItemText(4, _translate("Form", "HEPHY"))
        self.cbPcbTrayInstitution.setItemText(5, _translate("Form", "HPK"))
