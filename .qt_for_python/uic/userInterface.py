# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\hoctap\PROJECT1\KATodoList\ui\userInterface.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_userInterface(object):
    def setupUi(self, userInterface):
        userInterface.setObjectName("userInterface")
        userInterface.resize(1620, 920)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("e:\\hoctap\\PROJECT1\\KATodoList\\ui\\img/AppIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        userInterface.setWindowIcon(icon)
        userInterface.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listOfTask = QtWidgets.QTableWidget(userInterface)
        self.listOfTask.setGeometry(QtCore.QRect(100, 200, 1420, 580))
        self.listOfTask.setMouseTracking(False)
        self.listOfTask.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.listOfTask.setObjectName("listOfTask")
        self.listOfTask.setColumnCount(5)
        self.listOfTask.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.listOfTask.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.listOfTask.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.listOfTask.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.listOfTask.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.listOfTask.setHorizontalHeaderItem(4, item)
        self.btnSignOut_user = QtWidgets.QPushButton(userInterface)
        self.btnSignOut_user.setGeometry(QtCore.QRect(1420, 20, 100, 40))
        self.btnSignOut_user.setStyleSheet("\n"
"background-color: rgb(210, 212, 255);\n"
"font: 63 9pt \"Yu Gothic UI Semibold\";")
        self.btnSignOut_user.setObjectName("btnSignOut_user")
        self.toDoList = QtWidgets.QLabel(userInterface)
        self.toDoList.setGeometry(QtCore.QRect(670, 50, 300, 100))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.toDoList.setFont(font)
        self.toDoList.setObjectName("toDoList")
        self.btnAddTask = QtWidgets.QPushButton(userInterface)
        self.btnAddTask.setGeometry(QtCore.QRect(1100, 800, 120, 40))
        self.btnAddTask.setStyleSheet("background-color: rgb(210, 212, 255);\n"
"font: 63 9pt \"Yu Gothic UI Semibold\";")
        self.btnAddTask.setObjectName("btnAddTask")
        self.btnDeleteTask = QtWidgets.QPushButton(userInterface)
        self.btnDeleteTask.setGeometry(QtCore.QRect(1250, 800, 120, 40))
        self.btnDeleteTask.setStyleSheet("background-color: rgb(210, 212, 255);\n"
"font: 63 9pt \"Yu Gothic UI Semibold\";")
        self.btnDeleteTask.setObjectName("btnDeleteTask")
        self.btnSaveAll = QtWidgets.QPushButton(userInterface)
        self.btnSaveAll.setGeometry(QtCore.QRect(1400, 800, 120, 40))
        self.btnSaveAll.setStyleSheet("background-color: rgb(210, 212, 255);\n"
"font: 63 9pt \"Yu Gothic UI Semibold\";")
        self.btnSaveAll.setObjectName("btnSaveAll")

        self.retranslateUi(userInterface)
        QtCore.QMetaObject.connectSlotsByName(userInterface)

    def retranslateUi(self, userInterface):
        _translate = QtCore.QCoreApplication.translate
        userInterface.setWindowTitle(_translate("userInterface", "KATodoList"))
        item = self.listOfTask.horizontalHeaderItem(0)
        item.setText(_translate("userInterface", "Task"))
        item = self.listOfTask.horizontalHeaderItem(1)
        item.setText(_translate("userInterface", "Address"))
        item = self.listOfTask.horizontalHeaderItem(2)
        item.setText(_translate("userInterface", "Start"))
        item = self.listOfTask.horizontalHeaderItem(3)
        item.setText(_translate("userInterface", "End"))
        item = self.listOfTask.horizontalHeaderItem(4)
        item.setText(_translate("userInterface", "Check"))
        self.btnSignOut_user.setText(_translate("userInterface", "Sign out"))
        self.toDoList.setText(_translate("userInterface", "<html><head/><body><p><span style=\" font-size:36pt;\">Todo list</span></p></body></html>"))
        self.btnAddTask.setText(_translate("userInterface", "Add Task"))
        self.btnDeleteTask.setText(_translate("userInterface", "Delete Task"))
        self.btnSaveAll.setText(_translate("userInterface", "Save all"))
