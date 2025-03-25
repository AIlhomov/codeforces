#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <numeric>

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

    ll n;
    cin >> n;
    ll sum_we_got = 0;
    vector<ll> arr(n-1);
    for (ll i=0; i<n-1; i++){
        cin >> arr[i];
        sum_we_got += arr[i]; // the sum we get (n-1) numbers because we are missing one
    }
    
    ll sumTOTAL = ((n * (n + 1)) / 2); // take the total - the one we have (missing 1 number)
    cout << sumTOTAL - sum_we_got; // take the sumTOTAL - sum_we_got 



    return 0;
}