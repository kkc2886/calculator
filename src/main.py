import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon

class Calculator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('../image/icon.png'))
        self.resize(256,256)
        
        self.show()
        
if __name__=="__main__":
    app = QApplication(sys.argv)
    view = Calculator()
    sys.exit(app.exec_())
