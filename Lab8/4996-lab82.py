import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QColorDialog, QFontDialog

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.initMenu()

    def initUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle("Calculator App")

        label1 = QLabel('Enter the first number:', self)
        label1.setGeometry(20, 30, 150, 30)
        self.line_edit1 = QLineEdit(self)
        self.line_edit1.setGeometry(180, 30, 100, 30)

        label2 = QLabel('Enter the second number:', self)
        label2.setGeometry(20, 70, 150, 30)
        self.line_edit2 = QLineEdit(self)
        self.line_edit2.setGeometry(180, 70, 100, 30)

        self.result_label = QLabel('Result:', self)
        self.result_label.setGeometry(20, 150, 150, 30)

        self.result_text = QTextEdit(self)
        self.result_text.setGeometry(180, 150, 150, 100)
        self.result_text.setStyleSheet("background-color: lightgreen")

        plus_button = QPushButton('+', self)
        plus_button.setGeometry(20, 110, 40, 30)
        plus_button.clicked.connect(self.add_numbers)

        minus_button = QPushButton('-', self)
        minus_button.setGeometry(70, 110, 40, 30)
        minus_button.clicked.connect(self.subtract_numbers)

        multiply_button = QPushButton('*', self)
        multiply_button.setGeometry(120, 110, 40, 30)
        multiply_button.clicked.connect(self.multiply_numbers)

        divide_button = QPushButton('/', self)
        divide_button.setGeometry(170, 110, 40, 30)
        divide_button.clicked.connect(self.divide_numbers)

    def initMenu(self):
        menubar = self.menuBar()

        # File menu
        file_menu = menubar.addMenu('File')
        save_action = QAction('Save', self)
        save_action.triggered.connect(self.save_result)
        file_menu.addAction(save_action)

        open_action = QAction('Open', self)
        open_action.triggered.connect(self.open_result)
        file_menu.addAction(open_action)

        clear_action = QAction('Clear', self)
        clear_action.triggered.connect(self.clear_result)
        file_menu.addAction(clear_action)

        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(self.exit_program)
        file_menu.addAction(exit_action)

        # Edit menu
        edit_menu = menubar.addMenu('Edit')

        copy_action = QAction('Copy', self)
        copy_action.triggered.connect(self.copy_text)
        edit_menu.addAction(copy_action)

        paste_action = QAction('Paste', self)
        paste_action.triggered.connect(self.paste_text)
        edit_menu.addAction(paste_action)

        cut_action = QAction('Cut', self)
        cut_action.triggered.connect(self.cut_text)
        edit_menu.addAction(cut_action)

        # Config menu
        config_menu = menubar.addMenu('Config')

        color_action = QAction('Color', self)
        color_action.triggered.connect(self.change_color)
        config_menu.addAction(color_action)

        size_action = QAction('Size', self)
        size_action.triggered.connect(self.change_size)
        config_menu.addAction(size_action)

    def add_numbers(self):
        num1 = float(self.line_edit1.text())
        num2 = float(self.line_edit2.text())
        result = num1 + num2
        self.result_text.setPlainText(str(result))

    def subtract_numbers(self):
        num1 = float(self.line_edit1.text())
        num2 = float(self.line_edit2.text())
        result = num1 - num2
        self.result_text.setPlainText(str(result))

    def multiply_numbers(self):
        num1 = float(self.line_edit1.text())
        num2 = float(self.line_edit2.text())
        result = num1 * num2
        self.result_text.setPlainText(str(result))

    def divide_numbers(self):
        num1 = float(self.line_edit1.text())
        num2 = float(self.line_edit2.text())
        if num2 == 0:
            self.result_text.setPlainText("Error: Division by zero")
        else:
            result = num1 / num2
            self.result_text.setPlainText(str(result))

    def save_result(self):
        result_text = self.result_text.toPlainText()
        try:
            with open('result.txt', 'w') as file:
                file.write(result_text)
            QMessageBox.information(self, 'Information', 'Result saved to result.txt')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Error saving result: {str(e)}')

    def open_result(self):
        try:
            with open('result.txt', 'r') as file:
                result_text = file.read()
                self.result_text.setPlainText(result_text)
            QMessageBox.information(self, 'Information', 'Result loaded from result.txt')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Error loading result: {str(e)}')

    def clear_result(self):
        self.result_text.clear()

    def exit_program(self):
        sys.exit()
    def copy_text(self):
        text = self.result_text.toPlainText()
        clipboard = QApplication.clipboard()
        clipboard.setText(text)

    def paste_text(self):
        clipboard = QApplication.clipboard()
        text = clipboard.text()
        self.result_text.insertPlainText(text)

    def cut_text(self):
        self.copy_text()
        self.result_text.clear()
    def change_color(self):
        color_dialog = QColorDialog(self)
        color = color_dialog.getColor()
        if color.isValid():
            # Set the background color of the main window
            self.setStyleSheet(f"background-color: {color.name()};")

    def change_size(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.result_text.setFont(font)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CalculatorApp()
    ex.show()
    sys.exit(app.exec())