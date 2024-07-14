from wxauto import WeChat

wx = WeChat()

# friend = wx.GetFriendDetails()
# for f in friend:
#     print(f)

members = wx.GetGroupMembers()
for me in members:
    print(me)
