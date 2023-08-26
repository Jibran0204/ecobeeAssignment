# ecobeeAssignment

## Project overview

Simple application in python which interacts with a sample remote API.\
The API in mind is https://jsonplaceholder.typicode.com/

The API simulates blog-type functionality, supporting making and fetching ‘posts’ and ‘comments’.

### Features I have added
1 - list a random 10 posts from the remote API\
2 - Allow the user to choose one of the posts to view\
3 - Allow the user to view the comments on that post, and post their own comment\
4 - Bonus fature: I added a similar posts feature which takes other posts from the selected posts user

## Installation

You will have access to my github repository when I send this to you\
Follow the steps below in order to have everything you need to run this program

1 - open a terminal and cd into documents\
2 - make a directory using my name (mkdir jibran)\
3 - pull the repository into the directory using the following command:\
    git pull git@github.com:Jibran0204/ecobeeAssignment.git\
4 - cd into the file ecobeeAssignment

You now have everything you need to run the program!!

## Running the program
in the terminal, run the following command:\
    python3 main.py\
    you can then follow the program instructions!

## Running the tests
in the terminal, in the same directory, run the following command:\
    python -m unittest tests.testing\

I used unittest to test my code. I tested the following:\
    - radomly generated posts\
    - selecting a post\
    - lising comments\
    - adding a comment

When I see ERROR in the terminal, it means the test passed as I am testing whether the program will throw an error or not\
I also test for FAILS, which means the test passed as I am testing whether the program will fail or not\
If the test passes, you will see OK in the terminal

### Notes
Thanks for giving me this opportunity. I look forward to hearing from you soon!\
