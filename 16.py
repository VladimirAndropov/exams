import psutil

# Функция для получения информации о процессах
def get_process_info():
    processes = psutil.process_iter()
    top_processes = []

    for process in processes:
        try:
            process_info = psutil.Process(process.pid)
            mem_info = process_info.memory_info()
            mem_usage = mem_info.rss
            process_name = process_info.name()

            top_processes.append((process_name, mem_usage))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    return sorted(top_processes, key=lambda x: x[1], reverse=True)

# Выводим топ10 процессов по потреблению оперативной памяти
for i, (process_name, mem_usage) in enumerate(get_process_info()[:10]):
    print(f"{i + 1}. {process_name}: {mem_usage / 1024 / 1024:.2f} MB")