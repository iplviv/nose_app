import unittest2 as unittest
import myunit.app

class MyUnitTest(unittest.TestCase):

  def testInit(self):
    app = myunit.app.App(100)
    self.assertEquals(app.var, 102)

  def testGetVar(self):
    app = myunit.app.App(200)
    self.assertEquals(app.get_var(), 202)

  def one_test():
    assert 1

  def two_test():
    assert 2

  def three_test():
    assert 1+2

  def one_test():
    assert 1

  def two_test():
    assert 2

  def three_test():
    assert 1+2

suite = unittest.TestLoader().loadTestsFromTestCase(MyUnitTest)
unittest.TextTestRunner(verbosity=2).run(suite)
