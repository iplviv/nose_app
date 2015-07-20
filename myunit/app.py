import time

class App(object):

  def __init__(self, var):
    self.var = var

  def get_var(self):
    print "Sleeping 120 seconds..."
    time.sleep(120)
    return self.var
