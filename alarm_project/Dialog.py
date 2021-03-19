# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addAlarmDialog(object):
    def setupUi(self, addAlarmDialog):
        addAlarmDialog.setObjectName("addAlarmDialog")
        addAlarmDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        addAlarmDialog.resize(288, 175)
        self.buttonBox = QtWidgets.QDialogButtonBox(addAlarmDialog)
        self.buttonBox.setGeometry(QtCore.QRect(60, 140, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(addAlarmDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 271, 131))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.form = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.form.setContentsMargins(0, 0, 0, 0)
        self.form.setObjectName("form")
        self.lbl_alarmTitle = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_alarmTitle.setObjectName("lbl_alarmTitle")
        self.form.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_alarmTitle)
        self.le_alarmTitle = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.le_alarmTitle.setObjectName("le_alarmTitle")
        self.form.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.le_alarmTitle)
        self.lbl_time = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_time.setObjectName("lbl_time")
        self.form.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_time)
        self.te_time = QtWidgets.QTimeEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.te_time.sizePolicy().hasHeightForWidth())
        self.te_time.setSizePolicy(sizePolicy)
        self.te_time.setObjectName("te_time")
        self.form.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.te_time)
        self.lbl_sound = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_sound.setObjectName("lbl_sound")
        self.form.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_sound)

        self.retranslateUi(addAlarmDialog)
        self.buttonBox.accepted.connect(addAlarmDialog.accept)
        self.buttonBox.rejected.connect(addAlarmDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(addAlarmDialog)

    def retranslateUi(self, addAlarmDialog):
        _translate = QtCore.QCoreApplication.translate
        addAlarmDialog.setWindowTitle(_translate("addAlarmDialog", "Add new alarm"))
        self.lbl_alarmTitle.setText(_translate("addAlarmDialog", "Alarm title:"))
        self.lbl_time.setText(_translate("addAlarmDialog", "Set time:"))
        self.lbl_sound.setText(_translate("addAlarmDialog", "Set sound:"))
