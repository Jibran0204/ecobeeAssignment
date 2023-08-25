import unittest
from main import random_posts, select_post

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

class TestSelectedPosts(unittest.TestCase):

    mock_posts = [
    {'id': 1, 'title': 'Title 1', 'body': 'Body 1', 'userId': 1},
    {'id': 2, 'title': 'Title 2', 'body': 'Body 2', 'userId': 1},
    {'id': 3, 'title': 'Title 3', 'body': 'Body 3', 'userId': 2},
    {'id': 4, 'title': 'Title 4', 'body': 'Body 4', 'userId': 2},
    {'id': 5, 'title': 'Title 5', 'body': 'Body 5', 'userId': 3},
    {'id': 6, 'title': 'Title 6', 'body': 'Body 6', 'userId': 3},
    {'id': 7, 'title': 'Title 7', 'body': 'Body 7', 'userId': 4},
    {'id': 8, 'title': 'Title 8', 'body': 'Body 8', 'userId': 4},
    {'id': 9, 'title': 'Title 9', 'body': 'Body 9', 'userId': 5},
    {'id': 10, 'title': 'Title 10', 'body': 'Body 10', 'userId': 5}
]


    def test_selected_post(self):
        option = 1
        post = select_post(self.mock_posts, option)
        self.assertEqual(post, self.mock_posts[0])
        print("Test passed")
        
    def test_selected_post_negative_number(self):
        option = -1
        post = select_post(self.mock_posts, option)
        self.assertEqual(post, self.mock_posts[0])

    def test_selected_post_zero(self):
        option = 0
        post = select_post(self.mock_posts, option)
        self.assertEqual(post, self.mock_posts[0])

    def test_select_post_out_of_range(self):
        option = 11
        post = select_post(self.mock_posts, option)
        self.assertEqual(post, self.mock_posts[0])


            
if __name__ == "__main__":
    
    unittest.main()
