# pip install pyqt5

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, qApp
from PyQt5.QtWidgets import QCheckBox, QLabel, QLineEdit, QPushButton, QRadioButton, QButtonGroup, QTextEdit, QFileDialog, QAction
from PyQt5 import QtGui
import sys
import os


class app(QMainWindow):
 
    def __init__(self):
        super().__init__()

        self.init_variables()
        self.init_ui()


    def init_ui(self):
        """inits ui"""
        self.setWindowTitle("example window")
        # self.setGeometry(100,100,700,700)
        self.move(100, 100)
        self.setFixedSize(700,700)

        self.labels()
        self.buttons()
        self.line_edits()
        self.checkboxes()
        self.radiobuttons()
        self.text_edits()
        self.menu_bar()

        self.show()
        

    def init_variables(self):
        """inits class variables"""
        self.button_counter = 0
        self.img1_path = "pyqt5/images/img.png"
        self.file_dialog_path = ""

 
    def labels(self):
        """adds labels"""
        self.l1 = QLabel(self)
        self.l1.setText("label 1")
        # self.l1.move(120, 230)
        self.l1.setGeometry(120, 230, 100, 10)

        # add image
        self.l2 = QLabel(self)
        self.l2.setPixmap(QtGui.QPixmap(self.img1_path))
        self.l2.setGeometry(0, 0, 700, 200)


    def buttons(self):
        """adds buttons"""
        self.b1 = QPushButton(self)
        self.b1.setText("counter")
        self.b1.move(10, 220)
        self.b1.clicked.connect(self.on_click)
        
        self.b2 = QPushButton(self)
        self.b2.setText("clear")
        self.b2.move(10, 270)
        self.b2.clicked.connect(self.on_click)

        self.b3 = QPushButton(self)
        self.b3.setText("open file dialog")
        self.b3.move(10, 420)
        self.b3.clicked.connect(self.on_click)

    def line_edits(self):
        """adds line edits"""
        self.line1 = QLineEdit(self)
        self.line1.setText("")
        self.line1.move(120, 270)
    

    def checkboxes(self):
        """adds checkboxes"""
        self.checkbox1 = QCheckBox(self)
        self.checkbox1.setText("checkbox example")
        self.checkbox1.move(10, 320)
        self.checkbox1.setObjectName("checkbox1")
        # self.checkbox1.setDisabled(True)

        self.checkbox1.clicked.connect(self.on_click)


    def radiobuttons(self):
        """adds radiobuttons"""
        self.radiobutton1 = QRadioButton(self)
        self.radiobutton1.setText("radiobutton 1")
        self.radiobutton1.move(10, 370)
        self.radiobutton1.setObjectName("radiobutton1")
        self.radiobutton1.clicked.connect(self.on_click)

        self.radiobutton2 = QRadioButton(self)
        self.radiobutton2.setText("radiobutton 2")
        self.radiobutton2.move(120, 370)
        self.radiobutton2.setObjectName("radiobutton2")
        self.radiobutton2.clicked.connect(self.on_click)

        self.radiobutton3 = QRadioButton(self)
        self.radiobutton3.setText("radiobutton 3")
        self.radiobutton3.move(230, 370)
        self.radiobutton3.setObjectName("radiobutton3")
        self.radiobutton3.clicked.connect(self.on_click)


        # button groups
        self.button_group1 = QButtonGroup()
        self.button_group1.addButton(self.radiobutton1)
        self.button_group1.addButton(self.radiobutton2)
        self.button_group1.setObjectName("button_group1")

        # this can listen all buttons in the group but it has no attribute calles .text() 
        # so you cant use single listener function with it or use objectname()
        # self.button_group1.buttonClicked.connect(self.on_click)  


        self.button_group2 = QButtonGroup()
        self.button_group2.addButton(self.radiobutton3)
        self.button_group2.setObjectName("button_group2")


    def text_edits(self):
        """adds text edits"""
        self.te1 = QTextEdit(self)
        self.te1.setGeometry(350, 220, 300, 200)
        self.te1.setText("this is a biiiiiig text field")


    def menu_bar(self):
        """adds menu bar and actions under it"""
        # menu items
        self.bar = self.menuBar()

        self.file_menu = self.bar.addMenu("file")
        self.file_menu.triggered.connect(self.on_menu_click)

        self.edit_menu = self.bar.addMenu("edit")

        self.sub_menu = self.edit_menu.addMenu("sub menu")

        # actions
        self.open_file_function = QAction("open file", self)
        self.open_file_function.setShortcut("Ctrl+O")
        self.open_file_function.setObjectName("open_file_function")
        self.open_file_function.triggered.connect(self.on_click)
        self.file_menu.addAction(self.open_file_function)

        self.test_trigger = QAction("test trigger", self)
        self.test_trigger.setObjectName("test_trigger")
        self.file_menu.addAction(self.test_trigger)
        

        self.exit_function = QAction("exit", self)
        self.exit_function.setShortcut("Ctrl+Q")
        self.exit_function.setObjectName("exit")
        self.exit_function.triggered.connect(self.on_click)
        self.sub_menu.addAction(self.exit_function)
        



    def open_file(self):
        """opens file dialog"""
        file_name = QFileDialog.getOpenFileName(self, "file dialog example", self.file_dialog_path)
        print(file_name)
        
        if(os.path.exists(file_name[0])):
            return file_name[0]
        else:
            return None
    


    def on_menu_click(self, action):
        """triggers on menu clicks"""
        if(action.text() == "open file"):
            print("open file used")
        if(action.text() == "test trigger"):
            print("test trigger used")


    def on_click(self):
        """button click function for listeners"""
        sender = self.sender()

        # buttons
        if(sender.text() == "counter"):
            self.button_counter += 1
            self.l1.setText("counter is:{}".format(self.button_counter))
        elif(sender.text() == "clear"):
            self.line1.setText("")
        elif(sender.text() == "open file dialog"):
            self.open_file()

        # checkboxes
        elif(sender.objectName() == "checkbox1"):
            if(self.checkbox1.isChecked()):
                self.checkbox1.setText("checked")
            else:
                self.checkbox1.setText("not checked")

        # radiobuttons
        elif(sender.objectName() == "radiobutton1"):
            self.radiobutton1.setText("hi there")
        elif(sender.objectName() == "radiobutton2"):
            self.radiobutton2.setText("hi there")
        elif(sender.objectName() == "radiobutton3"):
            self.radiobutton3.setText("hi there")

        # menu items
        elif(sender.objectName() == "exit"):
            sys.exit()
        elif(sender.objectName() == "open_file_function"):
            self.open_file()

        print(sender.objectName())
        




application = QApplication(sys.argv)    

a = app()

sys.exit(application.exec_())