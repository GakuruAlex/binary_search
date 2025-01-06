# Binary Search #

For a list of sorted numbers in decreasing order

1.Determine the middle number of the list

2.If it matches the target , return the middle index as the answer

3.If the target is greater than the middle number, search the first half of the list

4.If the target is less than the middle number, search the second half number of the list.

5.If no more elements remain return -1

## Problem Statement ##

Given a list of sorted integers in descending order, find the position of a given number. Minimize the number of times you access the elements of the lit.

## Input ##

Cards: List of sorted integers in descending order i.e cards = [24, 16, 13, 11, 9, 8, 5, 2]

Query: Number whose position is to be determined i.e 2

## Output ##

Position: Index of number in the list i.e 7 (counting from 0) for query=2 in list above


## Test Cases ##

1.)Number is at the end of the list

2.)Number is somewhere in the middle of the list

3.)Number is at the beggining of the list

4.)List is empty

5.)Number doesnt exist in the list

6.)List with only one number

7.)Number is repeated in the list

8.)List contains repeating numbers

9.) List contains negative integers

10.)List contains both positive and negative numbers

11.) A query that doesn't exist that would have been at the start of the list i.e greater than all the existing numbers

12.) A query that doesn't exist that would have been at the end of the list i.e smaller than all the existing numbers

    tests = [

     {
         "input":{
             "cards":[24, 16, 13, 11, 9, 8, 5, 2],
             "query": 2
         },
         "output": 7
     },

     {
         "input":{
                 "cards":[24, 17, 10, 11, 9, 8, 4],
                 "query": 24
             },
             "output": 0
     },

     {
         "input":{
                 "cards":[20, 18, 17, 15, 8, 4, 2, 1, 0],
                 "query": 8
             },
             "output":4
     },
     {
         "input":{
             "cards":[],
             "query": 4
         },
         "output": -1
     
     },
     {
         "input":{
             "cards":[2],
             "query":2
         },
         "output":0
     },
     {
         "input":{
             "cards": [9,8, 8, 6, 5, 4, 2, 0],
             "query": 8
             },
             "output": 1
     },
     {
        "input":{
            "cards": [10, 8, 7, 6, 4, 3, 1, 0, -1, -2, -4, -5, -6],
            "query": -6
        },
        "output": 12
     },
     {
        "input":{
            "cards":[-1, -2, -4, -6, -7, -9, -10, -12, -15, -20],
            "query": -7
        },
        "output": 4
     }

            ]