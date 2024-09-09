from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QPixmap, QCursor
from PyQt5.QtCore import QSize, Qt
from login import Login
from watch_win import Soat

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1900,1000)
        self.setWindowTitle("Apple")
        self.setWindowIcon(QIcon('images/log.png'))
        self.v_main_lay = QVBoxLayout()
        self.h_saidbar_lay = QHBoxLayout()
        self.h_bottom_lay = QHBoxLayout()
        self.v_list_lay = QVBoxLayout()

        self.v_btn1_lay = QVBoxLayout()
        self.v_btn2_lay = QVBoxLayout()
        self.v_btn3_lay = QVBoxLayout()

        self.log_btn = QPushButton(clicked=self.apple)
        self.log_btn.setIcon(QIcon("images/apple.png"))
        self.log_btn.setIconSize(QSize(30,30))
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
        self.login_btn = QPushButton(clicked=self.login)
        self.login_btn.setIcon(QIcon("images/login.png"))
        self.login_btn.setIconSize(QSize(30,30))

        self.log_btn1 = QPushButton("Apple", clicked=self.apple)
        self.store_btn1 = QPushButton("Store", clicked=self.store)
        self.mac_btn1 = QPushButton("Mac", clicked=self.mac)
        self.ipad_btn1 = QPushButton("iPad", clicked=self.ipad)
        self.iphone_btn1 = QPushButton("iPhone", clicked=self.iphone)
        self.watch_btn1 = QPushButton("Watch", clicked=self.watch)
        self.vision_btn1 = QPushButton("Vision", clicked=self.vision)
        self.air_btn1 = QPushButton("AirPods", clicked=self.air)
        self.tvhome_btn1 = QPushButton("Tv & Home", clicked=self.tvhome)
        self.enter_btn1 = QPushButton("Entertainment", clicked=self.enter)
        self.acces_btn1 = QPushButton("Accessories", clicked=self.acces)
        self.login_btn1 = QPushButton("Login", clicked=self.login)

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
            i.setStyleSheet("""QPushButton{color:rgb(255,255,255);font-family:SF Pro Display, SF Pro Icons, Helvetica Neue, Helvetica, Arial, sans-serif;
                            font-size:15px;font-style:normal;border-radius:10px;margin-bottom: 4px; border:none}
                            QPushButton:hover{
                            background:rgb(238,242,246);color:rgb(51,51,51)}
                            """)
            i.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            i.setFixedWidth(90)
        for i in self.lst1:
            i.setStyleSheet("""QPushButton{color:rgb(255,255,255);font-size:SF Pro Display, SF Pro Icons, Helvetica Neue, Helvetica, Arial, sans-serif;
                            font-size:15px;font-style:normal; border-radius:100px ;margin-bottom:4px; border:none}
                            QPushButton:hover{
                            background:rgb(238,242,246);color:rgb(51,51,51)}
                            """)
            i.setFixedWidth(90)
        self.log_btn.setStyleSheet("QPushButton{border-radius:10px}")
        self.log_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.login_btn.setStyleSheet("QPushButton{border-radius:10px}")
        self.login_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.qlist = QListWidget()
        self.qlist.itemClicked.connect(self.item_clicked)
        self.qlist.setFrameShape(QListWidget.NoFrame)
        skrol = self.qlist.verticalScrollBar()
        skrol.setSingleStep(1)
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

        self.image = QListWidgetItem()
        self.image.setIcon(QIcon("images/rasm1.png"))
        self.image1 = QListWidgetItem()
        self.image1.setIcon(QIcon("images/rasm2.png"))
        self.image2 = QListWidgetItem()
        self.image2.setIcon(QIcon("images/rasm3.png"))
        self.image3 = QListWidgetItem()
        self.image3.setIcon(QIcon("images/rasm4.png"))
        self.image4 = QListWidgetItem()
        self.image4.setIcon(QIcon("images/rasm5.png"))
        self.image5 = QListWidgetItem()
        self.image5.setIcon(QIcon("images/rasm6.png"))
        self.qlist.addItem(self.image)
        self.qlist.addItem(self.image1)
        self.qlist.addItem(self.image2)
        self.qlist.addItem(self.image3)
        self.qlist.addItem(self.image4)
        self.qlist.addItem(self.image5)
        self.qlist.setIconSize(QSize(1840,800))
        
    def item_clicked(self,item):
        if item == self.image:
            self.store()
        elif item == self.image1:
            self.mac()
        elif item == self.image2:
            self.iphone()
        elif item == self.image3:
            self.tvhome()
        elif item == self.image4:
            self.tvhome()

    def apple(self):
        self.close()
        self.__init__()
        self.show()

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
        self.login_window = Login()
        self.login_window.show()


if __name__=="__main__":
    app = QApplication([])
    win = MyWindow()
    win.show()
    app.exec_()
