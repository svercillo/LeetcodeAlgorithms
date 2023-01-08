from pprint import pprint 
class Solution:
    def maxProfit(self, prices) -> int:
        lst = []
        for i in range(0, len(prices)):
            lst.append({})

        if len(prices) < 2:
            return 0
        lst[0]['min'] = prices[0]
        lst[0]['max'] = -1

        last_cpy = None

        for i in range(1, len(prices)):
            
            if prices[i] == prices[i-1]:

                lst[i]['max'] = lst[i-1]['max']
                lst[i]['min'] = lst[i-1]['min']

                lst[i]['cpy'] = True
                last_cpy = lst[i] 

                # print(prices[i])
                # pprint(lst)
                continue


            if (prices[i] > lst[i-1]['max'] and lst[i-1]['max'] != -1):
                lst[i]['min'] = lst[i-1]['min']
                lst[i]['max'] = prices[i]
                lst[i-1]['max'] = -1

            elif lst[i-1]['max'] == -1 and prices[i] > lst[i-1]['min']: 
                # print(prices[i])
                # print(prices[i])
                # print(prices[i])
                # print(prices[i])
                # print(prices[i])
                last_cpy = None
                y = i-1
                while y >0:
                    if 'cpy' in lst[y]:
                        last_cpy = lst[y]
                        break
                    elif lst[y]['max'] != -1:
                        break

                    y-=1
                if 'cpy' not in lst[i-1] and last_cpy is not None and last_cpy['min'] == lst[i-1]['min']:
                    lst[i]['min'] = prices[i]
                    lst[i]['max'] = -1
                    if lst[i]['min'] > lst[i-1]['min']:
                        lst[i]['max'] = lst[i]['min']
                        lst[i]['min'] = lst[i-1]['min']
                    
                else:

                    # if last_cpy and last_cpy['max'] > prices[i]:

                        
                        # lst[i]['min'] = prices[i]
                        # lst[i]['max'] = -1
                       
                    # else:
                    lst[i]['min'] = lst[i-1]['min']
                    lst[i]['max'] = prices[i]
                    
            elif prices[i] < lst[i-1]['max'] and prices[i] >  lst[i-1]['min'] :
                # print(prices[i], "SDFSDf")
                # print(lst[i-1])
                if 'cpy' in lst[i-1]:
                    if prices[i] > lst[i-1]['max']:
                        lst[i]['min']  = lst[i-1]['min']
                        lst[i]['max'] = prices[i]
                    else:
                        # print("WWWWWW")
                        lst[i]['min']  = prices[i]
                        lst[i]['max'] = -1
                        # lst[i]['min']  = lst[i-1]['min']
                        # lst[i]['max'] = -1
                else: 
                    
                    lst[i]['min']  = prices[i]
                    lst[i]['max'] = -1
            elif prices[i] < lst[i-1]['min']:

                lst[i]['min']  = prices[i]
                lst[i]['max'] = -1
            else:
                
                lst[i]['max'] = -1
                lst[i]['min'] = lst[i-1]['min']
                
            # print(prices[i])
            # pprint(lst)

        for i in range(len(lst)-1, -1, -1 ):
            if lst[i]['min'] != -1 and lst[i]['max'] != -1:
                # print(lst[i]['max'], lst[i]['min'], "+++++++++++++++++")
                j = i
                begin = True 
                while j >= 0:

                    # print(lst[j]['max'], lst[j]['min'])
                    if lst[j]['max'] == -1 and 'cpy' not in lst[j]:
                        break    
                    elif 'cpy' not in lst[j] and lst[j]['max'] != -1:
                        if  not begin:
                            lst[j ]['max'] = -1
                            to_delete = j 
                        else :
                            begin = False
                    j -=1 

        profit =0
        last = None
        _min = lst[0]['min']
        for d in lst: 
            if d['max']  > -1  and d['min']  > -1 and "cpy" not in d:
                # print("min", "max", d['min'], d['max'] )
                profit += d['max'] - d['min']
        
            last = d
        # pprint(profit)
        # pprint(lst)
        return profit
            
  
