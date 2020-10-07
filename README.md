## speed_test

#### Scheduled Internet speed tests on Windows

Batch file, VbScript and an exported Windows Task Scheduler task for scheduling an internet speed test in the background.
Writes to a csv ```log.csv```

#### Setup

Add the ```speedtest-cli``` package to a Python environment of your choice.

```bash

pip install speedtest-cli

```

Confirm paths in the batch file, Vbs script and scheduled task to match your folder structure. Ensure the Python executable in the batch file CALL statement is matches where you have installed the ```speedtest-cli``` package.

Using the VbScript method allows for running when user is logged on/off.

Log file is of the format:

|Download Speed (bytes/s)|Upload (bytes/s)|Ping(ms)|Datetime|
|------------------------|-----------------|--------|--------|

##### TODO
[] Schedule test using crontab through WSL