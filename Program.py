# Basic libraries to import for completing the whole work.
import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import csv
import os

class Mainwindow(QMainWindow):
    def __init__(self):
        super(Mainwindow, self).__init__()
        loadUi(r"C:\study\Semester3\DSALab\lab4\Part2\BMS.ui", self)  
        self.AddButton.clicked.connect(self.Add_bus)
        self.DeleteButton.clicked.connect(self.Delete_bus)
        self.EditButton.clicked.connect(self.edit_bus)
        self.BusInfoTable.clicked.connect(self.fill_bus)
        if not os.path.isfile('bus.csv'):
            with open('bus.csv', 'w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Name', 'ID', 'Number', 'Company'])
        self.load_table()

    def fill_bus(self):
        row = self.BusInfoTable.currentRow()
        self.Name.setText(self.StuInfoTable.item(row,0).text())
        self.ID.setText(self.StuInfoTable.item(row,1).text())
        self.Number.setText(self.StuInfoTable.item(row,2).text())
        self.CompanyEdit.setText(self.StuInfoTable.item(row,3).text())

    def resetValues(self):
        self.Name.setText("Bus Name")
        self.ID.setText("ID")
        self.Number.setText("Number")
        self.Company.setText("Company")   

    def Check_busID(self, bus_id):
        with open('bus.csv', 'r', encoding="utf-8", newline="") as fileInput:
            data = list(csv.reader(fileInput))
            for row in data:
                if bus_id == row[1]:  
                    return False
        return True

    def Add_bus(self):
        name = self.Name.text()
        bus_id = self.ID.text()
        number = self.Number.text()
        company = self.Company.text()

        if bus_id != "ID" and self.Check_busID(bus_id):
            bus_data = [name, bus_id, number, company]

            with open('bus.csv', 'a+', encoding="utf-8", newline="") as fileInput:
                writer = csv.writer(fileInput)
                writer.writerow(bus_data)
            self.load_table()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("--- Add a Bus ---")
            msg.setText("ID is already Added.")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            msg.setFont(font)
            msg.exec()
    def edit_bus(self):
        row = self.BusInfoTable.currentRow()
        old_id = self.BusInfoTable.item(row,1).text()
        name = self.Name.text()
        ID = self.ID.text()
        number = self.Number.text()
        company = self.Company.text()

        index_bus = None
        updated_data = []
        with open('bus.csv', "r", encoding="utf-8") as fileInput:
            reader = csv.reader(fileInput)
            counter = 0
            for row in reader:
                if len(row) > 0:
                    if old_id == row[1]:
                       bus_found = True
                       bus_data = []
                       bus_data.append(name)
                       bus_data.append(ID)
                       
                       bus_data.append(number)
                       bus_data.append(company)
                       updated_data.append(bus_data)
                    else:
                        updated_data.append(row)
                    
        if bus_found is True:
            fileName = 'C:/Users/monti/A-CRUD/students.csv'
            with open('student.csv', "w", encoding="utf-8",newline="") as fileInput:
                writer = csv.writer(fileInput)
                writer.writerows(updated_data)
            self.load_table()
            self.resetValues()
    def Delete_bus(self):
        if(self.ID.text() != "ID"):
            ID = self.ID.text()
            bus_found = False
            updated_data = []
            with open('bus.csv', "r", encoding="utf-8") as fileInput:
                reader = csv.reader(fileInput)
                for row in reader:
                    if len(row) > 0:
                        if ID != row[1]:
                            updated_data.append(row)
                        else:
                           bus_found = True
            

            if bus_found is True:
                with open('bus.csv', "w", encoding="utf-8", newline="") as fileInput:
                    writer = csv.writer(fileInput)
                    writer.writerows(updated_data)
                self.load_table()
                self.resetValues()
        
    def load_table(self):
        with open('bus.csv', "r", encoding="utf-8") as fileInput:
            data = list(csv.reader(fileInput))
            self.BusInfoTable.setRowCount(0)  
            self.BusInfoTable.setRowCount(len(data) - 1)
            for row in range(1, len(data)):
                self.BusInfoTable.setItem(row - 1, 0, QtWidgets.QTableWidgetItem(data[row][0])) 
                self.BusInfoTable.setItem(row - 1, 1, QtWidgets.QTableWidgetItem(data[row][1]))  
                self.BusInfoTable.setItem(row - 1, 2, QtWidgets.QTableWidgetItem(data[row][2]))  
                self.BusInfoTable.setItem(row - 1, 3, QtWidgets.QTableWidgetItem(data[row][3]))  

# main
app = QApplication(sys.argv)
window = Mainwindow()
window.show()
sys.exit(app.exec_())
