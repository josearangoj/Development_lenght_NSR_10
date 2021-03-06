# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(631, 608)
        self.btn_exit = QtWidgets.QPushButton(Form)
        self.btn_exit.setGeometry(QtCore.QRect(500, 390, 93, 28))
        self.btn_exit.setObjectName("btn_exit")
        self.btn_calculate = QtWidgets.QPushButton(Form)
        self.btn_calculate.setGeometry(QtCore.QRect(500, 330, 93, 28))
        self.btn_calculate.setObjectName("btn_calculate")
        self.data_entries = QtWidgets.QGroupBox(Form)
        self.data_entries.setGeometry(QtCore.QRect(20, 10, 601, 301))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(26, 59, 12))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 59, 12))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.data_entries.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Monospac821 BT")
        self.data_entries.setFont(font)
        self.data_entries.setFlat(False)
        self.data_entries.setObjectName("data_entries")
        self.gridLayoutWidget = QtWidgets.QWidget(self.data_entries)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 20, 561, 211))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.txt_sep = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_sep.setObjectName("txt_sep")
        self.gridLayout.addWidget(self.txt_sep, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)
        self.txt_fy = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_fy.setObjectName("txt_fy")
        self.gridLayout.addWidget(self.txt_fy, 1, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 4, 2, 1, 1)
        self.txt_fc = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_fc.setObjectName("txt_fc")
        self.gridLayout.addWidget(self.txt_fc, 0, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.txt_clear_dist = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_clear_dist.setObjectName("txt_clear_dist")
        self.gridLayout.addWidget(self.txt_clear_dist, 3, 1, 1, 1)
        self.txt_h_rebar = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_h_rebar.setObjectName("txt_h_rebar")
        self.gridLayout.addWidget(self.txt_h_rebar, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 2, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.data_entries)
        self.groupBox_3.setGeometry(QtCore.QRect(460, 240, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.radBtn_epoxic_yes = QtWidgets.QRadioButton(self.groupBox_3)
        self.radBtn_epoxic_yes.setGeometry(QtCore.QRect(10, 20, 95, 20))
        self.radBtn_epoxic_yes.setObjectName("radBtn_epoxic_yes")
        self.radBtn_epoxic_no = QtWidgets.QRadioButton(self.groupBox_3)
        self.radBtn_epoxic_no.setGeometry(QtCore.QRect(70, 20, 51, 20))
        self.radBtn_epoxic_no.setChecked(True)
        self.radBtn_epoxic_no.setObjectName("radBtn_epoxic_no")
        self.groupBox_2 = QtWidgets.QGroupBox(self.data_entries)
        self.groupBox_2.setGeometry(QtCore.QRect(180, 240, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.radBtn_confined_yes = QtWidgets.QRadioButton(self.groupBox_2)
        self.radBtn_confined_yes.setGeometry(QtCore.QRect(40, 20, 95, 20))
        self.radBtn_confined_yes.setObjectName("radBtn_confined_yes")
        self.radBtn_confined_no = QtWidgets.QRadioButton(self.groupBox_2)
        self.radBtn_confined_no.setGeometry(QtCore.QRect(120, 20, 51, 20))
        self.radBtn_confined_no.setChecked(True)
        self.radBtn_confined_no.setObjectName("radBtn_confined_no")
        self.groupBox = QtWidgets.QGroupBox(self.data_entries)
        self.groupBox.setGeometry(QtCore.QRect(30, 240, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.radBtn_liwe_yes = QtWidgets.QRadioButton(self.groupBox)
        self.radBtn_liwe_yes.setEnabled(True)
        self.radBtn_liwe_yes.setGeometry(QtCore.QRect(0, 20, 95, 20))
        self.radBtn_liwe_yes.setMouseTracking(True)
        self.radBtn_liwe_yes.setObjectName("radBtn_liwe_yes")
        self.radBtn_liwe_no = QtWidgets.QRadioButton(self.groupBox)
        self.radBtn_liwe_no.setGeometry(QtCore.QRect(60, 20, 51, 20))
        self.radBtn_liwe_no.setChecked(True)
        self.radBtn_liwe_no.setObjectName("radBtn_liwe_no")
        self.groupBox_Results = QtWidgets.QGroupBox(Form)
        self.groupBox_Results.setGeometry(QtCore.QRect(20, 310, 451, 291))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(26, 59, 12))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 59, 12))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.groupBox_Results.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Monospac821 BT")
        self.groupBox_Results.setFont(font)
        self.groupBox_Results.setObjectName("groupBox_Results")
        self.result_table = QtWidgets.QTextEdit(self.groupBox_Results)
        self.result_table.setGeometry(QtCore.QRect(20, 20, 411, 261))
        font = QtGui.QFont()
        font.setFamily("Monospac821 BT")
        font.setPointSize(9)
        self.result_table.setFont(font)
        self.result_table.setLineWidth(3)
        self.result_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.result_table.setObjectName("result_table")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(500, 360, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.btn_exit.raise_()
        self.btn_calculate.raise_()
        self.groupBox_Results.raise_()
        self.pushButton.raise_()
        self.data_entries.raise_()

        self.retranslateUi(Form)
        self.btn_exit.clicked.connect(Form.close)
        self.pushButton.clicked.connect(self.result_table.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Development lenghts - NSR-10"))
        self.btn_exit.setText(_translate("Form", "Exit"))
        self.btn_calculate.setText(_translate("Form", "Calculate"))
        self.data_entries.setTitle(_translate("Form", "Data Entries"))
        self.txt_sep.setText(_translate("Form", "0.2"))
        self.label_7.setText(_translate("Form", "Specified yield strength for rebar reinforcement [MPa]"))
        self.txt_fy.setText(_translate("Form", "420"))
        self.label_16.setText(_translate("Form", "Spacing between upside and downside rebars [m]"))
        self.txt_fc.setText(_translate("Form", "21"))
        self.label_13.setText(_translate("Form", "h\' ="))
        self.label_2.setText(_translate("Form", "f\'c ="))
        self.label_6.setText(_translate("Form", "Concrete Compressive Strength [MPa]"))
        self.txt_clear_dist.setText(_translate("Form", "0.04"))
        self.txt_h_rebar.setText(_translate("Form", "0.30"))
        self.label_3.setText(_translate("Form", "fy ="))
        self.label_4.setText(_translate("Form", "r ="))
        self.label.setText(_translate("Form", "s ="))
        self.label_8.setText(_translate("Form", "Spacing of the rebars [m]"))
        self.label_9.setText(_translate("Form", "Clear cover to face of bar [m]"))
        self.groupBox_3.setTitle(_translate("Form", "Epoxic coated bars"))
        self.radBtn_epoxic_yes.setText(_translate("Form", "Yes"))
        self.radBtn_epoxic_no.setText(_translate("Form", "No"))
        self.groupBox_2.setTitle(_translate("Form", "Confinement bars along development length"))
        self.radBtn_confined_yes.setText(_translate("Form", "Yes"))
        self.radBtn_confined_no.setText(_translate("Form", "No"))
        self.groupBox.setTitle(_translate("Form", "Lightweight concrete"))
        self.radBtn_liwe_yes.setText(_translate("Form", "Yes"))
        self.radBtn_liwe_no.setText(_translate("Form", "No"))
        self.groupBox_Results.setTitle(_translate("Form", "Results"))
        self.pushButton.setText(_translate("Form", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
