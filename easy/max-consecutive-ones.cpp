class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int n = nums.size();
        
        for (int i =0; i < n; i ++){
            int start = i;
            
            int count = 0;
            while (i < n && nums[i] == 1){
                count +=1;
                nums[i] = -1;
                i ++;
            }
            nums[start] = count; 
            if (nums[start] > 0){
                nums[start+count -1] = count;
            }
        }
        
        int _max = 0;
        for (int i =0; i < n; i++)
        {
            _max = max(nums[i], _max);
        }
        
        return _max;
    };
};
