#include <iostream>
#include <vector>
#include <string>
#include <stdio.h>
#include <math.h>
#include <algorithm>
 
using namespace std;

// ついでにクイックソートを実装
void QuickSort(vector<int> &a, int left, int right) {
  if (right - left <= 1) return;

  int pivot_index = (left + right) / 2; // 適当にここを中点とする
  int pivot = a[pivot_index];
  swap(a[pivot_index], a[right - 1]); // pivotと右端をswap

  int i = left; // i は左詰めされた pivot 未満要素の右端を示す
  for (int j = left; j < right - 1; ++j) {
    if (a[j] < pivot) {
      swap(a[i++], a[j]);
    }
  }
  swap(a[i], a[right - 1]); // pivot を適切な場所に挿入

  // 再帰的に解く
  QuickSort(a, left, i);
  QuickSort(a, i + 1, right);
}

int main() {
  int N;
  cin >> N;
  vector<int> a(N);
  for (int i=0; i < N; ++i) cin >> a[i];

  QuickSort(a, 0, N);
}