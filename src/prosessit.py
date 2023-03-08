from multiprocessing import Process

def prosessit(raja, task):

    prosessi1 = Process(target=task,args=(0,int(raja/6)))
    prosessi2 = Process(target=task,args=(int(raja/8),int(2*raja/8)))
    prosessi3 = Process(target=task,args=(int(2*raja/8),int(3*raja/8)))
    prosessi4 = Process(target=task,args=(int(3*raja/8),int(4*raja/8)))
    prosessi5 = Process(target=task,args=(int(4*raja/8),int(5*raja/8)))
    prosessi6 = Process(target=task,args=(int(5*raja/8),int(6*raja/8)))


    prosessi1.start()
    prosessi2.start()
    prosessi3.start()
    prosessi4.start()
    prosessi5.start()
    prosessi6.start()

    prosessi1.join()
    prosessi2.join()
    prosessi3.join()
    prosessi4.join()
    prosessi5.join()
    prosessi6.join()
