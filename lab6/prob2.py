import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self, name_ids):
        super().__init__()

        self.name_ids = name_ids

        self.setWindowTitle("My App")
        self.setGeometry(100, 100, 400, 200)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.text_field = QLineEdit()
        self.display_label = QLabel()

        layout.addWidget(self.text_field)
        layout.addWidget(self.display_label)

        self.widget = QWidget()
        self.widget.setLayout(layout)

        self.setCentralWidget(self.widget)

        self.text_field.returnPressed.connect(self.update_label)

    def update_label(self):
        user_input = self.text_field.text()
        full_text = user_input + ", " + self.name_ids["name"] + ", " + self.name_ids["id"]
        self.display_label.setText(full_text)

if __name__ == "__main__":
    name_ids = {"name": "Sujitra", "id": "653040499-6"}

    app = QApplication(sys.argv)
    window = MainWindow(name_ids)
    window.show()

    sys.exit(app.exec())
