#include<iostream>
using namespace std;
void mained(string str, int n, string &res)
{
     if (n == 0)
    {
        res.append(str);
        return;
    }
    int len = str.length();
    if (len <= n)
        return;
    int mini = 0;
    for (int i = 1; i<=n ; i++)
        if (str[i] < str[mini])
            mini = i;
    res.push_back(str[mini]);
    string new_str = str.substr(mini+1, len-mini);
    mained(new_str, n-mini, res);
}
string least(string str, int n)
{
    string res = "";
    mained(str, n, res);
    return res;
}

int main()
{
    string str;
    int n;
    cin>>str>>n;
    cout << least(str, n);
    return 0;
}
