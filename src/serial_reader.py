import time
import serial

class SerialReader:
    def __init__(self, port, baudrate, bytesize, parity, stopbits, timeout=1):
        self.port = port
        self.baudrate = baudrate
        self.bytesize = bytesize
        self.parity = parity
        self.stopbits = stopbits
        self.timeout = timeout
        
        self.serial_connection = None
    
    
    def open(self):
        try:
            self.serial_connection = serial.Serial(
                port = self.port, 
                baudrate=self.baudrate, 
                bytesize=self.bytesize, 
                parity=self.parity, 
                stopbits=self.stopbits, 
                timeout=self.timeout
            )
            if self.serial_connection.is_open:
                print(f"Successfully connected to {self.port} at {self.baudrate} baud.")
        except Exception as e:
            print(f"Failed to connected to {self.port} at {self.baudrate} baud: {e}")


    def read_data(self):
        if self.serial_connection and self.serial_connection.is_open:
            try:
                # data_num = 1
                while True:
                    if self.serial_connection.in_waiting > 0:
                        data = self.serial_connection.readline().decode('utf-8').strip()
                        print(f"Received: {data}")
                        # data_num += 1
                        #time.sleep(0.1) # Adjst the sleep time as needed
            except KeyboardInterrupt:
                print("Stopping the serial reader.")
            except Exception as e:
                print(f"Error while reading data: {e}")  
        else:
            print("Serial connection is not open.")
            
    
    def close(self):
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
            print(f"CLosed connection to {self.port}.")
            

if __name__ == "__main__":
    port = "com6"
    baudrate = 9600
    reader = SerialReader(port=port, baudrate=baudrate, bytesize=8, parity="N", stopbits=1)
    reader.open()
    
    try:
        reader.read_data()
    finally:
        reader.close()