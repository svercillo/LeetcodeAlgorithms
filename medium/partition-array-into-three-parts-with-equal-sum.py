class Solution {
public:
    bool canThreePartsEqualSum(vector<int>& arr) {
        int n = arr.size();
        vector<int> prefix;
        vector<int> suffix;
        
        for (int i=0;i<n;i++){
            prefix.push_back(0);
            suffix.push_back(0);
        }
        
        int total = 0;
        int presum = 0;
        int suffsum = 0;
        for (int i; i<n; i ++){
            presum += arr[i];
            prefix[i] = presum;
            
            suffsum += arr[n-1-i];
            suffix[n -1 -i] = suffsum; 
            
            total += arr[i];
        }
        for (int i =0; i<n-1; i++){
            for (int j = i+1; j < n; j++){
                int middle = total - prefix[i] - suffix[j]; 
                
                if (middle == prefix[i] && suffix[j] == middle){
                    return true;
                }
            }
        }
        return false;
    }
};
