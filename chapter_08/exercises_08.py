# 8.1 Message

def display_message():
    ''' This function simply states 
    what I am learning about in this chapter'''
    print("In Ch. 8 I am learning about writing functions and how passing arguments work.")

display_message()

# 8.2 Favorite Book
def favorite_book(title):
    """Prints out what a users favorite book is"""
    print(f"One of my favorite books is {title.title()}.")

favorite_book("neuromancer")