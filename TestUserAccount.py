#This script performs some simple tests on the UserAccount class.
from UserAccount import UserAccount


user= UserAccount("yuly1234","1234","you did it!")
user.print_secret(1234)

user.print_secret("1234")
