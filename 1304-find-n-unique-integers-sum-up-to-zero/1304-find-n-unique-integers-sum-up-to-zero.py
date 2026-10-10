class Solution:
    def sumZero(self, n: int) -> list[int]:
        ll = []
        if n == 1:
            ll.append(0)
            return ll
        elif n%2 == 0:
            for i in range(1,n):
                ll.append(i)
                ll.append(i * (-1))
                if len(ll) == n:
                    return ll
        else:
            ll.append(0)
            for i in range(1,n):
                ll.append(i)
                ll.append(i * (-1))
                if len(ll) == n:
                    return ll        