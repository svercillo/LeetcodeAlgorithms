class MovingAverage {
public:
    list<int> q;
    int size;
    int num = 0; 
    int sum = 0;
    MovingAverage(int s) {
        size = s;
    }
    
    double next(int val) {
        if (num < size){
            
            num ++;
            sum += val;
            q.push_back(val);
            return (double)sum / (double) num;
        } else {

            int first = q.front();
            q.pop_front();
            
            sum -= first; 
            sum += val;
            q.push_back(val);
            
            return (double) sum/ (double) num;
        };
    };
};
