from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(20, 20, 100, 30))
        self.label_name.setText("Book Name:")
        
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(130, 20, 200, 30))
        
        self.label_author = QtWidgets.QLabel(self.centralwidget)
        self.label_author.setGeometry(QtCore.QRect(20, 60, 100, 30))
        self.label_author.setText("Author:")
        
        self.lineEdit_author = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_author.setGeometry(QtCore.QRect(130, 60, 200, 30))
        
        self.label_year = QtWidgets.QLabel(self.centralwidget)
        self.label_year.setGeometry(QtCore.QRect(20, 100, 100, 30))
        self.label_year.setText("Publish Year:")
        
        self.lineEdit_year = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_year.setGeometry(QtCore.QRect(130, 100, 200, 30))
        
        self.label_type = QtWidgets.QLabel(self.centralwidget)
        self.label_type.setGeometry(QtCore.QRect(20, 140, 100, 30))
        self.label_type.setText("Book Type:")
        
        self.lineEdit_type = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_type.setGeometry(QtCore.QRect(130, 140, 200, 30))
        
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(350, 20, 100, 30))
        self.pushButton_add.setText("Add Book")
        
        
        self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete.setGeometry(QtCore.QRect(350, 60, 100, 30))
        self.pushButton_delete.setText("Delete Book")
        
       
        
        self.pushButton_search = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_search.setGeometry(QtCore.QRect(350, 100, 100, 30))
        self.pushButton_search.setText("Search Book")
        
        
        
        self.pushButton_list = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_list.setGeometry(QtCore.QRect(350, 140, 100, 30))
        self.pushButton_list.setText("List All Books")
        
        
        self.textEdit_results = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_results.setGeometry(QtCore.QRect(20, 180, 560, 200))
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Book Manager"))
