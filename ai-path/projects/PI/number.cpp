#include <iostream>

using namespace std;

typedef long long ll;

constexpr int maxSize = 10010;
ll tab[3][maxSize];
ll *freeAddr = &tab[2][0];

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

int main()
{
    // ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);

    Number number1(&tab[0][0], 3), number2(&tab[1][0], 3);

    tab[0][0] = 6;
    tab[0][1] = 1;
    tab[0][2] = 8;

    tab[1][0] = 4;
    tab[1][1] = 9;
    tab[1][2] = 3;

    // tab[0][0] = 0;
    // tab[0][1] = 0;
    // tab[0][2] = 0;
    // tab[0][3] = 1;

    // tab[1][0] = 4;
    // tab[1][1] = 9;
    
    // tab[0][0] = 999999999;
    // tab[0][1] = 999999999;

    // tab[1][0] = 999999999;
    // tab[1][1] = 999999999;

    // cout << "lol\n";

    // if (number1 <= number2)
    //     cout << "OK\n";
    // else
    //     cout << "NOT OK\n";

    // number1.add(number2);
    // number1.print();

    // number1.subtract(number2);
    // number1.print();

    // number1.multiply(3ll);
    // number1.print();

    // number1.multiply(number2);
    // number1.print();
    
    // number1.subtract(number2);
    // number1.print();

    return 0;
}

/*

816 + 394 = 1210
816 - 394 = 422
816 * 394 = 321504

*/