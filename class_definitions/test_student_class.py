import unittest

from class_definitions import student_class as _student


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.studen = _student.Student('Omar', 'Ghulam','BIS',6.0)

    def tearDown(self):
        del self.studen

    def test_initial_value_required_attributes(self):
        self.assertEqual(self.studen.last_name, 'Omar')
        self.assertEqual(self.studen.first_name, 'Ghulam')

    def test_inital_all_attributes(self):
    #     student1 = _student.Student('Omar', 'Ghulam', 'BIS', 60.0)  # this is not self.person from setUp, but local
    #     assert student1.last_name == 'Omar'  # note no self here on person or assert
    #     assert student1.first_name == 'Ghulam'
    #     assert student1.major == 'BIS'
    #     assert student1.gpa == 60.0
    #
    # def test_object_not_created_error_last_name(self):
    #     with self.assertRaises(ValueError):
    #        name = _student.Student('555', 'Ghulam', "BIS", 55.0)
    #
    # def test_object_not_created_error_fist_name(self):
    #     with self.assertRaises(ValueError):
    #         p = _student.Student('Omar', '333', "BIS", 65.0)
    #
    # def test_object_not_created_error_major(self):
    #         with self.assertRaises(ValueError):
    #             name = _student.Student('Omar', 'Ghulam', '55', 66.5)
    #
    # def test_person_class_display_name_gpa(self):
    #     name = _student.Student('Omar', 'Ghulam', 'BIS',54.0)  # Does not use person from setUp(), has local p
    #     self.assertEqual('Omar,Ghulam', 'Omar,Ghulam')


if __name__ == '__main__':
    unittest.main()
