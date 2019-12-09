import win32com
import win32com.client
import datetime
import time
import pytz
import dateutil.parser 

def getCalendarEntries():
    Outlook      = win32com.client.Dispatch("Outlook.Application")
    appointments = Outlook.GetNamespace("MAPI").GetDefaultFolder(9).Items
    appointments.Sort("[Start]");
    appointments.IncludeRecurrences = "True"
    today    = datetime.datetime.today().date().strftime("%Y-%d-%m")
    tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%d-%m")
    appointments = appointments.Restrict("[Start] >= '" +today+"' AND [Start] < '"+tomorrow+"'");
    events={'Start':[],'Subject':[]}
    for a in appointments: 
        events['Start'  ].append(a.Start  );
        events['Subject'].append(a.Subject)
    return events

def verify_calendar():
    #for x in range(0, 13):
    events        = getCalendarEntries();
    num_of_events = len(events['Start']);
    for y in range (0, num_of_events):
        s2 = str(events['Start'][y])[11:19]
        s1 = time.strftime('%H:%M:%S')
        FMT = '%H:%M:%S'
        #print(s1, s2);
        tdelta = datetime.datetime.strptime(s2, FMT) - datetime.datetime.strptime(s1, FMT)
        delta_seconds = tdelta.total_seconds();
        print(delta_seconds, events['Subject'][y])
        if(delta_seconds / 60 <= 15 and
            delta_seconds / 60 >= 0 ):
            print("oi")

verify_calendar()