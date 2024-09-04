import timeit
import random
import matplotlib.pyplot as plt
import platform
import psutil

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def benchmark_insertion_sort(sizes):
    times = []

    for size in sizes:
        numbers = [random.randint(1, 1000) for _ in range(size)]
        time_taken = timeit.timeit(lambda: insertion_sort(numbers.copy()), number=1)
        times.append(time_taken)
        print(f"Time taken to sort an array of size {size}: {time_taken:.4f} seconds")

    return times

def plot_benchmark(sizes, times):
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, marker='o', linestyle='-', color='b')
    plt.xlabel('Array Size')
    plt.ylabel('Time Taken (seconds)')
    plt.title('Insertion Sort Benchmarking')
    plt.grid(True)
    plt.show()

def get_system_info():
    uname = platform.uname()
    python_version = platform.python_version()
    cpu_info = platform.processor()
    memory_info = psutil.virtual_memory()
    
    info = {
        'OS': uname.system,
        'OS Version': uname.version,
        'Machine': uname.machine,
        'Processor': cpu_info,
        'Python Version': python_version,
        'Total Memory': f"{memory_info.total / (1024 ** 3):.2f} GB",
        'Available Memory': f"{memory_info.available / (1024 ** 3):.2f} GB"
    }
    
    return info

def print_system_info(info):
    print("\nSystem Information:")
    for key, value in info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    # Get and print system information
    system_info = get_system_info()
    print_system_info(system_info)
    
    # Define different array sizes to benchmark
    array_sizes = [50, 100,1000,2000,8000]
    
    # Perform benchmarking
    times = benchmark_insertion_sort(array_sizes)
    
    # Plot the results
    plot_benchmark(array_sizes, times)
