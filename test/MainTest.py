__author__ = 'dido-ubuntu'

import unittest

from test.test_booleanqueries import TestBooleanQueries

if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(TestBooleanQueries)
    unittest.TextTestRunner(verbosity=2).run(suite)
    """
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTrie)
    unittest.TextTestRunner(verbosity=2).run(suite)

    suite = unittest.TestLoader().loadTestsFromTestCase(TestPrefixSearch)
    unittest.TextTestRunner(verbosity=2).run(suite)

    suite = unittest.TestLoader().loadTestsFromTestCase(TestRandomSampling)
    unittest.TextTestRunner(verbosity=2).run(suite)

    suite = unittest.TestLoader().loadTestsFromTestCase(TestSortingAtomic)
    unittest.TextTestRunner(verbosity=2).run(suite)
    """