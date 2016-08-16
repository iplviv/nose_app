import time

def one_test():
  assert 1

def two_test():
  if time.time() / 60 % 2 < 0.7:
    time.sleep(30)
  assert 2

def three_test():
  assert 1 + 2

def four_test():
  if time.time() / 60 % 2 > 1.5:
    result = 15
  else:
    result = 16
  
  assert result == 4 * 4
