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

    int t;
    cin >> t;

    while (t--){
        int n;
        cin >> n;
        vector<int> a(n);
        for (int i=0; i<n; i++){
            cin >> a[i];
        }

        sort(a.begin(), a.end());
        bool itWorks = false;
        for (int i=0; i<n-1; i++){
            if (a[i]+1 == a[i+1] || a[i] == a[i+1]){
                itWorks = true;
            }
            else{
                itWorks = false;
                break;
            }
        }
        if (itWorks || a.size() == 1) cout << "YES\n";
        else cout << "NO\n";

    }
    



    return 0;
}