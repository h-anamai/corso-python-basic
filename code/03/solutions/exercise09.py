def save_user(username, password):
    print(f"User {username} saved with password {password}!")

if __name__ == "__main__":
    credentials = {'username': 'admin', 'password': 'password'}
    save_user(**credentials)