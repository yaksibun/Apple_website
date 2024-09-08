from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QPixmap, QCursor
from PyQt5.QtCore import QSize, Qt
import json

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1900,1000)
        self.setWindowTitle("Apple")
        self.setWindowIcon(QIcon('images/log.png'))
        self.setStyleSheet("background:rgb(29,29,31)")
        
        self.v_main_lay = QVBoxLayout()
        self.h_main2_lay = QHBoxLayout()
        self.v_btns_lay = QVBoxLayout()
        self.h_2btn_lay = QHBoxLayout()
        self.h_lbl_lay = QHBoxLayout()

        self.lbl = QLabel("Sign in for faster checkout.")
        self.lbl.setStyleSheet("font-family:Helvetica, Arial, sans-serif;color:white;font-size:60px;font-style:normal")
        self.lbl.setFixedHeight(200)
        self.lbl.move(100,200)

        self.lbl1 = QLabel("Sign in to Apple Store")
        self.lbl1.setStyleSheet("font-family:Helvetica, Arial, sans-serif;color:white;font-size:30px;font-style:normal")
        self.lbl1.setAlignment(Qt.AlignCenter)

        self.lblerror = QLabel("")
        self.lblerror.setStyleSheet("font-family:Helvetica, Arial, sans-serif;color:white;font-size:15px;font-style:normal")
        self.lblerror.setAlignment(Qt.AlignCenter)

        self.edit_email = QLineEdit()
        self.edit_email.setPlaceholderText("Enter your email")
        self.edit_email.setStyleSheet("color:white;margin-top:40px;font-size:18px")
        self.edit_email.setFixedHeight(80)

        self.edit_num = QLineEdit()
        self.edit_num.setPlaceholderText("Enter your number")
        self.edit_num.setStyleSheet("color:white;font-size:18px")
        self.edit_num.setFixedHeight(40)
        self.edit_num.hide()

        self.edit_parol = QLineEdit()
        self.edit_parol.setPlaceholderText("Password")
        self.edit_parol.setStyleSheet("color:white;font-size:18px")
        self.edit_parol.setFixedHeight(40)
        self.edit_parol.setEchoMode(QLineEdit.Password)

        self.log_btn = QPushButton("Register", clicked=self.register)
        self.log_btn.setStyleSheet("""QPushButton{color:white;font-family:SF Pro Display, SF Pro Icons, Helvetica Neue, Helvetica, Arial, sans-serif;
                            font-size:15px;font-style:normal;border-radius:10px;margin-bottom: 4px; border:none}
                            QPushButton:hover{
                            background:orange;color:rgb(51,51,51)}
                            """)
        self.log_btn.setFixedSize(150,30)
        self.log_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.log_btn2 = QPushButton("Register", clicked=self.register2)
        self.log_btn2.setStyleSheet("""QPushButton{color:white;font-family:SF Pro Display, SF Pro Icons, Helvetica Neue, Helvetica, Arial, sans-serif;
                            font-size:15px;font-style:normal;border-radius:10px;margin-bottom: 4px; border:none}
                            QPushButton:hover{
                            background:orange;color:rgb(51,51,51)}
                            """)
        self.log_btn2.setFixedSize(150,30)
        self.log_btn2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.log_btn2.hide()
        
        self.reg_btn = QPushButton("Login", clicked=self.login)
        self.reg_btn.setStyleSheet("""QPushButton{color:white;font-family:SF Pro Display, SF Pro Icons, Helvetica Neue, Helvetica, Arial, sans-serif;
                            font-size:15px;font-style:normal;border-radius:10px;margin-bottom: 4px; border:none}
                            QPushButton:hover{
                            background:orange;color:rgb(51,51,51)}
                            """)
        self.reg_btn.setFixedSize(150,30)
        self.reg_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.h_2btn_lay.addWidget(self.log_btn)
        self.h_2btn_lay.addWidget(self.log_btn2)
        self.h_2btn_lay.addWidget(self.reg_btn)

        self.check = QCheckBox("Remember me")
        self.check.setStyleSheet("color:white;font-family:Helvetica, Arial, sans-serif;font-size:20px")
        self.v_btns_lay.addWidget(self.lbl1)
        self.v_btns_lay.addWidget(self.lblerror)
        self.v_btns_lay.addWidget(self.edit_email)
        self.v_btns_lay.addWidget(self.edit_num)
        self.v_btns_lay.addWidget(self.edit_parol)
        self.v_btns_lay.addLayout(self.h_2btn_lay)
        self.v_btns_lay.addWidget(self.check)
        self.v_btns_lay.addStretch()

        self.h_main2_lay.addStretch()        
        self.h_main2_lay.addLayout(self.v_btns_lay)
        self.h_main2_lay.addStretch()

        self.v_main_lay.addWidget(self.lbl)
        self.v_main_lay.addLayout(self.h_main2_lay)
        self.setLayout(self.v_main_lay)

    def login(self):
        with open("users.json") as f:
            self.dictf = json.load(f)
        if self.dictf["email"] == self.edit_email.text() and self.dictf["password"] == self.edit_parol.text():
            self.hide()
        else:
            self.lblerror.setText("Your password or email address is incorrect")
            self.lblerror.setStyleSheet("font-family:Helvetica, Arial, sans-serif;color:white;font-size:20px;font-style:normal;color:red")



    def register(self):
        self.edit_num.show()
        self.log_btn2.show()
        self.log_btn.hide()

    def register2(self):
        email = self.edit_email.text()
        num = self.edit_num.text()
        parol = self.edit_parol.text()
        self.dict = {}
        try:
            if "@gmail.com" in email or "@email.com":
                if len(num) == 13 and num[0] == "+":
                    self.dict["email"] = email
                    self.dict["number"] = num
                    self.dict["password"] = parol
                    self.lblerror.setText("")
                    with open("users.json","w") as f:
                        json.dump(self.dict,f)
                    self.edit_num.hide()
                    self.log_btn2.hide()
                    self.log_btn.show()
                else:
                    self.lblerror.setText("Your password or email address is incorrect")
                    self.lblerror.setStyleSheet("font-family:Helvetica, Arial, sans-serif;color:red;font-size:20px;font-style:normal")
            else:
                self.lblerror.setText("Your password or email address is incorrect")
                self.lblerror.setStyleSheet("font-family:Helvetica, Arial, sans-serif;color:red;font-size:20px;font-style:normal")

        except:
            self.lblerror.setText("Fill in the information")
            self.lblerror.setStyleSheet("font-family:Helvetica, Arial, sans-serif;color:white;font-size:20px;font-style:normal")



if __name__ == "__main__":
    app = QApplication([])
    win = Login()
    win.show()
    app.exec_()