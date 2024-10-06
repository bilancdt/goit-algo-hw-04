import timeit
import random

# Алгоритм сортування вставками (Insertion Sort)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Алгоритм сортування злиттям (Merge Sort)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

# Функція для вимірювання часу виконання
def benchmark_sorting_algorithms():
    # Налаштування параметрів
    sizes = [100, 1000, 5000, 10000]  # Різні розміри масивів для тестування
    results = []

    for size in sizes:
        # Генерація випадкового масиву
        random_array = [random.randint(1, 100000) for _ in range(size)]
        nearly_sorted_array = sorted(random_array[:])  # Майже відсортований масив

        # Тестування сортування вставками
        insertion_time = timeit.timeit(lambda: insertion_sort(random_array[:]), number=1)
        results.append((size, 'Insertion Sort', insertion_time))

        # Тестування сортування злиттям
        merge_time = timeit.timeit(lambda: merge_sort(random_array[:]), number=1)
        results.append((size, 'Merge Sort', merge_time))

        # Тестування Timsort (вбудована функція sorted)
        timsort_time = timeit.timeit(lambda: sorted(random_array[:]), number=1)
        results.append((size, 'Timsort', timsort_time))

    return results

# Виведення результатів
def display_results(results):
    print(f"{'Size':<10}{'Algorithm':<20}{'Time (seconds)':<15}")
    print("=" * 45)
    for result in results:
        print(f"{result[0]:<10}{result[1]:<20}{result[2]:<15.6f}")

# Основна функція
if __name__ == "__main__":
    results = benchmark_sorting_algorithms()
    display_results(results)
