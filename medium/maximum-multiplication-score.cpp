#include <vector>
#include <limits>
using namespace std;

class Solution {
public:
    vector<int> a;
    vector<int> b;
    vector<vector<long long>> cache;

    long long maxScore(vector<int>& a, vector<int>& b) {
        this->a = a;
        this->b = b;
        int n = b.size();
        cache = vector<vector<long long>>(n, vector<long long>(5, numeric_limits<long long>::min()));

        return maxScoreHelper(0, 4);
    }

private:
    long long maxScoreHelper(int ind, int remaining) {
        if (remaining == 0) {
            return 0;
        } else if (ind == b.size()) {
            return numeric_limits<long long>::min();
        }

        if (cache[ind][remaining] != numeric_limits<long long>::min()) {
            return cache[ind][remaining];
        }

        long long res1 = numeric_limits<long long>::min();
        long long res_min_one = maxScoreHelper(ind + 1, remaining - 1);
        if (res_min_one != numeric_limits<long long>::min()) {
            res1 = static_cast<long long>(a[4 - remaining]) * static_cast<long long>(b[ind]) + res_min_one;
        }

        long long res2 = maxScoreHelper(ind + 1, remaining);

        long long res = max(res1, res2);
        cache[ind][remaining] = res;
        return res;
    }
};
