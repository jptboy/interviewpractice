#include <bits/stdc++.h>
using namespace std;

struct val{
    int first;
    int second;
};

template <typename T>
void printvec(vector<T>& v)
{
    for (auto val: v)
    {
        cout << "(" << val.first << "," << val.second << "),";
    } 
    cout << "\n";
}
int h(vector<pair<int,int>>& v, int i)
{
    auto itr = i + 1;
    while (itr < v.size() and v[i].second >= v[itr].first)
    {
        itr++;
    }
    return itr;
}
int f(vector<pair<int,int>>& v, int i)
{
    if (v.size() == 0) return 0;
    if (v.size() == 1) return 1;
    if (i >= v.size()) return 0;
    auto newi = h(v,i);
    return 1 + f(v, newi);
}
int maxChainLen(struct val p[], int n)
{
    auto ret = 0;
    vector<pair<int,int>> propervec;
    for (int i = 0; i < n; ++i)
    {
        propervec.push_back(pair<int,int>(p[i].first, p[i].second));
    }
    auto sortlambda = [&](pair<int,int> p1, pair<int,int> p2){
        return p1.first < p2.first;   
    };
    sort(propervec.begin(),propervec.end(),sortlambda);
    vector<int> answers;
    for (int i = 0; i < propervec.size(); i++)
    {
        answers.push_back(f(propervec,i));
    }
    ret = *max_element(answers.begin(), answers.end());
    return ret;
}


int main(int argc, char const *argv[])
{
    val vs[] ={{5,24},{15,28},{39,60},{27,40},{50,90}}; 
    auto ans = maxChainLen(vs,sizeof(vs)/sizeof(vs[0]));
    return 0;
}
