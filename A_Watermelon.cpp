#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <cmath>

using namespace std;

#define ll long long
#define inf 1e9

void fastio()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
}

int main()
{

    fastio();

    
    double n; 
    cin >>n;
    double divided = n / 2;
    // if the divided is not .5 and not even its YES
    if (divided == floor(divided) && int(divided) % 2 == 0) cout << "YES";
    //else check if an even number + the rest (if its an even number) to see if it equals to n
    //for example 2 + 4 = 6 (which is "YES")
    else {
        for (int i = 2; i<n; i += 2){
            if ((int(n)-i) % 2 == 0){
                if (i + (n-i) == n){
                    cout << "YES";
                    return 0;
                } 
            }
            
        }
        cout << "NO";
    }
    
    




    return 0;
}