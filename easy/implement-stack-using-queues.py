class MyStack {
public:

    queue<int> q;
    MyStack() {
    }
    
    void push(int x) {
        this->q.push(x);
    }
    
    int pop() {
        queue<int> q2;

        while(q.size() > 1){
            int top = q.front();
            this->q.pop();
            q2.push(top);
        }

        int res = q.front(); 
        q.pop();

        while (q2.size() > 0){
            q.push(q2.front());
            q2.pop();
        }
        return res;
    }
    
    int top() {
        queue<int> q2;

        while(q.size() > 1){
            int top = q.front();
            this->q.pop();
            q2.push(top);
        }

        int res = q.front(); 
        q2.push(res); 
        q.pop();

        while (q2.size() > 0){
            q.push(q2.front());
            q2.pop();
        }
        return res;
    }
    
    bool empty() {
        return this->q.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */
