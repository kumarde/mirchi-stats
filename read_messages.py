import groupy
import pickle
import operator

log_messages = pickle.load(open('log_messages', 'rb'))
mirchi_messages = pickle.load(open('mirchi_messages', 'rb'))

groups = groupy.Group.list()

for group in groups:
    if group.name == 'Maize M':
        mirchi_group = group
    if group.name == 'MIRCHI LOGISTICS':
        logs_group = group

max_liked = 0
max_liked_messages = []

likes = {}
likes_received = {}
ids_to_members = {}
members = mirchi_group.members()
#init members
for member in members:
    likes[member.nickname] = 0
    likes_received[member.user_id] = 0
    ids_to_members[member.user_id] = member.nickname  

for message in mirchi_messages:
    msg_likes = message.likes()
    if len(msg_likes) > 0:
        if message.user_id in likes_received:
            likes_received[message.user_id] += 1
        else:
            likes_received[message.user_id] = 1
    if len(msg_likes) > max_liked:
        max_liked_messages = []
        max_liked = len(msg_likes)
        max_liked_messages.append(message)
    for member in msg_likes:
        likes[member.nickname] += 1

print(len(mirchi_messages))

sorted_likes = sorted(likes.items(), key=operator.itemgetter(1))
sorted_likes_received = sorted(likes_received.items(), key=operator.itemgetter(1))

#for member in sorted_likes:
#    print(member[0], member[1])

for member in sorted_likes_received:
    if member[0] in ids_to_members:
        print(ids_to_members[member[0]], member[1])
#print(max_liked_messages)
