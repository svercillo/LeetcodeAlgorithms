class Trie{
    public:
        class Node{
            public:
            char value;
            int count = 0;
            unordered_map<char, Node*> children;
            Node(char value){
                this->value = value;
                this->count = 0;
            }
            Node(char value, int count){
                this->value = value;
                this->count = count;
            }

            ~Node(){
                for (const auto& [letter, child_node] : this->children){
                    delete child_node; // delete all children nodes
                }
            }
        };

        Node* root;
        Trie(){
            this->root = new Node('$');

        }
        
        ~Trie(){
            delete this->root;
        }

        void add_word(string word, int count){
            Node * node = this->root;
            for (auto c : word){
                Node * child_node;
                if (node->children.find(c) == node->children.end()){
                    child_node = new Node(c);
                    node->children[c] = child_node;
                } else { 
                    child_node = node->children[c];
                }
                node = child_node;
            }
            node->children['$'] = new Node('$', count);
        }

        int find_prefix_sum(string prefix){
            Node * node = this->root;
            for (auto c : prefix){
                Node * child_node;
                if (node->children.find(c) == node->children.end()){
                    return 0;
                } else { 
                    child_node = node->children[c];
                }
                node = child_node;
            }
            
            vector<Node*> queue;

            for (const auto&[letter, child_node] : node->children){
                queue.push_back(child_node);
            }


            int total_count = 0;
            while (queue.size()){
                vector<Node*> newq;
                for (auto node : queue){
                    if (node->value == '$'){
                        total_count += node->count;
                    } else {
                        for (const auto&[letter, child_node] : node->children){
                            newq.push_back(child_node);
                        }
                    }
                }
                queue = newq;
            }
            return total_count;
        }
};

class MapSum {
public:
    Trie * trie;
    MapSum() {
        trie = new Trie();
    }

    ~MapSum(){
        delete trie;
    }
    
    void insert(string key, int val) {
        trie->add_word(key, val);   
    }
    
    int sum(string prefix) {
        return trie->find_prefix_sum(prefix);
    }
};

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum* obj = new MapSum();
 * obj->insert(key,val);
 * int param_2 = obj->sum(prefix);
 */
