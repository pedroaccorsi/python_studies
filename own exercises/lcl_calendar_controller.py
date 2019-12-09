import win32com
import win32com.client
import datetime
import time

class Calendar_controller:

    mo_calendar_entries = None;
    mv_today            = None;
    mv_tomorrow         = None;

    def __init__(self):
        self.mo_calendar_entries = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI").GetDefaultFolder(9).Items
        self.mo_calendar_entries.Sort("[Start]");
        self.mo_calendar_entries.IncludeRecurrences = "True"
        self.mv_today    = datetime.datetime.today().date().strftime("%Y-%d-%m")
        self.mv_tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%d-%m")
        self.mo_calendar_entries = self.mo_calendar_entries.Restrict("[Start] >= '" +self.mv_today+"' AND [Start] < '"+self.mv_tomorrow+"'");


    def get_15min_away_appointment(self):
        ld_appointments        = self.get_todays_appointments();
        lv_num_of_appointments = len(ld_appointments['Start']);
        lv_now_time            = time.strftime('%H:%M:%S');
        for i in range (0, lv_num_of_appointments):
            lv_appoint_time     = str(ld_appointments['Start'][i])[11:19];
            lv_delta_in_minutes = self.get_delta_in_minutes(lv_appoint_time, lv_now_time);
            if (self.is_in_15_min(lv_delta_in_minutes) == True):
                return[ld_appointments['Subject'][i], lv_delta_in_minutes]
        return [None,None];


    def get_todays_appointments(self):
        rd_appointments = { 'Start':[], 'Subject': [] };
        for appointment in self.mo_calendar_entries:
            rd_appointments['Start'  ].append(appointment.Start  );
            rd_appointments['Subject'].append(appointment.Subject);
        return rd_appointments;


    def is_in_15_min(self, iv_delta_in_minutes):
        if ( iv_delta_in_minutes <= 15 and iv_delta_in_minutes >= 0):   
            return True;
        return False;


    def get_delta_in_minutes(self, iv_appointment, iv_now):
        lv_format = '%H:%M:%S';
        lo_delta  = datetime.datetime.strptime(iv_appointment, lv_format) - datetime.datetime.strptime(iv_now, lv_format)
        lv_delta_in_seconds = lo_delta.total_seconds();
        return int(lv_delta_in_seconds / 60);