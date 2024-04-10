import os
import psutil
import subprocess
import datetime

class SysMonitor:
    def __init__(self):
        pass

    def get_system_stats(self):
        cpu_percent = psutil.cpu_percent()
        memory_percent = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent
        network_stats = psutil.net_io_counters()

        print("CPU Usage: {}%".format(cpu_percent))
        print("Memory Usage: {}%".format(memory_percent))
        print("Disk Usage: {}%".format(disk_usage))
        print("Network Stats: Bytes Sent - {}, Bytes Received - {}".format(network_stats.bytes_sent, network_stats.bytes_recv))

    def list_running_processes(self):
        running_processes = subprocess.check_output(['ps', '-e']).decode().split('\n')
        for process in running_processes:
            print(process)

    def kill_process_by_pid(self, pid):
        try:
            subprocess.run(['kill', str(pid)])
            print("Process with PID {} terminated successfully.".format(pid))
        except Exception as e:
            print("Error terminating process:", e)

    def search_logs(self, keyword):
        try:
            with open('/var/log/syslog', 'r') as logfile:
                for line in logfile:
                    if keyword in line:
                        print(line)
        except FileNotFoundError:
            print("Log file not found.")

    def filter_logs_by_date(self, date_str):
        try:
            date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
            with open('/var/log/syslog', 'r') as logfile:
                for line in logfile:
                    if date.strftime('%b %d') in line:
                        print(line)
        except FileNotFoundError:
            print("Log file not found.")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

if __name__ == "__main__":
    sys_monitor = SysMonitor()

    while True:
        print("\n===== SysMonitor Menu =====")
        print("1. System Performance Stats")
        print("2. List Running Processes")
        print("3. Kill Process by PID")
        print("4. Search Logs by Keyword")
        print("5. Filter Logs by Date")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            sys_monitor.get_system_stats()
        elif choice == '2':
            sys_monitor.list_running_processes()
        elif choice == '3':
            pid = input("Enter PID of the process to kill: ")
            sys_monitor.kill_process_by_pid(pid)
        elif choice == '4':
            keyword = input("Enter keyword to search in logs: ")
            sys_monitor.search_logs(keyword)
        elif choice == '5':
            date = input("Enter date (YYYY-MM-DD) to filter logs: ")
            sys_monitor.filter_logs_by_date(date)
        elif choice == '6':
            print("Exiting SysMonitor.")
            break
        else:
            print("Invalid choice. Please try again.")
