#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <cmath>
#include <iomanip>

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

    ll n, l; // length l, lit by n lanterns
    cin >> n >> l;
    
    
    vector<ll> lanterns(n);

    for (ll i = 0; i < n; i++)
    {
        cin >> lanterns[i];
    }

    sort(lanterns.begin(), lanterns.end());
    
    vector<ll> diff(n-1);
    ll max_gap = 0;
    for (ll i = 1; i < n; i++)
    {
        max_gap = max(max_gap, lanterns[i] - lanterns[i-1]);
        //diff[i] = lanterns[i+1] - lanterns[i];
    }
    //sort(diff.begin(), diff.end());


    
    double d = max({(max_gap / 2.0), (double)lanterns[0], (double)(l - lanterns[n-1])});

    cout << fixed << setprecision(10) << d;

    //22258199.5000000000
    //9609228.0000000000

    return 0;
}