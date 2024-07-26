import unittest
from unittest.mock import patch
from src.person_class import Person

class TestPerson(unittest.TestCase):
    def setUp(self) -> None:
        self.person_test = Person('Daniel', 'Tenório')
        return super().setUp()

    def test_person_has_attr_name_with_correct_value(self):
        self.assertEqual(self.person_test.name, 'Daniel')

    def test_person_has_attr_name_is_str(self):
        self.assertIsInstance(self.person_test.name, str)
    
    def test_person_has_attr_last_name_with_correct_value(self):
        self.assertEqual(self.person_test.last_name, 'Tenório')

    def test_person_has_attr_last_name_is_str(self):
        self.assertIsInstance(self.person_test.last_name, str)

    def test_person_has_attr_obtive_data_with_init_false(self):
        self.assertFalse(self.person_test.obtive_data)

    def test_get_all_data_its_success_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True
            self.assertEqual(self.person_test.get_data(), 'CONECTED_SUCCESS')
            self.assertTrue(self.person_test.obtive_data)

    def test_get_all_data_its_fail_404(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False
            self.assertEqual(self.person_test.get_data(), 'False 404')
            self.assertFalse(self.person_test.obtive_data)

    def test_get_all_data_its_success_and_fail_sequence(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True
            self.assertEqual(self.person_test.get_data(), 'CONECTED_SUCCESS')
            self.assertTrue(self.person_test.obtive_data)

            fake_request.return_value.ok = False
            self.assertEqual(self.person_test.get_data(), 'False 404')
            self.assertFalse(self.person_test.obtive_data)

if __name__ == '__main__':
    unittest.main(verbosity=2)