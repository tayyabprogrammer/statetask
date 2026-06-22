"""
Simple Mobile App: Splash Screen + Login/Signup
Built with QtPy (using PySide6 backend) for Android/iOS deployment

QT_API must be set BEFORE importing anything from qtpy.
"""
import os
os.environ["QT_API"] = "pyside6"

import sys
from qtpy.QtWidgets import (
    QApplication, QWidget, QStackedWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QFrame
)
from qtpy.QtCore import Qt, QTimer
from qtpy.QtGui import QFont


# ---------------------------------------------------------
# Splash Screen
# ---------------------------------------------------------
class SplashScreen(QWidget):
    def __init__(self, on_finish):
        super().__init__()
        self.on_finish = on_finish
        self._build_ui()
        # Show splash for 2 seconds, then move to login
        QTimer.singleShot(2000, self.on_finish)

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)

        title = QLabel("MyApp")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Segoe UI", 32, QFont.Bold))
        title.setStyleSheet("color: #2D3142;")

        subtitle = QLabel("Loading...")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setFont(QFont("Segoe UI", 12))
        subtitle.setStyleSheet("color: #9C9C9C; margin-top: 10px;")

        layout.addWidget(title)
        layout.addWidget(subtitle)
        self.setStyleSheet("background-color: #FFFFFF;")


# ---------------------------------------------------------
# Login Screen
# ---------------------------------------------------------
class LoginScreen(QWidget):
    def __init__(self, switch_to_signup):
        super().__init__()
        self.switch_to_signup = switch_to_signup
        self._build_ui()

    def _build_ui(self):
        outer = QVBoxLayout(self)
        outer.setAlignment(Qt.AlignCenter)
        outer.setContentsMargins(40, 40, 40, 40)

        title = QLabel("Welcome Back")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Segoe UI", 22, QFont.Bold))
        title.setStyleSheet("color: #2D3142; margin-bottom: 20px;")

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
        switch_label.setStyleSheet("color: #9C9C9C; margin-top: 15px;")

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
        # Static UI only — no real auth logic yet
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


# ---------------------------------------------------------
# Signup Screen
# ---------------------------------------------------------
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
        title.setStyleSheet("color: #2D3142; margin-bottom: 20px;")

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
        switch_label.setStyleSheet("color: #9C9C9C; margin-top: 15px;")

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
        # Static UI only — no real auth logic yet
        name = self.name_input.text()
        print(f"Signup attempted with: {name}")


# ---------------------------------------------------------
# Main App Window (manages screen switching)
# ---------------------------------------------------------
class MainWindow(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MyApp")
        self.resize(360, 640)  # roughly phone-sized window for desktop testing

        self.splash = SplashScreen(self.show_login)
        self.login_screen = LoginScreen(self.show_signup)
        self.signup_screen = SignupScreen(self.show_login)

        self.addWidget(self.splash)
        self.addWidget(self.login_screen)
        self.addWidget(self.signup_screen)

        self.setCurrentWidget(self.splash)

    def show_login(self):
        self.setCurrentWidget(self.login_screen)

    def show_signup(self):
        self.setCurrentWidget(self.signup_screen)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
