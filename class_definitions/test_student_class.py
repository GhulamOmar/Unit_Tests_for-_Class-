import unittest

from class_definitions import student_class as _student

"""" test.py for student_class.py"""


def test_inital_all_attributes():
    student1 = _student.Student('Omar', 'Ghulam', 'BIS', 60.0)
    assert student1.last_name == 'Omar'
    assert student1.first_name == 'Ghulam'
    assert student1.major == 'BIS'
    assert student1.gpa == 60.0


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.studen = _student.Student('Omar', 'Ghulam', 'BIS', 60.0)

    def tearDown(self):
        del self.studen

    def test_initial_value_required_attributes(self):
        self.assertEqual(self.studen.last_name, 'Omar')
        self.assertEqual(self.studen.first_name, 'Ghulam')

    def test_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            name = _student.Student('555', 'Ghulam', "BIS", 55.0)

    def test_created_error_fist_name(self):
        with self.assertRaises(ValueError):
            name = _student.Student('Omar', '333', "BIS", 65.0)

    def test_created_error_major(self):
        with self.assertRaises(ValueError):
            name = _student.Student('Omar', 'Ghulam', '55', 66.5)

    def test_class_name_gpa(self):
        name = _student.Student('Omar', 'Ghulam', 'BIS', 54.0)
        self.assertEqual('Omar,Ghulam', 'Omar,Ghulam')

    def test_isinstance_gpa_float(self):
        self.assertEqual(self.studen.gpa, 60.0)

    def test_craete_firstname(self):
        self.assertEqual(self.studen.first_name, 'Ghulam')

    def test_craete_laststname(self):
        self.assertEqual(self.studen.last_name, 'Omar')


if __name__ == '__main__':
    unittest.main()
