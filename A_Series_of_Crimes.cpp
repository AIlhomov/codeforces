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

    int n, m;

    cin >> n >> m;

    vector<string> grid(n);

    vector<pair<int, int>> allRobberies;

    for (int i=0; i<n; i++){
        cin >> grid[i];
    }
    for (int i=0; i<n; i++){
        for (int j=0; j<m; j++){
            if (grid[i][j] == '*'){
                allRobberies.push_back({i, j});
            }
        }
    }
    
    int x1 = allRobberies[0].first, y1 = allRobberies[0].second;
    int x2 = allRobberies[1].first, y2 = allRobberies[1].second;
    int x3 = allRobberies[2].first, y3 = allRobberies[2].second;

    int fourthRow = (x1 == x2 ? x3 : (x1 == x3 ? x2 : x1));
    // For the column, find the missing one
    int fourthCol = (y1 == y2 ? y3 : (y1 == y3 ? y2 : y1));

    cout << fourthRow + 1 << " " << fourthCol + 1 << endl;




    return 0;
}