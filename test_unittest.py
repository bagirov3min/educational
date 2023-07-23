import unittest


def distance(x, y, x1, y1):
    return ((x - x1) ** 2 + (y - y1) ** 2) ** (0.5)


class TestDistance(unittest.TestCase):
    def test1(self):
        self.assertEqual(distance(1, 1, 1, 2), 1)

    def test2(self):
        self.assertEqual(distance(0, 0, 10, 0), 10)


def register(name, surname, value, data):
    user = {"name": name, "surname": surname, "value": value}
    if user not in data:
        data.append(user)
        return True
    return False


class TestRegister(unittest.TestCase):
    def test_register_new_user(self):
        data = []
        self.assertTrue(register("John", "Smith", 1, data))

    def test_register_exising_user(self):
        data = []
        register("John", "Smith", 1, data)
        self.assertFalse(register("John", "Smith", 1, data))


def merge_sort(a):
    if len(a) < 2:
        return a[:]
    else:
        median = int(len(a) / 2)
        left = merge_sort(a[:median])
        right = merge_sort(a[median:])
        return merge(left, right)


def merge(left, right):
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res


class TestSorted(unittest.TestCase):
    def test1(self):
        a = [5, 2, 4, 6, 1, 3, 2, 6]
        b = sorted(a)
        self.assertEqual(merge_sort(a), b)

    def test2(self):
        a = [70, 22, 1, 45, 233, 15, 1, 0]
        b = sorted(a)
        self.assertEqual(merge_sort(a), b)


unittest.main()
