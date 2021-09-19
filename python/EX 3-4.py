def comma(gold):
    times=0
    gold=str(gold)
    if len(gold)<4:
        return gold
    li=[]

    for i in range(len(gold)):
        li.append(gold[i])
    li.reverse()
    lengrh=len(li)

    for i in range(len(li)):
        times+=1
        if times%3==0 and times!=len:
            li[i]='.'+li[i]

    li.reverses()
    fin=''
    for i in range(len(li)):
        fin+=li[i]
    return fin


def bogri(start,eja,count):
    print("원금:",comma(start),"원, 이자:"+str(eja)+"%\n\n")
    eja = eja/100+1

    for i in range(count):
        count+=1
        start *=eja
        print(i+1, "년경과",comma(int(start)),"원")

#원금 삼천원, 연이율 3%
bogri(3000,3,3)
