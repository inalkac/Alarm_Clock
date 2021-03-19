import json
import os
from datetime import datetime,time
class Alarm():
    def __init__(self, newTitle, newTime, newSound):
        self.title = newTitle
        self.time = newTime
        self.sound = newSound

    @staticmethod
    def AlarmList(obj, path):
        return Alarm.GetAlarmList(obj, path)
    def GetAlarmList(self, path):
        try:
            with open(path, 'r', encoding='utf-8') as data_file:
                alarmList = json.load(data_file)
        except:
            alarmList = []
        finally:
            return alarmList       
    def SaveAlarm(self, path):
        newRecord = {
            'title' : self.title,
            'time' : self.time,
            'sound' : self.sound
        }
        recordsList = self.GetAlarmList(path)
        recordsList.append(newRecord)
        recordsList = self.Sort(recordsList)
        with open(path, 'w', encoding='utf-8') as data_file:
            json.dump(recordsList, data_file)
    def DeleteAlarm(self, alarm_name, path):
        alarm_name = alarm_name.split('at')
        alarm_name[0] = alarm_name[0].strip(' ')
        with open(path, 'r', encoding='utf-8') as data_file:
            alarmList = json.load(data_file)
        index = 0
        for item in alarmList:
            if alarm_name[0] in item['title']:
                alarmList.pop(index) 
                break
            index+=1
        with open(path, 'w', encoding='utf-8') as data_file:
            json.dump(alarmList, data_file)
    def Sort(self, current_alarm_list):
        current_alarm_list = sorted(current_alarm_list, key = lambda i: i['time'])
        return current_alarm_list
    @staticmethod
    def GetUpNextItem(obj, path):
        alarm_triggered = False
        current_alarm_list = Alarm.GetAlarmList(obj, path)
        now = datetime.strptime(datetime.now().time().strftime('%H:%M'),"%H:%M").time()
        if len(current_alarm_list) == 0:
            raise Exception ('No alarms')
        else:
            for item in current_alarm_list:
                current_alarm_time = datetime.strptime(item['time'],"%H:%M").time()
                if current_alarm_time == now:
                    alarm_triggered = True
                    title = item['title']
                elif current_alarm_time > now:
                    title = item['title']
                else:
                    title = current_alarm_list[0]['title']
        return (title, alarm_triggered)