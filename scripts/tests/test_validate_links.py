# -*- coding: utf-8 -*-

import unittest
import sys
import os

# Ajoute le chemin pour résoudre les imports
sys.path.insert(0, os.path.abspath('.'))

# Importe SEULEMENT les fonctions simples
from scripts.validate.links import find_links_in_text
from scripts.validate.links import check_duplicate_links
from scripts.validate.links import fake_user_agent
from scripts.validate.links import get_host_from_link

class TestValidateLinksSimple(unittest.TestCase):

    def test_find_links_in_text(self):
        """Test basic link finding functionality"""
        text = "Visit https://www.example.com and http://test.com"
        links = find_links_in_text(text)
        
        self.assertIsInstance(links, list)
        self.assertEqual(len(links), 2)
        self.assertIn('https://www.example.com', links)
        self.assertIn('http://test.com', links)

    def test_check_duplicate_links(self):
        """Test duplicate link detection"""
        links_with_duplicates = [
            'https://example.com',
            'https://example.com',  # Duplicate
            'https://test.com'
        ]
        
        links_without_duplicates = [
            'https://example.com',
            'https://test.com',
            'https://demo.com'
        ]
        
        # Test with duplicates
        has_duplicate, duplicates = check_duplicate_links(links_with_duplicates)
        self.assertTrue(has_duplicate)
        self.assertEqual(len(duplicates), 1)
        self.assertIn('https://example.com', duplicates)
        
        # Test without duplicates
        has_duplicate, duplicates = check_duplicate_links(links_without_duplicates)
        self.assertFalse(has_duplicate)
        self.assertEqual(len(duplicates), 0)

    def test_fake_user_agent(self):
        """Test user agent generation"""
        user_agent = fake_user_agent()
        self.assertIsInstance(user_agent, str)
        self.assertTrue(len(user_agent) > 0)

    def test_get_host_from_link(self):
        """Test host extraction from URLs"""
        test_cases = [
            ('https://www.example.com/path?query=1', 'www.example.com'),
            ('http://example.com', 'example.com'),
            ('https://sub.domain.co.uk/page', 'sub.domain.co.uk'),
        ]
        
        for link, expected_host in test_cases:
            with self.subTest(link=link):
                host = get_host_from_link(link)
                self.assertEqual(host, expected_host)

if __name__ == '__main__':
    # Pour exécuter directement avec Python
    unittest.main()