from collections import deque

def search(start_node, target='elon musk'):
    search_queue = deque()
    search_queue += graph[start_node]
    searched = set() # bu to'plam biz tekshirgan odamlarimizni qayta tekshirmasligimiz uchun kerak

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person == target:
                print(f"{target} ni topdik!")
                # print(searched)
                return True
            else:
                search_queue += graph[person]

    return  False


if __name__ == '__main__':
    graph  = {'siz': ['ali','vali','tohir'], 'ali': ['aziza','olim'], 'vali': ['botir','ziyoda'],'tohir':['elom musk,','mohir'], 'olim' : [], 'aziza':[], 'botir':[], 'ziyoda':['aziza'],'elon musk':[], 'mohir':[]}

    print(search('ali', 'olim'))