#include <iostream>
#include <string.h>
#include <vector>
#include <algorithm>
using namespace std;
 
bool roadblock(vector <string> bad, int a, int b, int c, int d){
    string pattern1 = to_string(a)+" "+to_string(b)+" "+to_string(c)+" "+to_string(d);
    string pattern2 = to_string(c)+" "+to_string(d)+" "+to_string(a)+" "+to_string(b);
    bool found_pattern1 = std::find(bad.begin(), bad.end(), pattern1) != bad.end();
    bool found_pattern2 = std::find(bad.begin(), bad.end(), pattern2) != bad.end();
    return found_pattern1 || found_pattern2;
    }
 
long long numWays(int w, int h, vector <string> bad){
	long long dp[h+1][w+1];
	memset(dp, 0, sizeof(dp));
	dp[0][0] = 1;
 
	for(int i=0; i<=h; i++){
		for(int j=0; j<=w; j++){
			if ((!roadblock(bad, j,i-1,j,i)) && (i!=0))
				dp[i][j] += dp[i-1][j];
			if ((!roadblock(bad, j-1,i,j,i)) && (j!=0))
				dp[i][j] += dp[i][j-1];
		}
	}
	return dp[h][w];
}
int main()
{
  vector <string> bad = {"0 2 0 3", "1 2 1 3", "2 2 2 3", "3 2 3 3", "4 2 4 3", "5 2 5 3", "6 2 6 3", "7 2 7 3", "8 2 8 3", "9 2 9 3"};
  cout<<numWays(20,100,bad)<<endl;
}
