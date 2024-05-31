import psutil


def top_memory_consumers():
    processes = [(p.info['pid'], p.info['name'], p.info['memory_info'].rss) for p in
                 psutil.process_iter(['pid', 'name', 'memory_info'])]
    processes.sort(key=lambda x: x[2], reverse=True)

    for pid, name, memory in processes[:10]:
        print(f"PID: {pid}, Name: {name}, Memory: {memory / (1024 * 1024):.2f} MB")


if __name__ == "__main__":
    top_memory_consumers()
