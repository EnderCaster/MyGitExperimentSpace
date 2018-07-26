#! -*- coding:utf8 -*-
""" Implement the text block generator
    divide pure text to text block
    """
def lines(file):
    for line in file:
        yield line
    yield '\n'
def blocks(file):
    block=[]
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield "".join(block).strip()
            block=[]