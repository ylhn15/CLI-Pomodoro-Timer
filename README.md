# CLI-Pomodoro-Timer
Pomodoro Timer with custom durations and messages for the CLI for MacOS and Linux.

Using either the built-in MacOS notifications or the Linux tool 'notify-send' to notify you when your time is up.

To start the timer with default values use:
`python3 pomodory.py` 

Optional flags are:
* `--title or -t {tite} to set a title`
* `--message or -m {message} to set a message`
* `--worktime or -w {time in minutes} to change the duration of the worktime (default 25 minutes)`
* `--shortbreak or -s {time in minutes} to change the duration of the short break (default 5 minutes)`
* `--longbreak or -l {time in minutes} to change the duration of the long break (default 5 minutes)`
* `--interval or -i {amount of intervals} to change the amount of intervals until a long break starts (default 4)`
