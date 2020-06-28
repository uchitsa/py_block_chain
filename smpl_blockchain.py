import hashlib
from datetime import datetime


class Blok:
    def __init__(self, idx, timestamp, data, prehash):
        self.idx = idx
        self.timestamp = timestamp
        self.data = data
        self.prehash = prehash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(
            str(self.idx).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.data).encode('utf-8') + str(self.prehash).encode('utf-8'))
        return sha.hexdigest()


def gen_blok():
    return Blok(0, datetime.now(), "Gen Blok", "0")


def next_blok(last_blok):
    cur_idx = last_blok.idx + 1
    cur_timestamp = datetime.now()
    cur_data = f"Blok {cur_idx}"
    cur_hash = last_blok.hash
    return Blok(cur_idx, cur_timestamp, cur_data, cur_hash)


blok_chain = []

blok_chain.append(gen_blok())

for _ in range(0, 10):
    blok_chain.append(next_blok(blok_chain[-1]))

for item in blok_chain:
    print(item.data)
