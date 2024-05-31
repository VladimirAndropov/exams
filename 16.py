import psutil

# Получаем список всех процессов и сортируем их по использованию памяти
processes = [(p.pid, p.memory_percent(), p.name()) for p in psutil.process_iter(['pid', 'memory_percent', 'name'])]
sorted_processes = sorted(processes, key=lambda x: x[1], reverse=True)

# Выводим информацию о топ 10 процессах
print("PID\t%MEM\tCOMMAND")
for pid, mem_percent, name in sorted_processes[:10]:
    print(f"{pid}\t{mem_percent:.2f}\t{name}")
