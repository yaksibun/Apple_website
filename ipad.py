from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import *
import sys

class IpadWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create the main QVBoxLayout
        self.v_main = QVBoxLayout()
        self.resize(1900,1000)

        # Create a QScrollArea for vertical scrolling (whole window scrollable vertically)
        vertical_scroll_area = QScrollArea()
        vertical_scroll_area.setWidgetResizable(True)

        # Create a container widget for the main layout
        container_widget = QWidget()
        container_widget.setLayout(self.v_main)

        vertical_scroll_area.setWidget(container_widget)


        # Layout of buttons at the top
        self.buttons_at_top = QHBoxLayout()

        # Buttons at the top
        self.apple_logo_btn = QPushButton("Apple", clicked=self.close)
        self.store_top_btn = QPushButton("Store", clicked=self.close)
        self.mac_top_btn = QPushButton("Mac")
        self.iphone_top_btn = QPushButton("iPhone")
        self.watch_top_btn = QPushButton("Watch")
        self.vision_top_btn = QPushButton("Vision")
        self.airpods_top_btn = QPushButton("Airpods")
        self.tv_and_home_top_btn = QPushButton("TV & Home")
        self.entertainment_top_btn = QPushButton("Entertainment")
        self.accessories_top_btn = QPushButton("Accessories")
        self.search_top_btn = QPushButton()
        self.search_top_btn.clicked.connect(self.Search_top_btn_message)
        self.search_top_btn.setIcon(QIcon(QPixmap("images\\search.png")))
        self.search_top_btn.setFixedSize(30, 30)
        
        self.bag_top_btn = QPushButton()
        self.bag_top_btn.setIcon(QIcon(QPixmap("images\\bag.png")))
        self.bag_top_btn.setFixedSize(30, 30)
        self.bag_top_btn.clicked.connect(self.Bag_top_btn_message)


        # Adding buttons to H layout
        self.buttons_at_top.addWidget(self.apple_logo_btn)
        self.buttons_at_top.addWidget(self.store_top_btn)
        self.buttons_at_top.addWidget(self.mac_top_btn)
        self.buttons_at_top.addWidget(self.iphone_top_btn)
        self.buttons_at_top.addWidget(self.watch_top_btn)
        self.buttons_at_top.addWidget(self.vision_top_btn)
        self.buttons_at_top.addWidget(self.airpods_top_btn)
        self.buttons_at_top.addWidget(self.tv_and_home_top_btn)
        self.buttons_at_top.addWidget(self.entertainment_top_btn)
        self.buttons_at_top.addWidget(self.accessories_top_btn)
        self.buttons_at_top.addWidget(self.search_top_btn)

        self.buttons_at_top.addWidget(self.bag_top_btn)

        # Window title
        self.setWindowTitle("Ipad")

        # Headline Shop iPhone
        self.headline_lay = QHBoxLayout()
        self.headline_lay2 = QVBoxLayout()

        self.lbl_headline = QLabel()
        self.lbl_headline.setText("Shop iPad")
        self.lbl_headline.setStyleSheet("font-size:40px")

        self.need_help_btn = QPushButton()
        self.need_help_btn.setFixedSize(230, 70)
        self.need_help_btn.setIcon(QIcon(QPixmap("images\\help.png")))
        self.need_help_btn.setIconSize(self.need_help_btn.size())
        self.need_help_btn.clicked.connect(self.Need_help_btn)
        

        self.visit_store_btn = QPushButton()
        self.visit_store_btn.setFixedSize(230, 70)
        self.visit_store_btn.setIcon(QIcon(QPixmap("images\\visit.png")))
        self.visit_store_btn.setIconSize(self.visit_store_btn.size())
        self.visit_store_btn.clicked.connect(self.Visit_btn)

        self.headline_lay2.addWidget(self.need_help_btn)
        self.headline_lay2.addWidget(self.visit_store_btn)
        self.headline_lay.addWidget(self.lbl_headline)
        self.headline_lay.addLayout(self.headline_lay2)

        

        # Theme H layout
        self.h_theme_btns = QHBoxLayout()
        self.h_theme_btns.setSpacing(0)


        # Buttons of theme H layout
        self.all_models_btn = QPushButton("All Models")
        self.shopping_guides_btn = QPushButton("Shopping guides")
        self.ways_to_save_btn = QPushButton("Ways to Save")
        self.sustainability_btn = QPushButton("Sustainability")
        self.accessories_btn = QPushButton("Accesories")
        self.setup_and_support_btn = QPushButton("Setup and Support")
        self.the_iphone_experience_btn = QPushButton("The iPhone Experience")
        self.special_stores_btn = QPushButton("Special Stores")

        # Adding buttons to theme H layout
        self.h_theme_btns.addWidget(self.all_models_btn)
        self.h_theme_btns.addWidget(self.shopping_guides_btn)
        self.h_theme_btns.addWidget(self.ways_to_save_btn)
        self.h_theme_btns.addWidget(self.sustainability_btn)
        self.h_theme_btns.addWidget(self.accessories_btn)
        self.h_theme_btns.addWidget(self.setup_and_support_btn)
        self.h_theme_btns.addWidget(self.the_iphone_experience_btn)
        self.h_theme_btns.addWidget(self.special_stores_btn)

        # All models. Take your pick label
        self.lbl_all_models = QLabel()
        self.lbl_all_models.setText("All models. Take your pick.")
        self.lbl_all_models.setStyleSheet("font-size:30px")

        # iPads pictures buttons' layout
        self.all_models_lay = QHBoxLayout()

        # iPads pictures buttons
        self.ipad_pro_btn = QPushButton("")
        self.ipad_pro_btn.setFixedSize(345, 425)
        self.ipad_pro_btn.clicked.connect(self.Ipad_pro_btn)
        self.ipad_air_btn = QPushButton("")
        self.ipad_air_btn.setFixedSize(345, 425)
        self.ipad_air_btn.clicked.connect(self.Ipad_air_btn)
        self.ipad_btn = QPushButton("")
        self.ipad_btn.setFixedSize(345, 425)
        self.ipad_btn.clicked.connect(self.Ipad_btn)
        self.ipad_mini_btn = QPushButton("")
        self.ipad_mini_btn.setFixedSize(345, 425)
        self.ipad_mini_btn.clicked.connect(self.Ipad_mini_btn)
        self.explore_all_ipad_accessories_btn = QPushButton("")
        self.explore_all_ipad_accessories_btn.setFixedSize(345, 425)
        self.explore_all_ipad_accessories_btn.clicked.connect(self.Explore_accessories)

        # Buttons' background images
        self.ipad_pro_btn.setIcon(QIcon(QPixmap("images\\ipad_pro.png")))
        self.ipad_pro_btn.setIconSize(self.ipad_pro_btn.size())

        self.ipad_air_btn.setIcon(QIcon(QPixmap("images\\ipad_air.png")))
        self.ipad_air_btn.setIconSize(self.ipad_air_btn.size())

        self.ipad_btn.setIcon(QIcon(QPixmap("images\\ipad.png")))
        self.ipad_btn.setIconSize(self.ipad_btn.size())

        self.ipad_mini_btn.setIcon(QIcon(QPixmap("images\\ipad_mini.png")))
        self.ipad_mini_btn.setIconSize(self.ipad_mini_btn.size())

        self.explore_all_ipad_accessories_btn.setIcon(QIcon(QPixmap("images\\explore_all_ipad_accessories.png")))
        self.explore_all_ipad_accessories_btn.setIconSize(self.explore_all_ipad_accessories_btn.size())

        # Adding buttons to the horizontal layout
        self.all_models_lay.addWidget(self.ipad_pro_btn)
        self.all_models_lay.addWidget(self.ipad_air_btn)
        self.all_models_lay.addWidget(self.ipad_btn)
        self.all_models_lay.addWidget(self.ipad_mini_btn)
        self.all_models_lay.addWidget(self.explore_all_ipad_accessories_btn)

        # Label for shopping guides 
        self.lbl_shopping_guides = QLabel()
        self.lbl_shopping_guides.setText("Shopping Guides. Can’t decide? Start here.")
        self.lbl_shopping_guides.setStyleSheet("font-size: 30px")

        # Layout for shopping guides
        self.shopping_guides_lay = QHBoxLayout()

        # Buttons for shopping layout 
        self.shopping_btn1 = QPushButton()
        self.shopping_btn1.setFixedSize(350, 380)
        self.shopping_btn1.clicked.connect(self.Shopping1)
        self.shopping_btn2 = QPushButton()
        self.shopping_btn2.setFixedSize(350, 380)
        self.shopping_btn2.clicked.connect(self.Shopping2)

        self.shopping_btn3 = QPushButton()
        self.shopping_btn3.setFixedSize(350, 380)
        self.shopping_btn3.clicked.connect(self.Shopping3)

        self.shopping_btn4 = QPushButton()
        self.shopping_btn4.setFixedSize(350, 380)
        self.shopping_btn4.clicked.connect(self.Shopping4)


        # Setting icons for shopping buttons
        self.shopping_btn1.setIcon(QIcon(QPixmap("images\\which_ipad.png")))
        self.shopping_btn1.setIconSize(self.shopping_btn1.size())

        self.shopping_btn2.setIcon(QIcon(QPixmap("images\\shop_with.png")))
        self.shopping_btn2.setIconSize(self.shopping_btn2.size())

        self.shopping_btn3.setIcon(QIcon(QPixmap("images\\man.png")))
        self.shopping_btn3.setIconSize(self.shopping_btn3.size())

        self.shopping_btn4.setIcon(QIcon(QPixmap("images\\woman.png")))
        self.shopping_btn4.setIconSize(self.shopping_btn4.size())

        # Adding shopping buttons to the layout
        self.shopping_guides_lay.addWidget(self.shopping_btn1)
        self.shopping_guides_lay.addWidget(self.shopping_btn2)
        self.shopping_guides_lay.addWidget(self.shopping_btn3)
        self.shopping_guides_lay.addWidget(self.shopping_btn4)

        self.lbl_way_to_save = QLabel()
        self.lbl_way_to_save.setText("Ways to save. Find what works for you.")
        self.lbl_way_to_save.setStyleSheet("font-size: 30px")

        #way to save
        self.way_to_save_lay = QHBoxLayout()
        #buttons
        self.way_to_save_btn1 = QPushButton()
        self.way_to_save_btn1.setFixedSize(345, 375)
        self.way_to_save_btn2 = QPushButton()
        self.way_to_save_btn2.setFixedSize(345, 375)
        self.way_to_save_btn3 = QPushButton()
        self.way_to_save_btn3.setFixedSize(345, 375)
        self.way_to_save_btn4 = QPushButton()
        self.way_to_save_btn4.setFixedSize(345, 375)
        self.way_to_save_btn5 = QPushButton()
        self.way_to_save_btn5.setFixedSize(345, 375)


        self.way_to_save_btn1.setIcon(QIcon(QPixmap("images\\1.png")))
        self.way_to_save_btn1.setIconSize(self.way_to_save_btn1.size())

        self.way_to_save_btn2.setIcon(QIcon(QPixmap("images\\2.png")))
        self.way_to_save_btn2.setIconSize(self.way_to_save_btn2.size())

        self.way_to_save_btn3.setIcon(QIcon(QPixmap("images\\3.png")))
        self.way_to_save_btn3.setIconSize(self.way_to_save_btn3.size())

        self.way_to_save_btn4.setIcon(QIcon(QPixmap("images\\4.png")))
        self.way_to_save_btn4.setIconSize(self.way_to_save_btn4.size())

        self.way_to_save_lay.addWidget(self.way_to_save_btn1)
        self.way_to_save_lay.addWidget(self.way_to_save_btn2)
        self.way_to_save_lay.addWidget(self.way_to_save_btn3)
        self.way_to_save_lay.addWidget(self.way_to_save_btn4)



        self.lbl_difference = QLabel()
        self.lbl_difference.setText("The Apple Store difference. Even more reasons to shop with us.")
        self.lbl_difference.setStyleSheet("font-size: 30px")

        

        self.difference_btn = QPushButton()
        

        self.difference_btn.setIcon(QIcon(QPixmap("images\\difference.png")))
        self.difference_btn.setIconSize(self.difference_btn.size())
        # Set the desired button size
        self.difference_btn.setFixedSize(470, 490)  # Width: 200px, Height: 150px

        #label
        self.lbl_ipad_accessories = QLabel()
        self.lbl_ipad_accessories.setText("iPad accessories. Work and create with ease.")
        self.lbl_ipad_accessories.setStyleSheet("font-size:30px")
        #layout
        self.ipad_accessories_lay = QHBoxLayout()
        #buttons of layout
        self.ipad_accessories_btn1 = QPushButton()
        self.ipad_accessories_btn1.setFixedSize(345, 425)
        self.ipad_accessories_btn2 = QPushButton()
        self.ipad_accessories_btn2.setFixedSize(275, 425)
        self.ipad_accessories_btn3 = QPushButton()
        self.ipad_accessories_btn3.setFixedSize(275, 425)
        self.ipad_accessories_btn4 = QPushButton()
        self.ipad_accessories_btn4.setFixedSize(275, 425)
        self.ipad_accessories_btn5 = QPushButton()
        self.ipad_accessories_btn5.setFixedSize(275, 425)
        self.ipad_accessories_btn6 = QPushButton()
        self.ipad_accessories_btn6.setFixedSize(275, 425)
        self.ipad_accessories_btn7 = QPushButton()
        self.ipad_accessories_btn7.setFixedSize(275, 425)

        self.ipad_accessories_btn1.setIcon(QIcon(QPixmap("images\\acces1.png")))
        self.ipad_accessories_btn1.setIconSize(self.ipad_accessories_btn1.size())

        self.ipad_accessories_btn2.setIcon(QIcon(QPixmap("access2.png")))
        self.ipad_accessories_btn2.setIconSize(self.ipad_accessories_btn2.size())

        self.ipad_accessories_btn3.setIcon(QIcon(QPixmap("images\\access3.png")))
        self.ipad_accessories_btn3.setIconSize(self.ipad_accessories_btn3.size())

        self.ipad_accessories_btn4.setIcon(QIcon(QPixmap("images\\access4.png")))
        self.ipad_accessories_btn4.setIconSize(self.ipad_accessories_btn4.size())

        self.ipad_accessories_btn5.setIcon(QIcon(QPixmap("images\\access5.png")))
        self.ipad_accessories_btn5.setIconSize(self.ipad_accessories_btn5.size())

        self.ipad_accessories_btn6.setIcon(QIcon(QPixmap("images\\access6.png")))
        self.ipad_accessories_btn6.setIconSize(self.ipad_accessories_btn6.size())

        self.ipad_accessories_btn7.setIcon(QIcon(QPixmap("images\\access7.png")))
        self.ipad_accessories_btn7.setIconSize(self.ipad_accessories_btn7.size())

        self.ipad_accessories_lay.addWidget(self.ipad_accessories_btn1)
        self.ipad_accessories_lay.addWidget(self.ipad_accessories_btn2)
        self.ipad_accessories_lay.addWidget(self.ipad_accessories_btn3)
        self.ipad_accessories_lay.addWidget(self.ipad_accessories_btn4)
        self.ipad_accessories_lay.addWidget(self.ipad_accessories_btn5)
        self.ipad_accessories_lay.addWidget(self.ipad_accessories_btn6)
        self.ipad_accessories_lay.addWidget(self.ipad_accessories_btn7)



        self.lbl_setup = QLabel()
        self.lbl_setup.setText("Setup and support. Our Specialists are here to help.")
        self.lbl_setup.setStyleSheet("font-size: 30px")


        self.setup_lay = QHBoxLayout()

        self.setup_btn1 = QPushButton()
        self.setup_btn1.setFixedSize(345, 380)
        self.setup_btn2 = QPushButton()
        self.setup_btn2.setFixedSize(345, 380)
        self.setup_btn3 = QPushButton()
        self.setup_btn3.setFixedSize(345, 380)
        self.setup_btn4 = QPushButton()
        self.setup_btn4.setFixedSize(345, 380)
        self.setup_btn5 = QPushButton()
        self.setup_btn5.setFixedSize(345, 380)
        self.setup_btn6 = QPushButton()
        self.setup_btn6.setFixedSize(345, 380)

        self.setup_btn1.setIcon(QIcon(QPixmap("images\\setup1.png")))
        self.setup_btn1.setIconSize(self.setup_btn1.size())
        self.setup_btn2.setIcon(QIcon(QPixmap("images\\setup2.png")))
        self.setup_btn2.setIconSize(self.setup_btn2.size())
        self.setup_btn3.setIcon(QIcon(QPixmap("images\\setup3.png")))
        self.setup_btn3.setIconSize(self.setup_btn3.size())
        self.setup_btn4.setIcon(QIcon(QPixmap("images\\setup4.png")))
        self.setup_btn4.setIconSize(self.setup_btn4.size())
        self.setup_btn5.setIcon(QIcon(QPixmap("images\\setup5.png")))
        self.setup_btn5.setIconSize(self.setup_btn5.size())
        self.setup_btn6.setIcon(QIcon(QPixmap("images\\setup6.png")))
        self.setup_btn6.setIconSize(self.setup_btn6.size())

        self.setup_lay.addWidget(self.setup_btn1)
        self.setup_lay.addWidget(self.setup_btn2)
        self.setup_lay.addWidget(self.setup_btn3)
        self.setup_lay.addWidget(self.setup_btn4)
        self.setup_lay.addWidget(self.setup_btn5)
        self.setup_lay.addWidget(self.setup_btn6)





        # experince label
        self.lbl_ipad_experience = QLabel()
        self.lbl_ipad_experience.setText("The iPad experience. Designed to connect with everything Apple.")
        self.lbl_ipad_experience.setStyleSheet("font-size:30px")

        # expience layout
        self.ipad_experience_lay = QHBoxLayout()

        #button of layout
        self.ipad_experience_btn1 = QPushButton()
        self.ipad_experience_btn1.setFixedSize(345, 380)
        self.ipad_experience_btn2 = QPushButton()
        self.ipad_experience_btn2.setFixedSize(345, 380)
        self.ipad_experience_btn3 = QPushButton()
        self.ipad_experience_btn3.setFixedSize(345, 380)

        self.ipad_experience_lay2 = QVBoxLayout()
        
        self.ipad_experience_lay2_btn1 = QPushButton()
        

        self.ipad_experience_lay2_btn1.setFixedSize(500, 240)
        self.ipad_experience_lay2_btn2 = QPushButton()
        self.ipad_experience_lay2_btn2.setFixedSize(500, 240)
        self.ipad_experience_lay2_btn1.setIcon(QIcon(QPixmap("images\\ipad_experience_lay2_btn1.png")))
        self.ipad_experience_lay2_btn1.setIconSize(self.ipad_experience_lay2_btn1.size())
        self.ipad_experience_lay2_btn2.setIcon(QIcon(QPixmap("images\\ipad_experience_lay2_btn2.png")))
        self.ipad_experience_lay2_btn2.setIconSize(self.ipad_experience_lay2_btn2.size())
        self.ipad_experience_lay2.addWidget(self.ipad_experience_lay2_btn1)
        self.ipad_experience_lay2.addWidget(self.ipad_experience_lay2_btn2)

        self.ipad_experience_btn4 = QPushButton()
        self.ipad_experience_btn4.setFixedSize(345, 380)

        self.ipad_experience_btn1.setIcon(QIcon(QPixmap("images\\ipad_experience_btn1.png")))
        self.ipad_experience_btn1.setIconSize(self.ipad_experience_btn1.size())
        self.ipad_experience_btn2.setIcon(QIcon(QPixmap("images\\ipad_experience_btn2.png")))
        self.ipad_experience_btn2.setIconSize(self.ipad_experience_btn2.size())
        self.ipad_experience_btn3.setIcon(QIcon(QPixmap("images\\ipad_experience_btn3.png")))
        self.ipad_experience_btn3.setIconSize(self.ipad_experience_btn3.size())
        self.ipad_experience_btn4.setIcon(QIcon(QPixmap("images\\ipad_experience_btn4.png")))
        self.ipad_experience_btn4.setIconSize(self.ipad_experience_btn4.size())

        self.ipad_experience_lay.addWidget(self.ipad_experience_btn1)
        self.ipad_experience_lay.addWidget(self.ipad_experience_btn2)
        self.ipad_experience_lay.addWidget(self.ipad_experience_btn3)
        self.ipad_experience_lay.addLayout(self.ipad_experience_lay2)

        self.ipad_experience_lay.addWidget(self.ipad_experience_btn4)


        #label
        self.lbl_special_saving = QLabel()
        self.lbl_special_saving.setText("Special savings. Exclusive savings for education, business, and more.")
        self.lbl_special_saving.setStyleSheet("font-size: 30px")
        #layout of label
        self.special_saving_lay = QHBoxLayout()
        #buttons
        self.special_saving_btn1 = QPushButton()
        self.special_saving_btn1.setFixedSize(345, 425)
        self.special_saving_btn2 = QPushButton()
        self.special_saving_btn2.setFixedSize(345, 425)
        self.special_saving_btn3 = QPushButton()
        self.special_saving_btn3.setFixedSize(345, 425)
        self.special_saving_btn4 = QPushButton()
        self.special_saving_btn4.setFixedSize(345, 425)

        self.special_saving_btn1.setIcon(QIcon(QPixmap("images\\special_saving_btn1.png")))
        self.special_saving_btn1.setIconSize(self.special_saving_btn1.size())
        self.special_saving_btn2.setIcon(QIcon(QPixmap("images\\special_saving_btn2.png")))
        self.special_saving_btn2.setIconSize(self.special_saving_btn2.size())
        self.special_saving_btn3.setIcon(QIcon(QPixmap("images\\special_saving_btn3.png")))
        self.special_saving_btn3.setIconSize(self.special_saving_btn3.size())
        self.special_saving_btn4.setIcon(QIcon(QPixmap("images\\special_saving_btn4.png")))
        self.special_saving_btn4.setIconSize(self.special_saving_btn4.size())

        self.special_saving_lay.addWidget(self.special_saving_btn1)
        self.special_saving_lay.addWidget(self.special_saving_btn2)
        self.special_saving_lay.addWidget(self.special_saving_btn3)
        self.special_saving_lay.addWidget(self.special_saving_btn4)


        #label at the end
        self.lbl_at_the_end = QLabel()
        self.lbl_at_the_end.setText("""
                                    ◊ Available for Qualified Purchasers only. Qualified Purchasers receive an Apple Gift Card when they purchase an Eligible Product at a Qualifying Location through September 30, 2024. 
                                    Gift card values may vary by Eligible Product. Only one Apple Gift Card per Eligible Product per Qualified Purchaser. Offer subject to availability. While supplies last. Qualified Purchasers 
                                    shall receive a discount equal to the value of the Apple Gift Card off the price of the Eligible Product, but will be charged for all items in their cart, including the Apple Gift Card. Important 
                                    notice regarding the checkout receipt and monthly statement for Apple Card Monthly Installments (ACMI) purchases with this promotion: Qualified Purchasers selecting ACMI (a 0% APR payment option 
                                    available only in the U.S.) as payment type at checkout shall receive a discount equal to the value of the Apple Gift Card off the price of the Eligible Product. This will result in one ACMI installment 
                                    plan over 12 months for the Eligible Product discounted by the instant credit, and a second ACMI installment plan over 12 months for the full price of the Apple Gift Card. The total combined amount charged 
                                    over the two separate ACMI installment plans will reflect the original full retail price of the Eligible Product. Separately, Qualified Purchasers will receive and be charged for the Apple Gift Card in 
                                    the amount of the applicable discount off the Eligible Product. Apple Card Monthly Installments (ACMI) is a 0% APR payment option that is only available if you select it at checkout in the U.S. for 
                                    eligible products purchased at Apple Store locations, apple.com, the Apple Store app, or by calling 1-800-MY-APPLE, and is subject to credit approval and credit limit. See https://support.apple.com/kb/HT211204 
                                    for more information about eligible products. APR ranges may vary based on when you accepted an Apple Card. Cardholders who accept an Apple Card on and/or after August 1, 2024: Variable APRs for Apple Card, other 
                                    than ACMI, range from 19.24% to 29.49% based on creditworthiness. Rates as of August 1, 2024. Existing cardholders: See your Customer Agreement for applicable rates and fee. If you buy an ACMI-eligible 
                                    product by choosing to pay in full with Apple Card (instead of using ACMI), that purchase is subject to the Apple Card variable APR, not 0% APR. Taxes and shipping on ACMI purchases are subject to the 
                                    variable APR, not 0% APR. When you buy an iPhone with ACMI, you’ll need to select AT&T, T-Mobile, or Verizon as your carrier when you check out. An iPhone purchased with ACMI is always unlocked, so you 
                                    can switch carriers at any time. ACMI is not available for purchases made online at the following special stores: Apple Employee Purchase Plan; participating corporate Employee Purchase Programs; Apple 
                                    at Work for small businesses; Government and Veterans and Military Purchase Programs; or on refurbished devices. The last month’s payment for each product will be the product's purchase price, less all 
                                    other payments at the monthly payment amount. ACMI financing is subject to change at any time for any reason, including but not limited to installment term lengths and eligible products. See 
                                    https://support.apple.com/kb/HT211204 for information about upcoming changes to ACMI financing. See the Apple Card Customer Agreement for more information about ACMI financing. Apple Card is issued 
                                    by Goldman Sachs Bank USA, Salt Lake City Branch. Available for qualifying applicants in the United States. If you reside in the U.S. territories, please call Goldman Sachs at 877-255-5923 with questions 
                                    about accessing this offer or applying for Apple Card. This offer cannot be combined with the Apple Employee Purchase Plan or business loyalty pricing. Additional restrictions apply. View full terms and 
                                    conditions of offer here.

                                    °°° The promotional Apple Education Pricing on AppleCare+ is available for eligible products only when the eligible product and AppleCare+ are purchased directly from an Apple Store or concurrently from 
                                    the online Apple Store for Education during the promotional period and cannot be combined with non-promotional Apple Education Pricing. AppleCare+ attached to eligible products outside of the promotional 
                                    period is not eligible for this promotional rate.

                                    This promotional AppleCare+ Education Pricing is applicable only to two-year paid upfront AppleCare+ for iPad and three-year paid upfront AppleCare+ for Mac and is not applicable to any recurring payment 
                                    AppleCare+ plans. In select Retail stores, the AppleCare+ Education Pricing may be available on select recurring payment AppleCare+ plans for iPad and Mac.

                                    Apple Education Pricing is available to current and newly accepted university students and their parents, as well as teachers and staff at all levels. Quantity limits apply.

                                    * Monthly pricing is available when you select Apple Card Monthly Installments (ACMI) as payment type at checkout at Apple, and is subject to credit approval and credit limit. Financing terms vary by product. 
                                    Taxes and shipping are not included in ACMI and are subject to your card’s variable APR. See the Apple Card Customer Agreement(Opens in a new window) for more information. ACMI is not available for purchases 
                                    made online at special storefronts. The last month’s payment for each product will be the product’s purchase price, less all other payments at the monthly payment amount. ACMI financing is subject to change at 
                                    any time for any reason, including but not limited to, installment term lengths and eligible products. See support.apple.com/kb/HT211204(Opens in a new window) for information about upcoming changes to ACMI financing.

                                    1. Trade‑in values will vary based on the condition, year, and configuration of your eligible trade‑in device. Not all devices are eligible for credit. You must be at least the age of majority to be eligible to trade 
                                    in for credit or for an Apple Gift Card. Trade‑in value may be applied toward qualifying new device purchase, or added to an Apple Gift Card. Actual value awarded is based on receipt of a qualifying device matching the 
                                    description provided when estimate was made. Sales tax may be assessed on full value of a new device purchase. In‑store trade‑in requires presentation of a valid photo ID (local law may require saving this information). 
                                    Offer may not be available in all stores, and may vary between in-store and online trade‑in. Some stores may have additional requirements. Apple or its trade‑in partners reserve the right to refuse, cancel, or limit 
                                    quantity of any trade‑in transaction for any reason. More details are available from Apple’s trade‑in partner for trade‑in and recycling of eligible devices. Restrictions and limitations may apply.

                                    2. Apple Card Monthly Installments (ACMI) is a 0% APR (Annual Percentage Rate) payment option that is only available if you select it at checkout in the U.S. for eligible products purchased at Apple Store locations, 
                                    apple.com(Opens in a new window), the Apple Store app, or by calling 1-800-MY-APPLE, and is subject to credit approval and credit limit. See Apple Support(Opens in a new window) for more information about eligible products. 
                                    APR ranges may vary based on when you accepted an Apple Card. Cardholders who accept an Apple Card on and/or after August 1, 2024: Variable APRs for Apple Card, other than ACMI, range from 19.24% to 29.49% based on creditworthiness. 
                                    Rates as of August 1, 2024. Existing cardholders: See your Customer Agreement for applicable rates and fee. If you buy an ACMI-eligible product by choosing to pay in full with Apple Card (instead of using ACMI), that purchase
                                    is subject to the Apple Card variable APR, not 0% APR. Taxes and shipping on ACMI purchases are subject to the variable APR, not 0% APR. When you buy an iPhone with ACMI, you’ll need to select AT&T, T-Mobile, or Verizon as your 
                                    carrier when you check out. An iPhone purchased with ACMI is always unlocked, so you can switch carriers at any time. ACMI is not available for purchases made online at the following special stores: Apple Employee Purchase Plan; 
                                    participating corporate Employee Purchase Programs; Apple at Work for small businesses; Government, and Veterans and Military Purchase Programs, or on refurbished devices. The last month’s payment for each product will be the 
                                    product’s purchase price, less all other payments at the monthly payment amount. ACMI financing is subject to change at any time for any reason, including but not limited to, installment term lengths and eligible products. See 
                                    Apple Support(Opens in a new window) for information about upcoming changes to ACMI financing. See the Apple Card Customer Agreement(Opens in a new window) for more information about ACMI financing.

                                    To access and use all Apple Card features and products available only to Apple Card users, you must add Apple Card to Wallet on an iPhone or iPad that supports and has the latest version of iOS or iPadOS. Apple Card is subject 
                                    to credit approval, available only for qualifying applicants in the United States, and issued by Goldman Sachs Bank USA, Salt Lake City Branch.

                                    If you reside in the U.S. territories, please call Goldman Sachs at 877-255-5923 with questions about Apple Card.

                                    3. Special pricing available to qualified customers. To learn more about how to start qualifying toward special pricing, talk to an Apple Specialist in a store or give us a call at 1‑800‑MY‑APPLE.

                                    ° Subscription required for Apple TV+.

                                    We approximate your location from your internet IP address by matching it to a geographic region or from the location entered during your previous visit to Apple.


                                    
            """)
        self.lbl_at_the_end.setStyleSheet("font-size: 13px")
        self.lbl_at_the_end.setAlignment(Qt.AlignCenter)

        





        
    







        










        # Adding all layouts to the main layout
        self.v_main.addLayout(self.buttons_at_top)
        self.v_main.addLayout(self.headline_lay)
        self.v_main.addLayout(self.h_theme_btns)
        self.v_main.addWidget(self.lbl_all_models)
        self.v_main.addLayout(self.all_models_lay)
        self.v_main.addWidget(self.lbl_shopping_guides)
        self.v_main.addLayout(self.shopping_guides_lay)
        self.v_main.addWidget(self.lbl_way_to_save)
        self.v_main.addLayout(self.way_to_save_lay)
        self.v_main.addWidget(self.lbl_difference)
        self.v_main.addWidget(self.difference_btn)
        self.v_main.addWidget(self.lbl_ipad_accessories)
        self.v_main.addLayout(self.ipad_accessories_lay)
        self.v_main.addWidget(self.lbl_setup)
        self.v_main.addLayout(self.setup_lay)
        self.v_main.addWidget(self.lbl_ipad_experience)
        self.v_main.addLayout(self.ipad_experience_lay)
        self.v_main.addWidget(self.lbl_special_saving)
        self.v_main.addLayout(self.special_saving_lay)
        self.v_main.addWidget(self.lbl_at_the_end)



        # Set the scroll area as the central widget
        layout = QVBoxLayout(self)
        layout.addWidget(vertical_scroll_area)
        self.setLayout(layout)

    def showMaximized(self):
        super().showMaximized()


    def Search_top_btn_message(self):
            search_top_btn_messagebox = QMessageBox()

            # Set the message box properties
            search_top_btn_messagebox.setWindowTitle("Message")
            search_top_btn_messagebox.setText("You can just search from the screen.")
            search_top_btn_messagebox.setIcon(QMessageBox.Information)
            search_top_btn_messagebox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            search_top_btn_messagebox.exec_()

    def Bag_top_btn_message(self):
         bag_messagebox = QMessageBox()

         bag_messagebox.setWindowTitle("Buy")
         bag_messagebox.setText("Choose what you want to buy")
         bag_messagebox.setIcon(QMessageBox.Information)
         bag_messagebox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
         bag_messagebox.exec_()

    def Need_help_btn(self):
         need_m = QMessageBox()
         need_m.setText("Not available in your country")
         need_m.setIcon(QMessageBox.Information)
         need_m.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
         need_m.exec_()
    def Visit_btn(self):
         visit_m = QMessageBox()
         visit_m.setText("Not available in your country")
         visit_m.setIcon(QMessageBox.Information)
         visit_m.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
         visit_m.exec_()
    

    def Ipad_pro_btn(self):
        ipad_pro_mbox = QMessageBox()
        ipad_pro_mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        ipad_pro_mbox.setDetailedText("""iPad Pro 11-inch
From $999or $83.25/mo. per month for 12 mo. months Footnote *
Buy- iPad Pro 11-inch
Apple M4 chip delivers outrageous performance for pro workflows and all-day battery life¹
Ultra Retina XDR display² with ProMotion, P3 wide color, and True Tone. Optional nano-texture glass.
Pro camera with LiDAR Scanner, and landscape 12MP Ultra Wide front camera with Center Stage
Stay connected with Wi-Fi 6E and 5G for superfast downloads and high-quality streaming³
Compatible with Apple Pencil Pro, Apple Pencil (USB-C), Magic Keyboard for iPad Pro, and Smart Folio⁴""")
        ipad_pro_mbox.exec_()
    
    def Ipad_air_btn(self):
         
        ipad_air_mbox = QMessageBox()
        ipad_air_mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        ipad_air_mbox.setDetailedText("""iPad Air 11-inch
From $599or $49.91/mo. per month for 12 mo. months Footnote *
Buy- iPad Air 11-inch
Apple M2 chip powers a huge leap in performance and all-day battery life¹
Liquid Retina display delivers a stunning, immersive viewing experience²
Landscape 12MP Ultra Wide front camera with Center Stage for a great video calling experience
Stay connected with Wi-Fi 6E and 5G for superfast downloads and high-quality streaming³
Compatible with Apple Pencil Pro, Apple Pencil (USB-C), Magic Keyboard, and Smart Folio⁴""")
        ipad_air_mbox.exec_()

    def Ipad_btn(self):
        ipad_mbox = QMessageBox()
        ipad_mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        ipad_mbox.setDetailedText("""
            Apple iPad (10th generation) hovering next to the Magic Keyboard Folio, angled to show the two-piece detachable design with adjustable stand, Apple Pencil (USB-C) in front.
Back stacked view of Silver, Yellow, Pink and Blue iPad showing the back camera and centred Apple logo.
12-megapixel Wide back camera, side volume buttons, Pink finish
Side view of iPad in Silver, Yellow, Pink and Blue, showing the side volume buttons, back camera and thin design

Available in 4 finishes
BluePinkYellowSilver
NEW PRICE
iPad
From $349or $29.08/mo. per month for 12 mo. months Footnote *
Buy- iPad
The A14 Bionic chip lets you run multiple apps and work smoothly between them
All-screen design with 10.9-inch Liquid Retina display¹ delivers an amazing viewing experience
Landscape 12MP Ultra Wide front camera with Center Stage for a great video calling experience
Stay connected with fast Wi‑Fi 6 and 5G wireless²
Compatible with Apple Pencil (USB‑C), Apple Pencil (1st generation),³ Magic Keyboard Folio, and Smart Folio⁴""")
        ipad_mbox.exec_()
    
    def Ipad_mini_btn(self):
        ipad_mini_mbox = QMessageBox()
        ipad_mini_mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        ipad_mini_mbox.setDetailedText("""Open Smart Folio wakes iPad mini display.
Back view of iPad mini showing all four colors.
Close-up of the back camera on iPad mini.
Side view of iPad mini in all four colors showing the thin design.

Available in 4 finishes
Space GrayPinkPurpleStarlight
iPad mini
From $499or $41.58/mo. per month for 12 mo. months Footnote *
Buy- iPad mini
A15 Bionic chip for incredible performance and all-day battery life footnote ¹
Stunning 8.3-inch Liquid Retina display with True Tone and P3 wide color footnote ²
12MP Ultra Wide front camera with Center Stage for great video calls
Stay connected with fast Wi‑Fi 6 and 5G wireless³
Compatible with Apple Pencil (2nd generation), Apple Pencil (USB-C), and Smart Folio⁴""")
        ipad_mini_mbox.exec_()
    
    def Explore_accessories(self):
        explore_mbox = QMessageBox()
        explore_mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        explore_mbox.setText("Ipad oldingmi uje, birinchi iPad ol keyin accessories olasan")
        explore_mbox.exec_()
    
    def Shopping1(self):
        shopping_m1 = QMessageBox()
        shopping_m1.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)    
        shopping_m1.setText("Puling yetgani")
        shopping_m1.exec_()
    def Shopping2(self):
        shopping_m2 = QMessageBox()
        shopping_m2.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)    
        shopping_m2.setText("Not aviable yet")
        shopping_m2.exec_()
    def Shopping3(self):
        shopping_m3 = QMessageBox()
        shopping_m3.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)    
        shopping_m3.setText("Not aviable in your country")
        shopping_m3.exec_()
    def Shopping4(self):
        shopping_m4 = QMessageBox()
        shopping_m4.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)    
        shopping_m4.setText("First Buy It")
        shopping_m4.exec_()






if __name__ == "__main__":
    app = QApplication(sys.argv)
    winIpad = IpadWindow()
    winIpad.showMaximized()
    sys.exit(app.exec_())

