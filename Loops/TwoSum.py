from typing import List


class TwoSum:
    def __init__(self):
        pass

    def get_two_sum(self, int_list: List[int], target: int) -> List[int]:
        dictionary = {}

        for enrate_idx, number in enumerate(int_list):
            remainder = target - number

            if remainder in dictionary:
                return [enrate_idx, dictionary[remainder]]
            else:
                dictionary[number] = 0


x = TwoSum()
print(x.get_two_sum([2, 7, 11, 15], 9))


