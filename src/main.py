import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('TSK Data Viewer')
        self.data_viewer()
        
    def data_viewer(self):
        # main layout
        main_layout = QVBoxLayout()
        
        # data viewr
        self.data_view_window = QTextEdit()
        main_layout.addWidget(self.data_view_window)
        
        # save & reset button
        ## button layout
        btn_layout = QHBoxLayout()
        
        ## save button
        self.save_button = QPushButton('Save')
        self.save_button.clicked.connect(self.on_clicked_save_btn)
        btn_layout.addWidget(self.save_button)
        
        ## reset button
        self.reset_button = QPushButton('Reset')
        self.reset_button.clicked.connect(self.on_clicked_reset_btn)
        btn_layout.addWidget(self.reset_button)
        
        # central widget setting
        main_layout.addLayout(btn_layout)
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        
    # button function
    # TODO: Save 버튼 기능 구현
    def on_clicked_save_btn(self):
        print("save button clicked!")
        pass
    
    # TODO: Reset 버튼 기능 구현
    def on_clicked_reset_btn(self):
        print("reset button clicked!!")
        pass


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    
if __name__ == '__main__':
    main()