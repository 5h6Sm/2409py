from PyQt5 import QtWidgets
from PyQt5 import QtCore


class Mywindows(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("파이썬푸시버튼")

        button = QtWidgets.QPushButton(self)
        button.setText("일반 버튼")

        disablebutton = QtWidgets.QPushButton(self)
        disablebutton.setText("비활성화버튼")
        disablebutton.setEnabled(False)

        checkButton = QtWidgets.QPushButton(self)
        checkButton.setText("체크버튼")
        checkButton.setCheckable(True)
        checkButton.toggle

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(button)
        layout.addWidget(disablebutton)
        layout.addWidget(checkButton)

        self.setLayout(layout)
        self.resize(400, 300)
        self.show()


app = QtWidgets.QApplication([])
win = Mywindows()
app.exec_()

# 위의 세줄은 항상 써주기!
