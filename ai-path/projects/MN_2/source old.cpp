#include <iostream>
#include <iomanip>

using namespace std;

constexpr int maxSize = 10;
double aTab[maxSize][maxSize];
double bTab[maxSize];
double answTab[maxSize];

void swapRows(int a, int b, int f, int l)
{
    if (a == b)
        return;

    for (int i = f; i < l; ++i)
        swap(aTab[i][a], aTab[i][b]);

    swap(bTab[a], bTab[b]);
}

void printMatrix(int n)
{
    for (int y = 0; y < n; ++y)
    {
        for (int x = 0; x < n; ++x)
            cout << aTab[x][y] << ' ';
        cout << "| " << bTab[y];
        cout << '\n';
    }
}

void subtract(int a, int b, int f, int l)
{
    double u = aTab[f][a];
    double d = aTab[f][b];

    for (int i = f + 1; i < l; ++i)
        aTab[i][b] -= aTab[i][a] * d / u;
    aTab[f][b] = 0.;
    bTab[b] -= bTab[a] * d / u;
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
            for (int x = 0; x < n; ++x)
                cin >> aTab[x][y];
            cin >> bTab[y];
        }

        // swapRows(1, 2, 0, n);
        // printMatrix(n);

        subtract(0, 1, 0, n);
        subtract(0, 2, 0, n);
        printMatrix(n);

        // for (int i = 0; i < n; ++i)
        // {
        //     int x = i;
        //     while (x < n)
        //     {
        //         if (aTab[i][x] != 0.)
        //             break;
        //         ++x;
        //     }

        //     if (x == n)
        //         continue;

        //     swapRows(i, x, i, n);

        //     ;
        // }
    }

    return 0;
}

/*

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