jk=[
    {'koda@123b.com':"abc"},
    {'mani@b.com':"ghu"},
    {'sai@b.com':"lok"},
    {'bannu@3.com':"raj"}
]
print(jk)
username=input("enter name:")
password=input("enter:")
temp={username:password}
while True:
  if temp in jk:
    print("user found")
  else:
    print("not found")
