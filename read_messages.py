import groupy
import pickle
import operator

log_messages = pickle.load(open('log_messages', 'rb'))
mirchi_messages = pickle.load(open('mirchi_messages', 'rb'))

mirchi_group = pickle.load(open('mirchi_group', 'rb'))
logs_group = pickle.load(open('log_group', 'rb'))

max_liked = 0
max_liked_messages = []

likes = {}
likes_received = {}
messages_sent = {}
likes_received_total = {}
ids_to_members = {}
members = mirchi_group.members()
#init members
for member in members:
    messages_sent[member.user_id] = 0
    likes[member.nickname] = 0
    likes_received[member.user_id] = 0
    ids_to_members[member.user_id] = member.nickname  

for message in mirchi_messages:
    msg_likes = message.likes()
    if message.user_id in messages_sent:
        messages_sent[message.user_id] += 1
    else:
        messages_sent[message.user_id] = 1
    if len(msg_likes) > 0:
        if message.user_id in likes_received:
            likes_received[message.user_id] += 1
        else:
            likes_received[message.user_id] = 1
        if message.user_id in likes_received_total:
            likes_received_total[message.user_id] += len(msg_likes)
        else:
            likes_received_total[message.user_id] = len(msg_likes)
    if len(msg_likes) > max_liked:
        max_liked_messages = []
        max_liked = len(msg_likes)
        max_liked_messages.append(message)
    for member in msg_likes:
        likes[member.nickname] += 1

sorted_likes = sorted(likes.items(), key=operator.itemgetter(1))
sorted_likes_received = sorted(likes_received.items(), key=operator.itemgetter(1))
sorted_likes_received_total = sorted(likes_received_total.items(), key=operator.itemgetter(1))
total_messages_sent = sorted(messages_sent.items(), key=operator.itemgetter(1))

#Likes_given
#for member in sorted_likes:
#    print(member[0], member[1])

#Likes received by message
#for member in sorted_likes_received:
#    if member[0] in ids_to_members:
#        print(ids_to_members[member[0]], member[1])

#for member in total_messages_sent:
#    if member[0] in ids_to_members:
#        print(ids_to_members[member[0]], member[1])

likeability = {}
for member in total_messages_sent:
    if member[0] in ids_to_members:
        lks = likes_received[member[0]]
        likeability[ids_to_members[member[0]]] = float(lks/member[1])

likeability_sorted = sorted(likeability.items(), key=operator.itemgetter(1))
for member in likeability_sorted:
    print(member[0], member[1])

#Total likes received 
#for member in sorted_likes_received_total:
#    if member[0] in ids_to_members:
#        print(ids_to_members[member[0]], member[1])
