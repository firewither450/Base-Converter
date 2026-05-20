from math import floor, log

class Num:
  def __init__(self, x, base = 10):
    self.num = str(x)
    if base == 0:
      self._base = 71859
    else:
      self._base = base if 2 <= base <= 71859 else 10

  def __get_chars(self, base):
    chars = ["0","1","2","3","4","5","6","7","8","9",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    count = 0
    while len(chars) < base:
      char = chr(count)
      if char.isprintable() and char not in chars:
        chars.append(char)
      count +=1
    return chars

  def __baseify(self, n, base = 10):
    if 0 <= int(base) <= 71859:
      base = base if 0 < base else 71859
      chars = self.__get_chars(base) 
      table = []
      x = int(n)
      exp = floor(log(x,base))
      for i in range(exp+1):
        table.append(floor(x/(base**exp)))
        x = x - base**exp * (floor(x/(base**exp)))
        exp -= 1
      final = ""
      for i in table:
        final = final + str(chars[i])
      return final
    else:
      raise ValueError("Not enough characters, max = 71859")

  def __unbaseify(self, num, base = 10):
    if base <= 71859:
      chars = self.__get_chars(base) 
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

  def base(self, to = 10):
    fro = self._base
    return self.__baseify(self.__unbaseify(str(self.num), fro), to)

  def __str__(self):
    return self.num
    
  def __int__(self):
    return int(self.__unbaseify(str(self.num), self._base)) 

  def denary(self):
    return self.__unbaseify(str(self.num), self._base)
  
  def hex(self):
    return self.__baseify(self.__unbaseify(str(self.num), self._base), 16)
  
  def binary(self):
    return self.__baseify(self.__unbaseify(str(self.num), self._base), 2)
  
  def get_base(self):
    return self._base
  

number = Num("1A", 18)
print(number.base(2))
print(int(number))
print(number.get_base())
