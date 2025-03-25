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

    int petya, vasya, tonya = 0;
    
    int count = 0;

    for (int i = 0; i < n; i++)
    {
        cin >> petya >> vasya >> tonya;

        if ((petya == 1 && vasya == 1) || (petya == 1 && tonya == 1) || (vasya == 1 && tonya == 1)
            || (petya == 1 && vasya == 1 && tonya == 1)){ count++; }
    }
    cout << count;



    return 0;
}