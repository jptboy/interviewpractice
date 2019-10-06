#include <bits/stdc++.h>
using namespace std;
int knapsack(int W, vector<int> values, vector<int> weights)
{
    vector<pair<int,int>> goods;
    for (int i = 0; i < values.size(); i++)
    {
        goods.push_back(pair<int,int>(values[i], weights[i]));
    }
    auto sortlambda = [&](pair<int,int> const& p1,pair<int,int> const& p2)
    {
        return p1.second < p2.second;
    };
    sort(goods.begin(), goods.end(), sortlambda);
    vector<vector<int>> dp(goods.size() + 1, vector<int>(W + 1, 0));
    for (int i = 1; i < goods.size() + 1; i++)
    {
        for (int j = 1; j < W + 1; j++)
        {
            auto newweight = j - goods[i - 1].second;
            auto v1 = 0;
            if (newweight < 0) v1 = -1;
            else
            {
                v1 = dp[i-1][newweight] + goods[i - 1].first;
            }
            auto v2 = dp[i-1][j];
            dp[i][j] = max(v1,v2);
        }
    }
    return dp[goods.size()][W];
}


int knapsack2(int dub, vector<int> values, vector<int> weights)
{
    vector<pair<int,int>> goods;
    for (int i = 0; i < values.size(); i++)
    {
        goods.push_back(pair<int,int>(values[i], weights[i]));
    }
    auto sortlambda = [&](pair<int,int> const& p1,pair<int,int> const& p2)
    {
        return p1.second < p2.second;
    };
    sort(goods.begin(), goods.end(), sortlambda);
    function<int(int, int)> f1 = [&](int i, int W)
    {
        if (i < 0 or W == 0) return 0;
        auto newW = W - goods[i].second;
        if (newW < 0) return f1(i - 1, W);
        return max(f1(i - 1, W), goods[i].first + f1(i - 1, newW));
    };
    return f1(goods.size() - 1, dub);
}

int main(int argc, char const *argv[])
{
    auto W = 83;
    auto vals = vector<int>({55,61,51,75,17,22,4,13,39,28,77,49,46,91,14,67,88,62,25,37,69,38,59,62,48,88,100,53});
    auto weights = vector<int>({96,16,34,53,88,6,50,26,76,10,8,4,37,18,73,54,30,31,97,2,28,24,2,30,79,77,33,86});
    auto ans = knapsack(W,vals,weights);
    cout << ans << "\n";
    return 0;
}
