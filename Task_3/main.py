# from colorama import Fore
from collections import Counter
import sys


def parse_log_line(line: str) -> dict:
    date,time,level,*message = line.split()
    return {
            'date': date,
            'time': time,
            'level': level,
            'message': ' '.join(message)
    }


def load_logs(file_path: str) -> list:
    logs = list()
    try:
        with open(file_path,'r', encoding='UTF-8') as f:
            for line in f:
                if line.strip():
                    logs.append(parse_log_line(line.strip()))
        return logs
    
    except FileNotFoundError:
        return logs


def filter_logs_by_level(logs:list,level:str) -> list:
    return [log for log in logs if log['level'].lower() == level.lower()]


def count_logs_by_level(logs:list)-> dict:
    count = Counter(log['level'] for log in logs)
    return dict(count)


def display_log_counts(counts:dict):
    print('Рівень логування | Кількість')
    print('-----------------|----------')
    for level, count in counts.items():
        print(f'{level:<17}| {count}')



def main():

    if len(sys.argv) < 2:
        print('No path found in the input!!')
        return
    
    path = sys.argv[1]
    level = sys.argv[2].strip() if len(sys.argv) > 2 else None
    log_list = load_logs(path)

    if not log_list:
        print('Logs file is empty!')
        return
    
    logs_count = count_logs_by_level(log_list)
    display_log_counts(logs_count)
        

    if level:
        filtered_logs= filter_logs_by_level(log_list,level)
        print(f'\nДеталі логів для рівня {level.upper()} \n')
        for log in filtered_logs:
            print(f'{log['date']} {log['time']} - {log['message']}')


if __name__ == '__main__':
    main()


