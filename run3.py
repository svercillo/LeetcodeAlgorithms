
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

from typing import Dict, List, Tuple

# create_routing_number_mapping combines a map from routing number to bank name with a list of relationships between
# bank names and bank IDs to create a single map with routing numbers as keys and a list of related bank IDs as values.
def create_routing_number_mapping(rn_to_name: Dict[str, str], name_to_bank_id: List[Tuple[str, int]]) -> Dict[str, List[int]]:
    def convertmap(name_to_bank_id): 
        mapping = {}
        for entry in name_to_bank_id:
            name, bank_id  = entry

            if name not in mapping:
                mapping[name] = []
            
            mapping[name].append(bank_id)
        return mapping 
    
    res = {}
    name_to_bank_id = convertmap(name_to_bank_id)
    
    print(name_to_bank_id)

    for rn in rn_to_name: 
        name = rn_to_name[rn]

        ids = [] 
        if name in name_to_bank_id:
            name_to_bank_id[name]
            
            # revisit 
            ids += name_to_bank_id[name]
            
        res[rn] = ids 
    
    return res


res = create_routing_number_mapping(
# routing number to bank nam 
{
    "123": "Wells Fargo",
    "456": "Chase",
    "789": "Capital One",
    "555": "First State Bank",
},
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