# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_module.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1199, 756)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(300, 0, 271, 51))
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setEnabled(True)
        self.label_7.setGeometry(QtCore.QRect(330, 80, 241, 16))
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(330, 300, 181, 16))
        self.label_3.setObjectName("label_3")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 160, 281, 531))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cbResolution = QtWidgets.QComboBox(self.frame)
        self.cbResolution.setEnabled(False)
        self.cbResolution.setGeometry(QtCore.QRect(180, 60, 101, 20))
        self.cbResolution.setObjectName("cbResolution")
        self.cbResolution.addItem("")
        self.cbResolution.addItem("")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_22.setGeometry(QtCore.QRect(0, 60, 181, 21))
        self.lineEdit_22.setReadOnly(True)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.cbShape = QtWidgets.QComboBox(self.frame)
        self.cbShape.setEnabled(False)
        self.cbShape.setGeometry(QtCore.QRect(180, 80, 101, 20))
        self.cbShape.setObjectName("cbShape")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.cbShape.addItem("")
        self.pbGoStepSensor = QtWidgets.QPushButton(self.frame)
        self.pbGoStepSensor.setGeometry(QtCore.QRect(240, 140, 41, 21))
        self.pbGoStepSensor.setObjectName("pbGoStepSensor")
        self.sbStepSensor = QtWidgets.QSpinBox(self.frame)
        self.sbStepSensor.setGeometry(QtCore.QRect(180, 139, 61, 21))
        self.sbStepSensor.setReadOnly(True)
        self.sbStepSensor.setMinimum(-1)
        self.sbStepSensor.setMaximum(2147483647)
        self.sbStepSensor.setObjectName("sbStepSensor")
        self.pbGoProtomodule = QtWidgets.QPushButton(self.frame)
        self.pbGoProtomodule.setGeometry(QtCore.QRect(240, 281, 41, 21))
        self.pbGoProtomodule.setObjectName("pbGoProtomodule")
        self.cbInspection = QtWidgets.QComboBox(self.frame)
        self.cbInspection.setEnabled(False)
        self.cbInspection.setGeometry(QtCore.QRect(180, 301, 101, 20))
        self.cbInspection.setObjectName("cbInspection")
        self.cbInspection.addItem("")
        self.cbInspection.addItem("")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_14.setGeometry(QtCore.QRect(0, 39, 141, 21))
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.leProtomodule = QtWidgets.QLineEdit(self.frame)
        self.leProtomodule.setGeometry(QtCore.QRect(140, 281, 101, 20))
        self.leProtomodule.setReadOnly(True)
        self.leProtomodule.setObjectName("leProtomodule")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 220, 141, 21))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_20.setGeometry(QtCore.QRect(0, 79, 181, 21))
        self.lineEdit_20.setReadOnly(True)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.listComments = QtWidgets.QListWidget(self.frame)
        self.listComments.setGeometry(QtCore.QRect(0, 351, 281, 91))
        self.listComments.setObjectName("listComments")
        self.pbGoPcb = QtWidgets.QPushButton(self.frame)
        self.pbGoPcb.setGeometry(QtCore.QRect(240, 261, 41, 21))
        self.pbGoPcb.setObjectName("pbGoPcb")
        self.sbStepPcb = QtWidgets.QSpinBox(self.frame)
        self.sbStepPcb.setGeometry(QtCore.QRect(180, 179, 61, 21))
        self.sbStepPcb.setReadOnly(True)
        self.sbStepPcb.setMinimum(-1)
        self.sbStepPcb.setMaximum(2147483647)
        self.sbStepPcb.setObjectName("sbStepPcb")
        self.pbGoBaseplate = QtWidgets.QPushButton(self.frame)
        self.pbGoBaseplate.setGeometry(QtCore.QRect(240, 221, 41, 21))
        self.pbGoBaseplate.setObjectName("pbGoBaseplate")
        self.leLocation = QtWidgets.QLineEdit(self.frame)
        self.leLocation.setGeometry(QtCore.QRect(140, 39, 141, 21))
        self.leLocation.setText("")
        self.leLocation.setReadOnly(True)
        self.leLocation.setObjectName("leLocation")
        self.pteWriteComment = QtWidgets.QPlainTextEdit(self.frame)
        self.pteWriteComment.setGeometry(QtCore.QRect(0, 451, 281, 61))
        self.pteWriteComment.setPlainText("")
        self.pteWriteComment.setObjectName("pteWriteComment")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(0, 240, 141, 21))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_53 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_53.setGeometry(QtCore.QRect(1, 0, 141, 20))
        self.lineEdit_53.setReadOnly(True)
        self.lineEdit_53.setObjectName("lineEdit_53")
        self.cbInsertUser = QtWidgets.QComboBox(self.frame)
        self.cbInsertUser.setEnabled(False)
        self.cbInsertUser.setGeometry(QtCore.QRect(140, 0, 141, 21))
        self.cbInsertUser.setObjectName("cbInsertUser")
        self.leBaseplate = QtWidgets.QLineEdit(self.frame)
        self.leBaseplate.setGeometry(QtCore.QRect(140, 221, 101, 20))
        self.leBaseplate.setReadOnly(True)
        self.leBaseplate.setObjectName("leBaseplate")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_11.setGeometry(QtCore.QRect(0, 179, 181, 21))
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.pbGoSensor = QtWidgets.QPushButton(self.frame)
        self.pbGoSensor.setGeometry(QtCore.QRect(240, 241, 41, 21))
        self.pbGoSensor.setObjectName("pbGoSensor")
        self.cbGrade = QtWidgets.QComboBox(self.frame)
        self.cbGrade.setEnabled(False)
        self.cbGrade.setGeometry(QtCore.QRect(180, 100, 101, 20))
        self.cbGrade.setObjectName("cbGrade")
        self.cbGrade.addItem("")
        self.cbGrade.addItem("")
        self.cbGrade.addItem("")
        self.pbAddComment = QtWidgets.QPushButton(self.frame)
        self.pbAddComment.setGeometry(QtCore.QRect(0, 511, 111, 21))
        self.pbAddComment.setObjectName("pbAddComment")
        self.leSensor = QtWidgets.QLineEdit(self.frame)
        self.leSensor.setGeometry(QtCore.QRect(140, 241, 101, 20))
        self.leSensor.setReadOnly(True)
        self.leSensor.setObjectName("leSensor")
        self.pbDeleteComment = QtWidgets.QPushButton(self.frame)
        self.pbDeleteComment.setGeometry(QtCore.QRect(160, 331, 121, 21))
        self.pbDeleteComment.setObjectName("pbDeleteComment")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_13.setGeometry(QtCore.QRect(0, 139, 181, 21))
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_23.setGeometry(QtCore.QRect(0, 280, 141, 21))
        self.lineEdit_23.setReadOnly(True)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.lineEdit_52 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_52.setGeometry(QtCore.QRect(0, 19, 141, 21))
        self.lineEdit_52.setReadOnly(True)
        self.lineEdit_52.setObjectName("lineEdit_52")
        self.lineEdit_39 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_39.setGeometry(QtCore.QRect(1, 301, 181, 20))
        self.lineEdit_39.setReadOnly(True)
        self.lineEdit_39.setObjectName("lineEdit_39")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(0, 260, 141, 21))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_16.setGeometry(QtCore.QRect(0, 331, 161, 21))
        self.lineEdit_16.setReadOnly(True)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lePcb = QtWidgets.QLineEdit(self.frame)
        self.lePcb.setGeometry(QtCore.QRect(140, 261, 101, 20))
        self.lePcb.setReadOnly(True)
        self.lePcb.setObjectName("lePcb")
        self.cbInstitution = QtWidgets.QComboBox(self.frame)
        self.cbInstitution.setEnabled(False)
        self.cbInstitution.setGeometry(QtCore.QRect(140, 20, 141, 21))
        self.cbInstitution.setObjectName("cbInstitution")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_21.setGeometry(QtCore.QRect(0, 99, 181, 21))
        self.lineEdit_21.setReadOnly(True)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.pbGoStepPcb = QtWidgets.QPushButton(self.frame)
        self.pbGoStepPcb.setGeometry(QtCore.QRect(240, 180, 41, 21))
        self.pbGoStepPcb.setObjectName("pbGoStepPcb")
        self.cbInstitutionStepSensor = QtWidgets.QComboBox(self.frame)
        self.cbInstitutionStepSensor.setEnabled(False)
        self.cbInstitutionStepSensor.setGeometry(QtCore.QRect(180, 160, 101, 21))
        self.cbInstitutionStepSensor.setObjectName("cbInstitutionStepSensor")
        self.cbInstitutionStepSensor.addItem("")
        self.cbInstitutionStepSensor.addItem("")
        self.cbInstitutionStepSensor.addItem("")
        self.cbInstitutionStepSensor.addItem("")
        self.cbInstitutionStepSensor.addItem("")
        self.cbInstitutionStepSensor.addItem("")
        self.cbInstitutionStepPcb = QtWidgets.QComboBox(self.frame)
        self.cbInstitutionStepPcb.setEnabled(False)
        self.cbInstitutionStepPcb.setGeometry(QtCore.QRect(180, 200, 101, 21))
        self.cbInstitutionStepPcb.setObjectName("cbInstitutionStepPcb")
        self.cbInstitutionStepPcb.addItem("")
        self.cbInstitutionStepPcb.addItem("")
        self.cbInstitutionStepPcb.addItem("")
        self.cbInstitutionStepPcb.addItem("")
        self.cbInstitutionStepPcb.addItem("")
        self.cbInstitutionStepPcb.addItem("")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(330, 320, 271, 121))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(0, 60, 191, 21))
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.dsbOffsetTranslationX = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.dsbOffsetTranslationX.setGeometry(QtCore.QRect(190, 0, 81, 21))
        self.dsbOffsetTranslationX.setReadOnly(True)
        self.dsbOffsetTranslationX.setMinimum(-1000.0)
        self.dsbOffsetTranslationX.setMaximum(1000.0)
        self.dsbOffsetTranslationX.setSingleStep(0.1)
        self.dsbOffsetTranslationX.setObjectName("dsbOffsetTranslationX")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(0, 80, 191, 21))
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_19.setGeometry(QtCore.QRect(0, 0, 191, 21))
        self.lineEdit_19.setReadOnly(True)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_26.setGeometry(QtCore.QRect(0, 20, 191, 21))
        self.lineEdit_26.setReadOnly(True)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.dsbOffsetTranslationY = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.dsbOffsetTranslationY.setGeometry(QtCore.QRect(190, 20, 81, 21))
        self.dsbOffsetTranslationY.setReadOnly(True)
        self.dsbOffsetTranslationY.setMinimum(-1000.0)
        self.dsbOffsetTranslationY.setMaximum(1000.0)
        self.dsbOffsetTranslationY.setSingleStep(0.1)
        self.dsbOffsetTranslationY.setObjectName("dsbOffsetTranslationY")
        self.dsbOffsetRotation = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.dsbOffsetRotation.setGeometry(QtCore.QRect(190, 40, 81, 21))
        self.dsbOffsetRotation.setReadOnly(True)
        self.dsbOffsetRotation.setMinimum(-180.0)
        self.dsbOffsetRotation.setMaximum(180.0)
        self.dsbOffsetRotation.setSingleStep(0.1)
        self.dsbOffsetRotation.setObjectName("dsbOffsetRotation")
        self.dsbThickness = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.dsbThickness.setGeometry(QtCore.QRect(190, 80, 81, 21))
        self.dsbThickness.setReadOnly(True)
        self.dsbThickness.setMinimum(-1.0)
        self.dsbThickness.setMaximum(100.0)
        self.dsbThickness.setSingleStep(0.01)
        self.dsbThickness.setObjectName("dsbThickness")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_24.setGeometry(QtCore.QRect(0, 40, 191, 21))
        self.lineEdit_24.setReadOnly(True)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.dsbFlatness = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.dsbFlatness.setGeometry(QtCore.QRect(190, 60, 81, 21))
        self.dsbFlatness.setReadOnly(True)
        self.dsbFlatness.setMinimum(-10.0)
        self.dsbFlatness.setMaximum(10.0)
        self.dsbFlatness.setSingleStep(0.01)
        self.dsbFlatness.setObjectName("dsbFlatness")
        self.ckWirebondingCompleted = QtWidgets.QCheckBox(self.frame_2)
        self.ckWirebondingCompleted.setGeometry(QtCore.QRect(0, 100, 201, 23))
        self.ckWirebondingCompleted.setCheckable(False)
        self.ckWirebondingCompleted.setObjectName("ckWirebondingCompleted")
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(330, 100, 361, 181))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pbAddFiles = QtWidgets.QPushButton(self.frame_3)
        self.pbAddFiles.setGeometry(QtCore.QRect(130, 140, 101, 31))
        self.pbAddFiles.setObjectName("pbAddFiles")
        self.pbDeleteFile = QtWidgets.QPushButton(self.frame_3)
        self.pbDeleteFile.setGeometry(QtCore.QRect(230, 110, 131, 21))
        self.pbDeleteFile.setObjectName("pbDeleteFile")
        self.listFiles = QtWidgets.QListWidget(self.frame_3)
        self.listFiles.setGeometry(QtCore.QRect(0, 0, 361, 111))
        self.listFiles.setObjectName("listFiles")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_17.setGeometry(QtCore.QRect(1, 110, 231, 21))
        self.lineEdit_17.setReadOnly(True)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.frame_4 = QtWidgets.QFrame(Form)
        self.frame_4.setGeometry(QtCore.QRect(10, 10, 261, 111))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")
        self.pbSave = QtWidgets.QPushButton(self.frame_4)
        self.pbSave.setGeometry(QtCore.QRect(50, 60, 71, 21))
        self.pbSave.setObjectName("pbSave")
        self.pbEdit = QtWidgets.QPushButton(self.frame_4)
        self.pbEdit.setGeometry(QtCore.QRect(130, 30, 71, 21))
        self.pbEdit.setObjectName("pbEdit")
        self.pbCancel = QtWidgets.QPushButton(self.frame_4)
        self.pbCancel.setGeometry(QtCore.QRect(130, 60, 71, 21))
        self.pbCancel.setObjectName("pbCancel")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit.setGeometry(QtCore.QRect(1, 1, 151, 19))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.leID = QtWidgets.QLineEdit(self.frame_4)
        self.leID.setGeometry(QtCore.QRect(150, 0, 111, 20))
        self.leID.setText("")
        self.leID.setReadOnly(True)
        self.leID.setObjectName("leID")
        self.leStatus = QtWidgets.QLineEdit(self.frame_4)
        self.leStatus.setGeometry(QtCore.QRect(80, 90, 171, 20))
        self.leStatus.setText("")
        self.leStatus.setReadOnly(True)
        self.leStatus.setObjectName("leStatus")
        self.pbLoad = QtWidgets.QPushButton(self.frame_4)
        self.pbLoad.setGeometry(QtCore.QRect(50, 30, 71, 21))
        self.pbLoad.setObjectName("pbLoad")
        self.lineEdit_27 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_27.setGeometry(QtCore.QRect(10, 90, 71, 20))
        self.lineEdit_27.setReadOnly(True)
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(10, 140, 151, 16))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        self.cbResolution.setCurrentIndex(-1)
        self.cbShape.setCurrentIndex(-1)
        self.cbInspection.setCurrentIndex(-1)
        self.cbInsertUser.setCurrentIndex(-1)
        self.cbGrade.setCurrentIndex(-1)
        self.cbInstitution.setCurrentIndex(-1)
        self.cbInstitutionStepSensor.setCurrentIndex(-1)
        self.cbInstitutionStepPcb.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_8.setText(_translate("Form", "Note:  modules are automatically created upon completion of a pcb step."))
        self.label_7.setText(_translate("Form", "Data storage"))
        self.label_3.setText(_translate("Form", "Module qualification"))
        self.cbResolution.setItemText(0, _translate("Form", "HD"))
        self.cbResolution.setItemText(1, _translate("Form", "LD"))
        self.lineEdit_22.setText(_translate("Form", "Resolution"))
        self.cbShape.setItemText(0, _translate("Form", "Full"))
        self.cbShape.setItemText(1, _translate("Form", "Top"))
        self.cbShape.setItemText(2, _translate("Form", "Bottom"))
        self.cbShape.setItemText(3, _translate("Form", "Left"))
        self.cbShape.setItemText(4, _translate("Form", "Right"))
        self.cbShape.setItemText(5, _translate("Form", "Five"))
        self.cbShape.setItemText(6, _translate("Form", "Full+Three"))
        self.pbGoStepSensor.setText(_translate("Form", "Go to"))
        self.pbGoProtomodule.setText(_translate("Form", "Go to"))
        self.cbInspection.setItemText(0, _translate("Form", "pass"))
        self.cbInspection.setItemText(1, _translate("Form", "fail"))
        self.lineEdit_14.setText(_translate("Form", "location"))
        self.lineEdit_2.setText(_translate("Form", "Baseplate ID"))
        self.lineEdit_20.setText(_translate("Form", "Geometry"))
        self.pbGoPcb.setText(_translate("Form", "Go to"))
        self.pbGoBaseplate.setText(_translate("Form", "Go to"))
        self.lineEdit_3.setText(_translate("Form", "Sensor ID"))
        self.lineEdit_53.setToolTip(_translate("Form", "height difference between highest and lowers corners"))
        self.lineEdit_53.setText(_translate("Form", "User name"))
        self.lineEdit_11.setText(_translate("Form", "PCB placement step"))
        self.pbGoSensor.setText(_translate("Form", "Go to"))
        self.cbGrade.setItemText(0, _translate("Form", "A"))
        self.cbGrade.setItemText(1, _translate("Form", "B"))
        self.cbGrade.setItemText(2, _translate("Form", "C"))
        self.pbAddComment.setText(_translate("Form", "Add comment"))
        self.pbDeleteComment.setText(_translate("Form", "Delete selected"))
        self.lineEdit_13.setText(_translate("Form", "Sensor placement step"))
        self.lineEdit_23.setText(_translate("Form", "Protomodule ID"))
        self.lineEdit_52.setText(_translate("Form", "institution"))
        self.lineEdit_39.setText(_translate("Form", "Visual inspection"))
        self.lineEdit_4.setText(_translate("Form", "PCB ID"))
        self.lineEdit_16.setText(_translate("Form", "Comments"))
        self.cbInstitution.setItemText(0, _translate("Form", "CERN"))
        self.cbInstitution.setItemText(1, _translate("Form", "FNAL"))
        self.cbInstitution.setItemText(2, _translate("Form", "UCSB"))
        self.cbInstitution.setItemText(3, _translate("Form", "UMN"))
        self.cbInstitution.setItemText(4, _translate("Form", "HEPHY"))
        self.cbInstitution.setItemText(5, _translate("Form", "HPK"))
        self.lineEdit_21.setText(_translate("Form", "Grade"))
        self.pbGoStepPcb.setText(_translate("Form", "Go to"))
        self.cbInstitutionStepSensor.setItemText(0, _translate("Form", "CERN"))
        self.cbInstitutionStepSensor.setItemText(1, _translate("Form", "FNAL"))
        self.cbInstitutionStepSensor.setItemText(2, _translate("Form", "UCSB"))
        self.cbInstitutionStepSensor.setItemText(3, _translate("Form", "UMN"))
        self.cbInstitutionStepSensor.setItemText(4, _translate("Form", "HEPHY"))
        self.cbInstitutionStepSensor.setItemText(5, _translate("Form", "HPK"))
        self.cbInstitutionStepPcb.setItemText(0, _translate("Form", "CERN"))
        self.cbInstitutionStepPcb.setItemText(1, _translate("Form", "FNAL"))
        self.cbInstitutionStepPcb.setItemText(2, _translate("Form", "UCSB"))
        self.cbInstitutionStepPcb.setItemText(3, _translate("Form", "UMN"))
        self.cbInstitutionStepPcb.setItemText(4, _translate("Form", "HEPHY"))
        self.cbInstitutionStepPcb.setItemText(5, _translate("Form", "HPK"))
        self.lineEdit_6.setText(_translate("Form", "Flatness (mm)"))
        self.lineEdit_5.setText(_translate("Form", "Thickness (mm)"))
        self.lineEdit_19.setText(_translate("Form", "x translational offset (μm)"))
        self.lineEdit_26.setText(_translate("Form", "y translational offset (μm)"))
        self.lineEdit_24.setText(_translate("Form", "Rotational offset (°)"))
        self.ckWirebondingCompleted.setText(_translate("Form", "Wirebonding completed"))
        self.pbAddFiles.setText(_translate("Form", "Add files"))
        self.pbDeleteFile.setText(_translate("Form", "Delete selected"))
        self.listFiles.setToolTip(_translate("Form", "ID (date sent) (SENDER to RECEIVER)"))
        self.lineEdit_17.setText(_translate("Form", "Testing data files"))
        self.pbSave.setText(_translate("Form", "Save"))
        self.pbEdit.setText(_translate("Form", "Edit"))
        self.pbCancel.setText(_translate("Form", "Cancel"))
        self.lineEdit.setText(_translate("Form", "Module ID"))
        self.pbLoad.setText(_translate("Form", "Load"))
        self.lineEdit_27.setText(_translate("Form", "Status:"))
        self.label_6.setText(_translate("Form", "Standard information"))
