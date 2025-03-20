#!/bin/bash
#
#
#
# Log file
LOG_FILE="/var/log/server_monitor.log"


CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')
CPU_USAGE=${CPU_USAGE:-0}
CPU_TRESHOLD=80.0

MEM_USAGE=$(free | grep Mem | awk '{print $3/$2 * 100.0}')
MEM_USAGE=${MEM_USAGE:-0}
MEM_THRESHOLD=80.0


DISK_USAGE=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')
DISK_USAGE=${DISK_USAGE:-0}
DISK_THRESHOLD=90


TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")

# Log function
log_message() {
    echo "$TIMESTAMP - $1" >> $LOG_FILE
}

# Alert function (Calls Python script)
send_alert() {
    python3 alert.py "$1"
}


if [ "$(echo "$CPU_USAGE > $CPU_TRESHOLD" | bc -l)" -eq 1 ]; then
	 log_message "ALERT: CPU usage high - $CPU_USAGE%"
    	 send_alert "High CPU usage detected: $CPU_USAGE%"
fi


if [ "$(echo "$MEM_USAGE > $MEM_THRESHOLD" | bc -l)" -eq 1 ]; then
    log_message "ALERT: Memory usage high - $MEM_USAGE%"
    send_alert "High Memory usage detected: $MEM_USAGE%"
fi


if [ "$DISK_USAGE" -gt "$DISK_THRESHOLD" ]; then
    log_message "ALERT: Disk usage high - $DISK_USAGE%"
    send_alert "High Disk usage detected: $DISK_USAGE%"
fi

log_message "System OK - CPU: $CPU_USAGE%, Memory: $MEM_USAGE%, Disk: $DISK_USAGE%"

exit 0

