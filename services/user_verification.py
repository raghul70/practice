store={}
# signup Code
def signup(id:int,email:str,password:str):
    if id in store:
        return {
            "message":"Already registered",
        }

    store[id]={
        'email':email,
        'password':password,
    }

    return {
        "message":"Signup Successful",
    }

# login Code

def login(id:int,email:str,password:str):
    if id in store and (store[id]['email']==email and store[id]['password']==password):
        return {
            "message":"Login Successful",
        }
    return {
        "message":"Login Failed",
    }

#logout Code

def logout(id:int):
    if id in store:
        del store[id]
        return {
            "message":"Logout Successful",
        }
    return {
        "message":"Logout Failed",
    }

def get_all_emails():
    emails=[]
    for i in store:
        emails.append(store[i]['email'])
    return emails
