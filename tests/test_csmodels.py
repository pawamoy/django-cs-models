# -*- coding: utf-8 -*-

"""Main test script."""



from django.test import TestCase

import csmodels


class MainTestCase(TestCase):
    """Main Django test case."""

    def setUp(self):
        """Setup method."""
        pass

    def test_main(self):
        """Main test method."""
        assert csmodels

    def tearDown(self):
        """Tear down method."""
        pass
