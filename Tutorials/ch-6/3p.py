Spam = ["Make a lot of money", "buy now", "subscribe this", "click this"]
text = input("Enter your comment: ")
if text in Spam:
    print("Your comment has been marked as spam and not posted.")
else:
    print("Your comment has been posted.")