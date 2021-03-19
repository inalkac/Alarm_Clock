import unittest
import os
from alarm_class import Alarm

class TestAlarm(unittest.TestCase):
    def testSort(self):
        list_to_test = [
            {'title':'alarm1', 'time': '24:00'},
            {'title':'alarm2', 'time': '18:35'}
        ]
        list_to_verify= [
            {'title':'alarm2', 'time': '18:35'},
            {'title':'alarm1', 'time': '24:00'}
        ]
        self.assertEqual(Alarm.Sort(self, list_to_test),list_to_verify)
    
    def testGetAlarmList(self):
        path = os.curdir + '/alarm_project/test_list.json'
        list_to_verify= [
            {'title':'alarm2', 'time': '18:35'},
            {'title':'alarm1', 'time': '24:00'}
        ]
        self.assertEqual(Alarm.GetAlarmList(self,path), list_to_verify)


if __name__ == '__main__':
    unittest.main()