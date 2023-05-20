class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        class Order:
            def __init__(self, amount, price, buy_order:bool):
                self.amount = amount 
                self.price = price
                self.buy_order = buy_order 

            def __lt__(self, other):
                if not self.buy_order:
                    return self.price < other.price
                else:
                    return self.price > other.price

            def __repr__(self):
                return f"Order<{self.amount}, {self.price}>"
        
        sell_backlog = []
        buy_backlog = []

        total_bl = 0

        def process_order(buy_order:bool, amount, price):
            nonlocal total_bl
            def valid_backlog_price(buy_order:bool, price, backlog_price):
                if buy_order:
                    return backlog_price <= price
                else:
                    return backlog_price >= price

            
            backlog = buy_backlog if not buy_order else sell_backlog
            excess_backlog = buy_backlog if buy_order else sell_backlog

            while len(backlog) and amount and valid_backlog_price(buy_order, price, backlog[0].price):
                top = backlog[0]
                if top.amount > amount:
                    top.amount -= amount
                    total_bl -= amount
                    amount = 0
                else:
                    heapq.heappop(backlog)
                    total_bl -= top.amount
                    amount -= top.amount

            if amount > 0:
                new_order = Order(amount, price, buy_order)
                total_bl += amount
                heapq.heappush(excess_backlog, new_order)

            total_bl %= (10 ** 9 + 7) 
    
        for price, amount, sell_order in orders:
            process_order(not sell_order, amount, price)
            # print(buy_backlog)
            # print(sell_backlog)
            # print()

        return total_bl
