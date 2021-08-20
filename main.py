from PyQt5 import QtWidgets
from ui import Ui_Form


class mywindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Model_1)
        self.pushButton_2.clicked.connect(self.Model_2)
        self.pushButton_3.clicked.connect(self.Model_3)
        self.pushButton_4.clicked.connect(self.Model_4)
        self.pushButton_5.clicked.connect(self.Model_5)
        self.pushButton_6.clicked.connect(self.Model_6)
        self.pushButton_7.clicked.connect(self.Model_7)
        self.pushButton_8.clicked.connect(self.Model_8)
        self.pushButton_9.clicked.connect(self.Model_9)
        self.pushButton_10.clicked.connect(self.Model_10)
        self.pushButton_11.clicked.connect(self.Model_11)
        self.pushButton_12.clicked.connect(self.Model_12)
        self.pushButton_13.clicked.connect(self.Model_13)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())
