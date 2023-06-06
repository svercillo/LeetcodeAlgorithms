class RLEIterator {
public:
    int ind = 0;
    int count = 0;
    vector<int> encoding;
    RLEIterator(vector<int>& encoding) {
        this->encoding = encoding;
    }
    
    int next(int n) {
        while (n > 0 && this->ind < this->encoding.size()){
            int remaining = this->encoding[this->ind] - this->count;

            if (n < remaining){ 
                this->count += n;
                n = 0;
                return this->encoding[this->ind + 1];
            } else if (n == remaining){
                // cout << "SDFSDFSDFSDF" << endl;
                this->count = 0;
                this->ind += 2;
                return this->encoding[this->ind -1];
            } else {
                n -= remaining;
                this->ind += 2;
                this->count = 0;
            }
        }

        return -1;
    }
};

/**
 * Your RLEIterator object will be instantiated and called as such:
 * RLEIterator* obj = new RLEIterator(encoding);
 * int param_1 = obj->next(n);
 */
