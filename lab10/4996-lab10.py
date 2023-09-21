import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox, QMenuBar, QMenu, QToolBar, QColorDialog, QFontDialog
from PyQt6.QtGui import QIcon, QColor, QFont
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtWidgets import QFileDialog, QMessageBox
from PyQt6.QtCore import QDir


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
        plus_button.clicked.connect(self.calculate_result)

        minus_button = QPushButton('-', self)
        minus_button.setGeometry(70, 110, 40, 30)
        minus_button.clicked.connect(self.calculate_result)

        multiply_button = QPushButton('*', self)
        multiply_button.setGeometry(120, 110, 40, 30)
        multiply_button.clicked.connect(self.calculate_result)

        divide_button = QPushButton('/', self)
        divide_button.setGeometry(170, 110, 40, 30)
        divide_button.clicked.connect(self.calculate_result)

    def initMenu(self):
        menubar = self.menuBar()
        
        # File menu
        self.file_menu = menubar.addMenu('File')


        # Edit menu
        self.edit_menu = menubar.addMenu('Edit')


        # Config menu
        config_menu = menubar.addMenu('Config')

    def calculate_result(self):
        num1_str = self.line_edit1.text()
        num2_str = self.line_edit2.text()

        if not num1_str.strip() or not num2_str.strip():
            QMessageBox.critical(self, 'Error', 'Please enter both numbers.')
            return

        try:
            num1 = float(num1_str)
            num2 = float(num2_str)
        except ValueError:
            QMessageBox.critical(self, 'Error', 'Please enter number .')
            return

        operator = self.sender().text()
        result = 0

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                QMessageBox.critical(self, 'Error', 'Division by zero is not allowed.')
                return
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

class WindowsMenusToolBar(CalculatorApp):
    def __init__(self):
        super().__init__()

    def initMenu(self):
        super().initMenu()

        open_action = self.file_menu.addAction('Open')
        open_action.setIcon(QIcon('file-open.svg'))
        open_action.triggered.connect(self.open_result)

        save_action = self.file_menu.addAction('Save')
        save_action.setIcon(QIcon('file-save.png'))
        save_action.triggered.connect(self.save_result)

        clear_action = self.edit_menu.addAction('Clear')
        clear_action.setIcon(QIcon('edit-clear.png'))
        clear_action.triggered.connect(self.clear_result)

        cut_action = self.edit_menu.addAction('Cut')
        cut_action.setIcon(QIcon('edit-cut.png'))  
        cut_action.triggered.connect(self.cut_text)

        copy_action = self.edit_menu.addAction('Copy')
        copy_action.setIcon(QIcon('edit-copy.png'))  
        copy_action.triggered.connect(self.copy_text) 
        
        paste_action = self.edit_menu.addAction('Paste')
        paste_action.setIcon(QIcon('edit-paste.png'))  
        paste_action.triggered.connect(self.paste_text) 

class MessageBoxDisplay(WindowsMenusToolBar):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator with Message Box")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.calculate_result()

    def calculate_result(self):
        num1_str = self.line_edit1.text()
        num2_str = self.line_edit2.text()

        if not num1_str.strip() or not num2_str.strip():
            QMessageBox.critical(self, 'Error', 'Please enter both numbers.')
            return

        try:
            num1 = float(num1_str)
            num2 = float(num2_str)
        except ValueError:
            QMessageBox.critical(self, 'Error', 'Please enter number .')
            return

        operator = self.sender().text()
        result = 0

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                QMessageBox.critical(self, 'Error', 'Division by zero is not allowed.')
                return
            else:
                result = num1 / num2

        self.result_text.setPlainText(str(result))
class CalculatorFileDialog(MessageBoxDisplay):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator with File Dialog")

    def initMenu(self):
        super().initMenu()

        save_action = self.file_menu.addAction('Save As')
        save_action.setIcon(QIcon('file-save.png'))
        save_action.triggered.connect(self._handleSaveMenus)

        open_action = self.file_menu.addAction('Open')
        open_action.setIcon(QIcon('file-open.svg'))
        open_action.triggered.connect(self._handleOpenMenus)

    def _handleSaveMenus(self):
        options = QFileDialog.Option.ReadOnly

        file_name, _ = QFileDialog.getSaveFileName(self, 'Save File', QDir.homePath(), 'Text Files (*.txt)', options=options)

        if file_name:
            try:
                with open(file_name, 'w') as file:
                    file.write(self.result_text.toPlainText())
                QMessageBox.information(self, 'Information', 'Result saved to ' + file_name)
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'Error saving result: {str(e)}')

    def _handleOpenMenus(self):
        options = QFileDialog.Option.ReadOnly

        file_name, _ = QFileDialog.getOpenFileName(self, 'Open File', QDir.homePath(), 'Text Files (*.txt)', options=options)

        if file_name:
            try:
                with open(file_name, 'r') as file:
                    result_text = file.read()
                    self.result_text.setPlainText(result_text)
                QMessageBox.information(self, 'Information', 'Result loaded from ' + file_name)
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'Error loading result: {str(e)}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CalculatorFileDialog()
    ex.show()
    sys.exit(app.exec())
