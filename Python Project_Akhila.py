#!/usr/bin/env python
# coding: utf-8

# In[1]:


###    A sample script of Game of Thrones was taken from the page and stored in the file conv.txt in the dataset provided.
###    Your task is to read the file and do the following:
###       1. Find out the number of unique characters in the sample conversation
###       2. Create a new text file for each of the characters with their name and store the unique words said by them in their 
###          respective file.Store one word in one line


# In[2]:


### Finding out the number of unique characters


# In[3]:


character_list = set()
text = open(r"D:\\Internshala\\Python\\conv.txt","r")
for line in text:
    if line != '\n':
        line = line.strip().split(':')
        character_list.add(line[0])   


# In[96]:


character_list


# In[4]:


len(character_list)


# In[5]:


### It has been found that there are 17 unique characters in Game of Thrones


# In[6]:


###     Create a new text file for each of the characters with their name and store the unique words 
###     said by them in their respective file.


# In[7]:


for characters in character_list:
    words = []
    words_list = []
    word_set = ()
    print('\n\n',characters,'------------------------------------------------------------')
    character_file = open("D:\\Internshala\\Python\\"+characters+".txt",'w')
    text = open(r"D:\\Internshala\\Python\\conv.txt","r")
    for lines in text:
        if lines.startswith(characters):
            line1 = lines.strip().split(':')
            words = line1[1].strip().split(' ')
            if words is not None:
                words_list.extend(words)
        else: 
            continue
    word_set = set(words_list)
    print(word_set)
    for i in word_set:
        character_file.write(i)
        character_file.write('\n')                    


# In[ ]:


###    The above shows the distinct words spoken by the characters.
###    The words of each character has been written in text files named after the character names


# In[ ]:


### For example, let us open the file named after character, 'ARYA'


# In[109]:


arya_file = open(r"D:\\Internshala\\Python\\ARYA.txt","r")
for lines in arya_file:
    print(lines)

