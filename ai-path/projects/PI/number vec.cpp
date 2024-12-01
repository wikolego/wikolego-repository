#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

class Number
{
public:
    ll m_base;
    vector<ll> m_vec;
public:
    Number()
    {
        m_base = 1'0ll;
    }
    void add(const Number &number)
    {
        for (ll i = 0ll, to_add = 0ll, sz = number.m_vec.size(); i < sz || to_add != 0; ++i)
        {
            if (i >= m_vec.size())
                m_vec.push_back(0);
            ll numberVal = (i < sz ? number.m_vec.at(i) : 0ll);
            ll num = m_vec.at(i) + numberVal + to_add;
            to_add = 0;
            if (num >= m_base)
            {
                to_add = 1ll;
                m_vec.at(i) = num - m_base;
            }
            else
                m_vec.at(i) = num;
        }
    }
    void subtract(const Number &number)
    {
        for (ll i = 0ll, sz = number.m_vec.size(); i < m_vec.size() && (i < sz || m_vec.at(i) < 0ll); ++i)
        {
            ll minusNum = (i < sz ? number.m_vec.at(i) : 0ll);
            m_vec.at(i) -= minusNum;
            if (m_vec.at(i) < 0ll)
            {
                m_vec.at(i) += m_base;
                --(m_vec.at(i + 1));
            }
        }
        if (m_vec.at(m_vec.size() - 1) == 0ll)
            m_vec.pop_back();
    }
    void multiply(const Number &number)
    {
        vector<ll> res;
        for (ll i = 0ll; i < m_vec.size(); ++i)
        {
            ll num = m_vec.at(i);
            for (ll x = 0ll, to_add = 0ll, sz = number.m_vec.size(); x < sz || to_add != 0ll; ++x)
            {
                ll numberVal = (x < sz ? number.m_vec.at(x) : 0ll);
                ll a = num * numberVal + to_add;
                to_add = a / m_base;
                if (res.size() <= i + x)
                    res.push_back(0ll);
                res.at(i + x) += a % m_base;
                to_add += res.at(i + x) / m_base;
                res.at(i + x) %= m_base;
            }
        }
        m_vec = res;
    }
    void multiply(const ll &number)
    {
        for (ll i = 0ll, to_add = 0ll, sz = m_vec.size(); i < sz || to_add != 0; ++i)
        {
            if (i >= m_vec.size())
                m_vec.push_back(0);
            ll num = m_vec.at(i) * number + to_add;
            
            m_vec.at(i) = num % m_base;
            to_add = num / m_base;
        }
    }
    bool operator<=(const Number &number)
    {
        if (m_vec.size() < number.m_vec.size())
            return true;
        if (number.m_vec.size() < m_vec.size())
            return false;

        for (int i = m_vec.size() - 1; i >= 0; --i)
        {
            if (m_vec.at(i) < number.m_vec.at(i))
                return true;
            if (number.m_vec.at(i) < m_vec.at(i))
                return false;
        }
        return true;
    }
    void print(const char *c = "\n")
    {
        for (int i = m_vec.size() - 1; i >= 0; --i)
            cout << m_vec.at(i) << ' ';
        cout << c;
    }
};

int main()
{
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);

    Number number1, number2;

    // number1.m_vec.push_back(4);
    // number1.m_vec.push_back(9);
    // number1.m_vec.push_back(3);

    // number2.m_vec.push_back(6);
    // number2.m_vec.push_back(1);
    // number2.m_vec.push_back(8);

    // if (number1 <= number2)
    //     cout << "OK\n";
    // else
    //     cout << "NOT OK\n";

    // number1.multiply(number2);
    // number1.print();

    // number1.multiply(5);
    // number1.print();

    // number1.m_vec.push_back(0);
    // number1.m_vec.push_back(0);
    // number1.m_vec.push_back(0);
    // number1.m_vec.push_back(1);

    // number2.m_vec.push_back(6);
    // number2.m_vec.push_back(1);
    // number2.m_vec.push_back(8);

    number1.subtract(number2);
    number1.print();

    return 0;
}

/*

394 * 816 = 321504

*/