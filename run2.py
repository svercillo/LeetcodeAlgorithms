
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
def applyCoupon(cart:list, couponarr:list):
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

    # greedy
    def createoverride(mapping, coupon):
        override = {}

        largestdisc = 0
        appliedcat = None
        largestdiscamount = 0
        for ccat in coupon["categories"]:
            if ccat in mapping:
                num = mapping[ccat]["num"]
                amount = mapping[ccat]["amount"]
                if coupon["minimum_num_items_required"] <= num and coupon["minimum_amount_required"] <= amount:             
                    dis = amount - applydiscount(coupon, amount)

                    if dis > largestdisc:
                        largestdisc = dis
                        largestdiscamount = amount
                        appliedcat = ccat

        if ccat is not None: 
            override[appliedcat] = largestdiscamount - largestdisc

        return override
    
    def invalidcouponcollectioncheck(couponarr):
        seen = set()
        for e in couponarr: 
            categories = e["categories"]
            for cat  in categories:
                if cat in seen:
                    raise  Exception("invalid coupon colletion")
                seen.add(cat)

    def createalloverrides(mapping, couponarr):
        totaloverride = {}
        overarr = []
        for coup in couponarr:
            overrde = createoverride(mapping, coup)
            totaloverride |= overrde
            overarr.append(overrde)
            
        return totaloverride
        

        
    mapping = createmapping(cart)
    couponarr = [defaultcoupon(e) for e in couponarr]
    invalidcouponcollectioncheck(couponarr)
    override = createalloverrides(mapping, couponarr)
    print(override)


    total = 0
    for cat in mapping:
        if cat in override:
            total += override[cat] 
        else:
            total += mapping[cat]["amount"]

    
    def minCost(i, applyCategoriesLeft):
        if i >= len(couponarr):
            return 0
        
        coupon = couponarr[i]        

        res = 0
        # if take coupon 
        res1 = minCost(i+ 1, applyCategoriesLeft) 
        disc_dollars, cat = discount(coupon)

        catdiff = applyCategoriesLeft.copy()
        catdiff.pop(cat)
        res2 = minCost(i+ 1, catdiff) - disc_dollars

        return min(res1, res2)


    return total


        

    


        



res = applyCoupon(
[ {'price': 2.00, 'category': 'fruit'},
  {'price': 20.00, 'category': 'toy'},
  {'price': 5.00, 'category': 'clothing'},
  {'price': 8.00, 'category': 'fruit'}
],

[  { 'categories': ['clothing', 'toy'],
    'percent_discount': None,
    'amount_discount': 6,
    'minimum_num_items_required': None,
    'minimum_amount_required': None
  },
  { 'categories': ['toy'],
    'percent_discount': 15,
    'amount_discount': None,
    'minimum_num_items_required': 2,
    'minimum_amount_required': 10.00
   }
]
)

print(res)