'''
Author: mukangt
Date: 2021-07-14 15:45:20
LastEditors: mukangt
LastEditTime: 2021-07-15 08:45:52
Description: 
'''
from PyQt5 import QtCore, QtGui, QtWidgets


class ListItem(QtWidgets.QListWidgetItem):
    def __init__(self, filename: str, pointSize: int = 10):
        super().__init__()

        self.setText(filename)
        # self.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        # self.setCheckState(QtCore.Qt.CheckState.Checked)

        font = QtGui.QFont()
        font.setPointSize(pointSize)
        self.setFont(font)