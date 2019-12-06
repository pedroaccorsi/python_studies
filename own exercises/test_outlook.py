import win32com
import win32com.client
import datetime
import time
import pytz
import dateutil.parser 

#def fix_timezone(dt):
#   local_tz = dt.astimezone().tzinfo # is there a cleaner way to get the local tz?
#    shifted = dt.replace(tzinfo=local_tz)
#    return shifted.astimezone(pytz.utc)

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
        #events['Start'  ].append( fix_timezone( (datetime.datetime.fromtimestamp( timestamp=a.Start.timestamp() ) ) ) );
        events['Start'  ].append(a.Start  );
        events['Subject'].append(a.Subject)
    return events

calendar = getCalendarEntries();

n=len(calendar['Start']);
i=0;

while( n ):
    #a = dateutil.parser.parse(str(calendar['Start'][i]))
    a = datetime.datetime.strptime(str(calendar['Start'][i])[0:19], '%Y-%m-%d %H:%M:%S')
    print( "Às" ,a.hour, ":" ,a.minute, ", evento: "+calendar['Subject'][i] );

    n-=1;
    i+=1; 

