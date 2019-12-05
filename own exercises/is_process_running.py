import os

CHAT_EXE = "ChatMonitor.exe";

def isChatRunning():
    rl_tasks = os.popen('tasklist /v').read().strip().split('\n')

    for i in range(len(rl_tasks)):
        task = rl_tasks[i]
        if CHAT_EXE in rl_tasks[i]:
            return True
            
    return False


 