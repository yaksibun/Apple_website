from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1900,1000)
        self.setWindowTitle("Apple")
        self.v_main_lay = QVBoxLayout()
        self.h_saidbar_lay = QHBoxLayout()
        self.h_bottom_lay = QHBoxLayout()
        self.v_list_lay = QVBoxLayout()

        self.v_btn1_lay = QVBoxLayout()
        self.v_btn2_lay = QVBoxLayout()
        self.v_btn3_lay = QVBoxLayout()

        self.log_btn = QPushButton("Apple" ,clicked=self.apple)
        self.store_btn = QPushButton("Store" ,clicked=self.store)
        self.mac_btn = QPushButton("Mac" ,clicked=self.mac)
        self.ipad_btn = QPushButton("iPad" ,clicked=self.ipad)
        self.iphone_btn = QPushButton("iPhone" ,clicked=self.iphone)
        self.watch_btn = QPushButton("Watch" ,clicked=self.watch)
        self.vision_btn = QPushButton("Vision" ,clicked=self.vision)
        self.air_btn = QPushButton("AirPods" ,clicked=self.air)
        self.tvhome_btn = QPushButton("Tv & Home" ,clicked=self.tvhome)
        self.enter_btn = QPushButton("Entertainment" ,clicked=self.enter)
        self.acces_btn = QPushButton("Accessories" ,clicked=self.acces)
        self.login_btn = QPushButton("Login" ,clicked=self.login)

        self.log_btn1 = QPushButton("Apple")
        self.store_btn1 = QPushButton("Store")
        self.mac_btn1 = QPushButton("Mac")
        self.ipad_btn1 = QPushButton("iPad")
        self.iphone_btn1 = QPushButton("iPhone")
        self.watch_btn1 = QPushButton("Watch")
        self.vision_btn1 = QPushButton("Vision")
        self.air_btn1 = QPushButton("AirPods")
        self.tvhome_btn1 = QPushButton("Tv & Home")
        self.enter_btn1 = QPushButton("Entertainment")
        self.acces_btn1 = QPushButton("Accessories")
        self.login_btn1 = QPushButton("Login")

        self.bt_lbl1 = QLabel("Shop and Learn")
        self.bt_lbl2 = QLabel("Apple Store")
        self.bt_lbl3 = QLabel("For Bussines")
        self.bt_lst = [self.bt_lbl1,self.bt_lbl2,self.bt_lbl3]
        for i in self.bt_lst:
            i.setStyleSheet("""color:black;font-size:SF Pro Display, SF Pro Icons, Helvetica Neue, Helvetica, Arial, sans-serif;
                            font-size:15px;font-style:normal; background:white
                            """)

        self.lst = [self.log_btn,self.store_btn,self.mac_btn,self.ipad_btn,self.iphone_btn,
                    self.watch_btn,self.vision_btn,self.air_btn,self.tvhome_btn,self.enter_btn,self.acces_btn,self.login_btn]
        self.lst1 = [self.log_btn1,self.store_btn1,self.mac_btn1,self.ipad_btn1,self.iphone_btn1,
                    self.watch_btn1,self.vision_btn1,self.air_btn1,self.tvhome_btn1,self.enter_btn1,self.acces_btn1,self.login_btn1]
        for i in self.lst:
            self.h_saidbar_lay.addWidget(i)
            i.setStyleSheet("""QPushButton{color:rgb(255,255,255);font-size:SF Pro Display, SF Pro Icons, Helvetica Neue, Helvetica, Arial, sans-serif;
                            font-size:15px;font-style:normal;border-radius:10px;margin-bottom: 4px; border:none}
                            QPushButton:hover{
                            background:rgb(238,242,246);color:rgb(51,51,51)}
                            """)
            i.setFixedWidth(90)
        for i in self.lst1:
            i.setStyleSheet("""QPushButton{color:rgb(255,255,255);font-size:SF Pro Display, SF Pro Icons, Helvetica Neue, Helvetica, Arial, sans-serif;
                            font-size:15px;font-style:normal; border-radius:100px ;margin-bottom:4px; border:none}
                            QPushButton:hover{
                            background:rgb(238,242,246);color:rgb(51,51,51)}
                            """)
            i.setFixedWidth(90)
            

        self.qlist = QListWidget()
        self.v_list_lay.addWidget(self.qlist)

        self.v_btn1_lay.addWidget(self.bt_lbl1)
        self.v_btn1_lay.addWidget(self.log_btn1)
        self.v_btn1_lay.addWidget(self.store_btn1)
        self.v_btn1_lay.addWidget(self.mac_btn1)
        self.v_btn1_lay.addWidget(self.ipad_btn1)

        self.v_btn2_lay.addWidget(self.bt_lbl2)
        self.v_btn2_lay.addWidget(self.iphone_btn1)
        self.v_btn2_lay.addWidget(self.watch_btn1)
        self.v_btn2_lay.addWidget(self.vision_btn1)
        self.v_btn2_lay.addWidget(self.air_btn1)

        self.v_btn3_lay.addWidget(self.bt_lbl3)
        self.v_btn3_lay.addWidget(self.tvhome_btn1)
        self.v_btn3_lay.addWidget(self.enter_btn1)
        self.v_btn3_lay.addWidget(self.acces_btn1)
        self.v_btn3_lay.addWidget(self.login_btn1)

        self.h_bottom_lay.addLayout(self.v_btn1_lay)
        self.h_bottom_lay.addLayout(self.v_btn2_lay)
        self.h_bottom_lay.addLayout(self.v_btn3_lay)

        self.v_main_lay.addLayout(self.h_saidbar_lay)
        self.v_main_lay.addLayout(self.v_list_lay)
        self.v_main_lay.addLayout(self.h_bottom_lay)

        self.setLayout(self.v_main_lay)
        self.setStyleSheet("background:rgb(29,29,31)")


    def apple(self):
        pass

    def store(self):
        pass

    def mac(self):
        pass

    def ipad(self):
        pass

    def iphone(self):
        pass

    def watch(self):
        pass

    def vision(self):
        pass

    def air(self):
        pass

    def tvhome(self):
        pass

    def enter(self):
        pass

    def acces(self):
        pass

    def login(self):
        pass


if __name__=="__main__":
    app = QApplication([])
    win = MyWindow()
    win.show()
    app.exec_()
