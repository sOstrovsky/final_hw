class LRUCache:
    def __init__(self, capacity: int) -> None:
        self._cache = {}
        self.capacity = capacity

    @property
    def cache(self):
        return next(iter(self._cache))

    @cache.setter
    def cache(self, new_elem):
        key, value = new_elem
        if key in self._cache:
            del self._cache[key]
        elif len(self._cache) >= self.capacity:
            del self._cache[next(iter(self._cache))]
        self._cache[key] = value

    def get(self, key: str):
        if key in self._cache:
            return self._cache.get(key)
        else:
            print('Такого значения в кеше нет')

    def print_cache(self):
        print('LRU Cache:')
        for key, value in self._cache.items():
            print(f'{key} : {value}')


def print_result():
    cache = LRUCache(3)
    cache.cache = ('key1', 'value1')
    cache.cache = ('key2', 'value2')
    cache.cache = ('key3', 'value3')

    cache.print_cache()
    print(cache.get('key2'))
    cache.cache = ('key4', 'value4')
    cache.print_cache()
