import multiprocessing

def calculate(x, y):
    return x ** y

def worker(x_values, results, start, end):
    for i in range(start, end):
        x = x_values[i]
        result = calculate(x, 2)
        results[i] = result

pool = multiprocessing.Pool(processes=5)

x_values = [i * 0.1 for i in range(11)]
results = [None] * len(x_values)

chunk_size = len(x_values) // 5
start = 0
end = chunk_size
for _ in range(5):
    pool.apply_async(worker, args=(x_values, results, start, end))
    start = end
    end = min(end + chunk_size, len(x_values))

pool.close()
pool.join()

for x, result in zip(x_values, results):
    print(f"calculate({x}, 2) = {result}")
