import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QScrollArea, QFrame, QMessageBox, QInputDialog
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QSize, pyqtSignal
import os
from functools import partial

class ClickableLabel(QLabel):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Apple AirPods")
        self.resize(1024, 768)

        self.orders_count = 0

        central_widget = QWidget(self)
        main_layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QScrollArea.NoFrame)
        main_layout.addWidget(scroll_area)

        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        scroll_area.setWidget(content_widget)

        # Header Section
        header = QFrame()
        header_layout = QHBoxLayout(header)
        header.setStyleSheet("background-color: #f8f8f8; border-bottom: 1px solid #ddd; padding: 10px;")
        
        title = QLabel("Apple AirPods")
        title.setFont(QFont('Arial', 24, QFont.Bold))
        header_layout.addWidget(title)
        
        header_layout.addStretch()

        buy_button_header = QPushButton("Buy Now")
        buy_button_header.setStyleSheet("background-color: #007bff; color: white; padding: 10px 20px; border-radius: 5px;")
        buy_button_header.setFixedSize(QSize(120, 40))
        buy_button_header.clicked.connect(self.on_buy_now_clicked)
        header_layout.addWidget(buy_button_header)

        # Hero Section with Images
        hero_section = QWidget()
        hero_layout = QVBoxLayout(hero_section)
        hero_section.setStyleSheet("background-color: #f1f1f1; text-align: center; padding: 20px;")
        content_layout.addWidget(header)
        content_layout.addWidget(hero_section)

        image_dir = os.path.join(os.path.dirname(__file__), 'images')
        image_paths = [
            os.path.join(image_dir, "pods.jpeg"),
            os.path.join(image_dir, "pods.jpeg"),
            os.path.join(image_dir, "pods.jpeg"),
            os.path.join(image_dir, "pods.jpeg")
        ]

        images_layout = QHBoxLayout()
        for i, image_path in enumerate(image_paths):
            image_frame = QFrame()
            image_layout = QVBoxLayout(image_frame)
            image_frame.setStyleSheet("margin: 10px;")

            hero_image = ClickableLabel()

            # Debug: Check if the image path exists and is valid
            if not os.path.isfile(image_path):
                print(f"Image file not found: {image_path}")
                hero_image.setText("Image not found")
                hero_image.setFixedSize(QSize(200, 200))
                hero_image.setStyleSheet("border: 1px solid #ddd; border-radius: 10px;")
            else:
                pixmap = QPixmap(image_path)
                if pixmap.isNull():
                    print(f"Failed to load image: {image_path}")
                    hero_image.setText("Image not found")
                    hero_image.setFixedSize(QSize(200, 200))
                else:
                    hero_image.setPixmap(pixmap.scaledToWidth(200))
                    hero_image.setFixedSize(QSize(200, 200))
                hero_image.setStyleSheet("border: 1px solid #ddd; border-radius: 10px;")
            
            # Connect image click event
            hero_image.clicked.connect(partial(self.on_buy_now_clicked, img_index=i))
            
            image_layout.addWidget(hero_image)
            images_layout.addWidget(image_frame)

        hero_section.setLayout(images_layout)

        # Features Section
        features_section = QWidget()
        features_layout = QVBoxLayout(features_section)
        features_section.setStyleSheet("background-color: #fff; text-align: center; padding: 20px;")
        content_layout.addWidget(features_section)

        features_title = QLabel("Features")
        features_title.setFont(QFont('Arial', 24, QFont.Bold))
        features_layout.addWidget(features_title)

        features = [
            ("High Quality Sound", "Enjoy rich, high-fidelity audio with every listen."),
            ("Seamless Integration", "Works perfectly with all your Apple devices."),
            ("Long Battery Life", "Up to 24 hours of listening time with the charging case.")
        ]

        for feature_title, feature_description in features:
            feature_frame = QFrame()
            feature_layout = QVBoxLayout(feature_frame)
            feature_frame.setStyleSheet("margin: 20px; border: 1px solid #ddd; padding: 10px; border-radius: 5px;")

            feature_header = QLabel(feature_title)
            feature_header.setFont(QFont('Arial', 18, QFont.Bold))
            feature_layout.addWidget(feature_header)

            feature_desc = QLabel(feature_description)
            feature_desc.setFont(QFont('Arial', 14))
            feature_desc.setStyleSheet("color: #666;")
            feature_layout.addWidget(feature_desc)

            features_layout.addWidget(feature_frame)

        # Footer Section
        footer = QFrame()
        footer_layout = QHBoxLayout(footer)
        footer.setStyleSheet("background-color: #f8f8f8; border-top: 1px solid #ddd; padding: 10px;")
        footer_text = QLabel("&copy; 2024 Apple Inc.")
        footer_text.setFont(QFont('Arial', 12))
        footer_text.setAlignment(Qt.AlignCenter)
        footer_layout.addWidget(footer_text)

        content_layout.addWidget(footer)

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
