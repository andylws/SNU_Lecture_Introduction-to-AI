#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output


class Post():
    def __init__(self, board_name, post_number):
        self.belong_to = board_name
        self.number = post_number
        self.title = ''
        self.content = ''
        
    def set_contents(self, title, content):
        self.title = title
        self.content = content
        
    def print_info(self):
        print('게시물 고유번호: %d' % self.number)
        print(self.title)
        print(self.content)
        print('이 게시물은 %s에서 %d번째로 작성된 글입니다.\n' % (self.belong_to, self.number))
        
        
class BulletinBoard():
    def __init__(self, board_name, num_max_posts):
        self.name = board_name
        self.num_max_posts = num_max_posts
        self.posts = []
        self.count = 0
        
    def write_post(self):
        if self.num_max_posts > len(self.posts):
            post = Post(self.name, self.count + 1)
            
            title = input('새 게시글의 제목을 입력하세요: ')
            content = input('새 게시글의 내용을 입력하세요: ')
            
            clear_output()
            
            post.set_contents(title, content)
            
            self.posts.append(post)
            
            self.count += 1
            
        else:
            print('게시판이 꽉 차서 더 이상 게시글을 작성할 수 없습니다.')
            
    def show_posts(self):
        for post in self.posts:
            post.print_info()
            
    def delete_post(self):
        num_to_delete = input('삭제할 게시글의 고유번호를 입력하세요: ')
        
        clear_output()
        
        deleted = False
        for i, post in enumerate(self.posts):
            if post.number == int(num_to_delete):
                del self.posts[i]
                deleted = True
                break
                
        if not deleted:
            print('삭제 실패: 해당 고유번호를 가진 게시글이 존재하지 않습니다.')
            

school_board = BulletinBoard('School', 5)
mini_board = BulletinBoard('Mini', 3)

current_board = school_board

while True:
    print('현재 게시판: %s\n' % current_board.name)
    current_board.show_posts()
    print('1. 학교 게시판 선택')
    print('2. 미니 게시판 선택')
    print('3. 현재 게시판에 새 게시글 작성')
    print('4. 현재 게시판에서 게시글 삭제')
    print('5. 종료')
    selection = input('행동할 번호를 선택하세요: ')
    
    clear_output()
    
    if selection == '1':
        current_board = school_board
    elif selection == '2':
        current_board = mini_board
    elif selection == '3':
        current_board.write_post()
    elif selection == '4':
        current_board.delete_post()
    elif selection == '5':
        break
    else:
        print('번호 입력이 잘못되었습니다.')


# In[2]:


class Engine():
    def __init__(self, displacement):
        print(1)
        self.displacement = displacement
        
class Car():
    def __init__(self, car_type, displacement):
        print(2)
        self.car_type = car_type
        self.engine = Engine(displacement)
        
print(3)
car_type = 'truck'
car = Car(car_type, 5500)


# In[3]:


class Wallet():
    def __init__(self):
        self.money = 0
        
    def put_money(money):
        self.money += money
        

wallet = Wallet()
wallet.put_money(5000)


# In[ ]:




