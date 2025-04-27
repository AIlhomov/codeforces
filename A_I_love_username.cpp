#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

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

    int n;
    cin >> n;
    vector<int> a(n);

    for (int i=0; i<n; i++){
        cin >> a[i];
    }
    int awesomeness = 0;
    
    int lowest = a[0], highest = a[0];

    for (int i=0; i<n; i++){
        if (a[i] > highest){
            highest = a[i];
            awesomeness += 1;
        }
        else if (a[i] < lowest){
            lowest = a[i];
            awesomeness += 1;
        }
    }
    cout << awesomeness << "\n";
    
    



    return 0;
}