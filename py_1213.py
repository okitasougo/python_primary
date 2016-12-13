# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 19:07:35 2016

@author: mengqian
"""
# looping techniques
# 1---when looping through dictionaries ,the key and corresponding value can be retrieved at the same time
# using the item() method
knight={'gallahad':'the pure','robin':'the brave'};
for i,j in knight.items():
    print i,j;
# 2---when looping through a sequence ,the position index and corresponding value can be retrieved
# at the same time using the enumerate() function
for i,j in enumerate(['tic','tac','toe']):
    print i,j;
# 3---to loop over two or more sequences at the same time,the entries can be paired with the zip()
# function
questions=['name','quest','color'];
answer=['mq','holy gail','blue'];
for i,j in zip(questions,answer):
    print 'what is your {0}?,i {1}'.format(i,j);
