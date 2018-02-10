"""
COMP - 705, Week 3
Python Practice
Vladimir Kazarin
"""


def squared_nums(num_list):
    """
    Squares numbers in num_list
    num_list: list of numbers
    Returns: list of these numbers squared
    """
    for i in range(len(num_list)):
    	num_list[i] = num_list[i] ** 2
    return num_list


def check_title(title_list):
    """
    Removes strings in title_list that have numbers and aren't title case
    title_list: list of strings
    Returns: list of strings that are titles
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
    """
    new_inventory = { }
    # used list to prevent dictionary changed size error
    for key, val in list(inventory):  
    	if not val == 0:
    	        new_inventory[key] = val
    return new_inventory


def average_grades(grades):
    """
    Takes grade values from a dictionary and averages them into a final grade
    grades: a dictionary of grades with:
      key: string of students name
      value: list of integer grades received in class
    Returns: dictionary that averages out the grades of each student
    """
    for key in inventory.keys():
    	inventory[key] = sum(inventory[key]) / len(inventory[key])
    return inventory
