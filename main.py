from practice.services.user_verification import (
    login,
    signup,
    logout,
    get_all_emails
)

print(signup(1,"xyz@gmail.com","xyz123!"))
print(login(1,"xyz@gmail.com","xyz123!"))

# Testing
print(signup(1,"xyz@gmail.com","xyz123!"))
print(login(2,"xyz@gmail.com","xyz123!"))

print(get_all_emails())
print(logout(1))