# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(627, 366)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(440, 220, 97, 26))
        self.start_button.setObjectName("start_button")
        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_button.setGeometry(QtCore.QRect(440, 250, 97, 26))
        self.stop_button.setObjectName("stop_button")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 411, 301))
        self.graphicsView.setObjectName("graphicsView")
        self.emotion_label = QtWidgets.QLabel(self.centralwidget)
        self.emotion_label.setGeometry(QtCore.QRect(430, 10, 181, 17))
        self.emotion_label.setObjectName("emotion_label")
        self.gaze_label = QtWidgets.QLabel(self.centralwidget)
        self.gaze_label.setGeometry(QtCore.QRect(430, 30, 181, 17))
        self.gaze_label.setObjectName("gaze_label")
        self.heart_label = QtWidgets.QLabel(self.centralwidget)
        self.heart_label.setGeometry(QtCore.QRect(430, 50, 181, 17))
        self.heart_label.setObjectName("heart_label")
        self.gsr_label = QtWidgets.QLabel(self.centralwidget)
        self.gsr_label.setGeometry(QtCore.QRect(430, 70, 181, 17))
        self.gsr_label.setObjectName("gsr_label")
        self.emotion_output_label = QtWidgets.QLabel(self.centralwidget)
        self.emotion_output_label.setGeometry(QtCore.QRect(440, 120, 151, 17))
        self.emotion_output_label.setObjectName("emotion_output_label")
        self.gaze_output_label = QtWidgets.QLabel(self.centralwidget)
        self.gaze_output_label.setGeometry(QtCore.QRect(440, 140, 151, 17))
        self.gaze_output_label.setObjectName("gaze_output_label")
        self.heart_output_label = QtWidgets.QLabel(self.centralwidget)
        self.heart_output_label.setGeometry(QtCore.QRect(440, 160, 151, 17))
        self.heart_output_label.setObjectName("heart_output_label")
        self.gsr_output_label = QtWidgets.QLabel(self.centralwidget)
        self.gsr_output_label.setGeometry(QtCore.QRect(440, 180, 151, 17))
        self.gsr_output_label.setObjectName("gsr_output_label")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(440, 280, 97, 26))
        self.save_button.setObjectName("save_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 627, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.stop_button.setText(_translate("MainWindow", "Stop"))
        self.emotion_label.setText(_translate("MainWindow", "・Emotion Software"))
        self.gaze_label.setText(_translate("MainWindow", "・Gaze Tracking Software"))
        self.heart_label.setText(_translate("MainWindow", "・Heart Rate Device"))
        self.gsr_label.setText(_translate("MainWindow", "・GSR Device"))
        self.emotion_output_label.setText(_translate("MainWindow", "Emotion: N/A"))
        self.gaze_output_label.setText(_translate("MainWindow", "Gaze: N/A"))
        self.heart_output_label.setText(_translate("MainWindow", "Heart: N/A"))
        self.gsr_output_label.setText(_translate("MainWindow", "GSR: N/A"))
        self.save_button.setText(_translate("MainWindow", "Save"))

