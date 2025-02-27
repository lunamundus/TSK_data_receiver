from PySide6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QPushButton

class SerialPortSettingDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        
        self.setWindowTitle('Serial Port Setting')
        self.resize(400, 300)
        self.serial_port_setting()

    def serial_port_setting(self):
        setting_layout = QVBoxLayout()
        
        # serial port setup
        self.port_label = QLabel('Serial Port')
        self.port_combobox = QComboBox()
        ## serial port combobox setup
        ## TODO: item 변경 예정 (TEST용)
        self.port_combobox.addItems(["COM1", "COM2", "COM3", "COM4", "COM5"])
        self.port_combobox.setCurrentIndex(0)
        port_layout = QHBoxLayout()
        port_layout.addWidget(self.port_label)
        port_layout.addWidget(self.port_combobox)
        
        # bit rate setup
        self.baudrate_label = QLabel('Bit Rate(baudrate)')
        self.baudrate_combobox = QComboBox()
        self.baudrate_combobox.addItems(["2400", "4800", "9600", "19200", "38400"])
        self.baudrate_combobox.setCurrentIndex(2)
        baudrate_layout = QHBoxLayout()
        baudrate_layout.addWidget(self.baudrate_label)
        baudrate_layout.addWidget(self.baudrate_combobox)
        
        # data bits setup
        self.bytesize_label = QLabel("Data Bits")
        self.bytesize_combobox = QComboBox()
        self.bytesize_combobox.addItems(["5", "6", "7", "8"])
        self.bytesize_combobox.setCurrentIndex(3)
        bytesize_layout = QHBoxLayout()
        bytesize_layout.addWidget(self.bytesize_label)
        bytesize_layout.addWidget(self.bytesize_combobox)
        
        # parity bits setup
        self.parity_label = QLabel("Parity Bit")
        self.parity_combobox = QComboBox()
        self.parity_combobox.addItems(["None", "Even", "Odd"])
        self.parity_combobox.setCurrentIndex(0)
        parity_layout = QHBoxLayout()
        parity_layout.addWidget(self.parity_label)
        parity_layout.addWidget(self.parity_combobox)

        # stop bits setup
        self.stopbits_label = QLabel('Stop Bits')
        self.stopbits_combobox = QComboBox()
        self.stopbits_combobox.addItems(["1", "1.5", "2"])
        self.stopbits_combobox.setCurrentIndex(0)
        stopbits_layout = QHBoxLayout()
        stopbits_layout.addWidget(self.stopbits_label)
        stopbits_layout.addWidget(self.stopbits_combobox)
        
        # OK & Cancel button
        btn_layout = QHBoxLayout()
        # OK button
        self.ok_button = QPushButton('OK')
        self.ok_button.clicked.connect(self.accept)
        btn_layout.addWidget(self.ok_button)
        # Cancel button
        self.cancel_button = QPushButton('Cancel')
        self.cancel_button.clicked.connect(self.reject)
        btn_layout.addWidget(self.cancel_button)
        
        # add layout to setting_layout 
        setting_layout.addLayout(port_layout)
        setting_layout.addLayout(baudrate_layout)
        setting_layout.addLayout(bytesize_layout)
        setting_layout.addLayout(parity_layout)
        setting_layout.addLayout(stopbits_layout)
        setting_layout.addLayout(btn_layout)

        self.setLayout(setting_layout)
        
    
    def get_settings(self):
        return {
            "port": self.port_combobox.currentText(),
            "baudrate": self.baudrate_combobox.currentText(),
            "bytesize": self.bytesize_combobox.currentText(),
            "parity": self.parity_combobox.currentText(),
            "stopbits": self.stopbits_combobox.currentText()
        }