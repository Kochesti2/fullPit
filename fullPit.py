#!/usr/bin/env python3
packages = ["sys" , "math"]
import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget , QLabel, QTextEdit, QGridLayout, QPushButton, QMessageBox
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.main()




    def main(self):

        def calc_leg(f,s):
            if f > s :
                return math.sqrt(math.pow(f,2)-math.pow(s,2))
            else :
                return  math.sqrt(math.pow(s,2)-math.pow(f,2))

        def on_click(self):
            firstStr = str(txt1.toPlainText())
            secondStr = str(txt2.toPlainText())
            thirdStr = str(txt3.toPlainText())

            if (firstStr=="" and secondStr=="") or (firstStr=="" and thirdStr=="") or (secondStr=="" and thirdStr==""):
                QMessageBox.information(QWidget(), "Message", "What should I do with empty fields?")
                return None
            if (firstStr!="" and secondStr!="" and thirdStr!=""):
                QMessageBox.information(QWidget(), "Message", "Please clear at least one box")
                return None

            if thirdStr=="":
                try:
                    param1 = float(txt1.toPlainText())
                except:
                    QMessageBox.information(QWidget(), "Message", "What the heck of input is that?")
                    txt1.setText("")
                    try:
                        param2 = float(txt2.toPlainText())
                    except:
                        txt2.setText("")
                    return None


                try:
                    param2 = float(txt2.toPlainText())
                except:
                    QMessageBox.information(QWidget(), "Message", "What the heck of input is that?")
                    txt2.setText("")
                    return None

                hip = math.sqrt(math.pow(param1,2)+math.pow(param2,2))
                txt3.setText("%.2f" % hip)


            if secondStr=="":
                try:
                    param1 = float(txt1.toPlainText())
                except:
                    QMessageBox.information(QWidget(), "Message", "What the heck of input is that?")
                    txt1.setText("")
                    try:
                        param2 = float(txt3.toPlainText())
                    except:
                        txt3.setText("")
                    return None


                try:
                    param2 = float(txt3.toPlainText())
                except:
                    QMessageBox.information(QWidget(), "Message", "What the heck of input is that?")
                    txt3.setText("")
                    return None

                hip = calc_leg(param1,param2)
                txt2.setText("%.2f" % hip)

            if firstStr=="":
                try:
                    param1 = float(txt2.toPlainText())
                except:
                    QMessageBox.information(QWidget(), "Message", "What the heck of input is that?")
                    txt1.setText("")
                    try:
                        param2 = float(txt3.toPlainText())
                    except:
                        txt3.setText("")
                    return None


                try:
                    param2 = float(txt3.toPlainText())
                except:
                    QMessageBox.information(QWidget(), "Message", "What the heck of input is that?")
                    txt3.setText("")
                    return None

                hip = calc_leg(param1,param2)
                txt1.setText("%.2f" % hip)

        grid = QGridLayout()
        grid.setSpacing(5)
        self.setStyleSheet("QWidget {background: 'yellow';}");

        #calcoli per lo schermo
        screen = app.primaryScreen()
        size = screen.size()
        sizeWith = size.width()/4
        sizeHeight = size.height()/3

        #labels
        lab1=QLabel()
        lab1.setText("Insert the first side")
        lab1.setAlignment(Qt.AlignCenter)
        grid.addWidget(lab1)


        txt1=QTextEdit()
        txt1.setText("")
        grid.addWidget(txt1)


        lab2=QLabel()
        lab2.setText("Insert the second side")
        lab2.setAlignment(Qt.AlignCenter)
        grid.addWidget(lab2)

        txt2=QTextEdit()
        txt2.setText("")
        grid.addWidget(txt2)

        button = QPushButton("Calculate")
        button.setToolTip('Calculate')
        grid.addWidget(button)

        txt3=QTextEdit()
        txt3.setText("")
        grid.addWidget(txt3)

        button.clicked.connect(on_click)





        self.resize(sizeWith, sizeHeight)
        self.move(300, 300)
        self.setWindowTitle('Pitagora')
        self.setLayout(grid)
        self.show()

        #sys.exit(app.exec_())


if __name__ == '__main__':
    app = QApplication(sys.argv)


    wid = MyWidget()


    sys.exit(app.exec_())
