# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_sensor.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1097, 726)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(10, 110, 261, 541))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(2)
        self.frame_2.setMidLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.pbGoShipment = QtWidgets.QPushButton(self.frame_2)
        self.pbGoShipment.setGeometry(QtCore.QRect(120, 60, 141, 21))
        self.pbGoShipment.setObjectName("pbGoShipment")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_9.setGeometry(QtCore.QRect(1, 41, 121, 20))
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(1, 60, 121, 21))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.leLocation = QtWidgets.QLineEdit(self.frame_2)
        self.leLocation.setGeometry(QtCore.QRect(120, 41, 141, 20))
        self.leLocation.setText("")
        self.leLocation.setReadOnly(True)
        self.leLocation.setObjectName("leLocation")
        self.listShipments = QtWidgets.QListWidget(self.frame_2)
        self.listShipments.setGeometry(QtCore.QRect(0, 80, 261, 91))
        self.listShipments.setObjectName("listShipments")
        self.cbShape = QtWidgets.QComboBox(self.frame_2)
        self.cbShape.setGeometry(QtCore.QRect(180, 220, 81, 20))
        self.cbShape.setObjectName("cbShape")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_10.setGeometry(QtCore.QRect(1, 220, 181, 21))
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(1, 240, 181, 21))
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(1, 200, 181, 21))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pbAddComment = QtWidgets.QPushButton(self.frame_2)
        self.pbAddComment.setGeometry(QtCore.QRect(0, 520, 111, 21))
        self.pbAddComment.setObjectName("pbAddComment")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_14.setGeometry(QtCore.QRect(1, 300, 141, 21))
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.pbDeleteComment = QtWidgets.QPushButton(self.frame_2)
        self.pbDeleteComment.setGeometry(QtCore.QRect(140, 300, 121, 21))
        self.pbDeleteComment.setObjectName("pbDeleteComment")
        self.pteWriteComment = QtWidgets.QPlainTextEdit(self.frame_2)
        self.pteWriteComment.setGeometry(QtCore.QRect(0, 450, 261, 71))
        self.pteWriteComment.setObjectName("pteWriteComment")
        self.listComments = QtWidgets.QListWidget(self.frame_2)
        self.listComments.setGeometry(QtCore.QRect(0, 320, 261, 121))
        self.listComments.setObjectName("listComments")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_17.setGeometry(QtCore.QRect(1, 21, 121, 20))
        self.lineEdit_17.setReadOnly(True)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_18.setGeometry(QtCore.QRect(1, 1, 121, 20))
        self.lineEdit_18.setReadOnly(True)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.cbType = QtWidgets.QComboBox(self.frame_2)
        self.cbType.setGeometry(QtCore.QRect(180, 200, 81, 21))
        self.cbType.setObjectName("cbType")
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.leBarcode = QtWidgets.QLineEdit(self.frame_2)
        self.leBarcode.setGeometry(QtCore.QRect(180, 180, 80, 20))
        self.leBarcode.setText("")
        self.leBarcode.setReadOnly(True)
        self.leBarcode.setObjectName("leBarcode")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_23.setGeometry(QtCore.QRect(0, 180, 181, 21))
        self.lineEdit_23.setReadOnly(True)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.cbInstitution = QtWidgets.QComboBox(self.frame_2)
        self.cbInstitution.setGeometry(QtCore.QRect(120, 20, 141, 21))
        self.cbInstitution.setObjectName("cbInstitution")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInsertUser = QtWidgets.QComboBox(self.frame_2)
        self.cbInsertUser.setGeometry(QtCore.QRect(120, 0, 141, 21))
        self.cbInsertUser.setObjectName("cbInsertUser")
        self.cbChannelDensity = QtWidgets.QComboBox(self.frame_2)
        self.cbChannelDensity.setGeometry(QtCore.QRect(180, 240, 81, 20))
        self.cbChannelDensity.setObjectName("cbChannelDensity")
        self.cbChannelDensity.addItem("")
        self.cbChannelDensity.addItem("")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(0, 260, 181, 21))
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.cbGrade = QtWidgets.QComboBox(self.frame_2)
        self.cbGrade.setGeometry(QtCore.QRect(180, 260, 81, 20))
        self.cbGrade.setObjectName("cbGrade")
        self.cbGrade.addItem("")
        self.cbGrade.addItem("")
        self.cbGrade.addItem("")
        self.lineEdit_9.raise_()
        self.lineEdit_3.raise_()
        self.leLocation.raise_()
        self.listShipments.raise_()
        self.lineEdit_10.raise_()
        self.lineEdit_6.raise_()
        self.lineEdit_4.raise_()
        self.pbAddComment.raise_()
        self.lineEdit_14.raise_()
        self.pbDeleteComment.raise_()
        self.pteWriteComment.raise_()
        self.listComments.raise_()
        self.pbGoShipment.raise_()
        self.cbShape.raise_()
        self.lineEdit_17.raise_()
        self.lineEdit_18.raise_()
        self.cbType.raise_()
        self.leBarcode.raise_()
        self.lineEdit_23.raise_()
        self.cbInstitution.raise_()
        self.cbInsertUser.raise_()
        self.cbChannelDensity.raise_()
        self.lineEdit_7.raise_()
        self.cbGrade.raise_()
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(10, 10, 261, 91))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.pbSave = QtWidgets.QPushButton(self.frame_3)
        self.pbSave.setGeometry(QtCore.QRect(90, 50, 71, 21))
        self.pbSave.setObjectName("pbSave")
        self.pbEdit = QtWidgets.QPushButton(self.frame_3)
        self.pbEdit.setGeometry(QtCore.QRect(0, 70, 81, 21))
        self.pbEdit.setObjectName("pbEdit")
        self.pbCancel = QtWidgets.QPushButton(self.frame_3)
        self.pbCancel.setGeometry(QtCore.QRect(170, 50, 71, 21))
        self.pbCancel.setObjectName("pbCancel")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit.setGeometry(QtCore.QRect(1, 1, 151, 19))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pbNew = QtWidgets.QPushButton(self.frame_3)
        self.pbNew.setGeometry(QtCore.QRect(0, 50, 81, 21))
        self.pbNew.setObjectName("pbNew")
        self.leID = QtWidgets.QLineEdit(self.frame_3)
        self.leID.setGeometry(QtCore.QRect(150, 0, 111, 20))
        self.leID.setText("")
        self.leID.setReadOnly(True)
        self.leID.setObjectName("leID")
        self.leStatus = QtWidgets.QLineEdit(self.frame_3)
        self.leStatus.setGeometry(QtCore.QRect(90, 70, 111, 20))
        self.leStatus.setText("")
        self.leStatus.setReadOnly(True)
        self.leStatus.setObjectName("leStatus")
        self.pbLoad = QtWidgets.QPushButton(self.frame_3)
        self.pbLoad.setGeometry(QtCore.QRect(70, 20, 131, 21))
        self.pbLoad.setObjectName("pbLoad")
        self.pbGoStepSensor = QtWidgets.QPushButton(Form)
        self.pbGoStepSensor.setGeometry(QtCore.QRect(510, 303, 51, 21))
        self.pbGoStepSensor.setObjectName("pbGoStepSensor")
        self.pbGoModule = QtWidgets.QPushButton(Form)
        self.pbGoModule.setGeometry(QtCore.QRect(510, 393, 51, 21))
        self.pbGoModule.setObjectName("pbGoModule")
        self.lineEdit_12 = QtWidgets.QLineEdit(Form)
        self.lineEdit_12.setGeometry(QtCore.QRect(310, 323, 121, 21))
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_8 = QtWidgets.QLineEdit(Form)
        self.lineEdit_8.setGeometry(QtCore.QRect(310, 393, 121, 21))
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_13 = QtWidgets.QLineEdit(Form)
        self.lineEdit_13.setGeometry(QtCore.QRect(310, 303, 121, 21))
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.pbGoProtomodule = QtWidgets.QPushButton(Form)
        self.pbGoProtomodule.setGeometry(QtCore.QRect(510, 323, 51, 21))
        self.pbGoProtomodule.setObjectName("pbGoProtomodule")
        self.sbStepSensor = QtWidgets.QSpinBox(Form)
        self.sbStepSensor.setGeometry(QtCore.QRect(430, 303, 81, 21))
        self.sbStepSensor.setReadOnly(True)
        self.sbStepSensor.setMinimum(-1)
        self.sbStepSensor.setMaximum(2147483647)
        self.sbStepSensor.setObjectName("sbStepSensor")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(310, 373, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(310, 283, 131, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(310, 223, 141, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_15 = QtWidgets.QLineEdit(Form)
        self.lineEdit_15.setGeometry(QtCore.QRect(310, 243, 131, 21))
        self.lineEdit_15.setReadOnly(True)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.cbInspection = QtWidgets.QComboBox(Form)
        self.cbInspection.setGeometry(QtCore.QRect(440, 243, 121, 21))
        self.cbInspection.setObjectName("cbInspection")
        self.cbInspection.addItem("")
        self.cbInspection.addItem("")
        self.leProtomodule = QtWidgets.QLineEdit(Form)
        self.leProtomodule.setGeometry(QtCore.QRect(430, 323, 80, 20))
        self.leProtomodule.setReadOnly(True)
        self.leProtomodule.setObjectName("leProtomodule")
        self.leModule = QtWidgets.QLineEdit(Form)
        self.leModule.setGeometry(QtCore.QRect(430, 393, 80, 20))
        self.leModule.setReadOnly(True)
        self.leModule.setObjectName("leModule")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(310, 30, 211, 16))
        self.label_4.setObjectName("label_4")
        self.frame_6 = QtWidgets.QFrame(Form)
        self.frame_6.setGeometry(QtCore.QRect(310, 111, 241, 81))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_6.setObjectName("frame_6")
        self.dsbKaptonFlatness = QtWidgets.QDoubleSpinBox(self.frame_6)
        self.dsbKaptonFlatness.setEnabled(False)
        self.dsbKaptonFlatness.setGeometry(QtCore.QRect(159, 40, 81, 20))
        self.dsbKaptonFlatness.setReadOnly(True)
        self.dsbKaptonFlatness.setDecimals(3)
        self.dsbKaptonFlatness.setMinimum(-1.0)
        self.dsbKaptonFlatness.setMaximum(2147483647.0)
        self.dsbKaptonFlatness.setSingleStep(0.05)
        self.dsbKaptonFlatness.setObjectName("dsbKaptonFlatness")
        self.lineEdit_32 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_32.setEnabled(False)
        self.lineEdit_32.setGeometry(QtCore.QRect(1, 20, 161, 20))
        self.lineEdit_32.setReadOnly(True)
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.cbCheckEdgesFirm = QtWidgets.QComboBox(self.frame_6)
        self.cbCheckEdgesFirm.setEnabled(False)
        self.cbCheckEdgesFirm.setGeometry(QtCore.QRect(159, 0, 81, 20))
        self.cbCheckEdgesFirm.setObjectName("cbCheckEdgesFirm")
        self.cbCheckEdgesFirm.addItem("")
        self.cbCheckEdgesFirm.addItem("")
        self.lineEdit_33 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_33.setEnabled(False)
        self.lineEdit_33.setGeometry(QtCore.QRect(1, 0, 161, 20))
        self.lineEdit_33.setReadOnly(True)
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.cbCheckGlueSpill = QtWidgets.QComboBox(self.frame_6)
        self.cbCheckGlueSpill.setEnabled(False)
        self.cbCheckGlueSpill.setGeometry(QtCore.QRect(159, 20, 81, 20))
        self.cbCheckGlueSpill.setObjectName("cbCheckGlueSpill")
        self.cbCheckGlueSpill.addItem("")
        self.cbCheckGlueSpill.addItem("")
        self.lineEdit_34 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_34.setEnabled(False)
        self.lineEdit_34.setGeometry(QtCore.QRect(1, 40, 161, 20))
        self.lineEdit_34.setReadOnly(True)
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.lineEdit_28 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_28.setEnabled(False)
        self.lineEdit_28.setGeometry(QtCore.QRect(1, 60, 161, 20))
        self.lineEdit_28.setReadOnly(True)
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.dsbThickness = QtWidgets.QDoubleSpinBox(self.frame_6)
        self.dsbThickness.setEnabled(False)
        self.dsbThickness.setGeometry(QtCore.QRect(160, 60, 79, 20))
        self.dsbThickness.setReadOnly(True)
        self.dsbThickness.setDecimals(3)
        self.dsbThickness.setMinimum(-1.0)
        self.dsbThickness.setMaximum(2147483647.0)
        self.dsbThickness.setSingleStep(0.05)
        self.dsbThickness.setObjectName("dsbThickness")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(310, 90, 241, 16))
        self.label_6.setObjectName("label_6")
        self.frame_7 = QtWidgets.QFrame(Form)
        self.frame_7.setEnabled(False)
        self.frame_7.setGeometry(QtCore.QRect(310, 50, 241, 21))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_7.setObjectName("frame_7")
        self.pbGoStepKapton = QtWidgets.QPushButton(self.frame_7)
        self.pbGoStepKapton.setEnabled(False)
        self.pbGoStepKapton.setGeometry(QtCore.QRect(190, 0, 51, 21))
        self.pbGoStepKapton.setObjectName("pbGoStepKapton")
        self.sbStepKapton = QtWidgets.QSpinBox(self.frame_7)
        self.sbStepKapton.setEnabled(False)
        self.sbStepKapton.setGeometry(QtCore.QRect(110, 1, 81, 19))
        self.sbStepKapton.setReadOnly(True)
        self.sbStepKapton.setMinimum(-1)
        self.sbStepKapton.setMaximum(2147483647)
        self.sbStepKapton.setObjectName("sbStepKapton")
        self.lineEdit_35 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_35.setEnabled(False)
        self.lineEdit_35.setGeometry(QtCore.QRect(1, 1, 111, 19))
        self.lineEdit_35.setReadOnly(True)
        self.lineEdit_35.setObjectName("lineEdit_35")

        self.retranslateUi(Form)
        self.cbShape.setCurrentIndex(-1)
        self.cbType.setCurrentIndex(-1)
        self.cbInstitution.setCurrentIndex(-1)
        self.cbInsertUser.setCurrentIndex(-1)
        self.cbChannelDensity.setCurrentIndex(-1)
        self.cbGrade.setCurrentIndex(-1)
        self.cbInspection.setCurrentIndex(-1)
        self.cbCheckEdgesFirm.setCurrentIndex(-1)
        self.cbCheckGlueSpill.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pbGoShipment.setText(_translate("Form", "Go to selected"))
        self.lineEdit_9.setText(_translate("Form", "Location"))
        self.lineEdit_3.setText(_translate("Form", "Shipments"))
        self.listShipments.setToolTip(_translate("Form", "ID (date sent) (SENDER to RECEIVER)"))
        self.cbShape.setItemText(0, _translate("Form", "full"))
        self.cbShape.setItemText(1, _translate("Form", "top"))
        self.cbShape.setItemText(2, _translate("Form", "bottom"))
        self.cbShape.setItemText(3, _translate("Form", "left"))
        self.cbShape.setItemText(4, _translate("Form", "right"))
        self.cbShape.setItemText(5, _translate("Form", "five"))
        self.cbShape.setItemText(6, _translate("Form", "three"))
        self.cbShape.setItemText(7, _translate("Form", "full+three"))
        self.lineEdit_10.setText(_translate("Form", "Geometry"))
        self.lineEdit_6.setText(_translate("Form", "Resolution type"))
        self.lineEdit_4.setText(_translate("Form", "Type (Si thickness)"))
        self.pbAddComment.setText(_translate("Form", "Add comment"))
        self.lineEdit_14.setText(_translate("Form", "Comments"))
        self.pbDeleteComment.setText(_translate("Form", "Delete selected"))
        self.lineEdit_17.setText(_translate("Form", "Institution"))
        self.lineEdit_18.setText(_translate("Form", "User name"))
        self.cbType.setItemText(0, _translate("Form", "120um"))
        self.cbType.setItemText(1, _translate("Form", "200um"))
        self.cbType.setItemText(2, _translate("Form", "300um"))
        self.lineEdit_23.setText(_translate("Form", "Barcode"))
        self.cbInstitution.setItemText(0, _translate("Form", "CERN"))
        self.cbInstitution.setItemText(1, _translate("Form", "FNAL"))
        self.cbInstitution.setItemText(2, _translate("Form", "UCSB"))
        self.cbInstitution.setItemText(3, _translate("Form", "UMN"))
        self.cbInstitution.setItemText(4, _translate("Form", "HEPHY"))
        self.cbInstitution.setItemText(5, _translate("Form", "HPK"))
        self.cbChannelDensity.setItemText(0, _translate("Form", "HD"))
        self.cbChannelDensity.setItemText(1, _translate("Form", "LD"))
        self.lineEdit_7.setText(_translate("Form", "Sensor grade"))
        self.cbGrade.setItemText(0, _translate("Form", "A"))
        self.cbGrade.setItemText(1, _translate("Form", "B"))
        self.cbGrade.setItemText(2, _translate("Form", "C"))
        self.pbSave.setText(_translate("Form", "Save"))
        self.pbEdit.setText(_translate("Form", "Edit"))
        self.pbCancel.setText(_translate("Form", "Cancel"))
        self.lineEdit.setText(_translate("Form", "Sensor ID"))
        self.pbNew.setText(_translate("Form", "New"))
        self.pbLoad.setText(_translate("Form", "Load / check DB"))
        self.pbGoStepSensor.setText(_translate("Form", "Go to"))
        self.pbGoModule.setText(_translate("Form", "Go to"))
        self.lineEdit_12.setText(_translate("Form", "On protomodule"))
        self.lineEdit_8.setText(_translate("Form", "On module"))
        self.lineEdit_13.setText(_translate("Form", "Placement step"))
        self.pbGoProtomodule.setText(_translate("Form", "Go to"))
        self.label.setText(_translate("Form", "module"))
        self.label_2.setText(_translate("Form", "sensor placement"))
        self.label_3.setText(_translate("Form", "sensor qualification"))
        self.lineEdit_15.setText(_translate("Form", "Visual inspection"))
        self.cbInspection.setItemText(0, _translate("Form", "pass"))
        self.cbInspection.setItemText(1, _translate("Form", "fail"))
        self.label_4.setText(_translate("Form", "Kapton application"))
        self.lineEdit_32.setToolTip(_translate("Form", "height difference between highest and lowers corners"))
        self.lineEdit_32.setText(_translate("Form", "Check glue spillage"))
        self.cbCheckEdgesFirm.setItemText(0, _translate("Form", "pass"))
        self.cbCheckEdgesFirm.setItemText(1, _translate("Form", "fail"))
        self.lineEdit_33.setToolTip(_translate("Form", "height difference between highest and lowers corners"))
        self.lineEdit_33.setText(_translate("Form", "Check edges firm"))
        self.cbCheckGlueSpill.setItemText(0, _translate("Form", "pass"))
        self.cbCheckGlueSpill.setItemText(1, _translate("Form", "fail"))
        self.lineEdit_34.setToolTip(_translate("Form", "height difference between highest and lowers corners"))
        self.lineEdit_34.setText(_translate("Form", "Kapton flatness (mm)"))
        self.lineEdit_28.setToolTip(_translate("Form", "height difference between highest and lowers corners"))
        self.lineEdit_28.setText(_translate("Form", "Kapton thickness (mm)"))
        self.label_6.setText(_translate("Form", "kaptonized sensor qualification"))
        self.pbGoStepKapton.setText(_translate("Form", "Go to"))
        self.lineEdit_35.setText(_translate("Form", "Kapton step"))

