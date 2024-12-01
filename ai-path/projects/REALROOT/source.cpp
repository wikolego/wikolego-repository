#include <iostream>

using namespace std;

constexpr int maxSize = 64;
double tab[maxSize];

double func(double x, int n)
{
    double a = tab[n - 1], b = 0.;
    
    for (int k = n - 2; k >= 0; --k)
    {
        b = x * b + a;
        a = x * a + tab[k];
    }

    // cout << a << ", " << b << '\n';

    return x - (a / b);
}

void deleteFromEquation(double x, int n)
{
    for (int i = n - 2; i >= 0; --i)
        tab[i] += tab[i + 1] * x;

    for (int i = 0; i < n; ++i)
        tab[i] = tab[i + 1];
}

void print(int n, const char *c = "\n")
{
    for (int i = n - 1; i >= 0; --i)
        cout << tab[i] << ' ';
    cout << c;
}

int main()
{
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    
    int n;
    cin >> n;

    for (int i = n - 1; i >= 0; --i)
    {
        cin >> tab[i];
    }

    while (n > 1)
    {
        double x = 0;
        for (int i = 0; i < 100; ++i)
            x = func(x, n);

        cout << x << '\n';

        deleteFromEquation(x, n);
        // print(n - 1);
        --n;
    }

    

    return 0;
}

/*

4
1 -2 -5 6


2
3 1


5
1 -4 7 -5 -2


*/