from wxauto import WeChat

wx = WeChat()

# 发送消息,
#'测试群02_worktool',
who = "测试群02_worktool"
wx.ChatWith(who=who)
at = ['村西']
# 发送图片
files = [
    r'C:\Users\pengxingsong\Pictures\素材\t2.jpg',  
    r'C:\Users\pengxingsong\Pictures\素材\tt1.txt'   
]

wx.SendMsg(msg= ' wxauto_测试忽略', who= who, at=at)
wx.SendFiles( filepath=files, who= who)
members = wx.GetGroupMembers()
wx.SendMsg(msg=" 群成员：" + format(members), who= who, at=at)

# 获取当前聊天页面（文件传输助手）消息，并自动保存聊天图片
# msgs = wx.GetAllMessage(savepic=True)
# for msg in msgs:
#     print(f"{msg[0]}: {msg[1]}")



print('wxauto测试完成！')
