class Solution:
    def maxTastiness(self, price: List[int], tastiness: List[int], maxAmount: int, maxCoupons: int) -> int:

        zipped = zip(price, tastiness)
        fruits = sorted(zipped, key =lambda k : k[0])

        @cache
        def max_tastiness(ind, money, coupons):
            n = len(fruits)

            if ind == n:
                return 0
            price, tastiness = fruits[ind]

            m_tastiness = 0
            # take without coupon
            if money >= price:
                m_tastiness = max_tastiness(ind+1, money - price, coupons) + tastiness
            
            # take with coupon
            if money >= price // 2 and coupons > 0: 
                m_tastiness = max(
                    m_tastiness,
                    max_tastiness(ind +1, money - price //2, coupons -1) + tastiness
                )
            
            # do not take
            m_tastiness = max(
                m_tastiness,
                max_tastiness(ind +1, money, coupons)
            )

            return m_tastiness


        return max_tastiness(0, maxAmount, maxCoupons)