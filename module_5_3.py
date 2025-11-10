import sys
from typing import List, Dict
from collections import Counter
from colorama import Fore

def load_logs(file_path):
   
    logs = []
    try:
        with open(file_path, "r", encoding="utf-8") as file_logs:
            for line in file_logs:
                parsed = parse_log_line(line)
                if parsed:
                    logs.append(parsed)
    except FileNotFoundError:
        print(f"Помилка: файл '{file_path}' не знайдено.")
        sys.exit(1)
    except Exception as error:
        print(f"Помилка при читанні файлу: {error}")
        sys.exit(1)
    return logs

def parse_log_line(line):
    parts = line.strip().split(" ", 3)
    if len(parts) < 4:
        return {}
    date, time, level, message = parts
    return {"date": date, "time": time, "level": level, "message": message}

def count_logs(logs):
    return Counter(log["level"] for log in logs)

def display_log_counts(counts):
    print(f"{'Рівень логування':<18} | {'Кількість'}")
    print("-" * 30)
    for level, count in counts.items():
        print(f"{Fore.GREEN}{level:<18} | {Fore.RESET}{count}")

def filter_logs_by_level(logs, level):

    level = level.upper()
    return list(filter(lambda log: log["level"] == level, logs))

def main():
    if len(sys.argv) < 2:
        print("Використання: python main.py <шлях до лог файлу> [рівень логування]")
        sys.exit(1)

    file_path = sys.argv[1]
    level = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    counts_level = count_logs(logs)
    display_log_counts(counts_level)

    if level:
        filtered_logs = filter_logs_by_level(logs, level)
        if filtered_logs:
            print(f"\nДеталі логів для рівня '{level.upper()}':")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            print(f"\nНемає записів рівня '{level.upper()}'.")

# if __name__ == "__main__":
#     main()

logs = load_logs("log.txt")
counts_level = count_logs(logs)
display_log_counts(counts_level)

