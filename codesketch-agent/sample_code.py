class UserService:
    def __init__(self, database):
        self.db = database

    def create_user(self, name, email):
        user_id = self.db.save({"name": name, "email": email})
        return user_id

    def get_user(self, user_id):
        return self.db.fetch(user_id)


class Database:
    def __init__(self):
        self.storage = {}
        self.counter = 1

    def save(self, data):
        user_id = self.counter
        self.storage[user_id] = data
        self.counter += 1
        return user_id

    def fetch(self, user_id):
        return self.storage.get(user_id, None)


def main():
    db = Database()
    user_service = UserService(db)

    # Create a new user
    new_user_id = user_service.create_user("Alice", "alice@example.com")
    print("Created User ID:", new_user_id)

    # Fetch that user
    user_info = user_service.get_user(new_user_id)
    print("User Info:", user_info)


if __name__ == "__main__":
    main()
