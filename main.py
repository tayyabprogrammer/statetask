"""
Main App Execution Window
Manages screen switching between modular files.
"""
import os
import sys

# QT_API initialization before any other imports
os.environ["QT_API"] = "pyside6"

from qtpy.QtWidgets import QApplication, QStackedWidget

# Custom files se screens import kiye
from splash_screen import SplashScreen
from login_screen import LoginScreen
from signup_screen import SignupScreen

class MainWindow(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MyApp")
        self.resize(360, 640) # Phone size emulation

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