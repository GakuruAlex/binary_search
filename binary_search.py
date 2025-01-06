from typing import List, Literal
def binary_search(cards: List[int], query: int)-> int:
    """_Determine the index of a given number in a list of sorted integers in descending order_

    Args:
        cards (List[int]): _List of integers in descending order_
        query (int): _Number whose position is to be determined_

    Returns:
        int: _Position of the given number_
    
    Example:
        >>> binary_search([2], 2)
        0
        >>> binary_search([10, 8, 7, 6, 5, 4, 2], 2)
        6
        >>> binary_search([10, 9, 7, 6, 5, 3, 1, 0], -1)
        -1
    """
    low, high = 0, len(cards) -1
    if len(cards) > 1:
        while low <= high:
            mid = (low + high) // 2
            
            result = condition(cards=cards, mid=mid, query=query)

            if result == "left":
                high = mid - 1
            elif result == "right":
                low = mid + 1
            else:
                return mid
        return -1
    elif len(cards) == 1:
        return 0 if cards[0] == query else -1
    else:
        return -1
def condition(cards: List[int], mid: int, query: int)->Literal['left', 'right', 'found']:
        """_Determine whether search space is left of the middle value , right of middle value or if target has been found._

        Args:
            cards (List[int]): _A list of sorted integers in descending order_
            mid (int): _Middle position of the current search list_
            query (int): _Number to determine its position_

        Returns:
            _str_: _left if query is equal to middle number and query is equal to number preceeding middle number or query is greater than middle number, right if query is less than middle number, found if number is equal_
        
        Example:
            >>> condition([10, 9, 8, 7, 6, 4, 3, 1], 7, 9)
            'left'
            >>> condition([10, 9, 8, 7, 6, 4, 3, 1], 7, 3)
            'right'
            >>> condition([10, 9, 8, 7, 6, 4, 3, 1], 7, 7)
            'found'
        """
        middle_number = cards[mid]
        preceeding_number = cards[mid - 1]
        if middle_number == query and preceeding_number == query or middle_number < query:
            return 'left'
        elif middle_number > query:
            return 'right'
        else:
            return 'found'
def main()-> None:
    cards: List[int] = list(map(int, input("List of integers in descending order, separated by whitespace: ").split(" ")))
    query: int = int(input("Number to find position: "))
    position: int = binary_search(cards=cards, query=query)
    print(f"{query} found at position {position} ")

if __name__ == "__main__":
    main()