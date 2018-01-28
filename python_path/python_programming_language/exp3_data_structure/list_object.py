#!/usr/bin/env python
#-*- utf-8 -*-
list_obj=['1',2,'exp3;']
list_obj.append('test4')
list_obj.extend(another_list)
position=1
list_obj.insert(position,'test5')
some_value='test'
list_obj.remove(some_value)
# if some_value exist, or raise an error
list_obj.pop(position)
list_obj.popleft()
# position is optional, del the object at position and return it
list_obj.index(some_value)
list_obj.count(some_value)

list_obj.sort()
list_obj.reverse()
# sort ASC and DESC

