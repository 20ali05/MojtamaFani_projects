import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel, QMainWindow, QTabWidget

class NewDeviceWindow(QWidget):
    #شماره فاکتور
    invoice_number = 0
    # کد کالا
    device_code = 0
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle("تعریف دستگاه جدید")
        self.setGeometry(200, 200, 400, 300)  # Adjusted size for better visibility

        # Create a vertical layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Add labels and line edits for each piece of information
        self.add_field(layout, "تاریخ دریافت:", QLineEdit(), "date_received_edit")
        self.add_field(layout, "نام فرستنده:", QLineEdit(), "customer_edit")
        tedad = self.add_field(layout, "تعداد دستگاه ها:", QLineEdit(), "device_count_edit")

        # Add a save button
        save_button = QPushButton("وارد کردن")
        save_button.clicked.connect(self.save_new_device)
        layout.addWidget(save_button)

    def add_field(self, layout, label_text, line_edit, object_name):
        # Create a horizontal layout for the label and line edit
        h_layout = QHBoxLayout()
        label = QLabel(label_text)
        h_layout.addWidget(label)
        h_layout.addWidget(line_edit)
        layout.addLayout(h_layout)

        # Set the object name for the line edit
        line_edit.setObjectName(object_name)

    def save_new_device(self):
        # Retrieve and print the information entered by the user
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        
        date_received = self.findChild(QLineEdit, "date_received_edit").text()
        device_count = self.findChild(QLineEdit, "device_count_edit").text()

        print("New Device Information:")
        print("Date Received:", date_received)
        print("Device Count:", device_count)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("office")
        self.setGeometry(200, 200, 400, 300)  # Adjusted size for better visibility

        # Create a vertical layout
        layout = QVBoxLayout()

        # Add buttons for each option
        new_device_button = QPushButton("دستگاه جدید")
        new_device_button.clicked.connect(self.show_new_device_window)
        layout.addWidget(new_device_button)

        manage_devices_button = QPushButton("مدیریت دستگاه ها")
        layout.addWidget(manage_devices_button)

        repaired_devices_button = QPushButton("دستگاه های بررسی شده")
        layout.addWidget(repaired_devices_button)

        not_repaired_devices_button = QPushButton("دستگاه های نابررسی شده")
        layout.addWidget(not_repaired_devices_button)

        task_bar_button = QPushButton("نوبت دهی")
        layout.addWidget(task_bar_button)

        # Create a central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def show_new_device_window(self):
        self.new_device_window = NewDeviceWindow()
        self.new_device_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())