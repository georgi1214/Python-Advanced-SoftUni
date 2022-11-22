n = int(input())
users = set()

for i in range(n):
    username = input()
    users.add(username)
for user in users:
    print(user)
