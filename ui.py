# -*- coding: utf-8 -*-

from PyQt5 import QtCore,QtWidgets
from PyQt5.QtGui import QPainter,QPolygon,QColor
from PyQt5.QtCore import QTimer
import numpy as np
from util import start,iteration_depth
from PyQt5.QtWidgets import QComboBox

algIndex = 0
m,iteration_time = start(0,0)
solutionNum = 1
model = 999


class Ui_Form(object):
    def setupUi(self,Form):
        Form.setObjectName("Form")
        Form.resize(950,800)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40,80,361,51))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0,0,0,0)
        self.gridLayout.setObjectName("gridLayout")


        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30,150,75,25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(30,200,75,25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(30,250,75,25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(30,300,75,25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(30,350,75,25))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(30,400,75,25))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(30,450,75,25))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(30,500,75,25))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(30,550,75,25))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setGeometry(QtCore.QRect(30,600,75,25))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(Form)
        self.pushButton_11.setGeometry(QtCore.QRect(30,650,75,25))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(Form)
        self.pushButton_12.setGeometry(QtCore.QRect(30,700,75,25))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(Form)
        self.pushButton_13.setGeometry(QtCore.QRect(30,750,75,25))
        self.pushButton_13.setObjectName("pushButton_13")

        # DropDownList
        q = QComboBox(self)  # define
        q.move(150,100)  # set position
        q.addItem("Depth First Search")
        q.addItem("Greedy Search")
        q.addItem("A* Search")
        q.addItem("Uniform Cost Search")
        q.addItem("Iterative Deepening")
        q.currentIndexChanged[int].connect(self.algorithm)

        # Label
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(700,150,200,50))
        self.label_5.setObjectName("label5")

        self.textBrowser = QtWidgets.QLabel(Form)
        self.textBrowser.setGeometry(QtCore.QRect(700,200,100,20))
        self.textBrowser.setObjectName("textBrowser")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10,80,131,41))
        # self.label_2 = QtWidgets.QLabel(Form)
        # self.label_2.setGeometry(QtCore.QRect(860, 120, 131, 41))
        # self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(60,20,891,41))
        self.label_3.setObjectName("label_3")
        self.next = QtWidgets.QPushButton(Form)
        self.next.setGeometry(QtCore.QRect(800,600,100,50))
        self.next.setObjectName("pushButton_2")

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(325,85,181,60))
        self.label_4.setObjectName("label_4")

        # total solution
        self.totalSolution = QtWidgets.QLabel(Form)
        self.totalSolution.setGeometry(QtCore.QRect(500,85,181,60))
        self.totalSolution.setObjectName("totalSolution")

        self.Draw = 0
        self.step = 0
        self.next.clicked.connect(self.clickButton_next)
        self.last = QtWidgets.QPushButton(Form)
        self.last.setGeometry(QtCore.QRect(700,600,100,50))
        self.last.setObjectName("pushButton_3")
        self.last.clicked.connect(self.clickButton_last)
        self.step = QtWidgets.QPushButton(Form)
        self.step.setGeometry(QtCore.QRect(700,550,200,50))
        self.step.setObjectName("show step")
        self.step.clicked.connect(self.clickButton_step)
        self.startButton = QtWidgets.QPushButton(Form)
        self.startButton.setGeometry(QtCore.QRect(700,500,200,50))
        self.startButton.setObjectName("start button")
        self.startButton.clicked.connect(self.clickButton_start)

        self.otherBtn = QtWidgets.QPushButton(Form)
        self.otherBtn.setGeometry(QtCore.QRect(30,100,75,25))
        self.otherBtn.setObjectName("otherbtn")
        self.otherBtn.clicked.connect(self.click_other)
        self.moreBtn = QtWidgets.QPushButton(Form)
        self.moreBtn.setGeometry(QtCore.QRect(30,50,75,25))
        self.moreBtn.setObjectName("moreBtn")
        self.moreBtn.clicked.connect(self.click_more)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self._index = 1
        self._step = iteration_depth
        self.Draw = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timeout)

        self._index = 1

    def click_other(self):
        global model
        model = -1
        self.update()
        print(model)

    def click_more(self):
        global model
        model = 999
        self.update()
        print(model)

    def algorithm(self,int):
        global algIndex
        algIndex = int
        # print("you choose ",int)
        return int

    def clickButton_start(self):
        global m,iteration_time,solutionNum,model
        solutionNum = 1
        self._index = solutionNum
        sender = self.sender()
        # print(sender.text() + 'is clicked')
        m,iteration_time = start(algIndex,model)
        self.update()

    # click last button, show the previous solution
    def clickButton_last(self):
        global solutionNum
        solutionNum = solutionNum if solutionNum == 1 else solutionNum - 1
        # print('last is clicked')
        self._index = self._index - 1
        self.update()

    # click next button, show the next solution
    def clickButton_next(self,i):
        global solutionNum
        solutionNum = solutionNum if solutionNum == len(m) else solutionNum + 1
        # print('next is clicked, solution ',solutionNum)
        self._index = self._index + 1
        self.update()

    # show Tangram pieces step by step
    def clickButton_step(self):
        sender = self.sender()
        # print(sender.text() + 'is clicked')
        self._step = 0
        self.timer.start(1000)

    def timeout(self):
        # print("time out")
        self._step = self._step + 1
        if self._step == iteration_depth:
            self.timer.stop()
        self.update()

    def Model_1(self):
        global model
        sender = self.sender()
        # print(sender.text() + 'is clicked')
        model = 0
        self.update()
        self.Draw = 1

    def Model_2(self):
        global model
        sender = self.sender()
        # print(sender.text() + 'is clicked')
        model = 1
        self.update()
        self.Draw = 2

    def Model_3(self):
        global model
        sender = self.sender()
        # print(sender.text() + 'is clicked')
        model = 2
        self.update()
        self.Draw = 3

    def Model_4(self):
        global model
        sender = self.sender()
        # print(sender.text() + 'is clicked')
        model = 3
        self.update()
        self.Draw = 4

    def Model_5(self):
        global model
        sender = self.sender()
        # print(sender.text() + 'is clicked')
        model = 4
        self.update()
        self.Draw = 5

    def Model_6(self):
        global model
        sender = self.sender()
        # print(sender.text() + 'is clicked')
        model = 5
        self.update()
        self.Draw = 6

    def Model_7(self):
        global model
        sender = self.sender()
        # print(sender.text() + 'is clicked')
        model = 6
        self.update()
        self.Draw = 7

    def Model_8(self):
        global model

        sender = self.sender()
        # print(sender.text() + 'is clicked')
        model = 7
        self.update()
        self.Draw = 8

    def Model_9(self):
        global model
        sender = self.sender()
        # print(sender.text() + 'is clicked')
        model = 8
        self.update()
        self.Draw = 9

    def Model_10(self):
        global model
        sender = self.sender()
        # print(sender.text() + 'is clicked')
        model = 9
        self.update()
        self.Draw = 10

    def Model_11(self):
        global model
        sender = self.sender()
        # print(sender.text() + 'is clicked')
        model = 10
        self.update()
        self.Draw = 11

    def Model_12(self):
        global model
        sender = self.sender()
        # print(sender.text() + 'is clicked')
        model = 11
        self.update()
        self.Draw = 12

    def Model_13(self):
        global model
        sender = self.sender()
        # print(sender.text() + 'is clicked')
        model = 12
        self.update()
        self.Draw = 13

    def retranslateUi(self,Form):
        # print("retranslateUI is called")
        _translate = QtCore.QCoreApplication.translate

        self.label.setText(_translate("Form",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Model</span></p></body></html>"))
        self.label_3.setText(_translate(
            "Form",
            "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#0055ff;\">Tangram Puzzle Solver</span></p></body></html>"))
        self.label_4.setText(_translate(
            "Form",
            "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Solution %d</span></p></body></html>" % solutionNum))
        self.next.setText(_translate("Form","Next"))
        self.last.setText(_translate("Form","Last"))
        self.step.setText(_translate("Form","Show Step"))
        self.otherBtn.setText(_translate("Form","heart"))
        self.moreBtn.setText(_translate("Form","more"))
        self.pushButton.setText(_translate("Form","Model 1"))
        self.pushButton_2.setText(_translate("Form","Model 2"))
        self.pushButton_3.setText(_translate("Form","Model 3"))
        self.pushButton_4.setText(_translate("Form","Model 4"))
        self.pushButton_5.setText(_translate("Form","Model 5"))
        self.pushButton_6.setText(_translate("Form","Model 6"))
        self.pushButton_7.setText(_translate("Form","Model 7"))
        self.pushButton_8.setText(_translate("Form","Model 8"))
        self.pushButton_9.setText(_translate("Form","Model 9"))
        self.pushButton_10.setText(_translate("Form","Model 10"))
        self.pushButton_11.setText(_translate("Form","Model 11"))
        self.pushButton_12.setText(_translate("Form","Model 12"))
        self.pushButton_13.setText(_translate("Form","Model 13"))
        self.startButton.setText(_translate("Form","Start"))

        self.label_5.setText(_translate("Form","Iteration time: "))
        self.textBrowser.setText(_translate("Form","%d" % iteration_time))

    def drawImage(self,painter,int):
        if (int == 0):
            painter.setPen(QColor(200,0,0))
            painter.setBrush(QColor(200,0,0))
        if (int == 1):
            painter.setPen(QColor(0,200,0))
            painter.setBrush(QColor(0,200,0))
        if (int == 2):
            painter.setPen(QColor(0,0,200))
            painter.setBrush(QColor(0,0,200))
        if (int == 3):
            painter.setPen(QColor(100,0,100))
            painter.setBrush(QColor(100,0,100))
        if (int == 4):
            painter.setPen(QColor(0,100,100))
            painter.setBrush(QColor(0,100,100))
        if (int == 5):
            painter.setPen(QColor(100,50,0))
            painter.setBrush(QColor(100,50,0))
        if (int == 6):
            painter.setPen(QColor(200,0,150))
            painter.setBrush(QColor(200,0,150))
        if (int == 7):
            painter.setPen(QColor(150,0,150))
            painter.setBrush(QColor(150,0,150))

    def paintEvent(self,e):
        # Parameter
        # column row pid number
        # m = [1, 3, 15, 2]
        painter = QPainter(self)
        if self.Draw == 1:
            painter.setPen(QColor(172,187,190))
            painter.setBrush(QColor(172,187,190))
            tinytri1 = QPolygon()
            tinytri1.setPoints(200,500,600,500,400,300,200,500)
            painter.drawPolygon(tinytri1)
        elif self.Draw == 2:
            painter.setPen(QColor(172,187,190))
            painter.setBrush(QColor(172,187,190))
            tinytri2 = QPolygon()
            tinytri2.setPoints(300,500,500,500,500,300,300,300,300,500)
            painter.drawPolygon(tinytri2)
        elif self.Draw == 3:
            painter.setPen(QColor(172,187,190))
            painter.setBrush(QColor(172,187,190))
            square = QPolygon()
            square.setPoints(200,400,300,500,500,300,400,200,200,400)
            painter.drawPolygon(square)
        elif self.Draw == 4:
            painter.setPen(QColor(172,187,190))
            painter.setBrush(QColor(172,187,190))
            bigtri1 = QPolygon()
            bigtri1.setPoints(200,500,400,500,600,300,400,300)
            painter.drawPolygon(bigtri1)
        elif self.Draw == 5:
            painter.setPen(QColor(172,187,190))
            painter.setBrush(QColor(172,187,190))
            bigtri2 = QPolygon()
            bigtri2.setPoints(300,500,600,200,400,200,300,300,300,500)
            painter.drawPolygon(bigtri2)
        elif self.Draw == 6:
            painter.setPen(QColor(172,187,190))
            painter.setBrush(QColor(172,187,190))
            smalltri1 = QPolygon()
            a = np.math.sqrt(2)
            smalltri1.setPoints(200,600,450,350,350,250,200,400,200,600)
            painter.drawPolygon(smalltri1)
        elif self.Draw == 7:
            painter.setPen(QColor(172,187,190))
            painter.setBrush(QColor(172,187,190))
            painter7 = QPolygon()
            a = np.math.sqrt(2)
            painter7.setPoints(200,500,500,500,300,300,200,300,200,500)
            painter.drawPolygon(painter7)
        elif self.Draw == 8:
            painter.setPen(QColor(172,187,190))
            painter.setBrush(QColor(172,187,190))
            painter8 = QPolygon()
            a = np.math.sqrt(2)
            painter8.setPoints(200,500,500,500,550,450,550,350,350,350,200,500)
            painter.drawPolygon(painter8)
        elif self.Draw == 9:
            painter.setPen(QColor(172,187,190))
            painter.setBrush(QColor(172,187,190))
            painter9 = QPolygon()
            a = np.math.sqrt(2)
            painter9.setPoints(200,500,250,550,450,350,400,300,200,300,200,500)
            painter.drawPolygon(painter9)
        elif self.Draw == 10:
            painter.setPen(QColor(172,187,190))
            painter.setBrush(QColor(172,187,190))
            painter10 = QPolygon()
            a = np.math.sqrt(2)
            painter10.setPoints(200,400,300,500,400,500,500,400,400,300,300,300,200,400)
            painter.drawPolygon(painter10)
        elif self.Draw == 11:
            painter.setPen(QColor(172,187,190))
            painter.setBrush(QColor(172,187,190))
            painter11 = QPolygon()
            a = np.math.sqrt(2)
            painter11.setPoints(200,400,250,450,450,450,550,350,500,300,300,300,200,400)
            painter.drawPolygon(painter11)
        elif self.Draw == 12:
            painter.setPen(QColor(172,187,190))
            painter.setBrush(QColor(172,187,190))
            painter12 = QPolygon()
            a = np.math.sqrt(2)
            painter12.setPoints(200,400,300,500,450,350,350,250,250,250,200,300,200,400)
            painter.drawPolygon(painter12)
        elif self.Draw == 13:
            painter.setPen(QColor(172,187,190))
            painter.setBrush(QColor(172,187,190))
            painter13 = QPolygon()
            a = np.math.sqrt(2)
            painter13.setPoints(200,500,300,500,450,350,450,250,350,250,200,400,200,500)
            painter.drawPolygon(painter13)

        global m

        # read step data

        d = len(m)
        if self._index > d:
            self._index = d
        if self._index < 1:
            self._index = 1
        x = self._index
        # print(m)
        for j in range(x - 1,x):
            for num in range(-1,7):
                color = m[j][num][3]
                if num > self._step - 1:
                    break
                if (m[j][num][2] == 8):
                    ini_2 = QPolygon()
                    ini_2.setPoints(m[j][num][1] * 50 + 200,m[j][num][0] * 50 + 150,m[j][num][1] * 50 + 250,
                                    m[j][num][0] * 50 +
                                    200,m[j][num][1] * 50 + 150,
                                    m[j][num][0] * 50 + 200,m[j][num][1] * 50 + 200,m[j][num][0] * 50 + 150)
                    painter.drawPolygon(ini_2)
                    self.drawImage(painter,color)
                # tiny triangle 2
                if (m[j][num][2] == 11):
                    ini_2 = QPolygon()
                    ini_2.setPoints(m[j][num][1] * 50 + 150,m[j][num][0] * 50 + 200,m[j][num][1] * 50 + 200,
                                    m[j][num][0] * 50 +
                                    250,m[j][num][1] * 50 + 200,
                                    m[j][num][0] * 50 + 150,m[j][num][1] * 50 + 150,m[j][num][0] * 50 + 200)
                    painter.drawPolygon(ini_2)
                    self.drawImage(painter,color)

                if (m[j][num][2] == 10):
                    ini_2 = QPolygon()
                    ini_2.setPoints(m[j][num][1] * 50 + 150,m[j][num][0] * 50 + 150,m[j][num][1] * 50 + 250,
                                    m[j][num][0] * 50 +
                                    150,m[j][num][1] * 50 + 200,
                                    m[j][num][0] * 50 + 200,m[j][num][1] * 50 + 150,m[j][num][0] * 50 + 150)
                    painter.drawPolygon(ini_2)
                    self.drawImage(painter,color)

                if (m[j][num][2] == 9):
                    ini_2 = QPolygon()
                    ini_2.setPoints(m[j][num][1] * 50 + 150,m[j][num][0] * 50 + 150,m[j][num][1] * 50 + 150,
                                    m[j][num][0] * 50 +
                                    250,m[j][num][1] * 50 + 200,
                                    m[j][num][0] * 50 + 200,m[j][num][1] * 50 + 150,m[j][num][0] * 50 + 150)
                    painter.drawPolygon(ini_2)
                    self.drawImage(painter,color)
                # square
                if (m[j][num][2] == 16):
                    ini_2 = QPolygon()
                    ini_2.setPoints(m[j][num][1] * 50 + 200,m[j][num][0] * 50 + 150,m[j][num][1] * 50 + 250,
                                    m[j][num][0] * 50 +
                                    200,m[j][num][1] * 50 + 200,
                                    m[j][num][0] * 50 + 250,m[j][num][1] *
                                    50 + 150,m[j][num][0] * 50 + 200,
                                    m[j][num][1] * 50 + 200,m[j][num][0] * 50 + 150)
                    painter.drawPolygon(ini_2)
                    self.drawImage(painter,color)
                # big triangle 1
                if (m[j][num][2] == 0):
                    ini_2 = QPolygon()
                    ini_2.setPoints(m[j][num][1] * 50 + 250,m[j][num][0] * 50 + 150,m[j][num][1] * 50 + 350,
                                    m[j][num][0] * 50 +
                                    250,m[j][num][1] * 50 + 150,
                                    m[j][num][0] * 50 + 250,m[j][num][1] * 50 + 250,m[j][num][0] * 50 + 150)
                    painter.drawPolygon(ini_2)
                    self.drawImage(painter,color)

                if (m[j][num][2] == 1):
                    ini_2 = QPolygon()
                    ini_2.setPoints(m[j][num][1] * 50 + 150,m[j][num][0] * 50 + 150,m[j][num][1] * 50 + 250,
                                    m[j][num][0] * 50 +
                                    250,m[j][num][1] * 50 + 150,
                                    m[j][num][0] * 50 + 350,m[j][num][1] * 50 + 150,m[j][num][0] * 50 + 150)
                    painter.drawPolygon(ini_2)
                    self.drawImage(painter,color)

                if (m[j][num][2] == 2):
                    ini_2 = QPolygon()
                    ini_2.setPoints(m[j][num][1] * 50 + 150,m[j][num][0] * 50 + 150,m[j][num][1] * 50 + 350,
                                    m[j][num][0] * 50 +
                                    150,m[j][num][1] * 50 + 250,
                                    m[j][num][0] * 50 + 250,m[j][num][1] * 50 + 150,m[j][num][0] * 50 + 150)
                    painter.drawPolygon(ini_2)
                    self.drawImage(painter,color)

                if (m[j][num][2] == 3):
                    ini_2 = QPolygon()
                    ini_2.setPoints(m[j][num][1] * 50 + 250,m[j][num][0] * 50 + 150,m[j][num][1] * 50 + 250,
                                    m[j][num][0] * 50 +
                                    350,m[j][num][1] * 50 + 150,
                                    m[j][num][0] * 50 + 250,m[j][num][1] * 50 + 250,m[j][num][0] * 50 + 150)
                    painter.drawPolygon(ini_2)
                    self.drawImage(painter,color)
                # small triangle
                if (m[j][num][2] == 6):
                    ini_2 = QPolygon()
                    ini_2.setPoints(m[j][num][1] * 50 + 150,m[j][num][0] * 50 + 150,m[j][num][1] * 50 + 250,
                                    m[j][num][0] * 50 +
                                    150,m[j][num][1] * 50 + 150,
                                    m[j][num][0] * 50 + 250,m[j][num][1] * 50 + 150,m[j][num][0] * 50 + 150)
                    painter.drawPolygon(ini_2)
                    self.drawImage(painter,color)

                if (m[j][num][2] == 5):
                    ini_2 = QPolygon()
                    ini_2.setPoints(m[j][num][1] * 50 + 150,m[j][num][0] * 50 + 150,m[j][num][1] * 50 + 250,
                                    m[j][num][0] * 50 +
                                    250,m[j][num][1] * 50 + 150,
                                    m[j][num][0] * 50 + 250,m[j][num][1] * 50 + 150,m[j][num][0] * 50 + 150)
                    painter.drawPolygon(ini_2)
                    self.drawImage(painter,color)

                if (m[j][num][2] == 4):
                    ini_2 = QPolygon()
                    ini_2.setPoints(m[j][num][1] * 50 + 250,m[j][num][0] * 50 + 150,m[j][num][1] * 50 + 250,
                                    m[j][num][0] * 50 +
                                    250,m[j][num][1] * 50 + 150,
                                    m[j][num][0] * 50 + 250,m[j][num][1] * 50 + 250,m[j][num][0] * 50 + 150)
                    painter.drawPolygon(ini_2)
                    self.drawImage(painter,color)

                if (m[j][num][2] == 7):
                    ini_2 = QPolygon()
                    ini_2.setPoints(m[j][num][1] * 50 + 150,m[j][num][0] * 50 + 150,m[j][num][1] * 50 + 250,
                                    m[j][num][0] * 50 +
                                    150,m[j][num][1] * 50 + 250,
                                    m[j][num][0] * 50 + 250,m[j][num][1] * 50 + 150,m[j][num][0] * 50 + 150)
                    painter.drawPolygon(ini_2)
                    self.drawImage(painter,color)
                # parallelogram
                if (m[j][num][2] == 12):
                    ini_2 = QPolygon()
                    ini_2.setPoints(m[j][num][1] * 50 + 200,m[j][num][0] * 50 + 150,m[j][num][1] * 50 + 300,
                                    m[j][num][0] * 50 +
                                    150,m[j][num][1] * 50 + 250,
                                    m[j][num][0] * 50 + 200,m[j][num][1] *
                                    50 + 150,m[j][num][0] * 50 + 200,
                                    m[j][num][1] * 50 + 200,m[j][num][0] * 50 + 150)
                    painter.drawPolygon(ini_2)
                    self.drawImage(painter,color)

                if (m[j][num][2] == 13):
                    ini_2 = QPolygon()
                    ini_2.setPoints(m[j][num][1] * 50 + 150,m[j][num][0] * 50 + 150,m[j][num][1] * 50 + 200,
                                    m[j][num][0] * 50 +
                                    200,m[j][num][1] * 50 + 200,
                                    m[j][num][0] * 50 + 300,m[j][num][1] *
                                    50 + 150,m[j][num][0] * 50 + 250,
                                    m[j][num][1] * 50 + 150,m[j][num][0] * 50 + 150)
                    painter.drawPolygon(ini_2)
                    self.drawImage(painter,color)

                if (m[j][num][2] == 14):
                    ini_2 = QPolygon()
                    ini_2.setPoints(m[j][num][1] * 50 + 150,m[j][num][0] * 50 + 200,m[j][num][1] * 50 + 200,
                                    m[j][num][0] * 50 +
                                    150,m[j][num][1] * 50 + 200,
                                    m[j][num][0] * 50 + 250,m[j][num][1] *
                                    50 + 150,m[j][num][0] * 50 + 300,
                                    m[j][num][1] * 50 + 150,m[j][num][0] * 50 + 200)
                    painter.drawPolygon(ini_2)
                    self.drawImage(painter,color)

                if (m[j][num][2] == 15):
                    ini_2 = QPolygon()
                    ini_2.setPoints(m[j][num][1] * 50 + 150,m[j][num][0] * 50 + 150,m[j][num][1] * 50 + 250,
                                    m[j][num][0] * 50 +
                                    150,m[j][num][1] * 50 + 300,
                                    m[j][num][0] * 50 + 200,m[j][num][1] *
                                    50 + 200,m[j][num][0] * 50 + 200,
                                    m[j][num][1] * 50 + 150,m[j][num][0] * 50 + 150)
                    painter.drawPolygon(ini_2)
                    self.drawImage(painter,color)

        # grid
        painter.setPen(QColor(0,0,0))
        line = QPolygon()

        for num1 in range(1,10):
            line.setPoints(150,150 + 50 * num1,650,150 + 50 * num1)
            painter.drawPolygon(line)
            line.setPoints(150 + 50 * num1,150,150 + 50 * num1,650)
            painter.drawPolygon(line)

        # update iteration value
        self.textBrowser.setText(QtCore.QCoreApplication.translate("Form",
                                                                   "<html><head/><body><p align=\"left\"><span style=\" font-size:12pt; font-weight:600;\">%d</span></p></body></html>" % iteration_time))
        self.label_4.setText(QtCore.QCoreApplication.translate(
            "Form",
            "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Solution %d</span></p></body></html>" % solutionNum))
        self.totalSolution.setText(QtCore.QCoreApplication.translate(
            "Form",
            "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Total: %d</span></p></body></html>" % len(
                m)))
