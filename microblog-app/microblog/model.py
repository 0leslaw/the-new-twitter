class Post:
    def __init__(self, post_id, user, content, timestamp, answered_to_id=None):
        self.post_id = post_id
        self.user = user
        self.content = content
        self.timestamp = timestamp
        self.answered_to_id = answered_to_id


class User:
    def __init__(self, user_id, email, name, desc=None):
        self.user_id = user_id
        self.email = email
        self.name = name
        self.desc = desc
