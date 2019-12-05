from win10toast import ToastNotifier
import time;
toaster = ToastNotifier()

def func():
    print("oi");

aa = toaster.show_toast("Example two",
                   "This notification is in it's own thread!",
                   icon_path=None,
                   duration=10,
                   threaded=True);


while toaster.notification_active(): 
    print("oi"); 
    time.sleep(1) 