
# 
'''




Price is a list of items: 
coupon has a usage description: 
    1. min number of items 
    2. all min are optional
    3. always need have either percent or amount
'''
'''
single coupon and a list of items
# Example Cart
[ {'price': 2.00, 'category': 'fruit'},
  {'price': 20.00, 'category': 'toy'},
  {'price': 5.00, 'category': 'clothing'},
  {'price': 8.00, 'category': 'fruit'}
]

{ 'category': 'fruit',
  'percent_discount': 15,
  'amount_discount': None,
  'minimum_num_items_required': 2,
  'minimum_amount_required': 10.00
}

you can apply all coupons, only one per category 
if multiple coupons applicable 
changes to coupon: 
[
  { 'categories': ['clothing', 'toy'],
    'percent_discount': None,
    'amount_discount': 6,
    'minimum_num_items_required': None,
    'minimum_amount_required': None
  },
  { 'categories': ['fruit'],
    'percent_discount': 15,
    'amount_discount': None,
    'minimum_num_items_required': 2,
    'minimum_amount_required': 10.00
   }
]

'''
def applyCoupon(cart:list, coupon:dict):
    # group by category
    def defaultcoupon(coupon):
        if (
            coupon["percent_discount"] is None and coupon["amount_discount"] is None
            or coupon["percent_discount"] is not None and coupon["amount_discount"] is not None
        ) :
            raise Exception("invalid coupon")
        if coupon["minimum_num_items_required"] is None:
            coupon["minimum_num_items_required"] = 0
        if coupon["minimum_amount_required"] is None:
            coupon["minimum_amount_required"] = 0
        return coupon

    def createmapping(cart ):
        mapping = {}
        for item in cart:
            cat = item["category"]
            if cat not in mapping: 
                mapping[cat] = {"num" : 0, "amount": 0 }

            mapping[cat]["num"] += 1
            mapping[cat]["amount"] += item["price"]

        return mapping
    
    def applydiscount(coupon, totalamount):
        if coupon["percent_discount"]:
            return (100 - coupon["percent_discount"] )/ 100 * totalamount
        if coupon["amount_discount"]:
            return max(totalamount - coupon["amount_discount"], 0)

    def createoverride(mapping, coupon):
        override = {} 
        ccat = coupon["category"]
        if ccat in mapping: 
            num = mapping[ccat]["num"]
            amount = mapping[ccat]["amount"]
            if coupon["minimum_num_items_required"] <= num and coupon["minimum_amount_required"] <= amount:             
                override[ccat] = applydiscount(coupon, amount)
        return override
        
    mapping = createmapping(cart)
    coupon = defaultcoupon(coupon)
    override = createoverride(mapping, coupon)

    print(mapping)
    print(coupon)
    print(override)


    total = 0
    for cat in mapping:
        if cat in override:
            total += override[cat] 
        else:
            total += mapping[cat]["amount"]

    return total



res = applyCoupon(
[ {'price': 2.00, 'category': 'fruit'},
  {'price': 20.00, 'category': 'toy'},
  {'price': 5.00, 'category': 'clothing'},
  {'price': 8.00, 'category': 'fruit'}
],

{ 'category': 'fruit',
  'percent_discount': None,
  'amount_discount': 1000,
  'minimum_num_items_required': None,
  'minimum_amount_required': 2
}
)

print(res)
