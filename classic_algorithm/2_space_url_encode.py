#!/usr/bin/env python3
# -*- utf-8 -*-


class Solution:
    def space_replacement(self, origin, length):
        """To replace space with %20
        in python, origin is an array
        """
        return self.python_only(origin, length)

    def python_only(self, origin, length):
        """in python, origin is an array
        This solution maybe not fit answer
        """
        for i in range(length):
            if origin[i] == ' ':
                origin[i] = '%20'
                length += 2

        return length

    def maybe_a_real_solution(self, origin, length):
        pointer = length-1
        for i in range(length):
            if origin[i] == ' ':
                length += 2

        for i in range(length):
            if pointer<=0:
                break
            if origin[pointer:pointer+1] == ' ':
                origin[i-2:i+1] = ['%', "2", '0']
                i -= 3
            else:
                origin[i:i+1] = origin[pointer]
            pointer-=1

        return length
