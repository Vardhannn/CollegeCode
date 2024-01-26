#MULTI PROCESSING

import multiprocessing
def worker(num, conn):
    result = num * 2
    conn.send(result)
    conn.close()
if __name__ == '__main__':
    parent_conn, child_conn = multiprocessing.Pipe()
    p = multiprocessing.Process(target=worker, args=(2, child_conn))
    p.start()
    result = parent_conn.recv()
    print(result)
    p.join()