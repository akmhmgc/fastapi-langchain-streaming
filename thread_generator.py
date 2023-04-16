import queue

class ThreadedGenerator:
    def __init__(self):
        self.queue = queue.Queue()

    def __iter__(self):
        return self

    def __next__(self):
        item = self.queue.get()
        if item is StopIteration:
            raise item
        return item

    def send(self, data):
        self.queue.put(data)

    def close(self):
        self.queue.put(StopIteration)


import threading
import time
import queue

# 生産者スレッドが実行する関数
def producer(threaded_generator):
    for i in range(3):
        time.sleep(.3)  # データ生成に時間がかかることをシミュレート
        threaded_generator.send(i)
    threaded_generator.close()

# インスタンスを作成
tg = ThreadedGenerator()

# 生産者スレッドを作成して開始
producer_thread = threading.Thread(target=producer, args=(tg,))
producer_thread.start()

# 消費者スレッド（メインスレッド）でデータを処理
for item in tg:
    print("Received:", item)
