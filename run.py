import math
import heapq
from pprint import pprint
from functools import cache

class Trie: 
    class Node:
        def __init__(self, char, eow=False):
            self.char = char
            self.nxt = {}

        def __repr__(self): 
            return f"{self.char}->"

        def __str__(self):
            return self.__repr__()

    def __init__(self, words):
        self.head = self.Node("_")
        for word in words:
            self.add_word(word)

    def add_word(self, word):
        node = self.head
        for c in word:
            if c not in node.nxt:
                node.nxt[c] = self.Node(c)
            node = node.nxt[c]



class Solution:
    def minimumCost(self, source: str, target: str, original, changed, cost) -> int:
        # dijsktra's with backtracking
        self.source = source
        self.target = target
        self.original = original
        self.changed = changed
        self.node_to_id = {node: i for i, node in enumerate(original + changed)}

        self.counter = len(self.node_to_id)
        # self.id_to_node = {i: node for i, node in enumerate(original + changed)}
        self.cost_map = self.calc_cost_map(cost)
        self.node_names = set(original + changed)
        self.trie = Trie(original)

        pprint(self.cost_map)

        res = self.min_cost_from_index(0) 
        return res if res != math.inf else -1

    # def calc_path_code(self, path):
    #     cost = 0
    #     last_node = None
    #     for node in path:
    #         if last_node is not None:
    #             cost += self.cost_map[last_node][node]
    #         last_node = node
    #     print(f"Path {path} cost is {cost}")
        
    
    def calc_cost_map(self, cost):
        cost_map = {}
        for i in range(len(self.original)):
            original_ind = self.node_to_id[self.original[i]]
            changed_ind = self.node_to_id[self.changed[i]]

            if original_ind not in cost_map:
                cost_map[original_ind] = {}
            
            if changed_ind not in cost_map[original_ind]:
                cost_map[original_ind][changed_ind] = cost[i]
            else: 
                cost_map[original_ind][changed_ind] = min(
                    cost[i],
                    cost_map[original_ind][changed_ind]
                )

        return cost_map


    @cache
    def min_cost_from_index(self, index):
        if index == len(self.source):
            return 0

        c = self.source[index]
        min_cost = math.inf

        # edge case where no jump is necessary
        if c == self.target[index]:
            min_cost = min(
                min_cost,
                self.min_cost_from_index(index+1) + 0
            )

        jump_str = c
        j = index + 1

        if jump_str in self.cost_map:

            if self.target[index:index+1] not in self.node_to_id:
                self.node_to_id[self.target[index:index+1]] = self.counter
                self.counter += 1

            if jump_str not in self.node_to_id:
                self.node_to_id[jump_str] = self.counter
                self.counter += 1
            
            cost_to_jump = self.get_min_cost_of_drop(self.node_to_id[jump_str], self.node_to_id[self.target[index:index+1]])
            min_cost = min(min_cost, self.min_cost_from_index(index+ 1) + cost_to_jump)
        

        if c in self.trie.head.nxt:
            node = self.trie.head.nxt[c]
            while j < len(self.source) and self.source[j] in node.nxt:
                node = node.nxt[self.source[j]]
                jump_str += self.source[j]

                if self.target[index:index+1] not in self.node_to_id:
                    self.node_to_id[self.target[index:index+1]] = self.counter
                    self.counter += 1

                if jump_str not in self.node_to_id:
                    self.node_to_id[jump_str] = self.counter
                    self.counter += 1

                print(jump_str)
                if self.node_to_id[jump_str] in self.cost_map:
                    cost_to_jump = self.get_min_cost_of_drop(self.node_to_id[jump_str], self.node_to_id[self.target[index:j+1]])
                    min_cost = min(min_cost, self.min_cost_from_index(j+ 1) + cost_to_jump)
                j += 1


        # if min_cost == math.inf:
        #     return -math.inf
            # raise Exception(f"failed to get min cost for index {index}", selfsource[index]) 

        return min_cost
    
    def print_path(self, node):
        res = ""
        while node:
            res += str(node.name) + "<-"
            node = node.last
        print(res)
        

    def get_min_cost_of_drop(self, starting, ending):
        class Node:
            def __init__(self, name, dist):
                self.name = name
                self.dist = dist
                self.last = None
                self.invalid = False


            def __repr__(self):
                return f"Node<{self.name}, min_dist={self.dist}>"

            def __lt__(self, other):
                return self.dist < other.dist
            
        # print("\n\nGetting min of drop", starting, "  ", ending)
        node_map = {index : Node(index, math.inf) for index in range(self.counter + 1)}
        q = [node_map[index] for index in range(self.counter + 1)]
        
        node_map[starting].dist = 0
        heapq.heapify(q)

        while len(q):
            while len(q) and q[0].invalid:
                heapq.heappop(q)

            if not len(q):
                break

            top = heapq.heappop(q)

            if top.name == ending:
                # print("Getting min of drop", starting, "  ", ending, ": ", top.dist)
                # self.print_path(top)
                return top.dist

            if top.name not in self.cost_map:
                continue
                # return math.inf


            print(top.name, self.cost_map[top.name])
            for neigh_name in self.cost_map[top.name]:
                neigh = node_map[neigh_name]
                if top.dist + self.cost_map[top.name][neigh_name] < neigh.dist:
                    neigh.invalid = True
                    new_neigh = Node(neigh_name, top.dist + self.cost_map[top.name][neigh_name])
                    new_neigh.last = top
                    node_map[neigh_name] = new_neigh
                    heapq.heappush(q, new_neigh) # push copy of node with updated cost

        return math.inf

res = Solution().minimumCost(source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20])
# res = Solution().minimumCost(source = "abcdefgh", target = "acdeeghh", original = ["bcd","fgh","thh"], changed = ["cde","thh","ghh"], cost = [1,3,5])
# res = Solution().minimumCost(source = "abcdefgh", target = "addddddd", original = ["bcd","defgh"], changed = ["ddd","ddddd"], cost = [100,1578])
# res = Solution().minimumCost(source ="a", target="d", original=["a"], changed=["b"], cost=[1])
# solution = Solution()
# res = solution.minimumCost(
#     source ="aaaddcaaccbabaaccbabbaadcccadbaacbddbaccabddbdbaaddbbacbddddbbdbccaadcaccacdbcbddbacabadaaccbadbbdbc",
#     target ="abaddcabcdbabcbadcaccaadabbadddbcacaaabdabbdcbbdbcbaaabbbcddcbddcbccadacddcbdcbacadbbadbdabcbadbbdac",
#     original =["ddddb","dccbb","dadac","dbdbb","ddbacabadaac","bcbccdcadabd","dacabcdaacca","dcdadacacbbd","dcccadbaacbddbacc","dcdcbccdccdbaaaac","bbbcccdbcdcadaabc","bccaadcaccacdb","bbcabcbcbaddbd","dbadadaddcddad","badaddbcddacca","bc","da","cb","ddbdbaaddbbac","dbcadcdbabddd","abdadacbbbcca","adaaabcabdbcc","caaccbabaaccbabba","abaadddbaaccbbacc","bbddaaadcbccccbac","cdbdbddaadbbbdbdd","bcbdaabaddbdcdcaa","aa","cb","dd"],
#     changed =["dccbb","dadac","dbdbb","bcddc","bcbccdcadabd","dacabcdaacca","dcdadacacbbd","acadbbadbdab","dcdcbccdccdbaaaac","bbbcccdbcdcadaabc","dabbadddbcacaaabd","bbcabcbcbaddbd","dbadadaddcddad","badaddbcddacca","dcbccadacddcbd","da","cb","ac","dbcadcdbabddd","abdadacbbbcca","adaaabcabdbcc","bdcbbdbcbaaab","abaadddbaaccbbacc","bbddaaadcbccccbac","cdbdbddaadbbbdbdd","bcbdaabaddbdcdcaa","cabcdbabcbadcacca","cb","dd","ba"],
#     cost =[67,56,64,83,100,73,95,97,100,98,20,92,58,70,95,77,95,93,69,92,77,53,96,68,83,96,93,64,81,100]
# )

# res = Solution().minimumCost(source = "eebhehaabeaaaaheheha", target = "abbbaeaebbhabehbabbb", original = ["e","h","e","h","a","a","a","h"],  changed = ["b","b","a","e","h","b","e","a"], cost = [10,10,10,8,9,6,10,10])


# 291455
# solution.calc_path_code(['f', 's', 'r', 'p', 'a'])
# solution.calc_path_code(['f', 'w', 'i', 'u', 'g', 'a'])
# solution.calc_path_code(['f', 'w', 'i', 'u', 'p', 'a'])

print(f"\n\nRESULT: {res}")






