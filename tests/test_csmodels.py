# -*- coding: utf-8 -*-

"""Main test script."""



from django.test import TestCase

import csmodels


class MainTestCase(TestCase):
    """Main Django test case"""
    def setUp(self):
        pass

    def test_main(self):
        assert csmodels

    def tearDown(self):
        pass
