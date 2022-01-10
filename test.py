import os
import sys, pickle
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow

class SignIn(QDialog):
    def __init__(self):
        super(SignIn, self).__init__()
        loadUi("ui/signIn.ui", self)
        self.btnSignUp_In.setStyleSheet("QPushButton""{""border-radius: 10px; border: 1px solid rgb(0, 85, 127);""}"
                                        "QPushButton::hover""{" "font-weight:bold; ""}"
                                        "QPushButton::pressed" "{" "background-color: #CCE5FF; ""}" )
        self.btnSignUp_In.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSignIn_In.setStyleSheet("QPushButton""{""color: #fff; background-color: rgb(0, 85, 127);border-radius: 10px; border: 1px solid rgb(0, 85, 127);""}"
                                        "QPushButton::hover""{" "font-weight:bold; ""}"
                                        "QPushButton::pressed" "{" "background-color: #fff; color: rgb(0, 85, 127)""}" )
        self.btnSignIn_In.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.passwordFillIn.setEchoMode(QtWidgets.QLineEdit.Password)
        self.btnSignUp_In.clicked.connect(self.gotoSignUp)
        self.btnSignIn_In.clicked.connect(self.login)

    def gotoSignUp(self):
        signup = SignUp()
        widget.addWidget(signup)
        widget.removeWidget(self)
        widget.setCurrentWidget(signup)

    def login(self):
        username = self.useNameFill.text()
        password = self.passwordFillIn.text()

        if username == "admin":
            if password == "admin123":
                admin = Admin()
                # admin.setUpTable()
                widget.addWidget(admin)
                widget.setCurrentWidget(admin)
            else:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Incorrect password!")
                msg.setWindowTitle("Warning")
                msg.setWindowIcon(QtGui.QIcon('img/AppIcon.png'))
                msg.exec_()
        else:
            with open ('data/user.dat', 'rb') as userdata:
                for line in userdata:  
                    if username in line[0]:
                        if line[1] == password:
                            user = User()
                            # user.setTable(line[0])
                            widget.addWidget(user)
                            widget.setCurrentIndex(widget.currentIndex()+3)
                            break
                        else:
                            msg = QtWidgets.QMessageBox()
                            msg.setIcon(QtWidgets.QMessageBox.Warning)
                            msg.setText("Incorrect password!")
                            msg.setWindowTitle("Warning")
                            msg.setWindowIcon(QtGui.QIcon('img/AppIcon.png'))
                            msg.exec_()
                    else:
                        msg = QtWidgets.QMessageBox()
                        msg.setIcon(QtWidgets.QMessageBox.Warning)
                        msg.setText("Invalid account!")
                        msg.setWindowTitle("Warning")
                        msg.setWindowIcon(QtGui.QIcon('img/AppIcon.png'))
                        msg.exec_()
                    # except EOFError:
                    #     msg = QtWidgets.QMessageBox()
                    #     msg.setIcon(QtWidgets.QMessageBox.Warning)
                    #     msg.setText("Invalid account!")
                    #     msg.setWindowTitle("Warning")
                    #     msg.setWindowIcon(QtGui.QIcon('img/AppIcon.png'))
                    #     msg.exec_()
                    #     break
        
                                    
class SignUp(QDialog):
    def __init__(self):
        super(SignUp, self).__init__()
        loadUi("ui/signUp.ui", self)
        self.btnSignIn_Up.setStyleSheet("QPushButton""{""border-radius: 10px; border: 1px solid rgb(0, 85, 127);""}"
                                        "QPushButton::hover""{" "font-weight:bold; ""}"
                                        "QPushButton::pressed" "{" "background-color: #CCE5FF; ""}" )
        self.btnSignIn_Up.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSignUp_Up.setStyleSheet("QPushButton""{""color: #fff; background-color: rgb(0, 85, 127);border-radius: 10px; border: 1px solid rgb(0, 85, 127);""}"
                                        "QPushButton::hover""{" "font-weight:bold; ""}"
                                        "QPushButton::pressed" "{" "background-color: #fff; color: rgb(0, 85, 127)""}" )
        self.btnSignUp_Up.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.passwordFillUp.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verifyPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.btnSignIn_Up.clicked.connect(self.gotoSignIn)
        self.btnSignUp_Up.clicked.connect(self.createAccount)

    def gotoSignIn(self):
        goto_signIn = SignIn()
        widget.removeWidget(self)
        widget.addWidget(goto_signIn)
        widget.setCurrentWidget(goto_signIn)
    
    def createAccount(self):
        userName = self.useNameFill.text()
        password = self.passwordFillUp.text()
        verifyPass = self.verifyPassword.text()

        if os.path.getsize('data/user.dat') == 0:
            userdata = open('data/user.dat','wb')
            users = dict()
            if password != verifyPass:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Verify Password is incorrect!")
                msg.setWindowTitle("Warning")
                msg.setWindowIcon(QtGui.QIcon('img/AppIcon.png'))
                msg.exec_()

            elif password == verifyPass:
                users[userName]= password
                pickle.dump(users, userdata)
                userdata.close()
                signin = SignIn()
                widget.removeWidget(self)
                widget.addWidget(signin)
                widget.setCurrentWidget(signin)

        else: 
            userdata = open('data/user.dat','rb+')
            users = pickle.load(userdata)
            print(users)
          
            if userName in users.keys():
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Username existed!")
                msg.setWindowTitle("Warning")
                msg.setWindowIcon(QtGui.QIcon('img/AppIcon.png'))
                msg.exec_()
            else:
                if password != verifyPass:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setText("Verify Password is incorrect!")
                    msg.setWindowTitle("Warning")
                    msg.setWindowIcon(QtGui.QIcon('img/AppIcon.png'))
                    msg.exec_()

                elif password == verifyPass:
                    users[userName]= password
                    print(users)
                    userdata.seek(0)
                    userdata.truncate()
                    pickle.dump(users, userdata)
                    userdata.close()
                    signin = SignIn()
                    widget.removeWidget(self)
                    widget.addWidget(signin)
                    widget.setCurrentWidget(signin)
        ##########################################
        # neu file rong:
        #     wb
        #     if pass != verify: thong bao loi 
        #     else pickle.dump => signIn
        # if file khong rong:
        #     rb+
        #     seek(0)
        #     truncate()
        #     if username in file: account existed 
        #     else:
        #         if pass != verify: thong bao loi
        #         else: pickle.dump => signIn

class User(QDialog):
    def __init__(self):
        super(User, self).__init__()
        loadUi("ui/userInterface.ui", self)

        self.btnSignOut_user.setStyleSheet("QPushButton""{""color: #fff; background-color: rgb(0, 85, 127);border-radius: 10px; border: 1px solid rgb(0, 85, 127);""}"
                                        "QPushButton::hover""{" "font-weight:bold; ""}"
                                        "QPushButton::pressed" "{" "background-color: #fff; color: rgb(0, 85, 127)""}" )
        self.btnSignOut_user.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        self.btnSaveAll.setStyleSheet("QPushButton""{""border-radius: 10px; border: 1px solid rgb(0, 85, 127);""}"
                                        "QPushButton::hover""{" "font-weight:bold; ""}"
                                        "QPushButton::pressed" "{" "background-color: #CCE5FF; ""}" )
        self.btnSaveAll.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        self.btnAddTask.setStyleSheet("QPushButton""{""border-radius: 10px; border: 1px solid rgb(0, 85, 127);""}"
                                        "QPushButton::hover""{" "font-weight:bold; ""}"
                                        "QPushButton::pressed" "{" "background-color: #CCE5FF; ""}" )
        self.btnAddTask.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        self.btnEditTask.setStyleSheet("QPushButton""{""border-radius: 10px; border: 1px solid rgb(0, 85, 127);""}"
                                        "QPushButton::hover""{" "font-weight:bold; ""}"
                                        "QPushButton::pressed" "{" "background-color: #CCE5FF; ""}" )
        self.btnEditTask.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        self.btnDeleteTask.setStyleSheet("QPushButton""{""border-radius: 10px; border: 1px solid rgb(0, 85, 127);""}"
                                        "QPushButton::hover""{" "font-weight:bold; ""}"
                                        "QPushButton::pressed" "{" "background-color: #CCE5FF; ""}" )
        self.btnDeleteTask.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.listOfTask.setColumnWidth(0, 300)
        self.listOfTask.setColumnWidth(1, 190)
        self.listOfTask.setColumnWidth(2, 120)
        self.listOfTask.setColumnWidth(3, 90)
        self.btnAddTask.clicked.connect(self.addTask)
        self.btnDeleteTask.clicked.connect(self.deleteTask)
        self.btnSignOut_user.clicked.connect(self.gotoLogin)
    
    def setTable(self, username):
        with open ('data/user.dat', 'rb') as userdata:
            while True:
                row = pickle.load(userdata)
                    # if row[0] == username:
                    #     # set table

    def addTask(self):
        self.listOfTask.insertRow(self.listOfTask.rowCount())

        # create checkbox
        for row in range(self.listOfTask.rowCount()):
            chkBoxItem = QtWidgets.QTableWidgetItem("Done")
            chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
            self.listOfTask.setItem(row, 3, chkBoxItem)
            
    def deleteTask(self):
        if self.listOfTask.rowCount()>0:
            currentRow = self.listOfTask.currentRow()
            self.listOfTask.removeRow(currentRow)
    
    def gotoLogin(self):
        signIn = SignIn()
        widget.removeWidget(self)
        widget.addWidget(signIn)
        widget.setCurrentWidget(signIn)

class Admin(QDialog):
    def __init__(self):
        super(Admin, self).__init__()
        loadUi("ui/adminInterface.ui", self)
        self.btnsignOutAdmin.setStyleSheet("QPushButton""{""color: #fff; background-color: rgb(0, 85, 127);border-radius: 10px; border: 1px solid rgb(0, 85, 127);""}"
                                        "QPushButton::hover""{" "font-weight:bold; ""}"
                                        "QPushButton::pressed" "{" "background-color: #fff; color: rgb(0, 85, 127)""}" )
        self.btnsignOutAdmin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.btnaddUser.setStyleSheet("QPushButton""{""border-radius: 10px; border: 1px solid rgb(0, 85, 127);""}"
                                        "QPushButton::hover""{" "font-weight:bold; ""}"
                                        "QPushButton::pressed" "{" "background-color: #CCE5FF; ""}" )
        self.btnaddUser.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        self.btneditUser.setStyleSheet("QPushButton""{""border-radius: 10px; border: 1px solid rgb(0, 85, 127);""}"
                                        "QPushButton::hover""{" "font-weight:bold; ""}"
                                        "QPushButton::pressed" "{" "background-color: #CCE5FF; ""}" )
        self.btneditUser.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        self.btndeleteUser.setStyleSheet("QPushButton""{""border-radius: 10px; border: 1px solid rgb(0, 85, 127);""}"
                                        "QPushButton::hover""{" "font-weight:bold; ""}"
                                        "QPushButton::pressed" "{" "background-color: #CCE5FF; ""}" )
        self.btndeleteUser.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.listOfUser.setColumnWidth(0, 720)
        self.listOfUser.setColumnWidth(1, 650)
        self.btnaddUser.clicked.connect(self.addUser)
        self.btndeleteUser.clicked.connect(self.deleteUser)
        self.btnsignOutAdmin.clicked.connect(self.logout)
        self.setUpTable()

    def setUpTable(self):
        fileUser = open ('data/user.dat', 'rb')
        users = pickle.load(fileUser)
        row = 0
        for user in users.keys():
            username = QtWidgets.QTableWidgetItem(user)
            password = QtWidgets.QTableWidgetItem(users[user])
            self.listOfUser.insertRow(self.listOfUser.rowCount())
            self.listOfUser.setItem(row, 0, username)
            self.listOfUser.setItem(row, 1, password)
            row += 1
        fileUser.close()


    def addUser(self):
        self.listOfUser.insertRow(self.listOfUser.rowCount())

    def deleteUser(self):
        if self.listOfUser.rowCount()>0:
            currentRow = self.listOfUser.currentRow()
            self.listOfUser.removeRow(currentRow)
    def logout(self):
        signIn = SignIn()
        widget.removeWidget(self)
        widget.addWidget(signIn)
        widget.setCurrentWidget(signIn)
        

#main
app = QApplication(sys.argv)
signIn = SignIn()
widget = QtWidgets.QStackedWidget()
widget.setWindowTitle('KATodoList')
widget.setWindowIcon(QtGui.QIcon('img/AppIcon.png'))
widget.addWidget(signIn)
widget.setFixedHeight(920)
widget.setFixedWidth(1620)
widget.show()
sys.exit(app.exec_())
