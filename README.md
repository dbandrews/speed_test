## speed_test

Batch file, VbScript and an exported Windows Task Scheduler task for scheduling a speed test in the background.
Writes to a csv ```log.csv```

### Setup

Add ```speedtest-cli``` to a Python environment of your choice.

```bash

pip install speedtest-cli

```

Confirm paths in the batch file, Vbs script and scheduled task to match your folder structure. Ensure the Python executable in the batch file CALL statement is correct.

Using the VbScript method allows for running when user is logged on/off.

Log file is of the format:

|Download Speed (bytes/s)|Upload (bytes/s)|Ping(ms)|Datetime|
|------------------------|-----------------|--------|--------|