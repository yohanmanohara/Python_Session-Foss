# Q: You are searching through a list of usernames to find a specific user. Once you find the user, you want to stop searching

usernames = ['alice', 'bob', 'charlie', 'david']
for user in usernames:
  if user == "charlie":
    print("User Charlie is found.")
    break

