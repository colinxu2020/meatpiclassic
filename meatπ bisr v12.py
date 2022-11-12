import webbrowser as webr,time as tm,random as r,turtle as t,os,keyword as kw,math
A,B,C,E,I,K,L,M,N,O,P,Q,R,S,T,U,W,X=abs,bin,chr,eval,input,t.bk,len,min,open,ord,print,int,r.randint,str,t.fd,tm.sleep,range,max
s='Copyright (c) 2022 Python Source Code Collecting Org.\nCopyright (c) 2022 dgncx(c) Org.\nAll Rights Reserved.\n'
P(s)
class Dt:
 try:
  nums66,et47,wheel62,hfms,block27,blockcol27,map135,map235,map138,a23,refl62,inits2293,excepter=E(N('Meatpi_Data.dat','r').read())
 except:
  P('ERROR\nData file not found or not available.\nYou can goto g9mee.csb.app for the latest version of the data file.')
  while 1:
    pass
class Sz:
 try:
  ls=E(N('Meatpi_Settings.dat','r').read())
  if L(ls)!=6:
   excepter
 except:
  ls=[1,None,1,0.6,I('Username (will be saved):'),1]
  N('Meatpi_Settings.dat','w').write(S(ls))
 name=['sound','deleted','output clearing','time gap between functions','username','exceptions recording']
def clear():
 if Sz.ls[2]==0:
  return 0
 if os.name=='nt':
  _=os.system('cls')
 else:
  _=os.system('clear')
nowin=0
try:
 import winsound
except:
 nowin=1
 Sz.ls[0]=0
 N('Meatpi_Settings.dat','w').write(S(Sz.ls))
 P('WARNING\nThe "winsound" module is not found in your computer.\nSound has been disabled automatically.')
 I('Press Enter to continue')
def ok1(now,s):
 if L(s)!=3 or s[0]<'A' or s[0]>'I' or Q(s[1:])<1 or Q(s[1:])>11 or s=='D06':
  return 0
 elif now[0]==s[0] and Q(s[1:])>Q(now[1:]) and not(now[0]=='D' and Q(s[1:])>6>Q(now[1:])):
  return 1
 elif now[1:]==s[1:] and O(now[0])>O(s[0]) and not(now[1:]=='06' and O(now[0])>O('D')>O(s[0])):
  return 1
 elif O(now[0])+Q(now[1:])==O(s[0])+Q(s[1:]) and O(now[0])>O(s[0]) and not(O(s[0])+Q(s[1:])==O('D')+6 and Q(s[1:])>6>Q(now[1:])):  
  return 1
 else:
  return 0
def ok2(now,s):
 if L(s)!=3 or s[0]<'A' or s[0]>'K' or Q(s[1:])<1 or Q(s[1:])>13 or s=='D08' or s=='I03':
  return 0
 elif now[0]==s[0] and Q(s[1:])>Q(now[1:]) and not(now[0]=='D' and Q(s[1:])>8>Q(now[1:])) and not(now[0]=='I' and Q(s[1:])>3>Q(now[1:])):
  return 1
 elif now[1:]==s[1:] and O(now[0])>O(s[0]) and not(now[1:]=='08' and O(now[0])>O('D')>O(s[0])) and not(now[1:]=='03' and O(now[0])>O('I')>O(s[0])):
  return 1
 elif O(now[0])+Q(now[1:])==O(s[0])+Q(s[1:]) and O(now[0])>O(s[0]) and not(O(s[0])+Q(s[1:])==O('D')+8 and Q(s[1:])>8>Q(now[1:])) and not(O(s[0])+Q(s[1:])==O('I')+3 and Q(s[1:])>3>Q(now[1:])):  
  return 1
 else:
  return 0
def mst():
 now=tm.time()
 add=now-1595692800.0
 tim=S(Q(add/86400*20000))
 ln=L(tim)
 tim=tim[0:ln-5]+':'+tim[ln-5]+':'+tim[ln-4:]
 return tim
class c64:
  vis=[]
def dfs64(mp64,x,y,col,m):
 c64.vis[x][y]=1
 res=1
 if m=='64':
  inbound=lambda x,y:(x>=0 and x<5 and y>=0 and y<5)
 elif m=='65':
  inbound=lambda x,y:(x>=0 and x<8 and y>=0 and y<8)
 else:
  inbound=lambda x,y:(x>=0 and x<6 and y>=0 and y<6)
 dx,dy=[0,0,1,-1],[1,-1,0,0]
 for i in W(4):
  vx,vy=x+dx[i],y+dy[i]
  if inbound(vx,vy):
   if mp64[vx][vy]==col and not c64.vis[vx][vy]:
    c64.vis[vx][vy]=1
    res+=dfs64(mp64,vx,vy,col,m)
 return res
def op66(modes,x,y,ds,dopr):
 if ds:
  P(S(x)+S(y)+'\n')
 cor=[]
 for i in W(7):
  cor.append(Dt.nums66[x][i])
 for i in W(7):
  cor.append(Dt.nums66[y][i])
 for i in W(14):
  if modes[i]==1:
   cor[i]=1
  if modes[i]==2:
   cor[i]=0
  if modes[i]==3:
   cor[i]=1-cor[i]
 ch1=lambda x:Q(cor[x])*'_'+(1-Q(cor[x]))*' '
 ch2=lambda x:Q(cor[x])*'|'+(1-Q(cor[x]))*' '
 if dopr:
  P(' '+ch1(0)+'   '+ch1(7))
  P(ch2(1)+ch1(3)+ch2(2)+' '+ch2(8)+ch1(10)+ch2(9))
  P(ch2(4)+ch1(6)+ch2(5)+' '+ch2(11)+ch1(13)+ch2(12))
 return cor
def read(k):
 P()
 P(Sz.name[k])
 if k!=4:
  P('current value:',Sz.ls[k])
 else:
  P("current value: '"+Sz.ls[k]+"'")
 Sz.ls[k]=E(I('new value: '))
def gcd(a,b):
 if a==1 or b==1:
  return 1
 elif a==0 or b==0:
  return X(a,b)
 else:
  return gcd(b,a%b)
def fff(n,x):
 a=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
 b=[]
 while 1:
  s=n//x
  y=n%x
  b=b+[y]
  if s==0:
   break
  n=s
 b.reverse()
 re=''
 for i in b:
  res+=a[i]
 return res
def getord62(c):
 if O('a')<=O(c) and O('z')>=O(c):
  return O(c)-O('a')
 else:
  return 26
def getchr62(x):
 if 0<=x and 25>=x:
  return C(O('a')+x)
 else:
  return ' '
def add62(c):
 for i in W(5):
  if c[-i-1]!=' ':
   c=c[0:9-i]+getchr62(getord62(c[-1])+1)+c[10-i:]
   break
  else:
   c=c[0:9-i]+'a'+c[10-i:]
 return c
hfms=Dt.hfms
inits=Dt.inits2293
players=inits[0]
boxes=inits[1]
targs=inits[2]
def playhf(tm):
 ops=['w','a','s','d']
 dx=[-1,0,1,0]
 dy=[0,-1,0,1]
 P('stages:%d'%(L(hfms)))
 for mp in hfms:
  stage=hfms.index(mp)
  U(1)
  clear()
  U(1)
  player=players[stage]
  box=boxes[stage]
  targ=targs[stage]
  boxfn=0
  while not(boxfn) or player!=targ:
   clear()
   P("STAGE <%d>"%(stage+1))
   for i in W(9):
    for j in W(11):
     s=''
     if [i,j]==player:
      s='i'
     elif not(boxfn) and [i,j]==box:
      s='@'
     elif [i,j]==targ:
      s='O'
     elif mp[i][j]:
      s='#'
     else:
      s='.'
     P(s,end='')
    P()
   op=I('Operation:')
   while not(op in ops):
    op=I('ERROR Please try again:')
   dirx=dx[ops.index(op)]
   diry=dy[ops.index(op)]
   onx=player[0]+dirx
   ony=player[1]+diry
   if boxfn and targ==[onx,ony]:
    player=[onx,ony]
    continue
   if mp[onx][ony]:
    continue
   elif box!=[onx,ony]:
    player=[onx,ony]
   elif mp[onx+dirx][ony+diry]:
    continue
   else:
    player=[onx,ony]
    box=[onx+dirx,ony+diry]
   if box==targ:
    boxfn=1
class Gl:
 do21,ss,run52=0,'',0
 ads=[\
'''wtlocker.eu.org PSCCO官方推荐的一款实用的聊天网站,登录即可开聊,功能齐全,快来试试吧!''',\
'''g9mee.csb.app PSCCO官方指定的小程序下载处,有c也有py,快来玩吧!''',\
'']
def zip08():
 ls=[]
 allres=[]
 allre2=[]
 for i in W(4):
  s='第'+S(i+1)+'个数:'
  ls.append(Q(I(s)))
 for i in W(4):
  for j in W(4):
   for k in W(4):
    for l in W(4):
     if i!=j and i!=k and i!=l and j!=k and j!=l and k!=l:
      ls2=[ls[i],ls[j],ls[k],ls[l]]
      for m in W(216):
       res=S(ls2[0])
       for now in W(1,4):
        nowe=ls2[now]
        po=(m%(6**(now)))//((6**(now-1)))
        if po==0:
         res+='+'+S(nowe)
        if po==1:
         res+='*'+S(nowe)
        if po==2:
         res+='-'+S(nowe)
        if po==3:
         res=S(nowe)+'-'+res
        if po==4:
         res+='/'+S(nowe)
        if po==5:
         res=S(nowe)+'/'+res
        res='('+res+')'
       try:
        if A(E(res)-24)<=0.001:
         allres.append(res)
       except:
        pass
      for m in W(216):
       re=''
       re1=''
       re2=''
       o1=(m%6)//1
       o2=(m%216)//36
       o3=(m%36)//6
       if o1==0:
        re1='('+S(ls[0])+'+'+S(ls[1])+')'
       if o1==1:
        re1='('+S(ls[0])+'*'+S(ls[1])+')'
       if o1==2:
        re1='('+S(ls[0])+'-'+S(ls[1])+')'
       if o1==3:
        re1='('+S(ls[1])+'-'+S(ls[0])+')'
       if o1==4:
        re1='('+S(ls[0])+'/'+S(ls[1])+')'
       if o1==5:
        re1='('+S(ls[1])+'/'+S(ls[0])+')'
       if o2==0:
        re2='('+S(ls[2])+'+'+S(ls[3])+')'
       if o2==1:
        re2='('+S(ls[2])+'*'+S(ls[3])+')'
       if o2==2:
        re2='('+S(ls[2])+'-'+S(ls[3])+')'
       if o2==3:
        re2='('+S(ls[3])+'-'+S(ls[2])+')'
       if o2==4:
        re2='('+S(ls[2])+'/'+S(ls[3])+')'
       if o2==5:
        re2='('+S(ls[3])+'/'+S(ls[2])+')'
       if o3==0:
        re='('+re1+'+'+re2+')'
       if o3==1:
        re='('+re1+'*'+re2+')'
       if o3==2:
        re='('+re1+'-'+re2+')'
       if o3==3:
        re='('+re2+'-'+re1+')'
       if o3==4:
        re='('+re1+'/'+re2+')'
       if o3==5:
        re='('+re2+'/'+re1+')'
       try:
        if A(E(re)-24)<=0.0001:
         allres.append(re)
       except:
        pass
 for res in allres:
  if not(res in allre2):
   allre2.append(res)
   P(res)
 if L(allres)==0:
  P('无法算出24!')
def zip21():
 import turtle as t
 if Gl.do21:
  t2.clear()
  t2.shape('blank')
 Gl.do21=1
 t.clear()
 t.color('black')
 t.up()
 t.goto(0,0)
 t.down()
 t.seth(0)
 t.speed(0)
 t.shape('square')
 t2=t.Turtle()
 t2.up()
 t2.shape('square')
 t2.goto(110,110)
 lsa=['I','H','G','F','E','D','C','B','A','']
 lsb=['01','02','03','04','05','06','07','08','09','10','11','']
 keypoint=['E03','H07','D05','F08','B09','C10','A11']
 for i in W(10):
  T(220);K(220)
  t.up()
  t.rt(180);T(20)
  t.write(lsa[i],font=('Arial',16))
  K(20);t.lt(180)
  t.down()
  if i!=9:
   t.lt(90);T(20);t.rt(90)
 t.up()
 t.goto(0,0)
 t.down()
 t.lt(90)
 for i in W(12):
  T(180);K(180)
  t.up()
  t.rt(180);T(20)
  t.write(lsb[i],font=('Arial',9))
  K(20);t.lt(180)
  t.down()
  if i!=11:
   t.rt(90);T(20);t.lt(90)
 t.up()
 t.goto(10,10)
 t.down()
 s='I01'
 x=I('谁先来（电脑先来输入1，你先来输入2）?')
 if x=='2':
  while s!='A11':
   t.color('blue')
   s2=I('你想走到哪里?')
   while not ok1(s,s2):
    s2=I('走不到，请重新输入：')
   s=s2
   t.goto(lsb.index(s2[1:])*20+10,lsa.index(s2[0])*20+10)
   U(0.3)
   for i in keypoint:
    if ok1(s,i):
     t.color('red')
     P('电脑决定走到',i)
     s=i
     t.goto(lsb.index(s[1:])*20+10,lsa.index(s[0])*20+10)
  P('电脑赢了!!!')
 else:
  while 1:
   t.color('red')
   m=1
   for i in keypoint:
    if ok1(s,i):
     P('电脑决定走到',i)
     m=0
     s=i
     t.goto(lsb.index(s[1:])*20+10,lsa.index(s[0])*20+10)
   if m:
    cc=R(1,4)
    if cc==1 and ok1(s,C(O(s[0])-1)+s[1:]):
     P('电脑决定走到',C(O(s[0])-1)+s[1:])
     s=C(O(s[0])-1)+s[1:]
     t.goto(lsb.index(s[1:])*20+10,lsa.index(s[0])*20+10)
    elif cc==2 and ok1(s,s[0]+((Q(s[1:])+1)<10)*'0'+S(Q(s[1:])+1)):
     s=s[0]+((Q(s[1:])+1)<10)*'0'+S(Q(s[1:])+1)
     P('电脑决定走到',s)
     t.goto(lsb.index(s[1:])*20+10,lsa.index(s[0])*20+10)
    else:
     s=C(O(s[0])-1)+((Q(s[1:])+1)<10)*'0'+S(Q(s[1:])+1)
     P('电脑决定走到',s)
     t.goto(lsb.index(s[1:])*20+10,lsa.index(s[0])*20+10)
   if s=='A11':
    P('电脑赢了!!!')
    break
   t.color('blue')
   s2=I('你想走到哪里?')
   while not ok1(s,s2):
    s2=I('走不到，请重新输入：')
   s=s2
   t.goto(lsb.index(s2[1:])*20+10,lsa.index(s2[0])*20+10)
   U(0.3)
   if s=='A11':
    P('你赢了!!!')
    break
 t.up()
def zip22():
 t.clear()
 t.speed(0)
 t.seth(0)
 t.shape('classic')
 t.color('black')
 t.up()
 t.goto(0,0)
 if Gl.do21:
  t2.clear()
  t2.shape('blank')
 t.goto(-150,-150)
 t.down()
 for i in W(-150,151,15):
  t.goto(i,-150)
  t.lt(90);T(300);K(300)
  if i!=150:
   t.up()
   K(16)
   t.write(i//15+11,font=('Arial',8))
   T(16)
   t.down()
  t.rt(90)
 for i in W(-150,151,15):
  t.goto(-150,i)
  T(300);K(300)
  if i!=150:
   t.up()
   K(16)
   t.write(i//15+11,font=('Arial',8))
   T(16)
   t.down()
 while 1:
  inp=I('''1.把一个格子涂上颜色
2.把从 x1,y1(左下角) 到 x2,y2(右上角) 的格子涂上颜色
3.退出
4.x1,y1 到 x2,y2 的那条线涂上颜色
填序号：''')
  if inp=='1':
   x=Q(I('请输入格子的横坐标：'))
   y=Q(I('请输入格子的纵坐标：'))
   c=B(Q(I('请输入颜色(黑:0 蓝:1 绿:2 青:3 红:4 紫:5 黄:6 白:7)：')))
   c=c[:2]+(5-L(c))*'0'+c[2:]
   t.up()
   t.goto((x-1)*15-150,(y-1)*15-150)
   t.down()
   t.fillcolor(Q(c[2]),Q(c[3]),Q(c[4]))
   t.begin_fill()
   for k in W(4):
    T(15);t.lt(90)
   t.end_fill()
  elif inp=='4':
   x1=Q(I('请输入第1个点的横坐标：'))
   y1=Q(I('请输入第1个点的纵坐标：'))
   x2=Q(I('请输入第2个点的横坐标：'))
   y2=Q(I('请输入第2个点的纵坐标：'))
   if x1>x2:
    x1,y1,x2,y2=x2,y2,x1,y1
   c=B(Q(I('请输入颜色(黑:0 蓝:1 绿:2 青:3 红:4 紫:5 黄:6 白:7)：')))
   c=c[:2]+(5-L(c))*'0'+c[2:]
   t.fillcolor(Q(c[2]),Q(c[3]),Q(c[4]))
   for x in W(x1,x2+1):
    try:
     y=Q(y1+((x-x1)/(x2-x1))*(y2-y1))
    except:
     y=y1
    t.up()
    t.goto((x-1)*15-150,(y-1)*15-150)
    t.down()
    t.begin_fill()
    for k in W(4):
     T(15);t.lt(90)
    t.end_fill()
   if y1<=y2:
    for y in W(y1,y2+1):
     try:
      x=Q(x1+((y-y1)/(y2-y1))*(x2-x1))
     except:
      x=x1
     t.up()
     t.goto((x-1)*15-150,(y-1)*15-150)
     t.down()
     t.begin_fill()
     for k in W(4):
      T(15);t.lt(90)
     t.end_fill() 
   else:
    for y in W(y2,y1+1):
     try:
      x=Q(x1+((y-y2)/(y1-y2))*(x2-x1))
      x=x2-(x-x1)
     except:
      x=x1
     t.up()
     t.goto((x-1)*15-150,(y-1)*15-150)
     t.down()
     t.begin_fill()
     for k in W(4):
      T(15);t.lt(90)
     t.end_fill()
  elif inp=='2':
   x1=Q(I('请输入左下角的横坐标：'))
   y1=Q(I('请输入左下角的纵坐标：'))
   x2=Q(I('请输入右上角的横坐标：'))
   y2=Q(I('请输入右上角的纵坐标：'))
   c=B(Q(I('请输入颜色(黑:0 蓝:1 绿:2 青:3 红:4 紫:5 黄:6 白:7)：')))
   c=c[:2]+(5-L(c))*'0'+c[2:]
   t.fillcolor(Q(c[2]),Q(c[3]),Q(c[4]))
   for x in W(x1,x2+1):
    for y in W(y1,y2+1):
     t.up()
     t.goto((x-1)*15-150,(y-1)*15-150)
     t.down()
     t.begin_fill()
     for k in W(4):
      T(15);t.lt(90)
     t.end_fill()
  elif inp=='3':
   break
  else:
   P('输入无效')
  for i in W(5):
   P()
def zip24():
 import turtle as t
 if Gl.do21:
  t2.clear()
  t2.shape('blank')
 Gl.do21=1
 t.clear()
 t.color('black')
 t.up()
 t.goto(0,0)
 t.down()
 t.seth(0)
 t.speed(0)
 t.shape('square')
 t2=t.Turtle()
 t2.up()
 t2.shape('square')
 t2.goto(150,150)
 t2.stamp()
 t2.goto(50,50)
 lsa=['K','J','I','H','G','F','E','D','C','B','A','']
 lsb=['01','02','03','04','05','06','07','08','09','10','11','12','13','']
 keypoint=['G02','J08','E05','H09','D07','F10','B11','C12','A13']
 for i in W(12):
  T(260);K(260)
  t.up()
  t.rt(180);T(20)
  t.write(lsa[i],font=('Arial',16))
  K(20);t.lt(180)
  t.down()
  if i!=11:
   t.lt(90);T(20);t.rt(90)
 t.up()
 t.goto(0,0)
 t.down()
 t.lt(90)
 for i in W(14):
  T(220);K(220)
  t.up()
  t.rt(180);T(20)
  t.write(lsb[i],font=('Arial',9))
  K(20);t.lt(180)
  t.down()
  if i!=13:
   t.rt(90);T(20);t.lt(90)
 t.up()
 t.goto(10,10)
 t.down()
 s='K01'
 x=I('谁先来（电脑先来输入1，你先来输入2）?')
 if x=='2':
  while s!='A13':
   t.color('blue')
   s2=I('你想走到哪里?')
   while not ok2(s,s2):
    s2=I('走不到，请重新输入：')
   s=s2
   t.goto(lsb.index(s2[1:])*20+10,lsa.index(s2[0])*20+10)
   U(0.3)
   for i in keypoint:
    if ok2(s,i):
     t.color('red')
     P('电脑决定走到',i)
     s=i
     t.goto(lsb.index(s[1:])*20+10,lsa.index(s[0])*20+10)
  P('电脑赢了!!!')
 else:
  while 1:
   t.color('red')
   m=1
   for i in keypoint:
    if ok2(s,i):
     P('电脑决定走到',i)
     m=0
     s=i
     t.goto(lsb.index(s[1:])*20+10,lsa.index(s[0])*20+10)
   if m:
    cc=R(1,4)
    if cc==1 and ok2(s,C(O(s[0])-1)+s[1:]):
     P('电脑决定走到',C(O(s[0])-1)+s[1:])
     s=C(O(s[0])-1)+s[1:]
     t.goto(lsb.index(s[1:])*20+10,lsa.index(s[0])*20+10)
    elif cc==2 and ok2(s,s[0]+((Q(s[1:])+1)<10)*'0'+S(Q(s[1:])+1)):
     s=s[0]+((Q(s[1:])+1)<10)*'0'+S(Q(s[1:])+1)
     P('电脑决定走到',s)
     t.goto(lsb.index(s[1:])*20+10,lsa.index(s[0])*20+10)
    else:
     s=C(O(s[0])-1)+((Q(s[1:])+1)<10)*'0'+S(Q(s[1:])+1)
     P('电脑决定走到',s)
     t.goto(lsb.index(s[1:])*20+10,lsa.index(s[0])*20+10)
   if s=='A13':
    P('电脑赢了!!!')
    break
   t.color('blue')
   s2=I('你想走到哪里?')
   while not ok2(s,s2):
    s2=I('走不到，请重新输入：')
   s=s2
   t.goto(lsb.index(s2[1:])*20+10,lsa.index(s2[0])*20+10)
   U(0.3)
   if s=='A13':
    P('你赢了!!!')
    break
 t.up()
def runfunc(m):
 clear()
 if m=='01':
  try:
   q=I('请输入算式（不带=）：')
   q_ev=E(q)
   P('答案是：',q_ev)
  except ZeroDivisionError:
   P('算式中含有除以0，无法计算')
  except:
   P('无法计算')
 elif m=='02':
  while 1:
   inp=I('''1.输出1到x以内的质数
2.输出x到y的质数
3.判断x是不是质数
4.退出
填1,2,3或4：''')
   bl=1
   if inp=='1':
    inp_1=E(I('x? '))
    ls=[]
    for i in W(inp_1+1):
     ls.append(1)
    for inp_el in W(2,inp_1+1):
     if ls[inp_el]==1:
      for k in W(inp_el**2,inp_1+1,inp_el):
       ls[k]=0
    ls2=[]
    for i in W(2,inp_1+1):
     if ls[i]==1:  
      ls2.append(i)
    P(ls2)
    P('计数:',L(ls2))
   elif inp=='2':
    ls=[]
    inp_4_1=E(I('x? '))
    inp_4_2=E(I('y? '))
    ls=[]
    for i in W(inp_4_2+1):
     ls.append(1)
    for inp_el in W(2,inp_4_2+1):
     if ls[inp_el]==1:
      for k in W(inp_el**2,inp_4_2+1,inp_el):
       ls[k]=0
    ls2=[]
    for i in W(2,inp_4_2+1):
     if ls[i]==1 and i>=inp_4_1:  
      ls2.append(i)
    P(ls2)
    P('计数:',L(ls2))
   elif inp=='3':
    inp_2=E(I('x? '))
    if inp_2<=1:
     P('不是')
     for i in W(5):
      P()
     continue
    for cpr_num in W(2,inp_2):
     if inp_2%cpr_num==0:
      P('不是')
      bl=0
      break
    if bl:
     P('是')
   elif inp=='4':
    break
   else:
    P('输入无效')
   for i in W(5):
    P()
 elif m=='03':
  s=E(I('数列首项? '))
  e=E(I('数列末项? '))
  while 1:
   q=I('输入公差回答1,输入个数回答2：')
   if q=='1':
    d=E(I('公差? '))
    n=(e-s)/d+1
   elif q=='2':
    n=E(I('个数? '))
   else:
    P('输入无效')
    continue
   P('答案是',(s+e)*n/2)
   break
 elif m=='04':
  a=E(I('分子? '))
  b=E(I('分母? '))
  i=2
  while i<((a+b)-A(a-b))/2+1:
   if a%i==0 and b%i==0:
    a,b=a/i,b/i
   else:
    i+=1
  P('化简后的分数是：',Q(a),'/',Q(b))
 elif m=='05':
  n=Q(I('要转换的数是? '))
  x=Q(I('要转换成多少进制? '))
  P(fff(n,x))
 elif m=='06':
  q=I('要转换的数是? ')
  nm=Q(I('这个数是多少进制的? '))
  try:
   P(Q(q,nm))
  except:
   P("数据输入错误")
 elif m=='07':
  a=E(I('第一个数是几? '))
  b=E(I('第二个数是几? '))
  P('答案是',math.lcm(a,b))
 elif m=='08':
  zip08()
 elif m=='09':
  ri=0
  ttime=0
  q=Q(I('一共要多少道题?'))
  for cd in [3,2,1]:
   P(cd)
   U(1)
  for n in W(1,q+1):
   a=R(1,100)
   b=R(1,100)
   start=tm.time()
   P('第%i道题：%i+%i='%(n,a,b),end='')
   re_i=Q(I(''))
   end=tm.time()
   ttime+=end-start
   if re_i==a+b:
    P('答对了!')
    ri+=1
   else:
    P('答错了...')
  P('平均时间：%.2f 秒'%(ttime/q))
  P('正确率：',ri/q*100,'%')
  P('分数：%.2f（超过100就算厉害的啦）'%(ri/q*100/(ttime/q/2.8)))
 elif m=='10':
  ttime,tlen=0,0
  ri=0
  q=Q(I('一共要多少道题?'))
  for cd in [3,2,1]:
   P(cd)
   U(1)
  for n in W(1,q+1):
   kwc=r.choice(kw.kwlist)
   P(kwc,end=' 请打出相同的单词:')
   start=tm.time()
   kwcin=I()
   end=tm.time()
   ttime,tlen=ttime+(end-start),tlen+L(kwc)
   if kwcin==kwc:
    ri+=1
  P('打出一个字母用的平均时间：%.2f 秒'%(ttime/tlen))
  P('正确率：',ri/q*100,'%')
  P('T值：%d (作者亲测227)'%(Q(tlen/ttime*ri/q*100)))
 elif m=='11':
  bl=Q(I("你要选一个从0到n的数，让电脑猜你选的是哪个数，请输入n:"))
  q=S(bl)
  nm=2
  ql=L(q)
  q=E(q)
  a=''
  while q!=0:
   w=q%nm
   if w>10:
    w=l[n.index(w)]
   a+=S(w)
   q=Q(q/nm)
  a=a[::-1]
  l=L(a)
  P('请选一个从0到%d的数，记在心里，想好了按回车'%(bl),end='')
  I()
  inp=[]
  ls=[]
  for i in W(0,2**l):
   a=B(i)[2:]
   for i in W(l-L(a)):
    a='0'+a
   ls.append(a)
  for i in W(l):
   tda=[]
   for tn in ls:
    if (tn[0-(i+1)]=='1'):
     tda.append(tn)
   tda2=[]
   for tt in tda:
    tt2=0
    for j in W(L(tt)):
     tt2+=(2**j)*Q(tt[0-(j+1)])
    if tt2<=bl:
     tda2.append(tt2)
   P('这个数在',tda2,'里吗?(否:0,是:1)')
   inp.append(Q(I()))
  it=0
  for i in W(l):
   it+=(2**i)*inp[i]
  P('你选的数是',it)
 elif m=='12':
  a=E(I('第一个数是几? '))
  b=E(I('第二个数是几? '))
  for i in W(1,M(a,b)+1)[::-1]:
   if a%i==0 and b%i==0:
    P('答案是',i)
    break
 elif m=='13':
  ls=[]
  P('''二元一次方程标准形式：
ax+by+c=0
dx+ey+f=0''')
  for i in ['a','b','c','d','e','f']:
   ls.append(E(I(('请输入'+i+':'))))
  a,b,c,d,e,f=ls[0],ls[1],ls[2],ls[3],ls[4],ls[5]
  P('x =',(c*e-b*f)/(b*d-a*e))
  P('y =',(c*d-a*f)/(a*e-b*d))
 elif m=='14':
  P('''一元二次方程标准形式：
ax²+bx+c=0''')
  a=E(I('请输入a：'))
  b=E(I('请输入b：'))
  c=E(I('请输入c：'))
  if (0-(c/a))>=0:
   if b/2/a>=0:
    P('x = sqrt(',(b*b-4*a*c)/(4*a*a),') -',b/2/a,'(',((b*b-4*a*c)/(4*a*a))**0.5-b/2/a,'or',0-((b*b-4*a*c)/(4*a*a))**0.5-b/2/a,')')
   else:
    P('x = sqrt(',(b*b-4*a*c)/(4*a*a),') +',0-(b/2/a),'(',(b*b-4*a*c)/(4*a*a)**0.5-b/2/a,'or',0-((b*b-4*a*c)/(4*a*a))**0.5-b/2/a,')')
  else:
   P('无实数解')
 elif m=='15':
  n=Q(I('请输入想分解的数：'))
  if n<1:
   P('无法分解')
  else:
   ls=[]
   x=2
   while n!=1:
    while n%x==0:
     n/=x
     ls.append(x) 
    x+=1
   P('分解后的列表',ls)
 elif m=='20':
  ls=[0]*10
  qu=Q(I('要计算到小数点后第几位?'))
  co,k,a,b,a1,b1=-1,2,4,1,12,4
  while 1:
   p,q,k=k*k,2*k+1,k+1
   a,b,a1,b1=a1,b1,p*a+q*a1,p*b+q*b1
   d,d1=a/b,a1/b1
   while d==d1:
    if co==-1:
     P(Q(d),end='.')
    else:
     P(Q(d),end='')
    ls[Q(d)]+=1
    co,a,a1=co+1,10*(a%b),10*(a1%b1)
    d,d1=a/b,a1/b1
    if co==qu:
     break
   if co==qu:
    break
  P('\n数字个数，包括个位的3:')
  for i in W(10):
   P(i,':',ls[i],'个')
 elif m=='21':
  zip21()
 elif m=='22':
  zip22()
 elif m=='23':
  if not(Sz.ls[0]):
   P('你似乎可能也许大概没开声音...?')
   U(0.8)
   return
  P("键盘上q-u,z-k分别对应低音1到高音1,键盘上的2,3,5,6,7,s,d,g,h,j分别对应低音1到高音1间的所有升降音,空格代表空拍")
  a=Dt.a23
  s=I()
  for j in s:
   if j!=' ':
    x=Q(245*2**(a.index(j)/12))
    P(j)
    winsound.Beep(x,200)
    for i in W(4000000):
     pp=1
   else:
    for i in W(6000000):
     pp=1
 elif m=='24':
  zip24()
 elif m=='26':
  P('电脑将随机生成一个n位数，你每次猜一个n位数。电脑会告诉你对了几个数字。')
  n=Q(I('n是几?'))
  x=S(R(10**(n-1),10**n-1))
  a=I('你猜是几?')
  while a!=x:
   n1,n2=0,0
   for i in W(n):
    n1+=Q(a[i]==x[i])
    n2+=Q(a[i] in x and a[i]!=x[i])
   P('位置且数字正确%d个，仅数字正确%d个。'%(n1,n2))
   a=I('你猜是几?')
  P('猜对了!')
 elif m=='27':
  score=0
  block=Dt.block27
  blockcol=Dt.blockcol27
  a=[]
  for i in W(20):
   a.append([0]*20)
  f=15
  while f:
   for c in W(1,9):
    P('.',end='')
   f-=1
   P()
  while 1:
   typ=R(1,9)
   score+=blockcol[typ]*2
   P('方块:')
   for i in W(3):
    for j in W(3):
     if block[typ][i][j]:
      P('#',end='')
     else:
      P('.',end='')
    P()
   col=Q(I('放在第几列?'))
   while col+blockcol[typ]>9:
    col=Q(I('无效列数,请重新输入:'))
   clear()
   brk=1
   place=15
   while place:
    for i in W(3):
     for j in W(3):
      if a[place-i+2][col+j] and block[typ][i][j]:
       brk=0
       break
     if brk==0:
      break
    if brk==0:
     break
    place-=1
   place+=1
   for i in W(3):
    for j in W(3):
     if block[typ][i][j]:
      a[place-i+2][col+j]=block[typ][i][j]
   f=15
   while f:
    bl=1
    for k in W(1,9):
     if a[f][k]==0:
      bl=0
    if bl:
     score+=12
     for x in W(f,15):
      for c in W(1,9):
       a[x][c]=a[x+1][c]
     a[15]=[0]*20
    f-=1
   f=15
   while f:
    for c in W(1,9):
     if a[f][c]:
      P('#',end='')
     else:
      P('.',end='')
    f-=1
    P()
   bl=0
   for k in W(1,9):
    if a[15][k]==1:
     bl=1
   if bl:
    P('分数:',score)
    P('游戏结束')
    break
 elif m=='28':
  trm=I('0为普通计时，1为倒计时：')
  if trm=='0':
   P('a为开始计时，b为结束计时，c为退出')
   tr=0
   c=I('请输入指令:')
   while c!='c':
    if c=='a':
     tr=tm.time()
    if c=='b':
     P('%.2f s'%(tm.time()-tr))
    c=I('请输入指令:')
  if trm=='1':
   t=Q(I('倒计时多少秒?'))
   while t>0:
    P(t,'s')
    t-=1
    U(1)
 elif m=='29':
  x=I('电脑显示一个"[回车]"后请立即按回车，有5~10s的准备时间，现在按回车开始:')
  U(R(5,10))
  s=tm.time()
  I('[回车]')
  e=tm.time()
  P('反应速度:%.2f s'%(e-s))
 elif m=='30':
  x=Q(I('随机下限:'))
  y=Q(I('随机上限:'))
  P(R(x,y-1)+r.random())
 elif m=='31':
  n=Q(I("多少个数据?"))
  sm=0
  for i in W(n):
   sm+=E(I('数据：'))
  P("%.2f"%(sm/n))
 elif m=='32':
  ls=[]
  f=[]
  lei=[]
  for i in W(1,18):
   t1=[]
   t2=[]
   for j in W(1,18):
    t1.append(R(0,3)==0)
    t2.append(0)
   ls.append(t1)
   f.append([0]*18)
   lei.append(t2)
  for i in W(1,9):
   for j in W(1,10-i):
    f[i][j]=1
    ls[i][j]=0
  tot=0
  for i in W(0,17):
   ls[i][0]=0
   ls[i][16]=0
   ls[0][i]=0
   ls[16][i]=0
  for i in W(1,16):
   for j in W(1,16):
    tot+=ls[i][j]
    for x in W(3):
     for y in W(3):
      lei[i][j]+=ls[i+x-1][j+y-1]
    if ls[i][j]==1:
     lei[i][j]=-1
  P('一共%d个雷'%(tot))
  while 1:
   cnt=0
   P('  123456789012345')
   for i in W(1,16):
    P(i%10,end=' ')
    for j in W(1,16):
     if f[i][j]:
      if ls[i][j]==0:
       P(lei[i][j],end='')
      else:
       P('/',end='')
      pass
     else: 
      cnt+=1
      P('#',end='')
      pass
    P()
   if cnt==0:
    P('通关!')
    break
   typ=I('请输入指令类型(0=点开,1=标记为雷)')
   x=Q(I('纵坐标'))
   y=Q(I('横坐标'))
   if typ=='0':
    if ls[x][y]==1:
     P('你输了!')
     break
    else:
     f[x][y]=1
   else:
    if ls[x][y]==0:
     P('你输了!')
     break
    else:
     f[x][y]=1
 elif m=='33':
  n=Q(I("打印多少行"))
  while n<=0:
   n=Q(I("不能小于1哦!请再次输入"))
  l=[]
  for i in W(1,n+1):
   l.append(1)
   if i>2:
    for j in W(2,i):
     j=i-j
     l[j]=l[j]+l[j-1]
   for j in W(i):
    if j==i-1:
     P(l[j])
    else:
     P(l[j],end=" ")
 elif m=='35':
  map1,map2=Dt.map135,Dt.map235
  le=['w','a','s','d']
  dx=[-1,0,1,0]
  dy=[0,-1,0,1]
  x,y=0,0
  mp=1
  while x!=4 or y!=7:
   for i in W(5):
    for j in W(8):
     if x==i and y==j and mp==1:
      P('i',end='')
     elif map1[i][j]==2:
      P('#',end='')
     elif map1[i][j]==0:
      P('.',end='')
     elif map1[i][j]==1:
      P('*',end='')
    P()
   P()
   for i in W(5):
    for j in W(8):
     if x==i and y==j and mp==2:
      P('i',end='')
     elif map2[i][j]==0:
      P('.',end='')
     else:
      P('*',end='')
    P()
   c=I('wasd移动位置,c切换地图')
   clear()
   if c=='c':
    mp=3-mp
    if mp==1:
     if map1[x][y]==1:
      mp=2
      P('失败')
    else:
     if map2[x][y]==1:
      mp=1
      P('失败')
   else:
    dxn=dx[le.index(c)]
    dyn=dy[le.index(c)]
    if mp==1:
     if map1[x+dxn][y+dyn]==1:
      P('失败')
     else:
      x+=dxn
      y+=dyn
    else:
     if map2[x+dxn][y+dyn]==1:
      P('失败')
     else:
      x+=dxn
      y+=dyn
  P('挑战成功!')
 elif m=='38':
  map1=Dt.map138
  le=['w','a','s','d']
  dx=[-1,0,1,0]
  dy=[0,-1,0,1]
  x,y=0,0
  while x!=14 or y!=14:
   for i in W(15):
    for j in W(15):
     if x==i and y==j:
      P('i',end='')
     elif A(x-i)<2 and A(y-j)<2 and map1[i][j]==1:
      P('*',end='')
     elif A(x-i)<2 and A(y-j)<2 and map1[i][j]==0:
      P('.',end='')
     elif A(x-i)<2 and A(y-j)<2 and map1[i][j]==2:
      P('#',end='')
     else:
      P('?',end='')
    P()
   c=I('wasd移动位置')
   clear()
   dxn=dx[le.index(c)]
   dyn=dy[le.index(c)]
   if map1[x+dxn][y+dyn]==1:
    pass
   else:
    x+=dxn
    y+=dyn
  P('挑战成功!')
 elif m=='39':
  x=Q(I('几行?'))
  y=Q(I('几列?'))
  n=Q(I('几个障碍物?'))
  bc=[]
  for i in W(n):
   bc.append(I('障碍物位置(请填写编号)?'))
  if bc==['D06'] and x==9 and y==11:
   P('\n我是人工智能，不是人工智障!别想作弊')
   return
  if (bc==['D08','I03'] or bc==['I03','D08']) and x==11 and y==13:
   P('\n我是人工智能，不是人工智障!别想作弊')
   return
  ls=[]
  for i in W(x+1):
   t=[]
   for j in W(y+1):
    t.append(0)
   ls.append(t)
  for i in W(x,0,-1):
   for j in W(y,0,-1):
    le=C(O('A')+x-i)
    nu='0'*(1-j//10)+S(j)
    if le+nu in bc:
     continue
    u=1
    for ti in W(i+1,x+1):
     let=C(O('A')+x-ti)
     if let+nu in bc:
      break
     if ls[ti][j]:
      u=0
    rp=1
    for tj in W(j+1,y+1):
     nut='0'*(1-tj//10)+S(tj)
     if le+nut in bc:
      break
     if ls[i][tj]:
      rp=0
    ur=1
    for dur in W(1,M(x-i,y-j)+1):
     let=C(O('A')+x-(i+dur))
     nut='0'*(1-(j+dur)//10)+S(j+dur)
     if let+nut in bc:
      break
     if ls[i+dur][j+dur]:
      ur=0
    if u and rp and ur:
     ls[i][j]=1
  for i in W(x,0,-1):
   for j in W(1,y+1):
    if ls[i][j]:
     P('# ',end='')
    else:
     P('* ',end='')
   P()
  P('上面图中#是关键点，你需要尽量去走那些点。')
 elif m=='40':
  P('\n')
  corr=R(1,16)
  ch=list(W(17))
  cl=ch[:corr]+ch[corr+1:]
  num=[0]
  while L(ch)>1:
   x=R(1,L(ch)-1)
   num.append(ch[x])
   ch=ch[:x]+ch[x+1:]
  vis=[0]*17
  rw=Q(I('从第几组开始(1~4)?'))
  nownum=0
  while nownum!=corr:
   P()
   P('第%d组'%(rw))
   for i in W(4):
    P('第%d个:'%(i+1),end='')
    if vis[(rw-1)*4+i+1]:
     P(num[(rw-1)*4+i+1])
    else:
     P('?')
   P()
   c=Q(I('第几个?'))
   nownum=(rw-1)*4+c
   if nownum==corr:
    break
   x=cl[R(1,L(cl)-1)]
   P()
   P('-====================-')
   P('编号:',num[nownum])
   P('提醒: %d组%d个不是答案'%((x-1)//4+1,(x-1)%4+1))
   P('-====================-')
   P()
   rw=num[nownum]%4+1
   vis[nownum]=1
  P('猜对了!!')
  P('彩蛋\n话说那谁遇到了一道生物题，它不知道√念什么，看看这道题吧!')
  P('A.根 B.sqrt C.平方根 D.根儿豪')
 elif m=='42':
  n=L(Sz.ls)
  for i in W(n):
   read(i)
  N('Meatpi_Settings.dat','w').write(S(Sz.ls))
 elif m=='43':
  N('Meatpi_Data.dat','w').write('')
  N('Meatpi_Settings.dat','w').write('')
  exit()
 elif m=='44':
  score=0
  ops=['w','a','s','d']
  inbound=lambda x,y:(x>=0 and x<4 and y>=0 and y<4)
  mp=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
  dx=[-1,0,1,0]
  dy=[0,-1,0,1]
  while 1:
   clear()
   ok=0
   for i in W(4):
    for j in W(4):
     if mp[i][j]==0:
      ok=1
   if not ok:
    P('游戏结束，得分:',score)
    break
   x=R(0,3)
   y=R(0,3)
   while mp[x][y]!=0:
    x=R(0,3)
    y=R(0,3)
   mp[x][y]=2-Q(R(0,22)!=0);
   for i in W(4):
    for j in W(4):
     P(C(mp[i][j]+O('@')),end='')
    P()
   P()
   op=I('Operation(q 4 quit):')
   if op=='q':
    P('游戏结束，得分:',score)
    break
   while not(op in ops):
    op=I('ERROR Please try again:')
   opn=ops.index(op)
   if opn%2:
    for i in W(4):
     nowls=[3,2,1,0]
     if opn/2:
      nowls=[0,1,2,3]
     for j in nowls:
      u,v=i,j;
      if mp[u][v]==0:
       continue
      while 1:
       u,v=u+dx[opn],v+dy[opn];
       if (not inbound(u,v)) or (mp[u][v]!=0 and mp[u][v]!=mp[u-dx[opn]][v-dy[opn]]):
        break
       elif mp[u][v]==0:
        mp[u][v]=mp[u-dx[opn]][v-dy[opn]]
        mp[u-dx[opn]][v-dy[opn]]=0
       else:
        mp[u][v]=mp[u][v]+1
        mp[u-dx[opn]][v-dy[opn]]=0
        break
   else:
    for j in W(4):
     nowls=[3,2,1,0]
     if opn/2:
      nowls=[0,1,2,3]
     for i in nowls:
      u,v=i,j;
      if mp[u][v]==0:
       continue
      while 1:
       u,v=u+dx[opn],v+dy[opn];
       if (not inbound(u,v)) or (mp[u][v]!=0 and mp[u][v]!=mp[u-dx[opn]][v-dy[opn]]):
        break
       elif mp[u][v]==0:
        mp[u][v]=mp[u-dx[opn]][v-dy[opn]]
        mp[u-dx[opn]][v-dy[opn]]=0
       else:
        mp[u][v]=mp[u][v]+1
        mp[u-dx[opn]][v-dy[opn]]=0
        break
   score+=1
 elif m=='47':
  ls=Dt.et47
  ls=ls[0]
  q=I('加密(1)/解密(2)?')
  if q=='1':
   s=I('请输入:')
   key=''
   for i in W(L(s)):
    key+=C(O('a')+R(0,15))
   P('你的密码是 '+key)
   outp=''
   for i in W(L(s)):
    outp+=fff(O(s[i])+ls[i%16][O(key[i])-O('a')],8)+'8'
   P(fff(Q(outp,9),16))
  else:
   s=fff(Q(I('请输入:'),16),9)
   key=I('密码:')
   now=''
   cnt=0
   for i in W(L(s)):
    if s[i]!='8':
     now+=S(s[i])
    else:
     P(C(Q(now,8)-ls[cnt%16][O(key[cnt])-O('a')]),end='')
     cnt+=1
     now=''
   P()
 elif m=='50':
  P('数学老师狂喜')
  for i in W(5):
   a,b=R(1,6),R(1,6)*(Q(R(0,1)>1)*2-1)
   c,d=R(1,6),R(1,6)*(Q(R(0,1)>1)*2-1)
   q,w,e=a*c,a*d+b*c,b*d
   P('(ax+b)(cx+d)=%dx2+%dx+%d'%(q,w,e))
   aa,bb,cc,dd=E(I('a?')),E(I('b?')),E(I('c?')),E(I('d?'))
   if aa*cc==q and aa*dd+bb*cc==w and bb*dd==e:
    P('AC')
   else:
    P('WA')
    P('Correct Answer:',a,b,c,d)
 elif m=='51':
  s=Sz.ls[4]
  k=0
  for i in s:
   k+=O(i)
  k%=100
  P('你的幸运数字是：'+'0'*(k<10)+S(k))
 elif m=='57':
  k=Q(I('定时多少秒后开始炸骗?'))
  P('倒计时中...')
  U(k)
  webr.open('https://www.bilibili.com/video/BV1VB4y197c1/')
 elif m=='58':
  while 1:
   I('Press Enter to get the current meatpi standard time ')
   P('\n')
   P(mst())
 elif m=='60':
  play60()
 elif m=='61':
  s=r'''\
while 1:
    print("'''+Sz.ls[4]+'''\
 is polite :)")'''
  N('creeper.py','w').write(s);
  P('哦，你的文件夹/桌面里貌似多了什么东西 :)')
 elif m=='62':
  P('此算法仅能加密小写字母和空格，请确认')
  wheel=Dt.wheel62
  refl=Dt.refl62
  s=I('加密或解密内容? ')
  c=I('密码(0~4的排列加上5个小写字母或空格,比如13420kkksc)?')
  new_wheel=[]
  for i in W(5):
   new_wheel.append(wheel[O(c[i])-O('0')])
   ls1=new_wheel[i][getord62(c[i+5]):]
   ls2=new_wheel[i][0:getord62(c[i+5])]
   ls1.extend(ls2)
   new_wheel.append(ls1)
  for ch in s:
   c=add62(c)
   new_wheel=[]
   for i in W(5):
    new_wheel.append(wheel[O(c[i])-O('0')])
    ls1=new_wheel[i][getord62(c[i+5]):]
    ls2=new_wheel[i][0:getord62(c[i+5])]
    ls1.extend(ls2)
    new_wheel.append(ls1)
   res=ch
   for i in new_wheel:
    res=getchr62(i[getord62(res)])
   res=getchr62(refl[getord62(res)])
   for i in new_wheel[::-1]:
    res=getchr62(i.index(getord62(res)))
   P(res,end='')
  P()
 elif m=='63':
  s=E(I('请输入该无理数的平方(例:阿姆斯特朗常数为242): '))
  e=E(I('计算到小数点后的位数: '))
  ei=0
  x=Q(s**0.5)
  P(S(x)+'.',end='')
  while ei<e:
   ei,s,x=ei+1,s*100,x*10
   while x**2<=s:
    x+=1
   x-=1
   P(S(x%10),end='')
  P()
 elif m=='64' or m=='65':
  empty88=[[0]*8,[0]*8,[0]*8,[0]*8,[0]*8,[0]*8,[0]*8,[0]*8]
  empty55=[[0]*5,[0]*5,[0]*5,[0]*5,[0]*5]
  if m=='64':
   mp64=empty55
   temp=5
   cols=3
  else:
   mp64=empty88
   temp=8
   cols=7
  for i in W(1,cols+1):
   for k in W(Q((temp*temp-1)/cols)):
    u,v=R(0,temp-1),R(0,temp-1)
    while mp64[u][v]!=0:
     u,v=R(0,temp-1),R(0,temp-1)
    mp64[u][v]=i
  while 1:
   ok=1
   clear()
   col=[' ','A','B','C']
   if m=='65':
    col=[' ','A','B','C','D','E','F','G']
   for u in W(temp):
    for v in W(temp):
     P(col[mp64[u][v]],end='')
    P()
   ops=['w','a','s','d']
   dx,dy=[-1,0,1,0],[0,-1,0,1]
   op=I('Operation:')
   while not(op in ops):
    op=I('ERROR Please try again:')
   done=0
   for u in W(temp):
    for v in W(temp):
     if mp64[u][v]==0:
      done=1
      if 0<=u-dx[ops.index(op)]<temp and 0<=v-dy[ops.index(op)]<temp:
       mp64[u][v],mp64[u-dx[ops.index(op)]][v-dy[ops.index(op)]]=mp64[u-dx[ops.index(op)]][v-dy[ops.index(op)]],mp64[u][v]
      break
    if done:
      break
   for i in W(1,cols+1):
    done=0
    for u in W(temp):
     for v in W(temp):
      if mp64[u][v]==i:
       if m=='64':
        c64.vis=empty55
       else:
        c64.vis=empty88
       ok=ok and (dfs64(mp64,u,v,i,m)==Q((temp*temp-1)/cols))
       done=1
      break
     if done:
      break
   if ok:
    P('You win!')
    break
 elif m=='66':
  modes=[]
  for i in W(14):
   modes.append(R(0,3))
  for i in [5,4,3,2,1,0]:
   for j in [5,4,3,2,1,0]:
    clear()
    op66(modes,i,j,1,1)
    U(1)
  x,y=R(6,9),R(6,9)
  clear()
  res=op66(modes,x,y,0,1)
  P()
  resi=Q(I('What is this number?'))
  xi=resi//10
  yi=resi%10
  if res==op66(modes,xi,yi,0,0):
   P('correct!')
  else:
   P('wrong... the answer is',x*10+y)
 elif m=='67':
  N('Meatpi_Exceptions.txt','w').write('')
 elif m=='69':
  emp66=[[0]*6,[0]*6,[0]*6,[0]*6,[0]*6,[0]*6]
  mp64=emp66
  for i in W(1,7):
   for k in W(Q(i<5)*8+Q(i>2)*1):
    u,v=R(0,5),R(0,5)
    while mp64[u][v]!=0:
     u,v=R(0,5),R(0,5)
    mp64[u][v]=i
  while 1:
   ok=1
   clear()
   col=[' ','A','B','C','D','+','-']
   for u in W(6):
    for v in W(6):
     P(col[mp64[u][v]],end='')
    P()
   ops=['1','2','3','4','q','w','e','r']
   dx,dy=[1,2,2,1,-1,-2,-2,-1],[2,1,-1,-2,2,1,-1,-2]
   op=I('Operation(e.g. +2 -e):')
   while not(op[1] in ops) or not(op[0] in ['+','-']):
    op=I('ERROR Please try again:')
   done=0
   for u in W(6):
    for v in W(6):
     if mp64[u][v]==col.index(op[0]):
      done=1
      if 0<=u-dx[ops.index(op[1])]<8 and 0<=v-dy[ops.index(op[1])]<8:
       mp64[u][v],mp64[u-dx[ops.index(op[1])]][v-dy[ops.index(op[1])]]=mp64[u-dx[ops.index(op[1])]][v-dy[ops.index(op[1])]],mp64[u][v]
      break
    if done:
      break
   for i in W(1,5):
    done=0
    for u in W(6):
     for v in W(6):
      if mp64[u][v]==i:
       c64.vis=emp66
       ok=ok and (dfs64(mp64,u,v,i,m)==8+Q(i>2)*1)
       done=1
      break
     if done:
      break
   if ok:
    P('You win!')
    break
 elif m=='70':
  map70=[]
  for i in W(4):
   map70.append([0]*4);
  for i in W(4):
   x=R(0,1)
   for u in W((i//2)*2,(i//2+1)*2):
    for v in W((i%2)*2,(i%2+1)*2):
     map70[u][v]+=x
  for i in W(16):
   x=R(0,1)
   map70[i//4][i%4]+=x
  x,y,steps=R(0,3),R(0,3),100
  while 1:
   map70[x][y]+=1
   steps-=1
   for i in W(4):
    for j in W(4):
     if i==x and j==y:
      P(C(O('A')+map70[i][j]),end='')
     else:
      P(C(O('a')+map70[i][j]),end='')
    P()
   op=I('Operation(wasd):')
   ops=['w','a','s','d']
   dx,dy=[-1,0,1,0],[0,-1,0,1]
   while not(op in ops):
    op=I('ERROR Please try again:')
   clear()
   vx,vy=x+dx[ops.index(op)],y+dy[ops.index(op)]
   if vx<0 or vx>3 or vy<0 or vy>3:
    steps+=1
    continue
   x,y,ok=vx,vy,1
   for i in W(4):
    for j in W(4):
     ok=ok and map70[i][j]==map70[0][0]
   if ok:
    break
  P('Score:',S(steps))
 elif m=='71':
  playhf(tm)
 else:
  pass
I('Initialization finished.\nPress Enter to continue')
clear()
def main():
 if Sz.ls[0]:
  winsound.Beep(360,200)
  winsound.Beep(286,200)
 try:
  Gl.do21,Gl.ss=0,''
  while 1:
   Gl.run52=0
   if nowin:
    Sz.ls[0]=0
   P('<<',tm.asctime(tm.localtime(tm.time())),'>>')
   P('<<',6*' ',mst(),6*' ','>>')
   P('      v12 (Nov 07, 2022)')
   P('''1> Caculations
2> Functions
3> Entertainments
4> System''')
   bm=I('\n>> ')
   clear()
   if bm=='1':
    P('''01> 普通计算器
02> 质数判断/生成器
03> 等差数列求和
04> 化简分数
05> 十进制变几进制
06> 几进制变十进制
07> 最小公倍数
12> 最大公因数
13> 解二元一次方程
14> 解一元二次方程
15> 质因数分解
20> 计算π
30> 生成随机数
31> 计算平均数
33> 帕斯卡三角形
63> 平方根式无理数计算器''')
   if bm=='2':
    P('''08> 算24
22> 画板
23> 音乐大师
28> 计时器
29> 测试反应速度
39> 坑碟游戏解析
47> 加密解密2
51> 计算幸运数字
57> 定时炸骗
58> Meatpi标准时间
61> creeper.py
62> 加密解密3''')
   if bm=='3':
    P('''09> 计算游戏
10> 打字游戏
11> 猜数游戏1
21> 坑碟游戏经典版
24> 坑碟游戏升级版
26> 猜数游戏2
27> 俄罗斯方块简化版
32> 扫雷
35> 2层迷宫(体验版)
38> 失明迷宫(体验版)
40> FJ的卡牌游戏
44> 2048
50> 因式分解小练习
64> 颜色华容道(3*8)
65> 颜色华容道(7*9)
66> FJ的手表
69> 根了个5
70> 铁板
71> 推箱子
''')
   if bm=='4':
    P('''42> 设置
43> 恢复出厂设置
67> 清理日志
''')
   m=I('\n>>> ')
   runfunc(m)
   P()
   U(Sz.ls[3])
   P(Gl.ads[R(0,L(Gl.ads)-2)])
   I('请按回车继续')
   clear()
 except KeyboardInterrupt:
  clear()
  main()
 except Exception as exc:
  if Sz.ls[5]:
   N('Meatpi_Exceptions.txt','a').write(tm.asctime(tm.localtime(tm.time()))+' '+S(type(exc))+' '+S(exc)+'\n')
  clear()
  main()
if __name__=='__main__':
 main()
else:
 raise ImportError('meatpi cannot be imported')