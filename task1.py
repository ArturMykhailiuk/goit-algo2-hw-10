import time
import random
import matplotlib.pyplot as plt


def randomized_quick_sort(arr):
    import random

    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    less_than_pivot = [x for x in arr if x < pivot]
    equal_to_pivot = [x for x in arr if x == pivot]
    greater_than_pivot = [x for x in arr if x > pivot]

    return (
        randomized_quick_sort(less_than_pivot)
        + equal_to_pivot
        + randomized_quick_sort(greater_than_pivot)
    )


def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    less_than_pivot = [x for x in arr if x < pivot]
    equal_to_pivot = [x for x in arr if x == pivot]
    greater_than_pivot = [x for x in arr if x > pivot]

    return (
        deterministic_quick_sort(less_than_pivot)
        + equal_to_pivot
        + deterministic_quick_sort(greater_than_pivot)
    )


def generate_random_array(size):
    return [random.randint(0, 1000000) for _ in range(size)]


def benchmark_sorting_algorithms():
    sizes = [10000, 50000, 100000, 500000]
    results = []

    for size in sizes:
        arr = generate_random_array(size)

        # Benchmark randomized quicksort
        start_time = time.time()
        for _ in range(5):
            randomized_quick_sort(arr.copy())
        randomized_time = (time.time() - start_time) / 5

        # Benchmark deterministic quicksort
        start_time = time.time()
        for _ in range(5):
            deterministic_quick_sort(arr.copy())
        deterministic_time = (time.time() - start_time) / 5

        results.append((size, randomized_time, deterministic_time))

    print_results(results)
    plot_execution_times(results)


def print_results(results):
    for size, randomized_time, deterministic_time in results:
        print(f"Array size: {size}")
        print(f"  Randomized QuickSort: {randomized_time:.4f} seconds")
        print(f"  Deterministic QuickSort: {deterministic_time:.4f} seconds")
        print()


def plot_execution_times(results):
    sizes = [size for size, _, _ in results]
    randomized_times = [randomized_time for _, randomized_time, _ in results]
    deterministic_times = [deterministic_time for _, _, deterministic_time in results]

    plt.figure(figsize=(10, 5))
    plt.plot(sizes, randomized_times, label="Randomized QuickSort", marker="o")
    plt.plot(sizes, deterministic_times, label="Deterministic QuickSort", marker="x")

    plt.title("QuickSort Execution Time Comparison")
    plt.xlabel("Array Size")
    plt.ylabel("Execution Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.savefig("quicksort_execution_times.png")
    plt.show()


if __name__ == "__main__":
    benchmark_sorting_algorithms()
