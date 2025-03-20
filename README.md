# Monitoring-tool
Monitoring Tool

Overview

This is a lightweight server monitoring tool that checks CPU, memory, and disk usage. If any resource exceeds the defined threshold, an alert is logged, and an email notification is sent using a Python script.

Features

✅ Monitors CPU, Memory, and Disk usage

✅ Logs alerts to a file

✅ Sends email notifications when thresholds are exceeded

✅ Configurable thresholds

✅ Uses environment variables for security

Prerequisites

Linux system (Ubuntu, Debian, or CentOS)

Python 3 installed

SMTP credentials for email notifications

Installation

1️⃣ Clone the repository

2️⃣ Set up environment variables

Edit your ~/.bashrc or ~/.bash_profile to add:

Then apply the changes:

3️⃣ Make the script executable

Usage

Run the monitoring script manually:

Or schedule it to run every 5 minutes using cron:

Add this line at the end:

Logs

All logs are stored in:

To view logs:

Troubleshooting

1️⃣ Permission issues with log file?

2️⃣ Email not sending?

Check if SMTP settings are correct

Ensure you have internet access

Try running the script manually with debug logs

Contributing

Feel free to submit issues or pull requests to improve this tool!
