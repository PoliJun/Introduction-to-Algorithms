# if 100n^2 < 2^n,return n
# else n+=1
def find_n():
  n = 1
  while True:
    if 100 * n ** 2 < 2 ** n:
      return n
    else:
      n += 1

if __name__ == "__main__":
  print(find_n())
