#include <iostream>
#include <vector>
#include <string>
#include <stdio.h>
#include <math.h>
#include <algorithm>
 
using namespace std;

int main() {
  int a,b,c;
  cin >> a >> b >> c;
  
  if ( c - (a-b) <=0 ) cout << 0 << endl;
  else cout << c - (a-b) << endl;
  return 0;
}