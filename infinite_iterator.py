class InfIter:
    def __init__(self, *list_to_be_used: list or range):
        if all(isinstance(item, int) for item in list_to_be_used):
            self.list_to_be_used = list(list_to_be_used)
        else:
            self.list_to_be_used = list(*list_to_be_used)
        self.current = 0

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        self.current += 1
        return self.list_to_be_used[(self.current - 1) % len(self.list_to_be_used)]

    def __repr__(self):
        return f"InfIter({self.list_to_be_used})"

    def __len__(self):
        return len(self.list_to_be_used)

    def __add__(self, value_to_be_added: list) -> list:
        return self.list_to_be_used + value_to_be_added

    def __setitem__(self, index: int, value_to_be_added: list):
        self.list_to_be_used[index % len(self)] = value_to_be_added

    def __getitem__(self, index: slice or int) -> list or str or int:
        # well it wouldn't be an infinite iterator without being able to return a slice
        # that's bigger than the list that's stored, so if the "to" list index is greater
        # than the actual list stored, so to do so, list comprehension is used to iterate
        # through the list, repeating whenever the "to" index is greater
        if isinstance(index, slice):
            stop = index.stop if index.stop is not None else len(self.list_to_be_used) - 1
            if stop > len(self.list_to_be_used):
                start = index.start if index.start is not None else 0
                step = index.step if index.step is not None else 1
                return [self.list_to_be_used[x % len(self)] for x in range(start, stop, step)]
            else:
                return self.list_to_be_used[stop % len(self.list_to_be_used)]
        # gets the numbers from the slice
        else:
            return self.list_to_be_used[index % len(self.list_to_be_used)]

    def __reversed__(self):
        self.list_to_be_used = self.list_to_be_used[::-1]
        return self

    def get_list(self) -> list:
        return self.list_to_be_used


# things that it works on
print("It works on strings")
inf_string = InfIter("hello")
for x in inf_string[:10]:
    print(x)

print("You can use it on a normal list")
inf_list = InfIter(list(range(1, 6)))
for x in inf_list[:10]:
    print(x)

print("you can pass a range")
inf_range = InfIter(range(1, 6))
for x in inf_range[:10]:
    print(x)

print("You can use *args")
inf_int = InfIter(1, 2, 3, 4, 5)
for x in inf_int[:10]:
    print(x)

print("It also works on generators")
generator_list = InfIter(x for x in range(1, 6))
for x in generator_list[:10]:
    print(x)


infinite_iterator_object = InfIter(range(1, 11))  # x for x in range(1, 11, 2))

print([infinite_iterator_object[x] for x in range(20)])

multiplied_values = [x * value for x, value in zip(range(1, 11),infinite_iterator_object.get_list())]

print(infinite_iterator_object)

for thing_index, to_be_multiplied_index, value \
        in zip(infinite_iterator_object, range(1, 111), multiplied_values):
    print(f"{thing_index} * {to_be_multiplied_index} = {value}")
