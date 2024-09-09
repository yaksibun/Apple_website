import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QScrollArea, QFrame, QMessageBox, QInputDialog
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtCore import Qt, QSize
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Apple AirPods")
        self.setWindowIcon(QIcon('images/log.png'))
        self.resize(1024, 768)

        self.orders_count = 0

        central_widget = QWidget()
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QScrollArea.NoFrame)
        
        content_widget = QWidget()
        content_layout = QVBoxLayout()
        content_widget.setLayout(content_layout)
        scroll_area.setWidget(content_widget)

        header = QFrame()
        header_layout = QHBoxLayout()
        header.setLayout(header_layout)
        header.setStyleSheet("background-color: #f8f8f8; border-bottom: 1px solid #ddd; padding: 10px;")
        
        title = QLabel("Apple AirPods")
        title.setFont(QFont('Arial', 24, QFont.Bold))
        title.setStyleSheet("margin: 0;")
        header_layout.addWidget(title)
        
        header_layout.addStretch()

        buy_button_header = QPushButton("Buy Now")
        buy_button_header.setStyleSheet("background-color: #007bff; color: white; padding: 10px 20px; border-radius: 5px;")
        buy_button_header.setFixedSize(QSize(120, 40))
        buy_button_header.clicked.connect(self.on_buy_now_clicked)
        header_layout.addWidget(buy_button_header)

        hero_section = QWidget()
        hero_layout = QVBoxLayout()
        hero_section.setLayout(hero_layout)
        hero_section.setStyleSheet("background-color: #f1f1f1; text-align: center; padding: 50px;")

        image_paths = [
            "C:/Users/Bunyod/OneDrive/Рабочий стол/Apple/SP750-airpods.jpeg",
            "C:/Users/Bunyod/OneDrive/Рабочий стол/Apple/SP750-airpods.jpeg",
            "C:/Users/Bunyod/OneDrive/Рабочий стол/Apple/SP750-airpods.jpeg",
            "C:/Users/Bunyod/OneDrive/Рабочий стол/Apple/SP750-airpods.jpeg"
        ]

        images_layout = QHBoxLayout()
        for i, image_path in enumerate(image_paths):
            image_frame = QFrame()
            image_layout = QVBoxLayout()
            image_frame.setLayout(image_layout)
            image_frame.setStyleSheet("margin: 10px;")

            hero_image = QLabel()
            
            if not os.path.isfile(image_path):
                hero_image.setText("Image not found")
                hero_image.setFixedSize(QSize(200, 200))
                hero_image.setStyleSheet("border: 1px solid #ddd; border-radius: 10px;")
            else:
                pixmap = QPixmap(image_path)
                if pixmap.isNull():
                    hero_image.setText("Image not found")
                    hero_image.setFixedSize(QSize(200, 200))
                else:
                    hero_image.setPixmap(pixmap.scaledToWidth(200))
                    hero_image.setFixedSize(QSize(200, 200))
                hero_image.setStyleSheet("border: 1px solid #ddd; border-radius: 10px;")
            
            image_layout.addWidget(hero_image)

            buy_button = QPushButton("Buy Now")
            buy_button.setStyleSheet("background-color: #007bff; color: white; padding: 10px; border-radius: 5px; margin-top: 10px;")
            buy_button.clicked.connect(lambda checked, img=i: self.on_buy_now_clicked(img))
            image_layout.addWidget(buy_button)

            images_layout.addWidget(image_frame)

        hero_section.setLayout(images_layout)

        features_section = QWidget()
        features_layout = QVBoxLayout()
        features_section.setLayout(features_layout)
        features_section.setStyleSheet("background-color: #fff; text-align: center; padding: 20px;")

        features_title = QLabel("Features")
        features_title.setFont(QFont('Arial', 24, QFont.Bold))
        features_title.setStyleSheet("margin-bottom: 20px;")
        features_layout.addWidget(features_title)

        features = [
            ("High Quality Sound", "Enjoy rich, high-fidelity audio with every listen."),
            ("Seamless Integration", "Works perfectly with all your Apple devices."),
            ("Long Battery Life", "Up to 24 hours of listening time with the charging case.")
        ]

        for feature_title, feature_description in features:
            feature_frame = QFrame()
            feature_layout = QVBoxLayout()
            feature_frame.setLayout(feature_layout)
            feature_frame.setStyleSheet("margin: 20px; border: 1px solid #ddd; padding: 10px; border-radius: 5px;")

            feature_header = QLabel(feature_title)
            feature_header.setFont(QFont('Arial', 18, QFont.Bold))
            feature_layout.addWidget(feature_header)

            feature_desc = QLabel(feature_description)
            feature_desc.setFont(QFont('Arial', 14))
            feature_desc.setStyleSheet("color: #666;")
            feature_layout.addWidget(feature_desc)

            features_layout.addWidget(feature_frame)

        footer = QFrame()
        footer_layout = QHBoxLayout()
        footer.setLayout(footer_layout)
        footer.setStyleSheet("background-color: #f8f8f8; border-top: 1px solid #ddd; padding: 10px;")

        footer_text = QLabel("&copy; 2024 Apple Inc.")
        footer_text.setFont(QFont('Arial', 12))
        footer_text.setAlignment(Qt.AlignCenter)
        footer_layout.addWidget(footer_text)

        content_layout.addWidget(header)
        content_layout.addWidget(hero_section)
        content_layout.addWidget(features_section)
        content_layout.addWidget(footer)

        main_layout.addWidget(scroll_area)

    def on_buy_now_clicked(self, img_index=None):
        name, ok = QInputDialog.getText(self, 'Order Information', 'Enter your name:')
        if ok and name:
            address, ok = QInputDialog.getText(self, 'Order Information', 'Enter your address:')
            if ok and address:
                self.orders_count += 1
                with open("orders.txt", "a") as file:
                    file.write(f"Order {self.orders_count}: Name: {name}, Address: {address}, Image Index: {img_index}\n")

                confirmation = QMessageBox()
                confirmation.setIcon(QMessageBox.Information)
                confirmation.setWindowTitle('Order Confirmation')
                confirmation.setText(f"Order placed successfully!\n\nName: {name}\nAddress: {address}")
                confirmation.setStandardButtons(QMessageBox.Ok)
                confirmation.exec_()
            else:
                QMessageBox.warning(self, 'Input Error', 'Address is required!')
        else:
            QMessageBox.warning(self, 'Input Error', 'Name is required!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
