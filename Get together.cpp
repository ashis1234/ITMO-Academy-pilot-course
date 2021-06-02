/*
    Auther: ghoshashis545 Ashis Ghosh
    College: Jalpaiguri Govt Enggineering College
*/
#include <bits/stdc++.h>
#include<algorithm>
#include<string>
using namespace std;
// #include <ext/pb_ds/assoc_container.hpp>
// #include <ext/pb_ds/tree_policy.hpp>
// using namespace __gnu_pbds;
// template <class type1>
// using ordered_multiset = tree <type1, null_type, less_equal <type1>, rb_tree_tag, tree_order_statistics_node_update>;
// typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> ordered_set; 

#define ll int
#define int long long
#define ld long double
#define ff first
#define ss string 
#define se second
#define sp(x) cout << fixed << setprecision(x)
#define endl "\n"
#define ub upper_bound
#define lb lower_bound
#define clr(a,x) memset(a,x,sizeof(a))
#define alt(v) v.begin(),v.end()
#define ralt(v) v.rbegin(),v.rend()
#define pb emplace_back
#define mp make_pair
#define fab(i,a,b) for(int i=(a);i<(b);i++)
#define fba(i,a,b) for(int i=(b);i>=(a);i--)
int mod=1000000007;
// int mod=998244353;
int dx[]={-1,1,0,0};
int dy[]={0,0,1,-1};

bool test  = 0;


int n;
vector<pair<int,int>> v;
void solve()
{
    cin >> n;
    v.resize(n);
    for(int i = 0; i < n; ++i)
        cin >>v[i].ff >> v[i].se;

    

    auto check = [&](long double mid){
        long double mx = 0.00000000000;
        for(int i = 0; i < n; ++i){
            long double x = v[i].ff;
            long double y = v[i].se;
            x = (long double)abs(x - mid)/y;
            mx = max(mx,x);
        }
        return mx;
    };
    
    
    long double l = -1000000000 , r = 1000000000 , m;
    while(r - l > 1e-6)
    {
        m = (long double) (r+l)/2;
        long double xl = check(m - 0.000001);
        long double x =  check(m);
        long double xr = check(m + 0.000001);
        if(x <= xl and x <= xr){
            sp(12)<<x;
            return;
        }
        if(xl >= x and x >= xr)
            l = m;
        else
            r = m;
    }

    

}
 
 
 
    
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
signed main()
{
    ios_base::sync_with_stdio(false);cin.tie(NULL);
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    //precompute();
    int t=1;
    if(test)
    cin>>t;
    while(t--)
    {
        solve();
    }
    return 0;
} 
s