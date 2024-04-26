import psutil

def top_10_memory_consumers():
    processes = []

    # Получаем список всех процессов
    all_processes = psutil.process_iter(attrs=['pid', 'name', 'memory_info'])

    # Для каждого процесса получаем информацию о потреблении памяти
    for process in all_processes:
        try:
            pid = process.info['pid']
            name = process.info['name']
            memory_info = process.info['memory_info']
            memory_usage = memory_info.vms / (1024 * 1024)  # Преобразуем в мегабайты
            processes.append((pid, name, memory_usage))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    # Сортируем процессы по потреблению памяти
    processes.sort(key=lambda x: x[2], reverse=True)

    # Выводим топ 10 процессов
    print("Top 10 Memory Consumers:")
    print("{:<10} {:
