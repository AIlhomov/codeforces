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

    int k, l, m, n, d;
    cin >> k >> l >> m >> n >> d;
    
    int damagedDragon = 0;

    for (int i=1; i<=d; i++){
        if (i % k == 0 || i % l == 0 || i % m == 0 || i % n == 0){
            damagedDragon += 1;
        }
    }
    cout << damagedDragon << "\n";
    

    return 0;
}