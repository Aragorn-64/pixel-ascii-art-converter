#include <bits/stdc++.h>
using namespace std;

int main(){

    int m,n;
    cin>>n>>m;
    int mat[m][n];


    //SANITIZATION / OPTIMIZATION of DATA:

    // for optimizing by ignoring empty borders
    int r_low=m/2, r_up=m/2;
    int c_low=n/2, c_up=n/2;

    // for optimizing by counting number of non empty per row and going to next row once achieved
    int temp, non_empty[m];

    for(int i=0; i<m; i++){
        non_empty[i]=0;
        for(int j=0; j<n; j++){
            cin>>mat[i][j];

            if(mat[i][j]!=255){
                //if non empty found before or after current row limits
                if(j<c_low) c_low=j;
                if(j>c_up) c_up=j;

                if(i<r_low) r_low=i;
                if(i>r_up) r_up=i;

                //updating count of non_empty
                non_empty[i]++;

            }

        }
        
    }


    // OUTPUT
    return 0;
    
}