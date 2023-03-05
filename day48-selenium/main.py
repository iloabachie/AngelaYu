# from selenium import webdriver
# import os, dotenv

# dotenv.load_dotenv('day48-selenium\\.env')
# token = os.getenv('TOKEN')
# username = os.getenv('USERZNAME')


# print(token, username)
# print(os.environ.get('TOKEN'))
# print(os.getenv('TEMP'))

# chrome_driver_path = 'D:\\Documents\\Python lessons\\chromedriver.exe'

# driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get('https://www.amazon.com')
# driver.find_element()

# driver.close() # closes active tab
# driver.quit() # closes the window





class TreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        
node2 = TreeNode(3, 5, 6)
node3 = TreeNode(4)

node0 = TreeNode(8, node2, node3)

tree = node0

print(tree.key, tree.left.key, tree.right.key, tree.left.left, tree.right.right)