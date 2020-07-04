import multiprocessing
import time


def washer(dishes, dish_queue):
    for dish in dishes:
        print('Washing', dish, 'dish')
        dish_queue.put(dish)
        time.sleep(0.5)


def dryer(dish_queue):
    while True:
        dish = dish_queue.get()
        print('Drying', dish, 'dish')
        time.sleep(1)
        dish_queue.task_done()


if __name__ == '__main__':

    dish_queue = multiprocessing.JoinableQueue()

    dryer_proc = multiprocessing.Process(target=dryer, args=(dish_queue,))
    dryer_proc.daemon = True
    dryer_proc.start()

    dishes = ['salad', 'bread', 'entree', 'dessert']
    washer(dishes, dish_queue)

    dish_queue.join()
