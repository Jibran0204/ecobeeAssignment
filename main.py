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
    # print("id: " + str(optionPost['id']))
    # print("userId: " + str(optionPost['userId']))

    print("\n")
    return optionPost


def get_comments(post):

    # get the post id
    post_id = post['id']
    response = requests.get(url + "/comments")

    # convert the response to json
    comments = response.json()
    
    # create an empty list to store the comments
    post_comments = []
    # loop through all comments
    for i in comments:
        # if the comment belongs to the post
        if i['postId'] == post_id:
            # add the comment to the list
            post_comments.append(i)
    return post_comments

def comment(comment, commentList):

    # add the comment to the list of comments
    commentList.append(comment)
    # print the comment
    print("Your comment!!:")
    print("Name: " + comment['name'])
    print("Email: " + comment['email'])
    print("Body: " + comment['body'])
    print("\n")
    return commentList

def list_comments(comments):
    for i in comments:
        print("Comment Details:")
        print("Name: " + i['name'])
        print("Email: " + i['email'])
        print("Body: " + i['body'])
        print("\n")

def view_similar_posts(post):
    # get the user id
    user_id = post['userId']
    response = requests.get(url + "/posts")

    # convert the response to json
    posts = response.json()
    
    # create an empty list to store the posts
    user_posts = []
    # loop through all posts
    for i in posts:
        # if the post belongs to the user
        if i['userId'] == user_id:
            # add the post to the list
            user_posts.append(i)
    return user_posts


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

    # using the same logic as above to get the comments
    commentDecision = input("Do you want to see the comments? (y/n): ")
    # error handling
    while(commentDecision != "y" and commentDecision != "n"):
        print("Invalid input")
        commentDecision = input("Do you want to see the comments? (y/n): ")

    # if the user wants to see the comments
    if commentDecision == "y":
        # uuse the get_comments function to get a list of comments
        comments = get_comments(posts[int(postNum) - 1])
        list_comments(comments)

    else:
        # exit the program
        print("Thanks for using the program :)")
        exit()

    # create a prompt to ask the user if they want to comment
    addCommentDecision = input("Do you want to comment? (y/n): ")
    # error handling
    while(addCommentDecision != "y" and addCommentDecision != "n"):
        print("Invalid input")
        addCommentDecision = input("Do you want to comment? (y/n): ")
    
    # if the user wants to comment
    if addCommentDecision == "y":
        # create a prompt to ask the user for their name
        name = input("Enter your name: ")
        # create a prompt to ask the user for their email
        email = input("Enter your email: ")
        # create a prompt to ask the user for their comment
        body = input("Enter your comment: ")
        # create a dictionary to store the comment
        userComment = {
            "postId": int(postNum),
            "id": len(comments) + 1,
            "name": name,
            "email": email,
            "body": body
        }
        comment(userComment, comments)
        list_comments(comments)
    else:
        # exit the program
        print("Thanks for using the program :)")
        exit()

    # create a prompt to ask the user if they want to view similar posts
    viewSimilarPostsDecision = input("Do you want to view similar posts? (y/n): ")
    # error handling
    while(viewSimilarPostsDecision != "y" and viewSimilarPostsDecision != "n"):
        print("Invalid input")
        viewSimilarPostsDecision = input("Do you want to view similar posts? (y/n): ")

    # if the user wants to view similar posts
    if viewSimilarPostsDecision == "y":
        # use the view_similar_posts function to get a list of similar posts
        similarPosts = view_similar_posts(posts[int(postNum) - 1])
        # print the similar posts
        print("Similar Posts:")
        for i in similarPosts:
            print(i['title'])
    else:
        # exit the program
        print("Thanks for using the program :)")
        exit()

if __name__ == "__main__":
    main()
