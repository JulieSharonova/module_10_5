import time
import multiprocessing


def read_info(name):
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break


filenames = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':

    # Линейный вызов
    start = time.time()
    for i in filenames:
        read_info(i)
    result = time.time() - start
    print(f'{result} (линейный)')

    # Многопроцессный
    start_time = time.time()
    with multiprocessing.Pool(processes=4) as pool:
            pool.map(read_info, filenames)
    time_res = time.time() - start_time
    print(f'{time_res}  (многопроцессный)')

