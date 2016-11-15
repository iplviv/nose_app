import unittest
import myunit.app

class MyUnitTest(unittest.TestCase):

  def testInit(self):
    app = myunit.app.App(300)
    self.assertEquals(app.var, 302)

  def testGetVar(self):
    app = myunit.app.App(400)
    self.assertEquals(app.get_var(), 402)

if __name__ == '__main__':
    unittest.main()

