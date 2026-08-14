class Solution:
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        x , y = a , b
        while y:
            x , y = y, x % y
        gcd = x
        lcm_val = (a*b)//gcd
        return [lcm_val,gcd]
        
                      