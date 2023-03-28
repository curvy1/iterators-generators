print ('Задача №1 FlatIterator')

import 

class FlatIteratorFlatIterator:

    def __init____init__(self, list_of_list):
        self.list_of_listlist_of_list = list_of_list
        self.cursorcursor = -1

    def __iter____iter__(self):
        self.itemitem = []
        for items in self.list_of_list:
            selfself.item.extend(items)
        return selfself

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.item):
            raise StopIteration
        else:
            return self.item[self.cursor]

def test_1():

    list_of_lists_1 = [
 ['a', 'b', 'c'],
 ['d', 'e', 'f', 'h', False],
 [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
 ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        print(flat_iterator_item, check_item)
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()

print ('Задача №2 flat_generator')

def flat_generator(list_of_lists):
    for check_list in list_of_lists:
        for item in check_list:
            yield item


def test_2():

    список_of_lists_1 = [
 ['a', 'b', 'c'],
 ['d', 'e', 'f', 'h', False],
 [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
 ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        print(flat_iterator_item, check_item)

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()