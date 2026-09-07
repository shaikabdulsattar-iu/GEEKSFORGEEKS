class Solution:

  def isPerfect(self, n: int) -> bool:
    if n <= 1:
      return False

    total = 1  # 1 is always a proper divisor
    i = 2
    while i * i <= n:
      if n % i == 0:
        total += i
        if i * i != n:  # Add paired factor if not a perfect square
          total += n // i
      i += 1

    return total == n