from PyQt5 import QtWidgets


class Mywindows(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("파이썬GUI")
        self.resize(400, 300)
        self.show()


app = QtWidgets.QApplication([])
win = Mywindows()
app.exec_()

# 위의 세줄은 항상 써주기!
