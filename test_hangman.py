import string
from unittest import TestCase

from hangman import is_word_guessed, get_guessed_word, get_available_letters, match_with_gaps


class Test(TestCase):
    def test_is_word_guessed(self):
        self.assertTrue(is_word_guessed("apple", ['p', 'e', 'a', 'l']))
        self.assertFalse(is_word_guessed("esoteric", ['e', 'a']))
        self.assertTrue(is_word_guessed("no", ['n', 'o', 't']))

    def test_get_guessed_word(self):
        self.assertEqual('_ _ _ _ ', get_guessed_word('true', []))
        self.assertEqual('_ _ _ _ ', get_guessed_word('true', ['a', 'b', 'c']))
        self.assertEqual('ne_ ', get_guessed_word('new', ['n', 'p', 'e']))
        self.assertEqual('_ _ ss', get_guessed_word('pass', ['s', 'q', 'b']))

    def test_get_available_letters(self):
        self.assertEqual(string.ascii_lowercase, get_available_letters([]))
        self.assertEqual('defghijklmnopqrstuvwxyz', get_available_letters(['a', 'b', 'c']))
        self.assertEqual('abcdefghijklmnopqrstuvw', get_available_letters(['x', 'y', 'z']))
        self.assertEqual('bcdefghijklmnpqrsuvwxyz', get_available_letters(['o', 't', 'a']))

    def test_match_with_gaps(self):
        self.assertFalse(match_with_gaps('te_ t', 'tact'))
        self.assertFalse(match_with_gaps('a_ _ le', 'banana'))
        self.assertTrue(match_with_gaps('a_ _ le', 'apple'))
        self.assertFalse(match_with_gaps('a_ ple', 'apple'))
