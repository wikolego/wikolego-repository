#include <iostream>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;

constexpr ull maxSize = 1000000, maxSize2 = 10010;
ll tab[3][maxSize];
ll dzTab[10][maxSize];
ll *freeAddr = &tab[2][0];
int resTab[maxSize2];

class Number
{
public:
    ll m_base;
    ll *m_tab;
    int m_size;
public:
    Number()
    {
        m_base = 1000000000ll;
        m_tab = nullptr;
        m_size = 0;
    }
    Number(ll *tab_pt, ll size)
    {
        m_base = 1000000000ll;
        m_tab = tab_pt;
        m_size = size;
    }
    Number(const Number &number, ll *tab_pt)
    {
        m_base = number.m_base;
        m_tab = tab_pt;
        m_size = number.m_size;

        for (int i = 0; i < m_size; ++i)
            m_tab[i] = number.m_tab[i];
    }
    void add(const Number &number)
    {
        if (m_size < number.m_size)
            m_size = number.m_size;
        for (int i = 0; i < number.m_size || m_tab[i] >= m_base; ++i)
        {
            m_tab[i] += number.m_tab[i];
            if (m_tab[i] >= m_base)
            {
                m_tab[i] -= m_base;
                ++(m_tab[i + 1]);
            }
        }
        if (m_tab[m_size] != 0ll)
            ++m_size;
    }
    void subtract(const Number &number)
    {
        for (int i = 0; i < m_size && (i < number.m_size || m_tab[i] < 0ll); ++i)
        {
            m_tab[i] -= number.m_tab[i];
            if (m_tab[i] < 0ll)
            {
                m_tab[i] += m_base;
                --(m_tab[i + 1]);
            }
        }
        while (m_size > 0 && m_tab[m_size - 1] == 0ll)
            --m_size;
    }
    void multiply(const Number &number)
    {
        int new_size = m_size + number.m_size - 1;
        for (int i = 0; i < m_size; ++i)
        {
            for (int x = 0; x < number.m_size || freeAddr[i + x] != 0; ++x)
            {
                freeAddr[i + x] += number.m_tab[x] * m_tab[i];
                freeAddr[i + x + 1] += freeAddr[i + x] / m_base;
                freeAddr[i + x] %= m_base;
            }
            m_tab[i] = 0;
        }
        swap(m_tab, freeAddr);
        m_size = new_size;
        if (m_tab[m_size] != 0)
            ++m_size;
    }
    void multiply(const ll &number)
    {
        for (int i = 0ll; i < m_size || m_tab[i] != 0ll; ++i)
        {
            freeAddr[i] += m_tab[i] * number;            
            freeAddr[i + 1] = freeAddr[i] / m_base;
            freeAddr[i] %= m_base;

            m_tab[i] = 0;
        }
        swap(m_tab, freeAddr);
        if (m_tab[m_size] != 0)
            ++m_size;
    }
    bool operator<=(const Number &number)
    {
        if (m_size < number.m_size)
            return true;
        if (number.m_size < m_size)
            return false;

        for (int i = m_size - 1; i >= 0; --i)
        {
            if (m_tab[i] < number.m_tab[i])
                return true;
            if (number.m_tab[i] < m_tab[i])
                return false;
        }
        return true;
    }
    void print(const char *c = "\n")
    {
        // cout << "size: " << m_size << '\n';
        for (int i = m_size - 1; i >= 0; --i)
            cout << m_tab[i] << ' ';
        cout << c;
    }
};

void func(int accuracy)
{
    ll u = accuracy, d = accuracy * 2ll + 1ll;
    Number valU(&tab[0][0], 1), valD(&tab[1][0], 1);
    tab[0][0] = 1;
    tab[1][0] = 1;

    while (u > 0ll)
    {
        valD.multiply(d);
        valU.multiply(u);
        valU.add(valD);

        u -= 1ll;
        d -= 2ll;
    }
    valU.multiply(2ll);

    Number dTab[10];
    dTab[0] = Number(&dzTab[0][0], 0);
    dTab[1] = Number(valD, &dzTab[1][0]);
    for (int i = 2; i < 10; ++i)
    {
        dTab[i] = Number(dTab[i - 1], &dzTab[i][0]);
        dTab[i].add(valD);
    }

    for (int i = 0; i < 10001; ++i)
    {
        int l = 0, r = 9, res = -1;
        while (l <= r)
        {
            int mid = (l + r) / 2;
            if (dTab[mid] <= valU)
            {
                res = mid;
                l = mid + 1;
            }
            else
                r = mid - 1;
        }
        resTab[i] = res;
        
        valU.subtract(dTab[res]);
        valU.multiply(10ll);
    }
}

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);

    func(33220);

    int t;
    cin >> t;

    while (t--)
    {
        int n;
        cin >> n;

        cout << "3.";
        for (int i = 1; i <= n; ++i)
            cout << resTab[i];
        cout << '\n';
    }

    return 0;
}


/*

3
1
2
3

3.1
3.14
3.141

*/