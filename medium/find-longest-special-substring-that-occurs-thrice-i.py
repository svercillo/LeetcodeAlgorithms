class Solution {
public:
    int maximumLength(string s) {
        int n = s.size();

        unordered_map<string, int> freq;
        for (int i =0; i < n; i ++){ 
            char c = s[i];
            for (int j = i; j<n && s[j] == c; j ++){ 
                int diff = j- i + 1;

                

                string sub = s.substr(i, diff);

                cout << sub << endl;

                // cout << i << ":" << j << " sub " << sub << endl; 
                if (freq.find(sub) == freq.end()){
                    freq[sub] = 0;
                } 
                freq[sub] += 1;
            }
        }

        
        int longest = -1;
        for (const auto& pair : freq){ 
            string key = pair.first;

            if (pair.second >= 3 && (int) pair.first.size() > longest){
                longest = pair.first.size();
            }

        }
    
        return longest;
    }
};
