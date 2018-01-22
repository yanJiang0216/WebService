import sqlite3
cx = sqlite3.connect("./data.db") #返回一个数据库连接对象
cu = cx.cursor()
cu.execute("create table car (id integer primary key ,start text,terminus text,fares real,surplus integer)")
city= ["西安","铜川","宝鸡","咸阳","渭南","延安","汉中","榆林","安康","商洛","兴平","韩城","华阴"]
fares=[50,40,60,70,45,35,55,65,30,25,75,80]
init_ticket = 30
i=0
for start in city:
    for terminus in city:
        if(start == terminus):
            continue
        cu.execute("insert into car values (?,?,?,?,?)",(i,start,terminus,fares[i%12],30))
        i=i+1
cu.execute("create table user (id integer primary key ,username text,password text,telphone text)")
cu.execute("create table ticket_user (id integer primary key ,username text,telphone text,start text,terminus text)")
cx.commit()
cu.close()
cx.close()

