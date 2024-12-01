#include <iostream>
#include <iomanip>

using namespace std;

constexpr int maxSize = 10;
double tab[maxSize + 1][maxSize];
double answTab[maxSize];
bool calculatedTab[maxSize]; // true if nth element is calculated

void swapRowsParts(int a, int b, int f, int l)
{
    if (a == b)
        return;

    for (int i = f; i <= l; ++i)
        swap(tab[i][a], tab[i][b]);
}

void divideRowPart(int a, int f, int l)
{
    if (tab[f][a] == 1.)
        return;
    
    for (int i = f + 1; i <= l; ++i)
        tab[i][a] /= tab[f][a];
    tab[f][a] = 1.;
}

void subtractRowPart(int a, int b, int f, int l)
{
    double u = tab[f][a];
    double d = tab[f][b];

    for (int i = f + 1; i <= l; ++i)
        tab[i][b] -= tab[i][a] * d / u;
    tab[f][b] = 0.;
}

void printMatrix(int n)
{
    for (int y = 0; y < n; ++y)
    {
        for (int x = 0; x < n; ++x)
            cout << tab[x][y] << ' ';
        cout << "| " << tab[n][y];
        cout << '\n';
    }
}

int main()
{
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    cout << fixed << setprecision(3);

    int t;
    cin >> t;

    while (t--)
    {
        int n;
        cin >> n;

        for (int y = 0; y < n; ++y)
        {
            calculatedTab[y] = false;


            for (int x = 0; x <= n; ++x)
                cin >> tab[x][y];
        }
        
        for (int i = 0, y = 0; i < n; ++i)
        {
            int a = y;
            while (a < n)
            {
                if (tab[i][a] != 0.)
                    break;
                ++a;
            }

            if (a == n)
                continue;

            swapRowsParts(y, a, i, n);
            divideRowPart(y, i, n);

            for (a = y + 1; a < n; ++a)
            {
                if (tab[i][a] == 0.)
                    continue;
                subtractRowPart(y, a, i, n);
            }

            ++y;
        }

        bool succ = true;
        for (int y = n - 1; y >= 0; --y)
        {
            int reqVal = tab[n][y];
            int x = n - 1;
            
            int firstIndex = 0;
            while (firstIndex < n && tab[firstIndex][y] == 0.)
                ++firstIndex;

            if (firstIndex == n)
            {
                if (reqVal != 0.)
                {
                    succ = false;
                    break;
                }
                continue;
            }

            for (int x = n - 1; x > firstIndex; --x)
            {
                if (!calculatedTab[x])
                {
                    answTab[x] = 1.;
                    calculatedTab[x] = true;
                }
                reqVal -= answTab[x] * tab[x][y];
            }
            answTab[firstIndex] = reqVal / tab[firstIndex][y];
            calculatedTab[firstIndex] = true;
        }

        if (succ)
        {
            cout << "tak\n";
            for (int i = 0; i < n; ++i)
                cout << answTab[i] << '\n';
        }
        else
            cout << "nie\n";
    }
    
    return 0;
}

/*

1
3
1 1 1 3
0 0 2 2
0 0 1 1



1
3
1 1 1 3
0 0 2 2
0 0 1 2



1
3
2 4 -2 2
4 9 -3 8
-2 -3 7 10



1
3
1 0 0 1
1 1 0 2
1 1 1 3




2
2
1 0 0
1 1 0
3
1 0 0 1
1 1 0 2
1 1 1 3

nie
tak
1.000
1.000
1.000

*/