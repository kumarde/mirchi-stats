import groupy
import pickle

groups = groupy.Group.list()
logs = groups[1]
mirchi = groups[0]

with open('mirchi_group', 'wb') as f:
    pickle.dump(mirchi, f)

with open('log_group', 'wb') as f:
    pickle.dump(logs, f)

log_messages = logs.messages()
while log_messages.iolder():
    pass

print(len(log_messages)==logs.message_count)
with open('log_messages', 'wb') as f:
    pickle.dump(log_messages, f)

mirchi_messages = mirchi.messages()
while mirchi_messages.iolder():
    pass

print(len(mirchi_messages))
print(len(mirchi_messages)==mirchi.message_count)

with open('mirchi_messages', 'wb') as f:
    pickle.dump(mirchi_messages, f)
