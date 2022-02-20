import random
import math

ctN=[('まる',''),('ひとつ','ついたち'),('ふたつ','ふつ'),('みっつ','みっ'),('よっつ','よっ'),('いつつ','いつ'),('むっつ','むい'),('ななつ','なの'),('やっつ','よう'),('ここのつ','ここの'),('とお',''),('はつ','')]
numberN=[('れい',''),('いち','いっ'),('に',''),('さん',''),('よん','し','よ'),('ご',''),('ろく','ろっ'),('なな','しち'),('はち','はっ'),('きゅう','く'),('じゅう','じっ')]
hundredN=['ひゃく','びゃく','ぴゃく']
thausandN=['せん','ぜん']

yearU='ねん'
monthU='がつ'
monthCt1U='かげつ'
dayU=['か','にち']
datCtU=['じゅう','かん']
weekCtU='じゅうかん'
OclockU='じ'
minuteU=['ぷん','ふん']
secondU='びょう'
pos=['まえ','ごろ','ぐらい']


def check(answer,s):
    if s==answer:
        print('Correct')
    else:
        print('W/A, the answer is',answer)

def count10(Ct10):
    st10=''
    if Ct10==0:
        st10=''
    elif Ct10==1:
        st10=numberN[10][0]
    else:
        st10=numberN[Ct10][0]+numberN[10][0]
    return st10

def count100(Ct100):
    st100=''
    if Ct100==3:
        st100=numberN[Ct100][0]+hundredN[1]
    elif Ct100==6 or Ct100==8:
        st100=numberN[Ct100][1]+hundredN[2]
    elif Ct100==1:
        st100=hundredN[0]
    elif Ct100==0:
        st100=''
    else:
        st100=numberN[Ct100][0]+hundredN[0]
    return st100

def count1000(Ct1000):
    st1000=''
    if Ct1000==3:
        st1000=numberN[Ct1000][0]+thausandN[1]
    elif Ct1000==8:
        st1000=numberN[Ct1000][1]+thausandN[0]
    elif Ct1000==1:
        st1000=thausandN[0]
    elif Ct1000==0:
        st1000=''
    else:
        st1000=numberN[Ct1000][0]+thausandN[0]
    return st1000

def QuizCt():
    p=10
    r=random.randint(0,p)
    question=str(r)+'(個)'
    answer=ctN[r][0]
    print(question)
    s=input()
    check(answer,s)

def QuizNumber():
    p=9999
    r=random.randint(0,p)
    question=r
    Ct1000=math.floor(r/1000)
    Ct100=math.floor((r-Ct1000*1000)/100)
    Ct10=math.floor((r-Ct1000*1000-Ct100*100)/10)
    CtRm=r%10

    if question<10:
        answer=numberN[r][0]

    elif question>=10 and question<100:
        answer=count10(Ct10)+numberN[CtRm][0]

    elif question>=100 and question<1000:
        if CtRm==0:
            answer=count100(Ct100)+count10(Ct10)
        else:
            answer=count100(Ct100)+count10(Ct10)+numberN[CtRm][0]

    elif question>=1000 and question<10000:
        if CtRm==0:
            answer=count1000(Ct1000)+count100(Ct100)+count10(Ct10)
        else:
            answer=count1000(Ct1000)+count100(Ct100)+count10(Ct10)+numberN[CtRm][0]
    print(question)
    s=input()
    check(answer,s)

def QuizYear():
    p=10
    r=random.randint(1,p)
    question=str(r)+'年'
    if r==4 or r==9 or r==7:
        answer=numberN[r][1]+yearU
    else:
        answer=numberN[r][0]+yearU
    print(question)
    s=input()
    check(answer,s)

def QuizMonth():
    p=12
    r=random.randint(1,p)
    question=str(r)+'月'
    if r==4 or r==9 or r==7:
        answer=numberN[r][1]+monthU
    elif r==11:
        answer=numberN[10][0]+numberN[1][1]+monthU
    elif r==12:
        answer=numberN[10][0]+numberN[2][0]+monthU
    else:
        answer=numberN[r][0]+monthU
    print(question)
    s=input()
    check(answer,s)

def QuizMonthCt1():
    p=12
    r=random.randint(1,p)
    question=str(r)+'か月'
    if r==1 or r==6 or r==10:
        answer=numberN[r][1]+monthCt1U
    elif r+1==11:
        answer=numberN[10][0]+numberN[1][1]+monthCt1U
    elif r+1==12:
        answer=numberN[10][0]+numberN[2][0]+monthCt1U
    else:
        answer=numberN[r][0]+monthCt1U
    print(question)
    s=input()
    check(answer,s)

def QuizDay():
    p=31
    r=random.randint(1,p)
    question=str(r)+'日'
    kaList=[2,3,4,5,6,7,8,9]
    diffNumList=[17,27,19,29]
    Ct10=math.floor(r/10)
    CtRm=r%10
    if r==1:
        answer=ctN[1][1]
    elif r in kaList:
        answer=ctN[r][1]+dayU[0]
    elif r==10:
        answer=ctN[r][0]+dayU[0]
    elif r==20:
        answer=ctN[11][0]+dayU[0]
    elif r==14 or r==24:
        answer=count10(Ct10)+ctN[CtRm][1]+dayU[0]
    elif r in diffNumList:
        answer=count10(Ct10)+numberN[CtRm][1]+dayU[1]
    elif CtRm==0:
        answer=count10(Ct10)+dayU[1]
    else:
        answer=count10(Ct10)+numberN[CtRm][0]+dayU[1]
    print(question)
    s=input()
    check(answer,s)

def QuizDayCt1():
    p=10
    r=random.randint(1,p)
    question=str(r)+'日(量)'
    if r==1:
        answer=numberN[1][0]+dayU[1]
    elif r==10:
        answer=ctN[r][0]+dayU[0]
    else:
        answer=ctN[r][1]+dayU[0]

    print(question)
    s=input()
    check(answer,s)

def QuizDayCt2():
    p=10
    r=random.randint(1,p)
    if r==1:
        question=str(r)+'日中'
    else:
        question=str(r)+'日間'

    if r==1:
        answer=numberN[1][0]+dayU[1]+datCtU[0]
    elif r==10:
        answer=ctN[r][0]+datCtU[1]
    else:
        answer=ctN[r][1]+dayU[0]+datCtU[1]

    print(question)
    s=input()
    check(answer,s)

def QuizWeekCt():
    p=10
    r=random.randint(1,p)
    question=str(r)+'週間'

    if r==1 or r==8 or r==10:
        answer=numberN[r][1]+weekCtU
    else:
        answer=numberN[r][0]+weekCtU

    print(question)
    s=input()
    check(answer,s)

print('Press ENTER to start, or q to quit.')
s=input()

while s!='q':
    qTypeList=['ct','number','year','month','monthCt','day','dayCt1','dayCt2','weekCt','time']
    p=8
    r=random.randint(0,p)
    qType=qTypeList[r]

    if qType=='ct':
        QuizCt()
    elif qType=='number':
        QuizNumber()
    elif qType=='year':
        QuizYear()
    elif qType=='month':
        QuizMonth()
    elif qType=='monthCt':
        QuizMonth()
    elif qType=='day':
        QuizDay()
    elif qType=='dayCt1':
        QuizDayCt1()
    elif qType=='dayCt2':
        QuizDayCt2()
    elif qType=='weekCt':
        QuizWeekCt()

    s=input()