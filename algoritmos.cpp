#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 1. Bubble Sort
void bubbleSort(vector<double>& arr) {
    long long n = arr.size();
    for (long long i = 0; i < n-1; i++) {
        bool swapped = false;
        for (long long j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                swap(arr[j], arr[j+1]);
                swapped = true;
            }
        }
        if (!swapped) break;
    }
}

// 2. Mergesort
void merge(vector<double>& arr, long long l, long long m, long long r) {
    long long n1 = m - l + 1, n2 = r - m;
    vector<double> L(n1), R(n2);
    for (long long i = 0; i < n1; i++) L[i] = arr[l + i];
    for (long long j = 0; j < n2; j++) R[j] = arr[m + 1 + j];
    
    long long i = 0, j = 0, k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) { arr[k] = L[i]; i++; }
        else { arr[k] = R[j]; j++; }
        k++;
    }
    while (i < n1) { arr[k] = L[i]; i++; k++; }
    while (j < n2) { arr[k] = R[j]; j++; k++; }
}

void mergeSort(vector<double>& arr, long long l, long long r) {
    if (l >= r) return;
    long long m = l + (r - l) / 2;
    mergeSort(arr, l, m);
    mergeSort(arr, m + 1, r);
    merge(arr, l, m, r);
}

// 4. Heapsort
void heapify(vector<double>& arr, long long n, long long i) {
    long long largest = i;
    long long l = 2 * i + 1;
    long long r = 2 * i + 2;
    if (l < n && arr[l] > arr[largest]) largest = l;
    if (r < n && arr[r] > arr[largest]) largest = r;
    if (largest != i) {
        swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}

void heapSort(vector<double>& arr) {
    long long n = arr.size();
    for (long long i = n / 2 - 1; i >= 0; i--) heapify(arr, n, i);
    for (long long i = n - 1; i > 0; i--) {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}	
