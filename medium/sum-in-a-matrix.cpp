class Solution {
public:
    int matrixSum(vector<vector<int>>& nums) {

        for (int i =0 ; i <nums.size(); i++){
            vector<int> col = nums[i];
            sort(nums[i].begin(), nums[i].end(), greater<int>());
        }

        int score = 0;
        int count = 0;
        while (nums[0].size() > 0){
            count += 1;
            int score_val = -numeric_limits<int>::infinity();
            for (int i=0; i<nums.size(); i++){
                
                pop_heap(nums[i].begin(), nums[i].end());
                int largest_row_val = nums[i][nums[i].size() -1];
                nums[i].pop_back();

                if (largest_row_val > score_val){
                    score_val = largest_row_val;
                }
            }
            score += score_val;
        }



        cout << count << endl;
        return score;
    }
};
