import time

class App(object):

  def __init__(self, var):
    self.var = var + 2

  def get_var(self):
    print "Sleeping 60 seconds..."
    time.sleep(60)
    return self.var
