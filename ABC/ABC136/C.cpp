#include <iostream>
#include <vector>
#include <string>
#include <stdio.h>
#include <math.h>
#include <algorithm>
 
using namespace std;

int main() {
  int N, flag, sa; cin >> N;
  vector<int> A(N);
  flag = true;
  
  for (int i=0; i<N; i++) cin >> A.at(i);
  for (int i=N-1; i>0; i--) {
    sa = A.at(i-1) - A.at(i);
    if ( sa >= 2) {
      flag = false;
      break;
    } else if (sa == 1) {
      A.at(i-1) -= 1;
    }
  }
  if (flag) cout << "Yes" << endl;
  else cout << "No" << endl;
  return 0;
}