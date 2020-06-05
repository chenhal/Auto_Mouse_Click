from pymouse import PyMouse
import time
welcome = "欢迎使用鼠标连点器！！ By DylanC"
print(welcome)
k = ('左','右','中')
m = PyMouse()
t = int(input('输入点击总次数（若你设置为0，则可能使你的电脑崩溃，慎用！）：'))
if (t == 0):
	print('[警告]你设定了不限制，你需要考虑您是否有办法关闭它！')
d = float(input('输入两次点击之间的间隔（单位为秒，可以为0）：'))
if (d < 0.005):
	print('[警告]你设定的间隔很小，你需要考虑您的计算机或要点击的东西是否可以承受它的疯狂输出。')
p = int(input('点击的键（1=左键，2=右键，3=中键）：'))
print('你已经设置完毕！')
print('你有5秒的时间移动鼠标到想要连点的地方或关闭点击器。')
for i in range(5):
	print('剩余',5-i,'S')
	time.sleep(1)
print('开始点击！')
s = time.time()
i = 0
while(i < t or t == 0):
	m.click(m.position()[0],m.position()[1],p)
	i=i+1
	time.sleep(d)
e = time.time()
print('[总结]点击',k[p-1],'键',t,'次，点击间隔为',d,'的任务成功结束，共用时约',round(e-s,2),'秒，平均每秒约点击',round(t/(e-s),2),'次。')

#Copyright by DylanC (Cll66.CN)
#使用一时爽，电脑维修厂,请一定适度使用！