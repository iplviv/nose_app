import time

class App(object):

  def __init__(self, var):
    self.var = var

  def get_var(self):
    time.sleep(60);
    return self.var
