LLIURE = "L"
OCUPAT = "O"
ESBORRAT = "B"


class MyHashMap:

    def __init__(self, cap=13):
        self._table = [[None, None, LLIURE] for _ in range(cap)]
        self._n = 0

    def _hash_function(self, key):
        return key % len(self._table)

    def _find(self, key):
        m = len(self._table)
        h = self._hash_function(key)

        for i in range(m):
            j = (h + i) % m
            if self._table[j][2] == LLIURE:
                return None
            if self._table[j][2] == OCUPAT and self._table[j][0] == key:
                return j

        return None

    def put(self, key, value):
        m = len(self._table)
        h = self._hash_function(key)
        primer_esborrat = None

        for i in range(m):
            j = (h + i) % m
            estat = self._table[j][2]

            if estat == OCUPAT and self._table[j][0] == key:
                self._table[j][1] = value
                return

            if estat == ESBORRAT and primer_esborrat is None:
                primer_esborrat = j

            if estat == LLIURE:
                pos = primer_esborrat if primer_esborrat is not None else j
                self._table[pos] = [key, value, OCUPAT]
                self._n += 1
                if self._n > len(self._table) // 2:
                    self._resize(2 * len(self._table) - 1)
                return

        if primer_esborrat is not None:
            self._table[primer_esborrat] = [key, value, OCUPAT]
            self._n += 1
            if self._n > len(self._table) // 2:
                self._resize(2 * len(self._table) - 1)

    def get(self, key):
        j = self._find(key)
        if j is not None:
            return self._table[j][1]
        return -1

    def remove(self, key):
        j = self._find(key)
        if j is not None:
            self._table[j] = [None, None, ESBORRAT]
            self._n -= 1

    def _resize(self, c):
        old_table = self._table
        self._table = [[None, None, LLIURE] for _ in range(c)]
        self._n = 0

        for slot in old_table:
            if slot[2] == OCUPAT:
                self.put(slot[0], slot[1])

    def __len__(self):
        return self._n
