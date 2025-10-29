class Solution {
public:
    int reverse(int x) {
        if (x == 0){
            return 0;
        }
        if (x < 0){ 
            int ndm = floor(log10(-(INT_MIN + 1))) +1;
            int ndx = to_string(x).size() -1;
            int max = INT_MIN;
            cout << INT_MIN << endl;

            cout << ndm << " " << ndx << endl;


            if (ndx > ndm){
                return 0;
            }

            int res = 0;
            bool invalid = false; 
            for (int i =0; i< ndx; i ++){
                int d = x % 10;
                x /= 10;

                
                int rem = max / pow(10, ndx -1 - i);
                int remm = rem % 10;

                cout << d << " max " << remm << endl;

                if (ndm == ndx){
                    
                    if (d < remm && !invalid){
                        return 0;
                    } else if(d > remm) {
                        invalid = true;
                    }
                }

                res += d * pow(10, ndx - 1- i);
            }


            return res;


        } else {
            int ndm = floor(log10(INT_MAX)) +1;
            int ndx = floor(log10(x)) + 1;
            int max = INT_MAX;


            cout << ndm << " " << ndx << endl;


            if (ndx > ndm){
                return 0;
            }

            int res = 0;
            bool invalid = false;
            for (int i =0; i< ndx; i ++){
                int d = x % 10;
                x /= 10;

                
                int rem = max / pow(10, ndx -1 - i);
                int remm = rem % 10;

                cout << d << " max " << remm << endl;

                if (ndm == ndx){
                    if (d > remm && !invalid){
                        return 0;
                    } else if (d < remm){
                        invalid = true;
                    }
                }

                res += d * pow(10, ndx - 1- i);

            }


            return res;



        }    
    }
};  
