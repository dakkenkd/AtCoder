#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;

int main() {
  int n;
  cin >> n;
  vector<ll> dp(2,1);
  rep(i,n) {
    string s;
    cin >> s;
    // 次のDPテーブルを作るための初期化
    vector<ll> p(2); swap(dp,p);
    // 前の y が 0,1の時ときと、現在の x が0,1のとき、 現在の y がどうなるかを調べる
    rep(j,2)rep(x,2) {
      int nj = j;
      if (s == "AND") nj &= x;
      else nj |= x;
      // dp[nj] → 現在のyになる場合の数
      // p[j] → 前の  y=0,1 である場合の数 
      dp[nj] += p[j];
    }
  }
  cout << dp[1] << endl;
  return 0;
}