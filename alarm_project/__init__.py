from alarm_class import Alarm
import MainWindow
import Dialog
import sys
import os
import json
from PyQt5 import QtWidgets, QtCore, QtGui, Qt
# List of alarms
class AlarmListView(QtWidgets.QListView):
    def __init__(self, list_view_inst):
        super(AlarmListView, self).__init__()
        self.model = QtGui.QStandardItemModel()
        self.listView = list_view_inst
        self.listView.setModel(self.model) 
        self.path = os.curdir + '/alarm_project/alarm_data.json'
    def UpNextAlarm(self):
        return Alarm.GetUpNextItem(self, self.path)
        
    def ShowList(self):
        self.model.clear()
        alarms_refresh = Alarm.AlarmList(self, self.path)
        for i in alarms_refresh:
            item = QtGui.QStandardItem(f"{i['title']} at {i['time']}")
            self.model.appendRow(item)            
    def DeleteItem(self):
        index = self.listView.selectionModel().currentIndex()
        item = self.listView.model().itemData(index).values().__str__()
        item = item[14:].strip("')]")
        Alarm.DeleteAlarm(self,item, self.path)
    
#Main window
class AlarmApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(AlarmApp, self).__init__()
        self.ui = MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        #set current time
        self.current_time = QtCore.QTimer()
        self.current_time.timeout.connect(self.RefreshWindow)
        self.current_time.start(1000) 
        #set list view
        self.instance_of_ListView = AlarmListView(self.ui.alarm_list)
        self.RefreshList()
        #set toolbar
        self.add = QtWidgets.QAction('add')
        self.ui.toolBar.addAction(self.add)
        self.add.triggered.connect(self.NewAlarm)
        self.refresh = QtWidgets.QAction('refresh')
        self.ui.toolBar.addAction(self.refresh)
        self.refresh.triggered.connect(self.RefreshList)
        self.delete = QtWidgets.QAction('delete')
        self.ui.toolBar.addAction(self.delete)
        self.delete.triggered.connect(self.DeleteAlarm)
        #on/off alarm
        self.alarm_on = True 
    #Refresh window
    def RefreshWindow(self): 
        now = QtCore.QDateTime.currentDateTime()
        self.ui.lbl_current.setText(now.toString('hh:mm'))
        try:
            up_next, trigger = self.instance_of_ListView.UpNextAlarm() #return alarm title and True if alarm time matches current time
            if trigger:
                if self.alarm_on:
                    self.Ring()
        except:
            up_next = 'No alarms' #alarm list is empty
        finally:
            self.ui.lbl_up_next.setText(up_next)
    def NewAlarm(self):
        self.dialog = QtWidgets.QDialog()
        self.dialog.ui = Dialog.Ui_addAlarmDialog()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.ui.buttonBox.button(QtWidgets.QDialogButtonBox.Save).clicked.connect(self.Save)
        self.dialog.exec_()
    def RefreshList(self):
        self.instance_of_ListView.ShowList()
    def Save(self):
        title = self.dialog.ui.le_alarmTitle.text()
        time = self.dialog.ui.te_time.time()
        newAlarm = Alarm(title,time.toString('hh:mm'),'test')
        path = os.curdir + '/alarm_project/alarm_data.json'
        newAlarm.SaveAlarm(path)
    def DeleteAlarm(self):
        self.instance_of_ListView.DeleteItem()
    def Ring(self):
        alarm_message = QtWidgets.QMessageBox.information(self, 'Ring! Ring!', self.ui.lbl_up_next.text(), QtWidgets.QMessageBox.Ok|QtWidgets.QMessageBox.Cancel)
        if alarm_message == QtWidgets.QMessageBox.Ok:
            self.alarm_on = False
        

             
def app():
    app = QtWidgets.QApplication([])
    win = AlarmApp()
    win.show()
    sys.exit(app.exec_())
app()