import random
import math

ctN=['',('ひとつ','ついたち'),('ふたつ','ふつ'),('みっつ','みっ'),('よっつ','よっ'),('いつつ','いつ'),('むっつ','むい'),('ななつ','なの'),('やっつ','よう'),('ここのつ','ここの'),('とお',''),('はつか','')]
numberN=['',('いち','いっ'),('に',''),('さん',''),('よん','し','よ'),('ご',''),('ろく','ろっ'),('なな','しち'),('はち','はっ'),('きゅう','く'),('じゅう','じっ')]
hundredN=['ひゃく','びゃく','ぴゃく']
thausandN=['せん','ぜん']
TenThausandN='まん'

yearE='ねん'
monthE='がつ'
monthCt1E='かげつ'
monthCt2E='かげつけん'
dayE=['か','にち']
dayCt1E=['にち','か']
datCt2E=['じゅう','かん']
weekCtE='じゅうかん'
OclockE='じ'
minuteE=['ぷん','ふん']
secondE='びょう'
pos=['まえ','ごろ','ぐらい']



def check():
    if s==answer:
        print('correct')
    else:
        print(answer)

def count100(r):
    Ct1000=math.floor(r/1000)
    Ct100=math.floor((r-Ct1000*1000)/100)
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

def count1000(r):
    Ct1000=math.floor(r/1000)
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

s=input()

while s!='q':
    qTypeList=['ct','number','year','month','monthCt','monthCt2','day','weekCt','Oclock']
    p=1
    r1=random.randint(0,p)
    qType=qTypeList[r1]
    question=''
    answer=''

    if qType=='ct':
        p=10
        r=random.randint(1,p)
        question=str(r)+'(個)'
        answer=ctN[r][0]
        print(question)
        s=input()
        check()

    elif qType=='number':
        p=9999
        r=random.randint(1,p)
        question=r
        print(question)
        Ct10=0
        Ct100=0
        Ct1000=0
        CtRm=r%10

        if question<=10:
            answer=numberN[r][0]

        elif question>10 and question<20:
            answer=numberN[9][0]+numberN[CtRm][0]

        elif question>=20 and question<99:
            Ct10=math.floor(r/10)
            answer=numberN[Ct10][0]+'じゅう'+numberN[CtRm][0]

        elif question>=100 and question<1000:
            Ct100=math.floor((r-Ct1000*1000)/100)
            Ct10=math.floor((r-Ct100*100)/10)
            if CtRm==0:
                answer=count100(r)+numberN[Ct10][0]+'じゅう'
            elif CtRm==0 and Ct10==1:
                answer=count100(r)+'じゅう'
            elif Ct10==0:
                answer=count100(r)+numberN[CtRm][0]
            else:
                answer=count100(r)+numberN[Ct10][0]+'じゅう'+numberN[CtRm][0]

        elif question>=1000 and question<10000:
            Ct1000=math.floor(r/1000)
            Ct100=math.floor((r-Ct1000*1000)/100)
            Ct10=math.floor((r-Ct1000*1000-Ct100*100)/10)
            if CtRm==0:
                answer=count1000(r)+count100(r)+numberN[Ct10][0]+'じゅう'
            elif CtRm==0 and Ct10==1:
                answer=count1000(r)+count100(r)+'じゅう'
            elif Ct10==0:
                answer=count1000(r)+count100(r)+numberN[CtRm][0]
            else:
                answer=count1000(r)+count100(r)+numberN[Ct10][0]+'じゅう'+numberN[CtRm][0]

        s=input()
        check()