#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = 5
b = 7

sum = a + b
sub = a - b
mul = a * b
div = a / b

print(sum)
print(sub)
print(mul)
print(div)


# In[2]:


for i in range(50):
  print('Hello World')


# In[3]:


for i in range(50):
  print(i)


# In[5]:


for i in range(1, 51):
  print(i)


# In[7]:


for i in range(1, 14):
  print('제' + str(i) + '의아해가무섭다고그리오.')


# In[8]:


for i in range(1, 14):
  if i % 2 == 0:
    print('제' + str(i) + '의아해는무서워하는아해라고그리오.')
  elif i % 2 == 1:
    print('제' + str(i) + '의아해는무서운아해라고그리오.')


# In[9]:


for i in range(1, 14):
  if i == 7:
    print('제' + str(i) + '의아해는운이좋은아해라고그리오.')
  else:
    if i % 2 == 0:
      print('제' + str(i) + '의아해는무서워하는아해라고그리오.')
    elif i % 2 == 1:
      print('제' + str(i) + '의아해는무서운아해라고그리오.')


# In[10]:


storage = []

for i in range(1, 100):
  if i % 7 == 0:
    storage.append(i)

print(storage)
print(len(storage))


# In[11]:


print(storage[0])
print(storage[4])
print(storage[-1])
print(storage[-2])
print(storage[3:])
print(storage[:4])
print(storage[1:6])


# In[12]:


def love_three(some_list):
  new_list = []

  for number in some_list:
    if number % 3 == 0:
      new_list.append(number)

  return new_list


other_list = love_three(storage)

print(other_list)

