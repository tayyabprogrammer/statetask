from qtpy.QtWidgets import QWidget, QVBoxLayout, QLabel
from qtpy.QtCore import Qt, QTimer
from qtpy.QtGui import QFont

class SplashScreen(QWidget):
    def __init__(self, on_finish):
        super().__init__()
        self.on_finish = on_finish
        self._build_ui()
        # Show splash for 2 seconds, then move to login
        QTimer.singleShot(4000, self.on_finish)

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)

        title = QLabel("State Life")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Segoe UI", 32, QFont.Bold))
        title.setStyleSheet("color: #576EC9;background: transparent;")

        subtitle = QLabel("Insurance Corporation of Pakistan")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setFont(QFont("Segoe UI", 12))
        subtitle.setStyleSheet("color: #000000; margin-top: 10px;background: transparent;")

        layout.addWidget(title)
        layout.addWidget(subtitle)
        self.setStyleSheet("background-color: #FFFFFF;")