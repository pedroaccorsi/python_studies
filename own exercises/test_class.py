from lcl_calendar_controller import *;

lo_calendar = Calendar_controller();



subject, start = lo_calendar.get_15min_away_appointment();
print(start, subject);

