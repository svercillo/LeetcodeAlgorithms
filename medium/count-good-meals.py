void printmap(map<int, int> myMap){
    for(auto it = myMap.cbegin(); it != myMap.cend(); ++it)
    {
        std::cout << it->first << ":" << it->second << endl;
    }
}


class Solution {
public:
    void printset(unordered_set<int> myset){
        // using begin() to print set
        for (auto it = myset.begin(); it !=
                               myset.end(); ++it)
            cout << *it << "->";
        cout << endl;
    }
    int countPairs(vector<int>& nums) {
        
        long long res = 0;
        int n = nums.size();

        map<int, int> freq;
        
        for (int i =0; i<nums.size(); i++){
            if (freq.find(nums[i]) == freq.end())
                freq[nums[i]] = 0;
            freq[nums[i]] += 1;
        }
        
        // printmap(freq);
        
        
        int max_pow = 23;
        vector<unordered_set<int>> sets;
        for (int i=0; i < max_pow; i++){
            unordered_set<int> set;
            sets.push_back(set);
        }
        
        
        for (auto& it : nums) {
            int ele = it;
            
            int c = 0;
            for (int c=0; c < max_pow; c++){
                
                int twopow = pow(2, c);
                int remainder = twopow - ele;
                
                if (freq.find(remainder) == freq.end())
                    continue;
        
                if (sets[c].find(ele) != sets[c].end()) continue;
                sets[c].insert(ele);

                // cout << ele << " -> " << remainder << " " << c << endl;
                if (remainder < ele){
                    continue;
                } else if (remainder == ele){
                    res += twochoose(freq[ele]);
                } else{
                    // cout << ele << " " << remainder << " " << freq[ele] << " " << freq[remainder] << endl;
                    res += freq[ele] * freq[remainder];
                }
            }
        }
        
        // cout << res << endl; 
        
        int res_i = res % 1000000007;
        return res_i;
    }
    
    long long twochoose(long long n){
        long long res = 0;
        return n * (n-1) / 2;
    }
};
