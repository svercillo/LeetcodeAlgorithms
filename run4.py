
'''
123 -> 1
456 -> 2
789 -> 3
555 -> 5,6
'''
# routing number to bank nam 
{
    "123": "Wells Fargo",
    "456": "Chase",
    "789": "Capital One",
    "555": "First State Bank",
}
# bank id 
[
  # There are multiple common ways to write the name of this bank
  ("Wells Fargo", 1),
  ("Wells", 1),

  ("Chase", 2),
  ("Capital One", 3),
  ("Bank of America", 4),

  # These are two different banks with the same name
  ("First State Bank", 5),
  ("First State Bank", 6),
]



'''
per_routing_number_distributions: {
    "123": {
        1: .8,
        2: .1,
        3: .1,
    },
    "456": {
        1: .10,
        2: .70,
        3: .20,
    },
    ...
}

baseline_distribution: {
    1: .40,
    2: .30,
    3: .20,
    4: .10,
}'''


from typing import Dict, List, Tuple



def create_routing_number_mapping(rn_to_name_arr: List[Dict[str, str]], name_to_bank_id: List[Tuple[str, int]],
                                per_routing_number_distributions, baseline_distribution) -> Dict[str, List[int]]:
    

    def convertmap(name_to_bank_id): 
        mapping = {}
        for entry in name_to_bank_id:
            name, bank_id  = entry

            if name not in mapping:
                mapping[name] = []
            
            mapping[name].append(bank_id)
        return mapping 
    
    
    name_to_bank_id = convertmap(name_to_bank_id)


    res = {} # routing number -> bankid -> freq

    for rn_to_name in rn_to_name_arr:
        for rn in rn_to_name: 
            name = rn_to_name[rn]

            if rn not in res:
                res[rn] = {}


            if name in name_to_bank_id:
                for id in name_to_bank_id[name]:
                    if id not in res[rn]:
                        res[rn][id] = 0
                    multiplier = 1
                    if rn in per_routing_number_distributions:
                        multiplier = per_routing_number_distributions[rn]
                    elif rn in baseline_distribution:
                        multiplier = baseline_distribution[rn]
                    else:
                        multiplier = 0.00000001

                    
                    res[rn][id] += 1 * multiplier

        
    for rn in res:
        mapping = res[rn]
        res[rn] = sorted([id for id in res[rn]], key=lambda id : (mapping[id], baseline_distribution[id]) , reverse=True)
        res[rn] = [k for _, k in res[rn]]
    

    print(res)

    return res


res = create_routing_number_mapping(
# routing number to bank nam 
[
  {
    "123": "Wells Fargo",
    "456": "Chase",
    "789": "Capital One",
    "555": "First State Bank",
  },
{
    "123": "Bank of America",
    "456": "Chase",
    "789": "Capital One",
    "555": "First State Bank",
  },
    {
    "123": "Bank of America",
    "456": "Chase",
    "789": "Capital One",
    "555": "First State Bank",
  },
    {
    "123": "Bank of America",
    "456": "Chase",
    "789": "Capital One",
    "555": "First State Bank",
  },
    {
    "123": "Bank of America",
    "456": "Chase",
    "789": "Capital One",
    "555": "First State Bank",
  },
    {
    "123": "Bank of America",
    "456": "Chase",
    "789": "Capital One",
    "555": "First State Bank",
  },
  {
    "123": "Wells",
    "456": "Chase",
  },
  {
    "789": "Capital One",
    "456": "Bank of America",
  },
  {
    "123": "Bank of America",
    "456": "Chase",
    "555": "Capital One",
  },
],
# bank id 
[
  # There are multiple common ways to write the name of this bank
  ("Wells Fargo", 1),
  ("Wells", 1),

  ("Chase", 2),
  ("Capital One", 3),
  ("Bank of America", 4),

  # These are two different banks with the same name
  ("First State Bank", 5),
  ("First State Bank", 6),
]
)

print(res)