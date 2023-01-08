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
        
        for (int i =0; i < n; i++)
            cout << nums[i] << endl;
        
        int _max = 0; 
        for (int i=0; i<n; i ++){
            
            
            if (nums[i] == -1)
                continue;
                
            else if (nums[i] != 0){
                _max = max(nums[i], _max);
                continue;
            }
                

            int tmax = 1;
            // cout << "Aa  ";            
            if (i - 1 >=0 && nums[i-1] != -1){
                tmax += nums[i-1];
                // cout << "sdsdf ";
            }
            
            if (i +1 < n && nums[i +1] != -1){
                // cout << "SDFSDF";
                tmax += nums[i +1];
            }
            _max = max(tmax, _max);
        }
        
        return _max;
    }
};
