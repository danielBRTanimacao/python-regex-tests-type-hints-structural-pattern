import unittest
from testes_tdd.src.baconwitheggs import bacon_with_eggs

class TestBaconWithEggs(unittest.TestCase):
    def test_bacon_with_eggs_need_to_raise_assertion_if_is_not_int(self):
        with self.assertRaises(AssertionError):
            bacon_with_eggs('')

    def test_bacon_with_eggs_need_to_return_bacon_with_eggs_if_enter_is_multiple_3_and_5(self):
        enters = (15, 30, 45, 60)
        exit_values = 'Bacon with eggs'

        for enter in enters:
            with self.subTest(enter=enter, exit_values=exit_values):
                self.assertEqual(
                    bacon_with_eggs(enter), 
                    exit_values, 
                    msg=f'"{enter}" não retornou "{exit_values}"'
                )

    def test_bacon_with_eggs_need_to_return_starve_if_enter_is_not_multiple_3_and_5(self):
        enters = (1, 2, 4, 7, 8)
        exit_values = 'Starve'

        for enter in enters:
            with self.subTest(enter=enter, exit_values=exit_values):
                self.assertEqual(
                    bacon_with_eggs(enter), 
                    exit_values, 
                    msg=f'"{enter}" não retornou "{exit_values}"'
                )

    def test_bacon_with_eggs_need_to_return_bacon_if_enter_is_multiple_3(self):
        enters = (3, 6, 9, 12)
        exit_values = 'Bacon'

        for enter in enters:
            with self.subTest(enter=enter, exit_values=exit_values):
                self.assertEqual(
                    bacon_with_eggs(enter), 
                    exit_values, 
                    msg=f'"{enter}" não retornou "{exit_values}"'
                )

    def test_bacon_with_eggs_need_to_return_eggs_if_enter_is_multiple_5(self):
        enters = (5, 10, 20, 25)
        exit_values = 'Eggs'

        for enter in enters:
            with self.subTest(enter=enter, exit_values=exit_values):
                self.assertEqual(
                    bacon_with_eggs(enter), 
                    exit_values, 
                    msg=f'"{enter}" não retornou "{exit_values}"'
                )


if __name__ == '__main__':
    unittest.main(verbosity=2)