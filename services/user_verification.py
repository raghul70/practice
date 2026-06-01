store={}
# signup Code
def signup(id:int,email:str,password:str):
    store[id]={
        'email':email,
        'password':password,
    }

    return {
        "message":"Login Successful",
    }

