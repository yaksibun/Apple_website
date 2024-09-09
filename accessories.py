from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QWidget

class Accessories(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        
        self.setWindowTitle("Accessories")
        self.setFixedSize(1900, 1000)
        self.setStyleSheet("background-color:#fff")
        self.v_main_lay = QVBoxLayout()
        self.h_side_lay = QHBoxLayout()
        # self.h_side_lay.setStyleSheet("background-color:#f5f5f7;")
        self.combo_box = QComboBox()
        self.combo_box.setStyleSheet("""
                            QComboBox{background-color:#f5f5f7;
                            color:#000000;
                            font-size:SF Pro Text, SF Pro Icons, Helvetica Neue, Helvetica, Arial, sans-serif;
                            font-size:24px;
                            font-weight:600;
                            font-style:normal;
                            border-radius:10px;
                            margin-bottom: 4px; 
                            border:none}
                            QComboBox::drop-down{border:0px;}""")
        self.combo_box.addItems(["Browse all ∨","Home", "Mac", "iPad", "iPhone", "Watch", "TV & Home", "Entertainment", "Accessories", "Support", "Account"])
        
        # self.combo_box.currentText
        
        self.btn_sidebar = QPushButton("Accessories",clicked=self.apple)
                
        self.btn_sidebar.setStyleSheet("""
                            QPushButton{
                            color:#000000;
                            font-size:SF Pro Text, SF Pro Icons, Helvetica Neue, Helvetica, Arial, sans-serif;
                            font-size:24px;
                            font-weight:600;
                            font-style:normal;
                            border-radius:10px;
                            margin-bottom: 4px; 
                            border:none}
                            # QPushButton:hover{
                            # background:rgb(238,242,246);color:rgb(51,51,51)}
                            """)
        self.h_side_lay.addWidget(self.btn_sidebar)
        self.h_side_lay.addStretch()
        self.h_side_lay.addWidget(self.combo_box)
        
        self.qlst_main = QListWidget()
        self.qlst_main.setIconSize(QSize(1840, 800))
        self.qlst_main.setFrameShape(QListWidget.NoFrame)
        
        widget = QWidget()
        
        item = QListWidgetItem()
        item.setSizeHint(widget.sizeHint())
        self.qlst_main.addItem(item)
        self.qlst_main.setItemWidget(item, widget)
        
        self.image1 = QListWidgetItem()  
        self.image1.setIcon(QIcon("images/a_main.png")) 
        
        self.image2 = QListWidgetItem()
        self.image2.setIcon(QIcon("images/a_main2.png"))
        
        self.image3 = QListWidgetItem()
        self.image3.setIcon(QIcon("images/a_main3.png"))
        
        self.image3 = QListWidgetItem()
        self.image3.setIcon(QIcon("images/a_main3.png"))
        
        self.image4 = QListWidgetItem()
        self.image4.setIcon(QIcon("images/a_main4.png"))
        
        self.image5 = QListWidgetItem()
        self.image5.setIcon(QIcon("images/a_main5.png"))
        
        self.image6 = QListWidgetItem()
        self.image6.setIcon(QIcon("images/a_main6.png"))
        
        self.image7 = QListWidgetItem()
        self.image7.setIcon(QIcon("images/a_main7.png"))
        
        self.image8 = QListWidgetItem()
        self.image8.setIcon(QIcon("images/a_main8.png"))
        
        self.image9 = QListWidgetItem()
        self.image9.setIcon(QIcon("images/a_main9.png"))
        
        self.image10 = QListWidgetItem()
        self.image10.setIcon(QIcon("images/a_main10.png"))
        
        self.qlst_main.addItem(self.image1)
        self.qlst_main.addItem(self.image2)
        self.qlst_main.addItem(self.image3)
        self.qlst_main.addItem(self.image4)
        self.qlst_main.addItem(self.image5)
        self.qlst_main.addItem(self.image6)
        self.qlst_main.addItem(self.image7)
        self.qlst_main.addItem(self.image8)
        self.qlst_main.addItem(self.image9)
        self.qlst_main.addItem(self.image10)
        
        self.v_main_lay.addLayout(self.h_side_lay)
        self.v_main_lay.addWidget(self.qlst_main)
        
        self.setLayout(self.v_main_lay)
        
        # cmb = self.combo_box.currentText()
        
    def apple(self):
        self.close()
        self.__init__()
        self.show()    
        
        
        
if __name__ == "__main__":
    app = QApplication([])
    win = Accessories()
    win.show()
    app.exec_()
