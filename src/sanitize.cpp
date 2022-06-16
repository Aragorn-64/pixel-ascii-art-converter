#include <bits/stdc++.h>
using namespace std;

int main(){
    int m,n;
    cin>>n>>m;

    int r_low=0, r_up=m-1;
    int c_low=0, c_up=n-1;

    int mat[m][n], temp;

    for(int i=0; i<m; i++){
        for(int j=0; j<n; j++){
            //cin>>mat[i][j];
            //if(mat[i][j])
            cin>>temp;
            if(temp>=255){
                cout<<" ";
            }
            else if(temp>=126){
                cout<<".";
            }
            else if(temp>=0){
                cout<<"i";
            }
        }
        cout<<"\n";
    }
    return 0;
    
}