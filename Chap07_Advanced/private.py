class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
            
m = Mapping([1,2,3])
#m.__init__([4,5,6]) # doesn't error
print(m.items_list)
m.update([4,5,6])
print(m.items_list)

ms = MappingSubclass([1,2,3])
print(ms.items_list)
#ms.update([4,5,6]) # error
ms.update(['k1', 'k2'], ['v1', 'v2'])
print(ms.items_list)