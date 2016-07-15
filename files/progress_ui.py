#!/usr/bin/env python3

# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget , QSizePolicy
from PyQt5.QtGui import QIcon
import ast , os
from newopen import Open

home_address = os.path.expanduser("~")
config_folder = str(home_address) + "/.config/persepolis_download_manager"

#setting
setting_file = config_folder + '/setting'
f = Open(setting_file)
setting_file_lines = f.readlines()
f.close()
setting_dict_str = str(setting_file_lines[0].strip())
setting_dict = ast.literal_eval(setting_dict_str) 

icons = str(setting_dict['icons']) + '/'


class ProgressWindow_Ui(QWidget):
    def __init__(self):
        super().__init__()

#window
        self.resize(595, 284)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(595, 284))
        self.setMaximumSize(QtCore.QSize(16777215, 16777215))

        self.setWindowIcon(QIcon('icon'))
        self.setWindowTitle("Persepolis Download Manager")


        self.gridLayout = QtWidgets.QGridLayout(self)
        self.verticalLayout = QtWidgets.QVBoxLayout()
#progress_tabWidget
        self.progress_tabWidget = QtWidgets.QTabWidget(self)
#informations_tab
        self.informations_tab = QtWidgets.QWidget()
#link_label
        self.link_label = QtWidgets.QLabel(self.informations_tab)
        self.link_label.setGeometry(QtCore.QRect(20, 10, 8000 , 16))
        
#status_label
        self.status_label = QtWidgets.QLabel(self.informations_tab)
        self.status_label.setGeometry(QtCore.QRect(20, 50, 500 , 16))
#downloaded_label
        self.downloaded_label = QtWidgets.QLabel(self.informations_tab)
        self.downloaded_label.setGeometry(QtCore.QRect(20, 70, 5000 , 16))
#save_label
        self.save_label = QtWidgets.QLabel(self.informations_tab)
        self.save_label.setGeometry(QtCore.QRect(20, 30, 5000 , 16))
#rate_label
        self.rate_label = QtWidgets.QLabel(self.informations_tab)
        self.rate_label.setGeometry(QtCore.QRect(20, 90, 5000 , 16))
#time_label
        self.time_label = QtWidgets.QLabel(self.informations_tab)
        self.time_label.setGeometry(QtCore.QRect(20, 110, 5000 , 16))

        self.connections_label = QtWidgets.QLabel(self.informations_tab)
        self.connections_label.setGeometry(QtCore.QRect(20, 130, 141, 16))
        self.progress_tabWidget.addTab(self.informations_tab, "")
#options_tab
        self.options_tab = QtWidgets.QWidget()
        self.widget = QtWidgets.QWidget(self.options_tab)
        self.widget.setGeometry(QtCore.QRect(30, 7, 511, 151))

        self.options_gridLayout = QtWidgets.QGridLayout(self.widget)
        self.options_gridLayout.setContentsMargins(0, 0, 0, 0)
#limit_checkBox
        self.limit_checkBox = QtWidgets.QCheckBox(self.widget)
        self.options_gridLayout.addWidget(self.limit_checkBox, 0, 0, 1, 1)
#after_checkBox
        self.after_checkBox = QtWidgets.QCheckBox(self.widget)
        self.options_gridLayout.addWidget(self.after_checkBox, 0, 1, 1, 1)
#limit_frame
        self.limit_frame = QtWidgets.QFrame(self.widget)
        self.limit_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.limit_frame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.widget1 = QtWidgets.QWidget(self.limit_frame)
        self.widget1.setGeometry(QtCore.QRect(44, 27, 151, 62))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
#limit_spinBox
        self.limit_spinBox = QtWidgets.QSpinBox(self.widget1)
        self.horizontalLayout.addWidget(self.limit_spinBox)
#limit_comboBox
        self.limit_comboBox = QtWidgets.QComboBox(self.widget1)
        self.limit_comboBox.addItem("")
        self.limit_comboBox.addItem("")
        self.horizontalLayout.addWidget(self.limit_comboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
#limit_pushButton
        self.limit_pushButton = QtWidgets.QPushButton(self.widget1)
        self.verticalLayout_2.addWidget(self.limit_pushButton)
        self.options_gridLayout.addWidget(self.limit_frame, 1, 0, 1, 1)
#after_frame
        self.after_frame = QtWidgets.QFrame(self.widget)
        self.after_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.after_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#after_comboBox
        self.widget = QtWidgets.QWidget(self.after_frame)
        self.widget.setGeometry(QtCore.QRect(77, 28, 150, 60))
 
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
 
        self.after_comboBox = QtWidgets.QComboBox(self.after_frame)
        self.after_comboBox.setGeometry(QtCore.QRect(73, 46, 111, 26))
        self.after_comboBox.addItem("")
        self.after_comboBox.addItem("")
        self.after_comboBox.addItem("")

        self.verticalLayout_3.addWidget(self.after_comboBox)
#after_pushButton    
        self.after_pushButton = QtWidgets.QPushButton(self.widget)
        self.verticalLayout_3.addWidget(self.after_pushButton)

        self.options_gridLayout.addWidget(self.after_frame, 1, 1, 1, 1)
        self.progress_tabWidget.addTab(self.options_tab, "")
        self.verticalLayout.addWidget(self.progress_tabWidget)



#download_progressBar
        self.download_progressBar = QtWidgets.QProgressBar(self)
        self.verticalLayout.addWidget(self.download_progressBar)

        self.button_horizontalLayout = QtWidgets.QHBoxLayout()
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.button_horizontalLayout.addItem(spacerItem)
#resume_pushButton
        self.resume_pushButton = QtWidgets.QPushButton(self)
        self.button_horizontalLayout.addWidget(self.resume_pushButton)
        self.resume_pushButton.setIcon(QIcon(icons + 'play'))
#pause_pushButton
        self.pause_pushButton = QtWidgets.QPushButton(self)
        self.button_horizontalLayout.addWidget(self.pause_pushButton)
        self.pause_pushButton.setIcon(QIcon(icons + 'pause'))
#stop_pushButton
        self.stop_pushButton = QtWidgets.QPushButton(self)
        self.button_horizontalLayout.addWidget(self.stop_pushButton)
        self.verticalLayout.addLayout(self.button_horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.stop_pushButton.setIcon(QIcon(icons + 'stop'))

        self.progress_tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)
#labels
        self.link_label.setText( "Link :")
        self.status_label.setText( "Status : ")
        self.downloaded_label.setText( "Downloaded :")
        self.save_label.setText( "Save as : ")
        self.rate_label.setText( "Transfer rate : ")
        self.time_label.setText( "Estimate time left :")
        self.connections_label.setText( "Number of connections : ")
        self.progress_tabWidget.setTabText(self.progress_tabWidget.indexOf(self.informations_tab),  "Download informations")
        self.limit_checkBox.setText( "Limit Speed")
        self.after_checkBox.setText( "After download")
        self.limit_comboBox.setItemText(0,  "KB/S")
        self.limit_comboBox.setItemText(1,  "MB/S")
        self.limit_pushButton.setText( "Apply")

        self.after_comboBox.setItemText(0,  "Shut Down as root")
        self.after_comboBox.setItemText(1,  "Shut Down")

        self.progress_tabWidget.setTabText(self.progress_tabWidget.indexOf(self.options_tab),  "Download Options")
        self.resume_pushButton.setText( "Resume")
        self.pause_pushButton.setText( "Pause")
        self.stop_pushButton.setText( "Stop")
        self.after_pushButton.setText("Apply")

