from multiprocessing import Queue


queue = Queue(3)
print(queue.empty())
queue.put(1)
queue.put(2)
queue.put(3)
print(queue.full())
print(queue.qsize())
print(queue.get())
print(queue.qsize())