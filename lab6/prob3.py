import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QMessageBox , QWidget , QVBoxLayout

class GreetingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("653040499-6")
        self.setGeometry(100, 100, 300, 200)
        self.label = QLabel("Sujitra oicharoen", self)
        self.label.setGeometry(100, 50, 100, 30)
        self.quit_button = QPushButton("Quit", self)
        self.quit_button.setGeometry(100, 100, 100, 30)
        self.quit_button.clicked.connect(QApplication.instance().quit)
        self.quit_button.setToolTip("Click to quit!")
        layout=QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.quit_button)
        con=QWidget()
        con.setLayout(layout)
        self.setCentralWidget(con)
        self.show()
    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Confirmation", 
                                     "Are you sure to quit?", 
                                     QMessageBox.StandardButton.Yes | 
                                     QMessageBox.StandardButton.No, 
                                     QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=GreetingApp()
    window.show()
    sys.exit(app.exec())