from qtpy.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from qtpy.QtCore import Qt
from qtpy.QtGui import QFont

class LoginScreen(QWidget):
    def __init__(self, switch_to_signup):
        super().__init__()
        self.switch_to_signup = switch_to_signup
        self._build_ui()

    def _build_ui(self):
        outer = QVBoxLayout(self)
        outer.setAlignment(Qt.AlignCenter)
        outer.setContentsMargins(40, 40, 40, 40)

        title = QLabel("Login")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Segoe UI", 22, QFont.Bold))
        title.setStyleSheet("color: #2D3142; margin-bottom: 20px;background: transparent;")

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")
        self.email_input.setFixedHeight(45)
        self.email_input.setStyleSheet(self._input_style())

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setFixedHeight(45)
        self.password_input.setStyleSheet(self._input_style())

        login_btn = QPushButton("Log In")
        login_btn.setFixedHeight(45)
        login_btn.setCursor(Qt.PointingHandCursor)
        login_btn.setStyleSheet(self._button_style())
        login_btn.clicked.connect(self._handle_login)

        switch_label = QLabel("Don't have an account?")
        switch_label.setAlignment(Qt.AlignCenter)
        switch_label.setStyleSheet("color: #000000; margin-top: 15px;background: transparent;")

        signup_link = QPushButton("Sign Up")
        signup_link.setCursor(Qt.PointingHandCursor)
        signup_link.setStyleSheet("""
            QPushButton {
                color: #4A6CF7;
                background: transparent;
                border: none;
                font-weight: bold;
            }
        """)
        signup_link.clicked.connect(self.switch_to_signup)

        outer.addWidget(title)
        outer.addSpacing(10)
        outer.addWidget(self.email_input)
        outer.addSpacing(12)
        outer.addWidget(self.password_input)
        outer.addSpacing(20)
        outer.addWidget(login_btn)
        outer.addWidget(switch_label)
        outer.addWidget(signup_link, alignment=Qt.AlignCenter)

        self.setStyleSheet("background-color: #FFFFFF;")

    def _handle_login(self):
        email = self.email_input.text()
        print(f"Login attempted with: {email}")

    @staticmethod
    def _input_style():
        return """
            QLineEdit {
                border: 1px solid #E0E0E0;
                border-radius: 8px;
                padding-left: 12px;
                font-size: 14px;
                background-color: #F7F7F9;
            }
            QLineEdit:focus {
                border: 1px solid #4A6CF7;
            }
        """

    @staticmethod
    def _button_style():
        return """
            QPushButton {
                background-color: #4A6CF7;
                color: white;
                border-radius: 8px;
                font-size: 15px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #3A5CE0;
            }
            QPushButton:pressed {
                background-color: #2E4BC0;
            }
        """