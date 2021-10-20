# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 11:28:09 2021

@author: vinoth
"""

# http://www.cheat-sheets.org/saved-copy/CheatSheet-Python-4_-Classes.20210604.pdf


class Fruits:
    pass


banana = Fruits()

banana.color= "yellow"


Fruits.taste = ('Sour', 'Sweet', 'Spicy','Raw')

banana.taste = 'Sweet'
print(banana.taste)


# class​​Dog​:""" Blueprint of a dog """# class variable shared by all instancesspecies = [​"canis lupus"​]def​​__init__​(self, name, color)​:self.name = nameself.state = ​"sleeping"self.color = colordef​​command​(self, x)​:if​ x == self.name:self.bark(​2​)elif​ x == ​"sit"​:self.state = ​"sit"else​:self.state = ​"wag tail"def​​bark​(self, freq)​:for​ i ​in​ range(freq):print(​"["​ + self.name+ ​"]: Woof!"​)



def summing():
    print('hello')
    


setattr(Fruits, 'text1', summing)



Fruits.text1()