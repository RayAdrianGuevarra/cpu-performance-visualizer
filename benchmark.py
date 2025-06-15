import time
import random
import numpy as np
import matplotlib.pyplot as plt

def matrix_multiplication():
    A = np.random.rand(300, 300)
    B = np.random.rand(300, 300)
    start = time.time()
    np.dot(A, B)
    return time.time() - start

def sorting_test():
    data = [random.random() for _ in range(1000000)]
    start = time.time()
    sorted(data)
    return time.time() - start

def list_comprehension():
    start = time.time()
    [x ** 2 for x in range(1000000)]
    return time.time() - start

def run_benchmarks():
    tests = {
        "Matrix Multiplication": matrix_multiplication,
        "Sorting Test": sorting_test,
        "List Comprehension": list_comprehension
    }

    results = {}
    for name, func in tests.items():
        print(f"Running {name}...")
        time_taken = func()
        results[name] = time_taken
        print(f"{name} took {time_taken:.4f} seconds")

    return results

def plot_results(results):
    tasks = list(results.keys())
    times = list(results.values())

    plt.bar(tasks, times, color="skyblue")
    plt.ylabel("Time (s)")
    plt.title("CPU Benchmarking Results")
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.savefig("cpu_benchmark.png")
    plt.show()

if __name__ == "__main__":
    results = run_benchmarks()
    plot_results(results)
