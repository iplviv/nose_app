import time

class App(object):

  def __init__(self, var):
    self.var = var + 2

  def get_var(self):
    print "Sleeping 10 seconds..."
    time.sleep(10)
    return self.var
