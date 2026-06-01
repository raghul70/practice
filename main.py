from practice.services.user_verification import (
    login,
    signup,
    logout
)

print(signup(1,"xyz@gmail.com","xyz123!"))
print(login(1,"xyz@gmail.com","xyz123!"))
print(logout(1))