# Python Scripts for crontab
![alt text](./Logo.png)
## What is cron?
---
The software utility cron is a time-based job scheduler in Unix-like computer operating systems. People who set up and maintain software environments use cron to schedule jobs, commands or scripts to run periodically at fixed times, dates, or intervals.
## How to set scripts in cron?
---
`$ crontab -e` - to open select-editor menu.
You'll see something like that
```
Select an editor.  To change later, run 'select-editor'.
  1. /bin/nano        <---- easiest
  2. /usr/bin/emacs24
  3. /usr/bin/jmacs
  4. /usr/bin/joe
  5. /usr/bin/jpico
  6. /usr/bin/jstar
  7. /usr/bin/mcedit
  8. /usr/bin/rjoe
  9. /usr/bin/vim.nox
  10. /usr/bin/vim.tiny
Choose 1-10 [1]:
```
Choose your favourite editor and press 'Enter'. You must use this pattern to set time intervals.

```
*    *    *    *    *
┬    ┬    ┬    ┬    ┬
│    │    │    │    └─  Weekday  (0=Sun .. 6=Sat)
│    │    │    └──────  Month    (1..12)
│    │    └───────────  Day      (1..31)
│    └────────────────  Hour     (0..23)
└─────────────────────  Minute   (0..59)
```
Next you must point bash script you want to run.
For example:

```
15 14 1 * * echo "Test" >> ~/temp.txt
```
This instruction will print 'Test' in file temp.txt in your home directory at 14:15 every month on the first day of month.
## How to run python scripts?
---
You should write the command `$ cd` and path to folder with python scripts. Then you should write
`$ python3` and sctipt's name.

Example:

```
15 14 1 * * export DISPLAY=:0 && cd /path/to/scripts/folder && python3 script_name.py
```

`export DISPLAY=:0` is necessary if your script use GUI system calls as my
## Finally
So, you must write two strings: for parser and schedule maker

Example:

```
* * * * * export DISPLAY=:0 && cd /path/to/scripts/folder && python3 Parser.py
* * * * * export DISPLAY=:0 && cd /path/to/scripts/folder && python3 MakeSchedule.py
```
## Realized on __Python 3.5.2__
***
__*My Contacts:*__
* [Telegram](https://telegram.me/calvados0806)
* [Vk](https://vk.com/id172058693)
* Email - flamaster0806@gmail.com
