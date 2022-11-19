from skpy import Skype

slogin = Skype('email addresss', 'pass')
contact = slogin.contacts["provide a id"]
contact.chat.sendMsg('Any message u want')


# printing ur  contacts
# for i in contact:
#     print(i)

