class Solution {
public:
    vector<vector<int>> highFive(vector<vector<int>>& items) {
        
        
        map <int, vector<int>> map; 
        
        for (int i =0; i < items.size(); i++){
            int id = items[i][0];
            int score = items[i][1];   
            
            if (map.find(id) == map.end()){
                vector<int> v; 
                map[id] = v;
            }
            map[id].push_back(score);
            sort(map[id].begin(), map[id].end(), greater<int>());
            if (map[id].size() == 6){
                map[id].pop_back();
            }
        }   
        vector<vector<int>> result;
        

        for (const auto &[k ,v] : map){
            int sum = 0;
            for (const auto &ele : v){
                sum += ele;
            }
            vector<int> entry;
            entry.push_back(k);
            entry.push_back(sum / v.size());
            result.push_back(entry);
        }
        return result; 
    }
};
