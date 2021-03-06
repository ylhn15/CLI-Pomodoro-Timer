from time import sleep
import os
import sys

def notify(title, text):
    if os.name is "Darwin":
        os.system("""
                  osascript -e 'display notification "{}" with title "{}"'
                    """.format(text, title))
    else: 
        os.system('notify-send "{}" "{}"'.format(title, text))
def timer():
    runtimes = 0
    worktime = 25
    shortbreak = 5
    longbreak = 30
    interval = 4
    worktitle = "Work"
    pausetitle = "Pause"
    workmessage = "Time to work"
    pausemessage = "Time for a pause"
    for arg in sys.argv:
        if arg == "--title" or arg == "-t":
            worktitle = sys.argv[sys.argv.index(arg)+1]
 #           if sys.argv[sys.argv.index(arg)+2].find("-") is -1:
 #               pausetitle = sys.argv[sys.argv.index(arg)+2]
        if arg == "--message" or arg == "-m":
            workmessage = sys.argv[sys.argv.index(arg)+1]
 #           if sys.argv[sys.argv.index(arg)+2].find("-") is -1:
 #               pausemessage = sys.argv[sys.argv.index(arg)+2]
        if arg == "--worktime" or arg == "-w":
            worktime = float(sys.argv[sys.argv.index(arg)+1])
        if arg == "--shortbreak" or arg == "-s":
            shortbreak = float(sys.argv[sys.argv.index(arg)+1])
        if arg == "--longbreak" or arg == "-l":
            longbreak = float(sys.argv[sys.argv.index(arg)+1])
        if arg == "--interval" or arg == "-i":
            interval = float(sys.argv[sys.argv.index(arg)+1])
    while True:
        lengthOfPauseInMinutes = 0
        if runtimes is 0:
            lengthOfPauseInMinutes = shortbreak
        elif runtimes % interval is 0:
            lengthOfPauseInMinutes = shortbreak
        elif runtimes % interval is not 0:
            lengthOfPauseInMinutes = longbreak
        notify(worktitle + " (" + str(worktime) + "Minutes )", workmessage)
        sleep(worktime * 60)
        notify(pausetitle + " (" + str(lengthOfPauseInMinutes) + "Minutes )", pausemessage)
        sleep(lengthOfPauseInMinutes * 60)
        runtimes = runtimes + 1
timer()

