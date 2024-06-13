// The Average Time Complexity is O(n(logn))
// The Worst Case of Time Complexity is O(n^2)
// The Space Complexity is O(logn)

const QuickSort = (arr, low = 0, high = arr.length - 1) => {
    if (low < high) {
        let pivotIndex = partition(arr, low, high);
        QuickSort(arr, low, pivotIndex - 1);
        QuickSort(arr, pivotIndex + 1, high);
    }
    return arr;
}

const partition = (arr, low, high) => {
    let pivot = arr[high];
    let i = low - 1;
    for (let j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            [arr[i], arr[j]] = [arr[j], arr[i]];
        }
    }
    [arr[i + 1], arr[high]] = [arr[high], arr[i + 1]];
    return i + 1;
}
