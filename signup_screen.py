from qtpy.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from qtpy.QtCore import Qt
from qtpy.QtGui import QFont
from login_screen import LoginScreen # Input/Button styles reuse karne ke liye

class SignupScreen(QWidget):
    def __init__(self, switch_to_login):
        super().__init__()
        self.switch_to_login = switch_to_login
        self._build_ui()

    def _build_ui(self):
        outer = QVBoxLayout(self)
        outer.setAlignment(Qt.AlignCenter)
        outer.setContentsMargins(40, 40, 40, 40)

        title = QLabel("Create Account")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Segoe UI", 22, QFont.Bold))
        title.setStyleSheet("color: #2D3142; margin-bottom: 20px;background: transparent;")

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Full Name")
        self.name_input.setFixedHeight(45)
        self.name_input.setStyleSheet(LoginScreen._input_style())

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")
        self.email_input.setFixedHeight(45)
        self.email_input.setStyleSheet(LoginScreen._input_style())

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setFixedHeight(45)
        self.password_input.setStyleSheet(LoginScreen._input_style())

        signup_btn = QPushButton("Sign Up")
        signup_btn.setFixedHeight(45)
        signup_btn.setCursor(Qt.PointingHandCursor)
        signup_btn.setStyleSheet(LoginScreen._button_style())
        signup_btn.clicked.connect(self._handle_signup)

        switch_label = QLabel("Already have an account?")
        switch_label.setAlignment(Qt.AlignCenter)
        switch_label.setStyleSheet("color: #000000; margin-top: 15px;background: transparent;")

        login_link = QPushButton("Log In")
        login_link.setCursor(Qt.PointingHandCursor)
        login_link.setStyleSheet("""
            QPushButton {
                color: #4A6CF7;
                background: transparent;
                border: none;
                font-weight: bold;
            }
        """)
        login_link.clicked.connect(self.switch_to_login)

        outer.addWidget(title)
        outer.addSpacing(10)
        outer.addWidget(self.name_input)
        outer.addSpacing(12)
        outer.addWidget(self.email_input)
        outer.addSpacing(12)
        outer.addWidget(self.password_input)
        outer.addSpacing(20)
        outer.addWidget(signup_btn)
        outer.addWidget(switch_label)
        outer.addWidget(login_link, alignment=Qt.AlignCenter)

        self.setStyleSheet("background-color: #FFFFFF;")

    def _handle_signup(self):
        name = self.name_input.text()
        print(f"Signup attempted with: {name}")