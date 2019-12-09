from infi.systray import SysTrayIcon
def say_hello(systray):
    print("Hello, World!")
menu_options = (("Say Hellopy", None, say_hello),)
systray = SysTrayIcon("icon.ico", "Example tray icon", menu_options)
systray.start()