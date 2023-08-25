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

# function to select a post
def select_post(posts, option):
    # convert the option to an integer also subtract 1 since index is 1-9
    option = int(option) - 1
    
    # error handling in case select post is run below
    if option < 0 or option > 11:
        return
    
    optionPost = posts[option]
    # print the selected option
    print("\nPost Details:")
    print("Title: " + optionPost['title'])
    print("Body: " + optionPost['body'])

    print("\n")
    return optionPost



def main():
    # call the random posts functions this will allow me to
    num = 10
    posts = random_posts(num)

    i = 0
    while i < len(posts):
        post = posts[i]
        print(f"{i+1}. {post.get('title')}")
        i += 1
    
    # ask the user to select a post
    postNum = input("select a number between 1-10: ")
    # error handling
    while(int(postNum) > 10 or int(postNum) < 1):
        print("Invalid number")
        postNum = input("select a number between 1-10: ")
        
    # call the select post function
    select_post(posts, postNum)



if __name__ == "__main__":
    main()
