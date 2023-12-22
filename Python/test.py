class Solution:
    def buyChoco(self, prices, money) -> int:
        listo = []
        for price in prices:
            if not listo[0] or price <= listo[0]:
                listo[0] = price
            elif not listo[1] or price <= listo[1]:
                listo[1] = price
        print(listo[0],listo[1])
        if listo[0] + listo[1] <= money:
            return money - (listo[0] + listo [1])
        else:
            return money

test1 = Solution()
print(test1.buyChoco([3,2,3],3))