"""Example mini tests for the server funcitons in server.py."""


import unittest

import palvelin.server
import palvelin.pages


class TestPalvelin(unittest.TestCase):
    """Test server.py handlers."""
    
    def setUp(self):
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    
    def test_index(self):
        """."""
        ret = palvelin.server.index()
        self.assertEqual(ret, palvelin.pages.indexPage)

    def test_pageone(self):
        """."""
        ret = palvelin.server.pageone()
        self.assertEqual(ret, palvelin.pages.pageOne)

    def test_pagetwo(self):
        """."""
        ret = palvelin.server.pagetwo()
        self.assertEqual(ret, palvelin.pages.pageTwo)

    def test_pagethree(self):
        """."""
        ret = palvelin.server.pagethree()
        self.assertEqual(ret, palvelin.pages.pageThree)
