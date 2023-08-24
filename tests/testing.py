import unittest

from main import random_posts

class TestRandomPosts(unittest.TestCase):

    # test that the number of posts returned is equal to the number of posts requested
    def test_random_posts(self):
        num_posts = 10
        posts = random_posts(num_posts)
        self.assertEqual(len(posts), num_posts)
        print("Test passed")

    # test random posts with no number
    def test_random_posts_no_number(self):
        posts = random_posts()
        self.assertEqual(len(posts), 10)
        print("Test passed")

    # test the random posts with negative number
    def test_random_posts_negative_number(self):
        posts = random_posts(-1)
        self.assertEqual(len(posts), 10)
        print("Test passed")


            



        
