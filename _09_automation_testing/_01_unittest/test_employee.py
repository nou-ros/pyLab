import unittest
from employee import Employee

from unittest.mock import patch

class TestEmployee(unittest.TestCase):

    # second way - instead of using the similar testing method 
    @classmethod
    def setUpClass(cls):
        print('SetUp Class')

    @classmethod
    def tearDownClass(cls):
        print('Tear Down Class')

    def setUp(self):
        print('Set Up')
        self.emp_1 = Employee("Uzumaki", "Naruto", 4000)
        self.emp_2 = Employee("Uchiha", "Sasuke", 2300)

    def tearDown(self):
        print('Tear Down\n')

    # first way
    def test_email(self):
        print('Test Email')
        self.assertEqual(self.emp_1.email, 'Uzumaki.Naruto@email.com')
        self.assertEqual(self.emp_2.email, 'Uchiha.Sasuke@email.com')

        self.emp_1.first = 'Nouros'
        self.emp_2.first = 'Kori'

        self.assertEqual(self.emp_1.email, 'Nouros.Naruto@email.com')
        self.assertEqual(self.emp_2.email, 'Kori.Sasuke@email.com')
    
    def test_fullname(self):
        print('Test Fullname')
        self.assertEqual(self.emp_1.fullname, 'Uzumaki Naruto')
        self.assertEqual(self.emp_2.fullname, 'Uchiha Sasuke')

        self.emp_1.first = 'Nouros'
        self.emp_2.first = 'Kori'

        self.assertEqual(self.emp_1.fullname, 'Nouros Naruto')
        self.assertEqual(self.emp_2.fullname, 'Kori Sasuke')

    def test_apply_raise(self):
        print('Test Apply Raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 4200)
        self.assertEqual(self.emp_2.pay, 2415)

        '''
        Mocking is a process used in unit testing when the unit being tested has external dependencies. The purpose of mocking is to isolate and focus on the code being tested and not on the behavior or state of external dependencies.
        '''

    # test mock 
    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Naruto/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Sasuke/June')
            self.assertEqual(schedule, 'Bad Response!')

if __name__ == '__main__':
    unittest.main()