# pip install pyqt5

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5 import QtGui
import sys



class App(QWidget):

    def __init__(self):
        super().__init__()

        self.init_variables()
        self.init_ui()
        self.action_listeners()


    
    def init_ui(self):
        """inits ui"""
        self.setWindowTitle("login")
        self.setGeometry(200,200,250,150)
        
        self.labels()
        self.buttons()
        self.line_edits()
        self.layouts()
        self.ui()

        self.show()
        

    def init_variables(self):
        """inits class variables"""
        pass


    def ui(self):
        """application design"""
        self.vertical_layout.addWidget(self.user_name_line)
        self.vertical_layout.addWidget(self.password_line)
        self.vertical_layout.addStretch()
        self.vertical_layout.addWidget(self.info_label)
        self.vertical_layout.addWidget(self.submit_button)

        self.horizontal_layout.addStretch()
        self.horizontal_layout.addLayout(self.vertical_layout)
        self.horizontal_layout.addStretch()

        self.setLayout(self.horizontal_layout)

    
    # ui elements
    def labels(self):
        """adds labels"""
        self.info_label = QLabel()
        self.info_label.setText("")


    def buttons(self):
        """adds buttons"""
        self.submit_button = QPushButton()
        self.submit_button.setText("submit")


    def line_edits(self):
        """adds line edits"""
        self.user_name_line = QLineEdit()
        self.user_name_line.setText("")
        
        self.password_line = QLineEdit()
        self.password_line.setText("")
        self.password_line.setEchoMode(QLineEdit.Password)


    def layouts(self):
        """adds layouts"""
        self.vertical_layout = QVBoxLayout()
        self.horizontal_layout = QHBoxLayout()



    # action listeners
    def action_listeners(self):
        """action listeners"""
        self.submit_button.clicked.connect(self.on_button_click)
        self.user_name_line.returnPressed.connect(self.on_line_edit_change)
        self.password_line.returnPressed.connect(self.on_line_edit_change)


    def on_button_click(self):
        """button click function for listeners"""
        sender = self.sender()
        if(sender.text() == "submit"):
            self.submit()


    def on_line_edit_change(self):
        """line edit change function for listeners"""
        self.submit()


  




    def submit(self):
        if(not self.password_line.text() or not self.user_name_line.text()):
            self.info_label.setText("fill all fields")
        else:
            self.info_label.setText("")
            print("form submitted")







application = QApplication(sys.argv)    

app = App()

sys.exit(application.exec_())