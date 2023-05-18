class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.cust_num = 0

        self.price_map = {}
        for i in range(len(products)):
            self.price_map[products[i]] = prices[i]
    
        self.discount = discount

    def getBill(self, product: List[int], amounts: List[int]) -> float:
        
        bill_tot = 0
        for i, pid in enumerate(product):
            price = self.price_map[pid] * amounts[i]
            bill_tot += price
        
        if self.cust_num == self.n -1:
            bill_tot = bill_tot * ((100 - self.discount)/ 100)

        self.cust_num += 1 
        self.cust_num %= self.n

        return bill_tot
