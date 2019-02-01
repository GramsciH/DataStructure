import unittest

import ghclist

class TestGHCList(unittest.TestCase):
    def setUp(self):
        self.ghc_list = ghclist.GHCList()

    def test_empty_true(self):
        self.assertTrue(self.ghc_list.empty())

    def test_empty_false(self):
        self.ghc_list.add(1)
        self.assertFalse(self.ghc_list.empty())

    def test_add(self):
        self.ghc_list.add(2)
        self.assertEqual(self.ghc_list.elem, 2)

    def test_first_elem(self):
        self.ghc_list.add(1)
        self.ghc_list.add(3)
        self.ghc_list.add(4)
        self.assertEqual(self.ghc_list.get_first_elem(), 1)

    def test_length(self):
        self.ghc_list.add(1)
        self.ghc_list.add(3)
        self.ghc_list.add(4)
        self.assertEqual(self.ghc_list.length(), 3)

    def test_get_item_first_elem(self):
        self.ghc_list.add(1)
        self.ghc_list.add(3)
        self.ghc_list.add(4)
        self.assertEqual(self.ghc_list[0], 1)

    def test_get_item_second_elem(self):
        self.ghc_list.add(1)
        self.ghc_list.add(3)
        self.ghc_list.add(4)
        self.assertEqual(self.ghc_list[1], 3)

    def test_get_item_third_elem(self):
        self.ghc_list.add(1)
        self.ghc_list.add(3)
        self.ghc_list.add(4)
        self.ghc_list.add(5)
        self.assertEqual(self.ghc_list[2], 4)

    def test_get_item_last_elem(self):
        self.ghc_list.add(1)
        self.ghc_list.add(3)
        self.ghc_list.add(4)
        self.ghc_list.add(5)
        self.assertEqual(self.ghc_list[3], 5)

    def test_get_item_out_range(self):
        self.ghc_list.add(1)
        self.ghc_list.add(3)

        with self.assertRaises(IndexError):
            self.ghc_list[2]

    def test_get_item_negative_index(self):
        self.ghc_list.add(1)
        self.ghc_list.add(3)

        with self.assertRaises(IndexError):
            self.ghc_list[-2]

    def test_remove_item_second_elem(self):
        self.ghc_list.add(1)
        self.ghc_list.add(3)
        self.ghc_list.add(4)
        self.assertEqual(self.ghc_list.remove(1), 3)

    def test_remove_item_out_range(self):
        self.ghc_list.add(1)
        self.ghc_list.add(3)

        with self.assertRaises(IndexError):
            self.ghc_list.remove(2)

    def test_remove_item_review_length(self):
        self.ghc_list.add(1)
        self.ghc_list.add(3)
        self.ghc_list.add(4)
        self.ghc_list.remove(0)
        self.assertEqual(self.ghc_list.length(), 2)

if __name__ == '__main__':
    unittest.main()
