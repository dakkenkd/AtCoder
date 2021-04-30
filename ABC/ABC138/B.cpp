#include <iostream>
#include <vector>
#include <string>
#include <stdio.h>
#include <math.h>
#include <algorithm>
 
using namespace std;

int main() {
  int N; cin >>N;
  vector<double> A(N);
  for (int i=0; i<N; ++i) {
    cin >> A.at(i);
    A.at(i) = 1.0/A.at(i);
  }
  double ans;
  for (int i=0; i<N; ++i) ans += A.at(i);
  cout << 1.0/ans << endl;
  return 0;
}