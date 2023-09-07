import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTextEdit, QHBoxLayout, QVBoxLayout, QWidget

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        menubar = self.menuBar()

        file_menu = menubar.addMenu('File')
        edit_menu = menubar.addMenu('Edit')
        config_menu = menubar.addMenu('Config')

        label_num1 = QLabel('Enter the first number:')
        self.line_edit_num1 = QLineEdit()
        self.line_edit_num1.setStyleSheet("background-color: yellow;")
        self.line_edit_num1.setFixedWidth(150)

        label_num2 = QLabel('Enter the second number:')
        self.line_edit_num2 = QLineEdit()
        self.line_edit_num2.setStyleSheet("background-color: yellow;")
        self.line_edit_num2.setFixedWidth(150)

        self.result_text_edit = QTextEdit()
        self.result_text_edit.setStyleSheet("background-color: lightgreen; color: black;")
        self.result_text_edit.setReadOnly(True)

        add_button = QPushButton('+', self)
        subtract_button = QPushButton('-', self)
        multiply_button = QPushButton('*', self)
        divide_button = QPushButton('/', self)

        add_button.clicked.connect(self.calculate_add)
        subtract_button.clicked.connect(self.calculate_subtract)
        multiply_button.clicked.connect(self.calculate_multiply)
        divide_button.clicked.connect(self.calculate_divide)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(add_button)
        buttons_layout.addWidget(subtract_button)
        buttons_layout.addWidget(multiply_button)
        buttons_layout.addWidget(divide_button)

        result_layout = QHBoxLayout()
        result_label = QLabel('Result:')
        result_layout.addWidget(result_label)
        result_layout.addWidget(self.result_text_edit)
        result_layout.addStretch()

        first_num_layout = QHBoxLayout()
        first_num_layout.addWidget(label_num1)
        first_num_layout.addWidget(self.line_edit_num1)

        second_num_layout = QHBoxLayout()
        second_num_layout.addWidget(label_num2)
        second_num_layout.addWidget(self.line_edit_num2)

        main_layout = QVBoxLayout()
        main_layout.addLayout(first_num_layout)
        main_layout.addLayout(second_num_layout)
        main_layout.addLayout(buttons_layout)
        main_layout.addLayout(result_layout)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.setWindowTitle('Simple Calculator')
        self.setGeometry(100, 100, 400, 300)

    def calculate_add(self):
        try:
            num1 = float(self.line_edit_num1.text())
            num2 = float(self.line_edit_num2.text())
            result = num1 + num2
            self.result_text_edit.setPlainText(str(result))
        except ValueError:
            self.result_text_edit.setPlainText('Invalid input')

    def calculate_subtract(self):
        try:
            num1 = float(self.line_edit_num1.text())
            num2 = float(self.line_edit_num2.text())
            result = num1 - num2
            self.result_text_edit.setPlainText(str(result))
        except ValueError:
            self.result_text_edit.setPlainText('Invalid input')

    def calculate_multiply(self):
        try:
            num1 = float(self.line_edit_num1.text())
            num2 = float(self.line_edit_num2.text())
            result = num1 * num2
            self.result_text_edit.setPlainText(str(result))
        except ValueError:
            self.result_text_edit.setPlainText('Invalid input')

    def calculate_divide(self):
        try:
            num1 = float(self.line_edit_num1.text())
            num2 = float(self.line_edit_num2.text())
            if num2 != 0:
                result = num1 / num2
                self.result_text_edit.setPlainText(str(result))
            else:
                self.result_text_edit.setPlainText('Cannot divide by zero')
        except ValueError:
            self.result_text_edit.setPlainText('Invalid input')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = CalculatorApp()
    calculator.show()
    sys.exit(app.exec())
