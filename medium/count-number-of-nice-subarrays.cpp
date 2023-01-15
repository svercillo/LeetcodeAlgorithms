class Solution
{
public:
    int numberOfSubarrays(vector<int> &nums, int k)
    {
        vector<int> inds;

        for (int i = 0; i < nums.size(); ++i)
        {
            if (nums[i] % 2 != 0)
                inds.push_back(i);
        }

        if (inds.size() < k)
            return 0;

        int res = 0;

        for (int i = 0; i < inds.size() - k + 1; i++)
        {
            int j = i + k - 1;
            int start = i == 0 ? -1 : inds[i - 1];
            int end = j == inds.size() - 1 ? nums.size() : inds[j + 1];

            res += (inds[i] - start) * (end - inds[j]);
        }

        return res;
    }
};
