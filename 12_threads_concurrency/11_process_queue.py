#  For processes the memory is not shared  so to overcome this we can use Queue or Pipe to share data between processes

from multiprocessing import Process, Queue

def prepare_chai(queue):
    queue.put("Masala chai is ready")

if __name__ == '__main__':
    # Create a Queue object
    queue = Queue()

    processes = [Process(target=prepare_chai, args=(queue,)) for _ in range(2)]
    [p.start() for p in processes]
    [p.join() for p in processes]
    while not queue.empty():
        print(queue.get())  # Retrieve and print items from the queue