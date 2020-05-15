from test import UserLogin
import unittest

class adminTestFunction(unittest.TestCase):

    def setUp(self):
        self.userLogin = UserLogin()
        self.username = self.userLogin.username
        self.password = self.userLogin.password
        self.driver = self.userLogin.driver
        print("000000000")

    def test_adminloginx(self):
        self.userLogin.adminLogin()
        print("111111111111")

    def test_StartMatchx(self):
        self.userLogin.StartMatch()
        print("22222222")

    def test_addQuestions(self):
        self.userLogin.addQuestions()
        print("33333")

    def tearDown(self):
        self.driver.close()
        print("4444444")

def suite_1():
    suite = unittest.TestSuite()
    suite.addTest(adminTestFunction('test_adminloginx'))

if __name__ == '__main__':
    # unittest.main()
    unittest.TextTestRunner().run(suite_1())

