from PyQt5.QtCore import QThread, pyqtSignal
import time


class qthread_example(QThread):
    trigger = pyqtSignal()

    def __init__(self):
        super().__init__()

    def emit_trigger(self):
        self.trigger.emit()

    def run(self):
        counter = 0
        while True:
            if(counter == 3):
                counter = 0
                self.emit_trigger()
                print("trigger emitted")
            print("tread is running")
            time.sleep(1)
            counter += 1


from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
import sys


class app_example(QMainWindow):
 
    def __init__(self):
        super().__init__()

        self.init_ui()

        self.counter = 0

        self.qthread_example = qthread_example()
        self.qthread_example.start()
        self.qthread_example.trigger.connect(self.change_label)


    def init_ui(self):
        """inits ui"""
        self.setWindowTitle("qtread example")

        self.move(100, 100)
        self.setFixedSize(300,50)

        self.labels()

        self.show()
        


    def labels(self):
        """adds labels"""
        self.l1 = QLabel(self)
        self.l1.setText("label")
        self.l1.setGeometry(10, 15, 270, 15)

    
    def change_label(self):
        self.counter += 1
        self.l1.setText("this is triggered from qthread counter:{}".format(self.counter))




app = QApplication(sys.argv)    
a = app_example()
sys.exit(app.exec())








