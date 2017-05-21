import threading, time

print('Start the programming.')


def take_an_ap():
    time.sleep(5)
    print('Wake up.')

thread_obj = threading.Thread(target=take_an_ap)
thread_obj.start()
# print的几个常规参数'cat','dog'， 一个关键字参数sep = '&'，写法如下：
thread_obj = threading.Thread(target=print, args=['cat','dog'], kwargs={'sep': ' & '})
thread_obj.start()

print('a', 'b', 'c', sep=' # ')

print('Ending the programming.')