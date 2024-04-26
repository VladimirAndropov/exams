# Напишите простой многопоточный загрузчик URL.
# Список URL скрипт принимает как аргументы командной строки.

import threading
import urllib.request
import sys

def download_url(url):
	try:
		response = urllib.request.urlopen(url)
		print("Загружено:", url)
	except Exception as e:
		print("Ошибка загрузки:", url, "Причина:", e)

def main():
	urls = sys.argv[1:] 
	threads = []  

	for url in urls:
		thread = threading.Thread(target=download_url, args=(url,))
		thread.start()  
		threads.append(thread)  

	
	for thread in threads:
		thread.join() 

if __name__ == "__main__":
	main()