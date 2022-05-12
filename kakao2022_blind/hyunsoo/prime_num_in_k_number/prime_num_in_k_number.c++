#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <cmath>

using namespace std;

bool check(long long num)
{
    if (num == 2)
        return true;
    if (num == 1 || num % 2 == 0)
        return false;

    for (long long i = 3; i <= (long long)sqrt(num); i += 2)
    {
        if (num % i == 0)
            return false;
    }

    return true;
}

string convert(int num, int base)
{
    int q = num / base, r = num % base;
    if (q)
        return convert(q, base) + to_string(r);
    else
        return to_string(r);
}

int solution(int n, int k)
{
    string number = k == 10 ? to_string(n) : convert(n, k);
    stringstream ss(number);

    int answer = 0;
    // 스트림에서 구분자로 구분해서 하나씩 얻어올 때 마다 value에 담음
    // 끝까지 가서 null 나오면 while문 종료
    string value;
    while (getline(ss, value, '0'))
    {
        if (value.size() && check(stol(value)))
            answer++;
    }

    return answer;
}

int main()
{
    cout << solution(437674, 3) << '\n'; // 3
    // cout << solution(110011, 10) << '\n'; // 2
    return 0;
}