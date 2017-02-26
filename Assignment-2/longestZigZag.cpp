#include <iostream>
#include <vector>
using namespace std;
int longestZigZag(vector <int> sequence){
    int n = sequence.size();
    int dp[n][2];
    //dp[i][0] = lenth of longest subsequence when ith element is larger than i-1th element
    //dp[i][1] = lenth of longest subsequence when ith element is smaller than i-1th element
    for(int i = 0; i<n; i++){
        dp[i][0] = dp[i][1] = 1;
    }
    int ans = 1;
    for(int i = 0; i<n; i++){
        for(int j = 0; j<i; j++){
            if(sequence[j]>sequence[i]){
                dp[i][0] = max(dp[i][0],dp[j][1]+1);
            }
            if(sequence[j]<sequence[i]){
                dp[i][1] = max(dp[i][1],dp[j][0]+1);
            }
        }
        ans = max(ans, max(dp[i][0], dp[i][1]));
    }
    return ans;
}
int main(){
    vector <int> seq = {374, 40, 854, 203, 203, 156, 362, 279, 812, 955, 
		600, 947, 978, 46, 100, 953, 670, 862, 568, 188, 
		67, 669, 810, 704, 52, 861, 49, 640, 370, 908, 
		477, 245, 413, 109, 659, 401, 483, 308, 609, 120, 
		249, 22, 176, 279, 23, 22, 617, 462, 459, 244};
    cout<<longestZigZag(seq)<<endl;
	return 0;
}
