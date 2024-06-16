#We have two lists, one containing the possible ages of the children, and the second containing the first name of each child. We want to associate the possible ages for each child in the list. To do that we need to run through both lists simultaneously. The section on visualization will help you better understand the concept of a nested loop.

children=["John", "Peter", "Charles"]
ages=[15,18]
for child in children:   # for each child, we will go through each age
      for age in ages:  # each age is executed for each value of child
            print(child, age) 






""" The output will be:

John 15              

John 18

Peter 15

Peter 18

Charles 15

Charles 18 """

 
