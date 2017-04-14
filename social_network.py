from uuid import uuid4
from datetime import datetime

class UserDoesNotExistError(Exception):
    def __init__(self, uuid):
        super(UserDoesNotExistError, self).__init__(
            "User with uuid {} does not exist!".format(uuid))


class UserAlreadyExistsError(Exception):
    def __init__(self, uuid):
        super(UserAlreadyExistsError, self).__init__(
            "User with uuid {} already exists!".format(uuid))


class UsersNotConnectedError(Exception):
    def __init__(self):
        super(UsersNotConnectedError, self).__init__(
            "Users are not connected!")

class User:
    def __init__(self, full_name):
        self.full_name = full_name
        self.uuid = uuid4()
        self.posts = []

    def add_post(self, post_content):
        if(len(self.posts) == 50):
            self.posts.pop(0)
        self.posts.append(Post(self.full_name, self.post_content))

    def get_post(self):
        for post in self.posts:
            yield post

class Post:
    def __init__(self, author, content):
        self.author = author
        self.published_at = datetime.now()
        self.content = content

class SocialGraph:
    def __init__(self):
        self.graph = {}
        self.links = {}

    def add_user(self, user):
        if user in self.graph.values():
            raise UserAlreadyExistsError
        self.graph[user.uuid] = user

    def get_user(self, user_uuid):
        if user_uuid not in self.graph:
            raise UserDoesNotExistError
        return self.graph[user_uuid]

    def delete_user(self, user_uuid):
        if user_uuid not in self.graph:
            raise UserDoesNotExistError
        del self.users[user_uuid]
        if user_uuid in self.links:
            del self.links[user_uuid]

    def follow(self, follower, followee):
        self.graph[self.get_user(follower)].add(followee)

    def unfollow(self, follower, followee):
        self.graph[self.get_user(follower)].remove(followee)

    def is_following(self, follower, followee):
        return followee in self.graph[self.get_user(follower)]

    def followers(self, user_uuid):
        if user_uuid not in self.graph:
            raise UserDoesNotExistError
        if user_uuid not in self.links:
            raise UserDoesNotExistError
