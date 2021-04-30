#include <iostream>
#include <vector>
#include <string>
#include <stdio.h>
#include <math.h>
#include <algorithm>
 
using namespace std;
int digit(int a){
  int res=0;
  
  while(a){
    a/=10;
    res++;
  }
  return res;
}

int main() {
  int n; cin >> n;
  
  int res=0;
  
  for (int i=1; i<=n; i++){
    int d = digit(i);
    if (d%2==1) res++;
  }
  cout << res << endl;
  
}