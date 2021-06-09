import bcrypt

def user_login(username, password):
    password1 = b"super secret password"
    new = str(password).encode('utf-8')
    # Hash a password for the first time, with a randomly-generated salt
    hashed = bcrypt.hashpw(b"animal", bcrypt.gensalt())
    # Check that an unhashed password matches one that has previously been
    # hashed
    if bcrypt.checkpw(new, hashed):
        return True
    else:
        return False