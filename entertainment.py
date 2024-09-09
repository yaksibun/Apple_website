from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt

class Entertainment(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Entertainment")
        self.setStyleSheet("background-color:#000")
        self.setFixedSize(1900, 1000)

        self.v_main_lay = QVBoxLayout()

        self.qlist_main = QListWidget()
        self.qlist_main.setIconSize(QSize(1840, 800))
        self.qlist_main.setFrameShape(QListWidget.NoFrame)

        # 1-matn
        list_lbl = QLabel("Meet the A-list of \nentertainment")
        list_lbl.setStyleSheet("""
            color:#f5f5f7;
            font-family:SF Pro Display, SF Pro Icons, Helvetica Neue, Helvetica, Arial, sans-serif;
            font-size: 94px;
            line-height: 1.0909090909;
            font-weight: 700;
            letter-spacing: -0.014em;
        """)
        list_lbl.setAlignment(Qt.AlignCenter)

        # 2-matn
        list_lbl2 = QLabel("Award‑winning movies. Binge‑worthy shows. Your favorite music mastered in\n Spatial Audio. The most epic collection of mobile games. And the world’s largest\n library of 4K Ultra HD fitness content. The best entertainment and experiences\n live here — only on Apple.")
        list_lbl2.setStyleSheet("""
            color:#f5f5f7;
            font-size: 24px;
            line-height: 1.2353641176;
            font-weight: 600;
            letter-spacing: -0.037em;
            font-family: SF Pro Text, SF Pro Icons, Helvetica Neue, Helvetica, Arial, sans-serif;
        """)
        list_lbl2.setAlignment(Qt.AlignCenter)

        widget = QWidget()
        v_layout = QVBoxLayout()
        v_layout.addWidget(list_lbl)
        v_layout.addWidget(list_lbl2)
        widget.setLayout(v_layout)

        item = QListWidgetItem()
        item.setSizeHint(widget.sizeHint()) 
        self.qlist_main.addItem(item)
        self.qlist_main.setItemWidget(item, widget)  

        self.image = QListWidgetItem()
        self.image.setIcon(QIcon("images/learnmore.png"))
        self.image1 = QListWidgetItem()
        self.image1.setIcon(QIcon("images/godzilla.png"))
        self.image2 = QListWidgetItem()
        self.image2.setIcon(QIcon("images/slayd.png"))
        self.image3 = QListWidgetItem()
        self.image3.setIcon(QIcon("images/listenmusic.png"))
        self.image4 = QListWidgetItem()
        self.image4.setIcon(QIcon("images/slayd2.png"))
        self.image5 = QListWidgetItem()
        self.image5.setIcon(QIcon("images/mikki.png"))
        self.image6 = QListWidgetItem()
        self.image6.setIcon(QIcon("images/yoga.png"))
        self.image7 = QListWidgetItem()
        self.image7.setIcon(QIcon("images/slayd3.png"))
        self.image8 = QListWidgetItem()
        self.image8.setIcon(QIcon("images/slayd4.png"))
        self.image9 = QListWidgetItem()
        self.image9.setIcon(QIcon("images/slayd5.png"))
        self.image10 = QListWidgetItem()
        self.image10.setIcon(QIcon("images/slayd6.png"))
        self.image11 = QListWidgetItem()
        self.image11.setIcon(QIcon("images/slayd7.png"))
        self.image12 = QListWidgetItem()
        self.image12.setIcon(QIcon("images/slayd8.png"))
        
        
        

        self.qlist_main.addItem(self.image)
        self.qlist_main.addItem(self.image1)
        self.qlist_main.addItem(self.image2)
        self.qlist_main.addItem(self.image3)
        self.qlist_main.addItem(self.image4)
        self.qlist_main.addItem(self.image5)
        self.qlist_main.addItem(self.image6)
        self.qlist_main.addItem(self.image7)
        self.qlist_main.addItem(self.image8)
        self.qlist_main.addItem(self.image9)
        self.qlist_main.addItem(self.image10)
        self.qlist_main.addItem(self.image11)
        self.qlist_main.addItem(self.image12)
        
        

        # Tugmalar
        self.one_btn = QPushButton("")
        self.one_btn.setIcon(QIcon("images/appleone.png"))
        self.one_btn.setIconSize(QSize(80, 80))

        self.tv_btn = QPushButton("")
        self.tv_btn.setIcon(QIcon("images/appletv.png"))
        self.tv_btn.setIconSize(QSize(80, 80))

        self.music_btn = QPushButton("")
        self.music_btn.setIcon(QIcon("images/applemusic.png"))
        self.music_btn.setIconSize(QSize(80, 80))

        self.arcade_btn = QPushButton("")
        self.arcade_btn.setIcon(QIcon("images/applearcade.png"))
        self.arcade_btn.setIconSize(QSize(80, 80))

        self.fitnes_btn = QPushButton("")
        self.fitnes_btn.setIcon(QIcon("images/applefitness.png"))
        self.fitnes_btn.setIconSize(QSize(80, 80))

        self.news_btn = QPushButton("")
        self.news_btn.setIcon(QIcon("images/applenews.png"))
        self.news_btn.setIconSize(QSize(80, 80))

        self.podcasts_btn = QPushButton("")
        self.podcasts_btn.setIcon(QIcon("images/applepodcasts.png"))
        self.podcasts_btn.setIconSize(QSize(80, 80))

        self.books_btn = QPushButton("")
        self.books_btn.setIcon(QIcon("images/applebooks.png"))
        self.books_btn.setIconSize(QSize(80, 80))

        self.lst_image_btns = [
            self.one_btn, self.tv_btn, self.music_btn, self.arcade_btn,
            self.fitnes_btn, self.news_btn, self.podcasts_btn, self.books_btn
        ]
        self.h_sidebar_lay = QHBoxLayout()
        for i in self.lst_image_btns:
            self.h_sidebar_lay.addWidget(i)

        self.h_sidebar_lbl_lay = QHBoxLayout()
        self.apple_one_btn = QPushButton("Apple One")
        self.apple_tv_btn = QPushButton("Apple TV+")
        self.apple_music_btn = QPushButton("Apple Music")
        self.apple_arcade_btn = QPushButton("Apple Arcade")
        self.apple_fitnes_btn = QPushButton("Apple Fitness+")
        self.apple_news_btn = QPushButton("Apple News+")
        self.apple_podcasts_btn = QPushButton("Apple Podcasts")
        self.apple_books_btn = QPushButton("Apple Books")

        self.lst_lbl_btns = [
            self.apple_one_btn, self.apple_tv_btn, self.apple_music_btn,
            self.apple_arcade_btn, self.apple_fitnes_btn, self.apple_news_btn,
            self.apple_podcasts_btn, self.apple_books_btn
        ]

        for i in self.lst_lbl_btns:
            self.h_sidebar_lbl_lay.addWidget(i)
            i.setStyleSheet(
                "color:#fff;font-size:15px;font-family: SF Pro Text, SF Pro Icons, "
                "Helvetica Neue, Helvetica, Arial, sans-serif;line-height: 1.3;"
                "font-weight: 400; letter-spacing: 0.01em;"
            )

        self.v_image_lbl_btns = QVBoxLayout()
        self.v_image_lbl_btns.addLayout(self.h_sidebar_lay)
        self.v_image_lbl_btns.addLayout(self.h_sidebar_lbl_lay)
        self.h_image_lbl_btns = QHBoxLayout()
        self.h_image_lbl_btns.addStretch()
        self.h_image_lbl_btns.addLayout(self.v_image_lbl_btns)
        self.h_image_lbl_btns.addStretch()

        self.v_main_lay.addLayout(self.h_image_lbl_btns)
        self.v_main_lay.addWidget(self.qlist_main)

        self.setLayout(self.v_main_lay)


if __name__ == "__main__":
    app = QApplication([])
    win = Entertainment()
    win.show()
    app.exec_()
