from random import randrange, shuffle
import math
import sys
sys.path.insert(0, '../graph')
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        self.count = 0

    def add_friendship(self, user_id, friend_id):
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            self.count += 1

    def add_user(self, name):
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for n in range(num_users):
            self.add_user(n)

        # Create friendships
        total_friends = 0
        max_friends = num_users * avg_friendships
        while total_friends < max_friends:
            user = randrange(1, num_users + 1)
            friend = randrange(1, num_users + 1)

            #update friend until a unique friend is found
            while user == friend or friend in self.friendships[user]:
                friend = randrange(1, num_users + 1)
            self.add_friendship(user, friend)
            total_friends += 2

    def get_all_social_paths(self, user_id):
        visited = {}  # Note that this is a dictionary, not a set
        queue = Queue()
        queue.enqueue({'id': user_id, 'path': [user_id]})

        while queue.size() > 0:
            user = queue.dequeue()
            visited[user['id']] = user['path']
            for friend in self.friendships[user['id']]:
                if friend not in visited:
                    visited[friend] = user['path'] + [friend]
                    queue.enqueue({'id': friend, 'path': visited[friend]})

        return visited

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 3)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)