#include <iostream>
#include <string.h>
using namespace std;

int search(int list[],int r,int key){
	int l=0;
	while(r-l>1){
		int mid=(l+r)/2;
		if(list[mid]>key)
			r=mid;
		else
			l=mid;
	}
	return r;
}

int lis(long long int a[],int start,int n){
	int *lis=new int[n];
	memset(lis,0,sizeof(lis[0])*n);
 
	lis[0]=a[start];
	int len=1;
	for(int i=start+1;i<start+n;i++){
		if(a[i]<lis[0])
		lis[0]=a[i];
		
		else if (a[i]>lis[len-1])
		lis[len++]=a[i];
		
		else
		lis[search(lis,len-1,a[i])]=a[i];
	}
	return len;
}

int main() {
	int t;
    cin>>t;
    while(t--){
		int n;
		cin>>n;
		long long int a[2*n];
		for(int i=0;i<n;i++){
			cin>>a[i];
			a[n+i]=a[i];	//each element can access n elements after it in clockwise order 
		}
	    int max=0;
		int ans;
		for(int i=0;i<n;i++){	
    		ans=lis(a,i,n);
    		if(ans>max)
    			max=ans;	
   		}
		cout<<max<<endl;
	}
	return 0;
}
