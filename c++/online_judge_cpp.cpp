#include<iostream>
using namespace std;

int main(){
  int x, y, z;
  cin >> x >> y;
  
  z = (x > y)? 0: (x < y)? 1: 2; 
  if (z == 0) cout << "a > b" << endl;
  else if (z == 1) cout << "a < b" << endl;
  else cout << "a == b" << endl;
  return 0;
}