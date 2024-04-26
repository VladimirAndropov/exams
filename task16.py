import psutil

def top_10_memory_consumers():
    # Получение списка всех процессов
    all_processes = list(psutil.process_iter(attrs=['pid', 'name', 'memory_info']))

    # Сортировка процессов по потреблению оперативной памяти
    sorted_processes = sorted(all_processes, key=lambda p: p.info['memory_info'].rss, reverse=True)

    # Вывод информации о топ 10 процессах по потреблению оперативной памяти
    print("Топ 10 процессов по потреблению оперативной памяти:")
    for i, process in enumerate(sorted_processes[:10], 1):
        pid = process.info['pid']
        name = process.info['name']
        memory_usage = process.info['memory_info'].rss / (1024 * 1024)  # Преобразование из байт в мегабайты
        print(f"{i}. PID: {pid}, Имя: {name}, Потребление памяти: {memory_usage:.2f} MB")

if __name__ == "__main__":
    top_10_memory_consumers()
