"""
COMP - 705, Week 4, Unit Testing
Python Practice
Vladimir Kazarin
"""

def squared_nums(num_list):
    """
    Squares numbers in num_list
    num_list: list of numbers
    Returns: list of these numbers squared

    >>> squared_nums([1, 2, 3])
    [1, 4, 9]
    >>> squared_nums([])
    []
    >>> squared_nums([-1, -2, -3])
    [1, 4, 9]
    >>> squared_nums([1, 0])
    [1, 0]
    """
    for i in range(len(num_list)):
    	num_list[i] = num_list[i] ** 2
    return num_list


def check_title(title_list):
    """
    Removes strings in title_list that have numbers and aren't title case
    title_list: list of strings
    Returns: list of strings that are titles

    >>> check_title(['Hello World', 'Hello_world', 'Title'])
    ['Hello World', 'Title']
    >>> check_title(['Hello_World', 'A great 3 Days', 'hello World'])
    ['Hello_World']
    >>> check_title(['10, 11, 12'])
    []
    """
    filtered_list = []
    for input_string in title_list:
        if not any(char.isdigit() for char in input_string):
            if input_string.istitle():
                filtered_list.append(input_string)
    return filtered_list


def restock_inventory(inventory):
    """
    Increases inventory of each item in dictionary by 10
    inventory: a dictionary with:
      key: string that is the name of the inventory item
      value: integer that equals the number of that item currently on hand
    Returns: updated dictionary where each inventory item is restocked

    >>> restock_inventory({'pencil':10, 'pen':8, 'paper':7})
    {'pencil':20, 'pen':18, 'paper':17} 
    >>> restock_inventory({'pencil':0, 'pen':-3, 'paper':-11})
    {'pencil':10, 'pen':7, 'paper':-1}
    >>> restock_inventory({'pencil':0.5, 'pen':-3.2, 'paper':11.0})
    {'pencil':10.5, 'pen':6.8, 'paper':21.0}
    """
    for key in inventory.keys():
    	inventory[key] += 10
    return inventory


def filter_0_items(inventory):
    """
    Removes items that have a value of 0 from a dictionary of inventories
    inventory: dictionary with:
       key: tring that is the name of the inventory item
       value: nteger that equals the number of that item currently on hand
    Returns: the same inventory_dict with any item that had 0 quantity removed

    >>> filter_0_items({'pencil':10, 'pen':8, 'paper':7}) 
    {'pen':8, 'paper':7, 'pencil':10}
    >>> filter_0_items({'pencil':0, 'pen':-3, 'paper':-11})
    {'pen':-3, 'paper':-11}
    >>> filter_0_items({'pencil':0.5, 'pen':-3.2, 'paper':0.0})
    {'pen':-3.2, 'pencil':0.5}
    """
    new_inventory = { }
    # used list to prevent dictionary changed size error
    for key in inventory:  
    	if not inventory[key] == 0:
    	        new_inventory[key] = inventory[key]
    return new_inventory


def average_grades(grades):
    """
    Takes grade values from a dictionary and averages them into a final grade
    grades: a dictionary of grades with:
      key: string of students name
      value: list of integer grades received in class
    Returns: dictionary that averages out the grades of each student

    >>> average_grades({'Michael':[100, 78, 88, 900/10], 'Daniel':[80, 95, 77, 64.0], 'Josh':[99, 89, 94, 66]}) 
    {'Josh': 87.0, 'Daniel': 79.0, 'Michael': 89.0}
    >>> average_grades({'Michael':[5*20, 188 * .5, 88], 'Daniel':[80.5, .15, 66, 64.0], 'Josh':[99 + 1 * -2, 40/.5]})
    {'Josh': 88.5, 'Daniel': 52.6625, 'Michael': 94.0}
    >>> average_grades({'Michael':[78], 'Daniel':[90], 'Josh':[900/-9]})
    {'Josh': -100.0, 'Daniel': 90.0, 'Michael': 78.0}

    """
    for key in grades.keys():
    	grades[key] = sum(grades[key]) / len(grades[key])
    return grades


if __name__ == '__main__':
    import doctest
    doctest.testmod()