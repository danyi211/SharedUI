# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_supplies.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1097, 749)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 101, 21))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.listAralditeComments = QtWidgets.QListWidget(Form)
        self.listAralditeComments.setGeometry(QtCore.QRect(10, 120, 261, 141))
        self.listAralditeComments.setObjectName("listAralditeComments")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 100, 131, 21))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pbAralditeDeleteComment = QtWidgets.QPushButton(Form)
        self.pbAralditeDeleteComment.setGeometry(QtCore.QRect(140, 100, 131, 21))
        self.pbAralditeDeleteComment.setObjectName("pbAralditeDeleteComment")
        self.pteAralditeWriteComment = QtWidgets.QPlainTextEdit(Form)
        self.pteAralditeWriteComment.setGeometry(QtCore.QRect(10, 270, 261, 71))
        self.pteAralditeWriteComment.setObjectName("pteAralditeWriteComment")
        self.pbAralditeAddComment = QtWidgets.QPushButton(Form)
        self.pbAralditeAddComment.setGeometry(QtCore.QRect(10, 340, 111, 23))
        self.pbAralditeAddComment.setObjectName("pbAralditeAddComment")
        self.pbAralditeEditNew = QtWidgets.QPushButton(Form)
        self.pbAralditeEditNew.setGeometry(QtCore.QRect(200, 10, 71, 21))
        self.pbAralditeEditNew.setObjectName("pbAralditeEditNew")
        self.pbAralditeSave = QtWidgets.QPushButton(Form)
        self.pbAralditeSave.setGeometry(QtCore.QRect(200, 30, 71, 21))
        self.pbAralditeSave.setObjectName("pbAralditeSave")
        self.pbAralditeCancel = QtWidgets.QPushButton(Form)
        self.pbAralditeCancel.setGeometry(QtCore.QRect(200, 50, 71, 21))
        self.pbAralditeCancel.setObjectName("pbAralditeCancel")
        self.dAralditeReceived = QtWidgets.QDateEdit(Form)
        self.dAralditeReceived.setGeometry(QtCore.QRect(110, 30, 91, 21))
        self.dAralditeReceived.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dAralditeReceived.setMaximumDate(QtCore.QDate(2030, 12, 31))
        self.dAralditeReceived.setMinimumDate(QtCore.QDate(2000, 1, 1))
        self.dAralditeReceived.setCalendarPopup(True)
        self.dAralditeReceived.setObjectName("dAralditeReceived")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 30, 101, 21))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 50, 101, 21))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 435, 101, 21))
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_6.setGeometry(QtCore.QRect(10, 415, 101, 21))
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.listWedgeComments = QtWidgets.QListWidget(Form)
        self.listWedgeComments.setGeometry(QtCore.QRect(10, 505, 261, 121))
        self.listWedgeComments.setObjectName("listWedgeComments")
        self.lineEdit_7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(10, 485, 131, 21))
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pbWedgeDeleteComment = QtWidgets.QPushButton(Form)
        self.pbWedgeDeleteComment.setGeometry(QtCore.QRect(140, 485, 131, 21))
        self.pbWedgeDeleteComment.setObjectName("pbWedgeDeleteComment")
        self.pbWedgeCancel = QtWidgets.QPushButton(Form)
        self.pbWedgeCancel.setEnabled(True)
        self.pbWedgeCancel.setGeometry(QtCore.QRect(200, 435, 71, 21))
        self.pbWedgeCancel.setObjectName("pbWedgeCancel")
        self.pbWedgeAddComment = QtWidgets.QPushButton(Form)
        self.pbWedgeAddComment.setGeometry(QtCore.QRect(10, 705, 111, 23))
        self.pbWedgeAddComment.setObjectName("pbWedgeAddComment")
        self.lineEdit_8 = QtWidgets.QLineEdit(Form)
        self.lineEdit_8.setGeometry(QtCore.QRect(10, 395, 101, 21))
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.dWedgeReceived = QtWidgets.QDateEdit(Form)
        self.dWedgeReceived.setEnabled(False)
        self.dWedgeReceived.setGeometry(QtCore.QRect(110, 415, 91, 21))
        self.dWedgeReceived.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dWedgeReceived.setMaximumDate(QtCore.QDate(2030, 12, 31))
        self.dWedgeReceived.setMinimumDate(QtCore.QDate(2000, 1, 1))
        self.dWedgeReceived.setCalendarPopup(True)
        self.dWedgeReceived.setObjectName("dWedgeReceived")
        self.pteWedgeWriteComment = QtWidgets.QPlainTextEdit(Form)
        self.pteWedgeWriteComment.setGeometry(QtCore.QRect(10, 635, 261, 71))
        self.pteWedgeWriteComment.setObjectName("pteWedgeWriteComment")
        self.pbWedgeSave = QtWidgets.QPushButton(Form)
        self.pbWedgeSave.setEnabled(True)
        self.pbWedgeSave.setGeometry(QtCore.QRect(200, 415, 71, 21))
        self.pbWedgeSave.setObjectName("pbWedgeSave")
        self.dWedgeExpires = QtWidgets.QDateEdit(Form)
        self.dWedgeExpires.setEnabled(False)
        self.dWedgeExpires.setGeometry(QtCore.QRect(110, 435, 91, 21))
        self.dWedgeExpires.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dWedgeExpires.setMaximumDate(QtCore.QDate(2030, 12, 31))
        self.dWedgeExpires.setMinimumDate(QtCore.QDate(2000, 1, 1))
        self.dWedgeExpires.setCalendarPopup(True)
        self.dWedgeExpires.setObjectName("dWedgeExpires")
        self.pbWedgeEditNew = QtWidgets.QPushButton(Form)
        self.pbWedgeEditNew.setGeometry(QtCore.QRect(200, 395, 71, 21))
        self.pbWedgeEditNew.setObjectName("pbWedgeEditNew")
        self.sbWedgeID = QtWidgets.QSpinBox(Form)
        self.sbWedgeID.setGeometry(QtCore.QRect(110, 395, 91, 21))
        self.sbWedgeID.setMaximum(2147483647)
        self.sbWedgeID.setObjectName("sbWedgeID")
        self.pbSylgardEditNew = QtWidgets.QPushButton(Form)
        self.pbSylgardEditNew.setGeometry(QtCore.QRect(530, 10, 71, 21))
        self.pbSylgardEditNew.setObjectName("pbSylgardEditNew")
        self.lineEdit_13 = QtWidgets.QLineEdit(Form)
        self.lineEdit_13.setGeometry(QtCore.QRect(320, 50, 121, 21))
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(Form)
        self.lineEdit_14.setGeometry(QtCore.QRect(320, 120, 151, 21))
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.sbSylgardID = QtWidgets.QSpinBox(Form)
        self.sbSylgardID.setGeometry(QtCore.QRect(470, 10, 61, 21))
        self.sbSylgardID.setMaximum(2147483647)
        self.sbSylgardID.setObjectName("sbSylgardID")
        self.pbSylgardCancel = QtWidgets.QPushButton(Form)
        self.pbSylgardCancel.setGeometry(QtCore.QRect(530, 50, 71, 21))
        self.pbSylgardCancel.setObjectName("pbSylgardCancel")
        self.listSylgardComments = QtWidgets.QListWidget(Form)
        self.listSylgardComments.setGeometry(QtCore.QRect(320, 140, 281, 121))
        self.listSylgardComments.setObjectName("listSylgardComments")
        self.lineEdit_15 = QtWidgets.QLineEdit(Form)
        self.lineEdit_15.setGeometry(QtCore.QRect(320, 10, 151, 21))
        self.lineEdit_15.setReadOnly(True)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.pbSylgardDeleteComment = QtWidgets.QPushButton(Form)
        self.pbSylgardDeleteComment.setGeometry(QtCore.QRect(470, 120, 131, 21))
        self.pbSylgardDeleteComment.setObjectName("pbSylgardDeleteComment")
        self.pteSylgardWriteComment = QtWidgets.QPlainTextEdit(Form)
        self.pteSylgardWriteComment.setGeometry(QtCore.QRect(320, 270, 281, 71))
        self.pteSylgardWriteComment.setObjectName("pteSylgardWriteComment")
        self.lineEdit_16 = QtWidgets.QLineEdit(Form)
        self.lineEdit_16.setGeometry(QtCore.QRect(320, 30, 121, 21))
        self.lineEdit_16.setReadOnly(True)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.pbSylgardAddComment = QtWidgets.QPushButton(Form)
        self.pbSylgardAddComment.setGeometry(QtCore.QRect(320, 340, 111, 23))
        self.pbSylgardAddComment.setObjectName("pbSylgardAddComment")
        self.pbSylgardSave = QtWidgets.QPushButton(Form)
        self.pbSylgardSave.setGeometry(QtCore.QRect(530, 30, 71, 21))
        self.pbSylgardSave.setObjectName("pbSylgardSave")
        self.dSylgardExpires = QtWidgets.QDateEdit(Form)
        self.dSylgardExpires.setGeometry(QtCore.QRect(440, 50, 91, 21))
        self.dSylgardExpires.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dSylgardExpires.setMaximumDate(QtCore.QDate(2030, 12, 31))
        self.dSylgardExpires.setMinimumDate(QtCore.QDate(2000, 1, 1))
        self.dSylgardExpires.setCalendarPopup(True)
        self.dSylgardExpires.setObjectName("dSylgardExpires")
        self.dSylgardReceived = QtWidgets.QDateEdit(Form)
        self.dSylgardReceived.setGeometry(QtCore.QRect(440, 30, 91, 21))
        self.dSylgardReceived.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dSylgardReceived.setMaximumDate(QtCore.QDate(2030, 12, 31))
        self.dSylgardReceived.setMinimumDate(QtCore.QDate(2000, 1, 1))
        self.dSylgardReceived.setCalendarPopup(True)
        self.dSylgardReceived.setObjectName("dSylgardReceived")
        self.dBondWireReceived = QtWidgets.QDateEdit(Form)
        self.dBondWireReceived.setGeometry(QtCore.QRect(430, 410, 91, 21))
        self.dBondWireReceived.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dBondWireReceived.setMaximumDate(QtCore.QDate(2030, 12, 31))
        self.dBondWireReceived.setMinimumDate(QtCore.QDate(2000, 1, 1))
        self.dBondWireReceived.setCalendarPopup(True)
        self.dBondWireReceived.setObjectName("dBondWireReceived")
        self.lineEdit_17 = QtWidgets.QLineEdit(Form)
        self.lineEdit_17.setGeometry(QtCore.QRect(320, 430, 111, 21))
        self.lineEdit_17.setReadOnly(True)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.listBondWireComments = QtWidgets.QListWidget(Form)
        self.listBondWireComments.setGeometry(QtCore.QRect(320, 500, 271, 121))
        self.listBondWireComments.setObjectName("listBondWireComments")
        self.pbBondWireEditNew = QtWidgets.QPushButton(Form)
        self.pbBondWireEditNew.setGeometry(QtCore.QRect(520, 390, 71, 21))
        self.pbBondWireEditNew.setObjectName("pbBondWireEditNew")
        self.pbBondWireDeleteComment = QtWidgets.QPushButton(Form)
        self.pbBondWireDeleteComment.setGeometry(QtCore.QRect(460, 480, 131, 21))
        self.pbBondWireDeleteComment.setObjectName("pbBondWireDeleteComment")
        self.pbBondWireCancel = QtWidgets.QPushButton(Form)
        self.pbBondWireCancel.setGeometry(QtCore.QRect(520, 430, 71, 21))
        self.pbBondWireCancel.setObjectName("pbBondWireCancel")
        self.lineEdit_18 = QtWidgets.QLineEdit(Form)
        self.lineEdit_18.setGeometry(QtCore.QRect(320, 480, 141, 21))
        self.lineEdit_18.setReadOnly(True)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.sbBondWireID = QtWidgets.QSpinBox(Form)
        self.sbBondWireID.setGeometry(QtCore.QRect(440, 390, 81, 21))
        self.sbBondWireID.setMaximum(2147483647)
        self.sbBondWireID.setObjectName("sbBondWireID")
        self.pteBondWireWriteComment = QtWidgets.QPlainTextEdit(Form)
        self.pteBondWireWriteComment.setGeometry(QtCore.QRect(320, 630, 271, 71))
        self.pteBondWireWriteComment.setObjectName("pteBondWireWriteComment")
        self.pbBondWireSave = QtWidgets.QPushButton(Form)
        self.pbBondWireSave.setGeometry(QtCore.QRect(520, 410, 71, 21))
        self.pbBondWireSave.setObjectName("pbBondWireSave")
        self.dBondWireExpires = QtWidgets.QDateEdit(Form)
        self.dBondWireExpires.setGeometry(QtCore.QRect(430, 430, 91, 21))
        self.dBondWireExpires.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dBondWireExpires.setMaximumDate(QtCore.QDate(2030, 12, 31))
        self.dBondWireExpires.setMinimumDate(QtCore.QDate(2000, 1, 1))
        self.dBondWireExpires.setCalendarPopup(True)
        self.dBondWireExpires.setObjectName("dBondWireExpires")
        self.lineEdit_19 = QtWidgets.QLineEdit(Form)
        self.lineEdit_19.setGeometry(QtCore.QRect(320, 410, 111, 21))
        self.lineEdit_19.setReadOnly(True)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lineEdit_20 = QtWidgets.QLineEdit(Form)
        self.lineEdit_20.setGeometry(QtCore.QRect(320, 390, 121, 21))
        self.lineEdit_20.setReadOnly(True)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.pbBondWireAddComment = QtWidgets.QPushButton(Form)
        self.pbBondWireAddComment.setGeometry(QtCore.QRect(320, 700, 111, 23))
        self.pbBondWireAddComment.setObjectName("pbBondWireAddComment")
        self.ckIsAralditeEmpty = QtWidgets.QCheckBox(Form)
        self.ckIsAralditeEmpty.setGeometry(QtCore.QRect(10, 75, 161, 17))
        self.ckIsAralditeEmpty.setObjectName("ckIsAralditeEmpty")
        self.ckIsSylgardEmpty = QtWidgets.QCheckBox(Form)
        self.ckIsSylgardEmpty.setGeometry(QtCore.QRect(320, 95, 161, 17))
        self.ckIsSylgardEmpty.setObjectName("ckIsSylgardEmpty")
        self.ckIsBondWireEmpty = QtWidgets.QCheckBox(Form)
        self.ckIsBondWireEmpty.setGeometry(QtCore.QRect(320, 455, 161, 17))
        self.ckIsBondWireEmpty.setObjectName("ckIsBondWireEmpty")
        self.ckIsWedgeEmpty = QtWidgets.QCheckBox(Form)
        self.ckIsWedgeEmpty.setGeometry(QtCore.QRect(10, 460, 161, 17))
        self.ckIsWedgeEmpty.setObjectName("ckIsWedgeEmpty")
        self.dAralditeExpires = QtWidgets.QDateEdit(Form)
        self.dAralditeExpires.setGeometry(QtCore.QRect(110, 50, 91, 21))
        self.dAralditeExpires.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dAralditeExpires.setMaximumDate(QtCore.QDate(2030, 12, 31))
        self.dAralditeExpires.setMinimumDate(QtCore.QDate(2000, 1, 1))
        self.dAralditeExpires.setCalendarPopup(True)
        self.dAralditeExpires.setObjectName("dAralditeExpires")
        self.leSylgardCuring = QtWidgets.QLineEdit(Form)
        self.leSylgardCuring.setGeometry(QtCore.QRect(460, 70, 141, 20))
        self.leSylgardCuring.setObjectName("leSylgardCuring")
        self.lineEdit_21 = QtWidgets.QLineEdit(Form)
        self.lineEdit_21.setGeometry(QtCore.QRect(320, 70, 141, 21))
        self.lineEdit_21.setReadOnly(True)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.leAralditeID = QtWidgets.QLineEdit(Form)
        self.leAralditeID.setGeometry(QtCore.QRect(110, 10, 91, 20))
        self.leAralditeID.setObjectName("leAralditeID")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setText(_translate("Form", "Araldite batch"))
        self.lineEdit_3.setText(_translate("Form", "Comments"))
        self.pbAralditeDeleteComment.setText(_translate("Form", "delete selected"))
        self.pbAralditeAddComment.setText(_translate("Form", "add comment"))
        self.pbAralditeEditNew.setText(_translate("Form", "edit/new"))
        self.pbAralditeSave.setText(_translate("Form", "save"))
        self.pbAralditeCancel.setText(_translate("Form", "cancel"))
        self.lineEdit_2.setText(_translate("Form", "Received"))
        self.lineEdit_4.setText(_translate("Form", "Expires"))
        self.lineEdit_5.setText(_translate("Form", "Expires"))
        self.lineEdit_6.setText(_translate("Form", "Received"))
        self.lineEdit_7.setText(_translate("Form", "Comments"))
        self.pbWedgeDeleteComment.setText(_translate("Form", "delete selected"))
        self.pbWedgeCancel.setText(_translate("Form", "cancel"))
        self.pbWedgeAddComment.setText(_translate("Form", "add comment"))
        self.lineEdit_8.setToolTip(_translate("Form", "Loctite = silver epoxy"))
        self.lineEdit_8.setText(_translate("Form", "Wedge batch"))
        self.pbWedgeSave.setText(_translate("Form", "save"))
        self.pbWedgeEditNew.setText(_translate("Form", "edit/new"))
        self.pbSylgardEditNew.setText(_translate("Form", "edit/new"))
        self.lineEdit_13.setText(_translate("Form", "Expires"))
        self.lineEdit_14.setText(_translate("Form", "Comments"))
        self.pbSylgardCancel.setText(_translate("Form", "cancel"))
        self.lineEdit_15.setText(_translate("Form", "Sylgard batch"))
        self.pbSylgardDeleteComment.setText(_translate("Form", "delete selected"))
        self.lineEdit_16.setText(_translate("Form", "Received"))
        self.pbSylgardAddComment.setText(_translate("Form", "add comment"))
        self.pbSylgardSave.setText(_translate("Form", "save"))
        self.lineEdit_17.setText(_translate("Form", "Expires"))
        self.pbBondWireEditNew.setText(_translate("Form", "edit/new"))
        self.pbBondWireDeleteComment.setText(_translate("Form", "delete selected"))
        self.pbBondWireCancel.setText(_translate("Form", "cancel"))
        self.lineEdit_18.setText(_translate("Form", "Comments"))
        self.pbBondWireSave.setText(_translate("Form", "save"))
        self.lineEdit_19.setText(_translate("Form", "Received"))
        self.lineEdit_20.setText(_translate("Form", "Bond wire batch"))
        self.pbBondWireAddComment.setText(_translate("Form", "add comment"))
        self.ckIsAralditeEmpty.setText(_translate("Form", "Batch is empty"))
        self.ckIsSylgardEmpty.setText(_translate("Form", "Batch is empty"))
        self.ckIsBondWireEmpty.setText(_translate("Form", "Batch is empty"))
        self.ckIsWedgeEmpty.setText(_translate("Form", "Batch is empty"))
        self.lineEdit_21.setText(_translate("Form", "Curing agent batch"))

