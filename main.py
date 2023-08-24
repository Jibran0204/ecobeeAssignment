# imported requests because it is a library that allows me to send HTTP requests
import requests
# imported random because it is a library that allows me to generate random numbers.
# this will be used for the first task
import random

# url of the API
url = "https://jsonplaceholder.typicode.com"


# getting random posts:
def random_posts(NumPosts):
    # use the base url and the /posts endpoint to get all posts
    response = requests.get(url + "/posts")
    # convert the response to json
    # the response is a string and we want to be able to access the data as a dictionary
    post = response.json()
    # use the random library to generate random numbers
    random_post = random.sample(post, NumPosts)
    # return
    return random_post

def main():
    # call the random posts functions this will allow me to
    num = 10
    posts = random_posts(num)

    i = 0
    while i < len(posts):
        post = posts[i];
        print(f"{i+1}. {post.get('title')}")
        i += 1
    

if __name__ == "__main__":
    main()
