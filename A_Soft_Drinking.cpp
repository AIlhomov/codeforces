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

    // n friends
    // k * l = drink
    // drink / n = toasts
    // c * d = limit
    // p / np = toasts2 ?
    // min(toasts, limit, toasts2) / n
    int n, k, l, c, d, p, nl, np;
    cin >> n >> k >> l >> c >> d >> p >> nl >> np;
    
    int drink = k * l;
    int toasts = drink / nl;
    int limit = c * d;
    int toasts2 = p / np;
    cout << min({toasts, limit, toasts2}) / n;




    return 0;
}