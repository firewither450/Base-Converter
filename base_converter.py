import unicodedata
import math

class Num:
  def __init__(self, x, base = 10):
    self.num = str(x)
    if base == 0:
      self._base = 71859
    else:
      self._base = base if 2 <= base <= 71859 else 10

  def base(self, to = 10):
    fro = self._base
    def _get_chars(base):
      chars = ["0","1","2","3","4","5","6","7","8","9",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
      count = 0
      while len(chars) < base:
        char = chr(count)
        if char.isprintable() and char not in chars:
          chars.append(char)
        count +=1
      return chars

    def _baseify(n, base = 10):
      if 0 <= int(base) <= 71859:
        base = base if 0 < base else 71859
        chars = _get_chars(base)
        table = []
        x = int(n)
        exp = math.floor(math.log(x,base))
        for i in range(exp+1):
          table.append(math.floor(x/(base**exp)))
          x = x - base**exp * (math.floor(x/(base**exp)))
          exp -= 1
        final = ""
        for i in table:
          final = final + str(chars[i])
        return final
      else:
        raise ValueError("Not enough characters, max = 71859")
    def _unbaseify(num, base = 10):
      if base <= 71859:
        chars = _get_chars(base)
        x = 0
        exp = len(num)-1
        for i in num:
          if i in chars:
            x += chars.index(i) * base** exp
            exp -=1
          else:
            raise SyntaxError("ERROR! Digit not recognised")
        return x
      else:
        raise ValueError("Not enough characters, max = 71859")

    return _baseify(_unbaseify(str(self.num),fro),to)

  def __str__(self):
    return self.num
  def __int__(self):
    return self.num


number = Num("A4", 16)
print(number.base(16**2))
