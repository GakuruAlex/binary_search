from typing import List
def binary_search(cards: List[int], query: int)-> int:
    """_Determine the index of a given number in a list of sorted integers in descending order_

    Args:
        cards (List[int]): _List of integers in descending order_
        query (int): _Number whose position is to be determined_

    Returns:
        int: _Position of the given number_
    """
    low, high = 0, len(cards) -1

    while low <= high:
        mid = (low + high) // 2
        if cards[mid] == query:
            result = 
        elif cards[mid] < query:
            high = mid - 1
        else:
            low = mid + 1
    return -1
def condition(cards: List[int], mid: int, query: int):
        if cards[mid] == query and cards[mid - 1] == query:
            return 'left'
        elif cards[mid] and cards[mid + 1] == query:
            return 'right'
        elif cards[mid] < query:
            return 'left'
        elif cards[mid] > query:
            return 'right'
        else:
            return 'found'
def main()-> None:
    print(binary_search([20, 18, 15, 14, 13, 12, 1], -1))

if __name__ == "__main__":
    main()