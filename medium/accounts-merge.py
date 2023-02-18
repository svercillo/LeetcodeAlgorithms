from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        ind = 0
        email_to_ind = {}

        names_to_graph = defaultdict(lambda: {})
        names_to_sizes = defaultdict(lambda: {})


        
        def find(_id, name):
            graph = names_to_graph[name]
            while graph[_id] != _id:
                _id = graph[_id]
            return _id

        def union(group_ids, name):

            print(name, group_ids)
            sizes = names_to_sizes[name]
            graph = names_to_graph[name]

            largest_id = group_ids[0]
            largest_size = sizes[largest_id]
            for base_id in group_ids:
                if sizes[base_id] > largest_size:
                    largest_size  = sizes[base_id]
                    largest_id = base_id


            for _id in group_ids:
                if _id == largest_id:
                    continue
                graph[_id] = largest_id
                sizes[largest_id] += sizes[_id]
            
            for _id in group_ids:
                if _id != largest_id:
                    sizes.pop(_id, None)

            # print(graph)

    
        for account in accounts:
            name = account[0]
            graph = names_to_graph[name]
            sizes = names_to_sizes[name]

            group_ids = []
            for email in account[1:]:
                if email in email_to_ind:
                    email_ind = email_to_ind[email]
                else:
                    ind += 1
                    email_ind = ind
                    email_to_ind[email] = email_ind
            
                if email_ind not in graph:
                    base_id = email_ind
                    graph[base_id] = base_id
                    sizes[base_id] = 1
                else:
                    base_id = find(email_ind, name)
                    sizes[base_id] += 1

                group_ids.append(base_id)

            union(group_ids, name)
        
        ind_to_email = {}
        for email in email_to_ind:
            ind = email_to_ind[email]
            ind_to_email[ind] = email


        # print(names_to_graph)

        res = []

        for name in names_to_graph:
            graph = names_to_graph[name]
            sizes = names_to_sizes[name]

            acnts = defaultdict(lambda : [])
            for _id in graph:
                base_id = find(_id, name)
                acnts[base_id].append(ind_to_email[_id])

            for base_id in acnts:
                acnts[base_id].sort()
                res.append([name] + acnts[base_id])
                

            
        return res


                
            
