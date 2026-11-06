
import time
import random
import matplotlib.pyplot as plt

def test_sorting(size):
    data = [random.randint(1, 10000) for _ in range(size)]

    start = time.perf_counter()
    sorted(data)
    end = time.perf_counter()

    return end - start


def main():
    sizes = [100, 500, 1000, 2000, 5000]
    runtimes = []

    print("PHASE 4: PERFORMANCE TESTING")
    print("-" * 40)

    for size in sizes:
        runtime = test_sorting(size)
        runtimes.append(runtime)

        print("Dataset size:", size)
        print("Runtime:", round(runtime, 6), "seconds")
        print("-" * 40)

    plt.plot(sizes, runtimes, marker="o")
    plt.xlabel("Dataset Size")
    plt.ylabel("Runtime (seconds)")
    plt.title("Sorting Performance Analysis")
    plt.grid(True)
    plt.savefig("runtime_chart.png")
    plt.show()

    print("Chart saved as runtime_chart.png")
    print("Time complexity of sorting: O(n log n)")


if __name__ == "__main__":
    main()
