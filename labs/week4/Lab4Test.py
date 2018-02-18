import unittest

class Lab4Test(unittest.TestCase):

    def test_squared_nums(self):
        """
        Tests lab4.squared( )
        """
        func = lab4.squared_nums
        case1 = [1, 2, 3]
        expected1 = [1, 4, 9]
        case2 = []
        expected2 = []
        case3 = [-1, -2, -3]
        expected3 = [1, 4, 9]
        case4 = [1,0]
        expected4 = [1, 0]        
        self.assertEqual(func(case1), expected1)
        self.assertEqual(func(case2), expected2)
        self.assertEqual(func(case3), expected3)
        self.assertEqual(func(case4), expected4)


    def test_check_title(self):
        """
        Tests lab4.check_title
        """
        func = lab4.check_title
        case1 = ['Hello World', 'Hello_world', 'Title']
        expected1 = ['Hello World', 'Title']
        case2 = ['Hello_World', 'A great 3 Days', 'hello World']
        expected2 = ['Hello_World']
        case3 = ['10, 11, 12']
        expected3 = []        
        self.assertEqual(func(case1), expected1)
        self.assertEqual(func(case2), expected2)
        self.assertEqual(func(case3), expected3)


    def test_restock_inventory(self):
        """
        Tests lab4.restock_inventory
        """
        func = lab4.restock_inventory
        case1 = {'pencil':10, 'pen':8, 'paper':7}
        expected1 = {'pencil':20, 'pen':18, 'paper':17}
        case2 = {'pencil':0, 'pen':-3, 'paper':-11}
        expected2 = {'pencil':10, 'pen':7, 'paper':-1}
        case3 = {'pencil':0.5, 'pen':-3.2, 'paper':11.0}
        expected3 = {'pencil':10.5, 'pen':6.8, 'paper':21.0}       
        self.assertEqual(func(case1), expected1)
        self.assertEqual(func(case2), expected2)
        self.assertEqual(func(case3), expected3)


    def test_filter_0_items(self):
        """
        Tests lab4.filter_0_items
        """
        func = lab4.filter_0_items
        case1 = {'pencil':10, 'pen':8, 'paper':7}
        expected1 = {'pen':8, 'paper':7, 'pencil':10}
        case2 = {'pencil':0, 'pen':-3, 'paper':-11}
        expected2 = {'pen':-3, 'paper':-11}
        case3 = {'pencil':0.5, 'pen':-3.2, 'paper':0.0}
        expected3 = {'pen':-3.2, 'pencil':0.5}    
        self.assertEqual(func(case1), expected1)
        self.assertEqual(func(case2), expected2)
        self.assertEqual(func(case3), expected3)


    def test_average_grades(self):
        """
        Tests lab4.average_grades
        """
        func = lab4.average_grades
        case1 = {'Michael':[100, 78, 88, 900/10], 'Daniel':[80, 95, 77, 64.0], 'Josh':[99, 89, 94, 66]}
        expected1 = {'Josh': 87.0, 'Daniel': 79.0, 'Michael': 89.0}
        case2 = {'Michael':[5*20, 188 * .5, 88], 'Daniel':[80.5, .15, 66, 64.0], 'Josh':[99 + 1 * -2, 40/.5]}
        expected2 = {'Josh': 88.5, 'Daniel': 52.6625, 'Michael': 94.0}
        case3 = {'Michael':[78], 'Daniel':[90], 'Josh':[900/-9]}
        expected3 = {'Josh': -100.0, 'Daniel': 90.0, 'Michael': 78.0}      
        self.assertEqual(func(case1), expected1)
        self.assertEqual(func(case2), expected2)
        self.assertEqual(func(case3), expected3)


if __name__ == '__main__':
    try:
        import lab4
        print("lab4.py module found.Testing...")
        unittest.main( )
    except ImportError:
        print("Missing lab4.py module")        