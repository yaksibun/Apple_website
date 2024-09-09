from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt


class Soat(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Apple Watch Section")
        self.setFixedSize(1924, 950)

        self.cart = []

        main_layout = QVBoxLayout(self)

        header = QLabel("Apple Watch")
        header.setStyleSheet("font-size: 36px; font-weight: bold;")
        header.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(header)

        image_layout = QHBoxLayout()

        image_label1 = QLabel(self)
        pixmap1 = QPixmap("watchs_imgs/watchs1.png")
        image_label1.setPixmap(pixmap1)
        image_label1.setAlignment(Qt.AlignCenter)

        image_label2 = QLabel(self)
        pixmap2 = QPixmap("watchs_imgs/watchs2.png")
        image_label2.setPixmap(pixmap2)
        image_label2.setAlignment(Qt.AlignCenter)

        image_label3 = QLabel(self)
        pixmap3 = QPixmap("watchs_imgs/watchs3.png")
        image_label3.setPixmap(pixmap3)
        image_label3.setAlignment(Qt.AlignCenter)

        image_layout.addWidget(image_label1)
        image_layout.addWidget(image_label2)
        image_layout.addWidget(image_label3)

        main_layout.addLayout(image_layout)

        series_buttons_layout = QHBoxLayout()
        series9_btn = QPushButton("Watch Series 9")
        ultra2_btn = QPushButton("Watch Ultra 2")
        se_btn = QPushButton("Watch SE")
        series9_btn.clicked.connect(self.seria_9)
        ultra2_btn.clicked.connect(self.ultra_2)
        se_btn.clicked.connect(self.se)
        self.back = QPushButton("Back home", clicked=self.hide_watchs)



        series9_btn.setFixedSize(500, 50)
        ultra2_btn.setFixedSize(500, 50)
        se_btn.setFixedSize(500, 50)

        series9_btn.setStyleSheet("""
            QPushButton {
                font-size: 22px;
                background: #7B68EE;
                border-radius: 8px;
            }
            QPushButton:hover {
                font-size: 24px;
                background-color: #00FF00;
                color: black;
                border-radius: 8px;
            }
        """)

        ultra2_btn.setStyleSheet("""
            QPushButton {
                font-size: 22px;
                background: #7B68EE;
                border-radius: 8px;
            }
            QPushButton:hover {
                font-size: 24px;
                background-color: #00FF00;
                color: black;
                border-radius: 8px;
            }
        """)

        se_btn.setStyleSheet("""
            QPushButton {
                font-size: 22px;
                background: #7B68EE;
                border-radius: 8px;
            }
            QPushButton:hover {
                font-size: 24px;
                background-color: #00FF00;
                color: black;
                border-radius: 8px;
            }
        """)
        series_buttons_layout.addWidget(series9_btn)
        series_buttons_layout.addWidget(ultra2_btn)
        series_buttons_layout.addWidget(se_btn)

        main_layout.addLayout(series_buttons_layout)

        features_label = QLabel("Amazing Features of Apple Watch:")
        features_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        features_layout = QVBoxLayout()

        feature1 = QLabel("- Advanced Health Monitoring")
        feature2 = QLabel("- Precision GPS and Ultra Tracking")
        feature3 = QLabel("- Stylish, Durable, and Customizable")

        features_layout.addWidget(feature1)
        features_layout.addWidget(feature2)
        features_layout.addWidget(feature3)

        main_layout.addWidget(features_label)
        main_layout.addLayout(features_layout)

        self.cart_label = QLabel("Shopping Cart:")
        self.cart_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.cart_display = QLabel("")
        self.cart_display.setStyleSheet("font-size: 18px;")
        self.back.setStyleSheet("""
            QPushButton {
                font-size: 30px;
                border-radius: 5px;
            }
            QPushButton:hover {
                font-size: 35px;
                color: blue;
            }
        """)
        self.lbl = QLabel("""
        
More ways to shop: Find an Apple Store or other retailer near you. Or call 1-800-MY-APPLE  United States Copyright © 2024 Apple Inc. All rights reserved.  Privacy Policy Terms of Use Sales and Refunds Legal Site Map  The ability to measure blood oxygen is no longer available on 
Apple Watch units sold by Apple in the United States beginning January 18, 2024. These are indicated with part numbers ending in LW/A. Learn how to identify your Apple Watch.  The Oceanic+ app requires Apple Watch Ultra or Apple Watch Ultra 2. A subscription is required. 
Available on the App Store. Always follow diving protocols and dive with a companion and have a secondary device.


        """)
        self.lbl.setStyleSheet("font-size: 15px; color: #aaa")
        main_layout.addWidget(self.cart_label)
        main_layout.addWidget(self.cart_display)
        main_layout.addWidget(self.back)
        main_layout.addWidget(self.lbl)

        self.setLayout(main_layout)


    def hide_watchs(self):
        self.hide()


    def show_watch_info(self, name, price, image_path):
        self.dialog = QDialog(self)
        self.dialog.setWindowTitle(f"{name} - {price}")
        self.dialog.setFixedSize(400, 400)

        layout = QVBoxLayout()

        info_label = QLabel(f"Details about {name}:\nPrice: {price}")
        layout.addWidget(info_label)

        image_label = QLabel()
        pixmap = QPixmap(image_path)
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(image_label)


        buy_button = QPushButton("Buy")
        buy_button.setStyleSheet("""
            QPushButton {
                font-size: 22px;
                background: #40E0D0;
                border-radius: 8px;
            }
            QPushButton:hover {
                font-size: 24px;
                background-color: #00FF00;
                color: black;
                border-radius: 8px;
            }
        """)
        buy_button.clicked.connect(lambda: self.add_to_cart(name, price))
        layout.addWidget(buy_button)

        self.dialog.setLayout(layout)
        self.dialog.exec_()

    def add_to_cart(self, name, price):
        self.cart.append(f"{name} - {price}")
        self.cart_display.setText("\n".join(self.cart))
        self.dialog.hide()



    def seria_9(self):
        self.show_watch_info("Watch Series 9", "$399", "watchs_imgs/watchs1.png")

    def ultra_2(self):
        self.show_watch_info("Watch Ultra 2", "$799", "watchs_imgs/watchs2.png")

    def se(self):
        self.show_watch_info("Watch SE", "$279", "watchs_imgs/watchs3.png")


if __name__ == '__main__':
    app = QApplication([])
    window = Soat()
    window.show()
    app.exec_()
