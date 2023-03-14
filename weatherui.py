# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ASUS\Downloads\WeatherToday.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from cProfile import label
from turtle import color, title
import matplotlib.pyplot as plt
import numpy as np
from weather import get_weather_data,write_data
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Figurecanvas
URL = "https://www.google.com/search?lr=lang_en&ie=UTF-8&q=weather"
class canvas(Figurecanvas):
    def __init__(self, parent):
        _translate = QtCore.QCoreApplication.translate
        fig, self.ax = plt.subplots(figsize = (8,3.5), dpi = 200, nrows= 2, ncols= 2)
        super().__init__(fig)
        self.setObjectName("weather_today")
        self.setParent(parent)
        data_hcmc = get_weather_data(URL+"hochiminhcity")
        data_hn = get_weather_data(URL+"hanoi")
        data_dn = get_weather_data(URL+"danang")
        write_data(data_hn)
        write_data(data_hcmc)
        write_data(data_dn)

        next_day_name = []
        next_day_temp_max = []
        next_day_temp_min = []
        for dayweather in data_hn["next_days"]:
            next_day_name.append(dayweather["name"])
            next_day_temp_max.append(int(dayweather["max_temp"]))
            next_day_temp_min.append(int(dayweather["min_temp"]))
        next_day_name.pop(7)
        next_day_temp_max.pop(7)
        next_day_temp_min.pop(7)
        rects1 = self.ax[0][0].plot(next_day_name,next_day_temp_max,color = 'red',label = 'temp_max' )
        rects2 = self.ax[0][0].plot(next_day_name, next_day_temp_min,color = 'blue', label = 'temp_min')
        self.ax[0][0].set(xlabel = 'Day', ylabel = 'Temp', title = "HA NOI")
        fig.tight_layout()
        self.ax[0][0].grid()
        next_day_temp_max1 = []
        next_day_temp_min1 = []
        for dayweather in data_dn["next_days"]:
            next_day_temp_max1.append(int(dayweather["max_temp"]))
            next_day_temp_min1.append(int(dayweather["min_temp"]))
        next_day_temp_max1.pop(7)
        next_day_temp_min1.pop(7)
        rects1 = self.ax[0][1].plot(next_day_name,next_day_temp_max1,color = 'red',
                    label='temp_max')
        rects2 = self.ax[0][1].plot(next_day_name, next_day_temp_min1,color = 'blue',
                    label='temp_min')
        self.ax[0][1].set(xlabel = 'Day', ylabel = 'Temp',title = 'DA NANG')
        self.ax[0][1].grid()
        next_day_name2 = []
        next_day_temp_max2 = []
        next_day_temp_min2 = []
        for dayweather in data_hcmc["next_days"]:
            next_day_temp_max2.append(int(dayweather["max_temp"]))
            next_day_temp_min2.append(int(dayweather["min_temp"]))
        next_day_temp_max2.pop(7)
        next_day_temp_min2.pop(7)
        rects1 = self.ax[1][0].plot(next_day_name,next_day_temp_max2 ,color = 'red',
                    label='temp_max')
        rects2 = self.ax[1][0].plot(next_day_name, next_day_temp_min2,color = 'blue',
                    label='temp_min')
        self.ax[1][0].set(xlabel = 'Day', ylabel = 'Temp',title = 'thanh pho Ho Chi Minh')
        self.ax[1][0].grid()
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1600,700)
        chart = canvas(self)
class Ui_weatherui(object):
    def setupUi(self, weatherui):
        weatherui.setObjectName("weatherui")
        weatherui.resize(855, 606)
        self.buttonBox = QtWidgets.QDialogButtonBox(weatherui)
        self.buttonBox.setGeometry(QtCore.QRect(310, 390, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(weatherui)
        self.buttonBox.accepted.connect(weatherui.accept) # type: ignore
        self.buttonBox.rejected.connect(weatherui.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(weatherui)

    def retranslateUi(self, weatherui):
        _translate = QtCore.QCoreApplication.translate
        weatherui.setWindowTitle(_translate("weatherui", "Dialog"))

