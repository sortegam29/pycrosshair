import sys
from PyQt5 import QtWidgets, QtCore, QtGui

class CrosshairOverlay(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.Tool |
            QtCore.Qt.WindowTransparentForInput
        )

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.resize(100, 100)

        screen = QtWidgets.QApplication.primaryScreen().geometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)

        pen = QtGui.QPen(QtGui.QColor("white"), 2)
        painter.setPen(pen)

        center_x = self.width() // 2
        center_y = self.height() // 2

        painter.drawLine(center_x, center_y - 10, center_x, center_y + 10)
        painter.drawLine(center_x - 10, center_y, center_x + 10, center_y)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

def run():
    app = QtWidgets.QApplication(sys.argv)
    overlay = CrosshairOverlay()
    overlay.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()