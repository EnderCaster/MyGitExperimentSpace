#! -*- coding:utf8 -*-
"""add suitable HTML to text block"""
class Handler:
    """parent class for processing program"""
    def callback(self,prefix,name,*args):
        method=getattr(self,prefix+name,None)
        if callable(method) : return method(*args)
    def start(self,name):
        self.callback('start_',name)
    def end(self,name):
        self.callback('end_',name)
    def sub(self,name):
        def substitution(match):
            result=self.callback('sub_',name,match)
            if result is None :result=match.group(0)
            return result
        return substitution
class HTMLRenderer(Handler):
    """processing program"""
    def start_document(self):
        print("<html><head><title>HackIT</title></head><body>")
    def end_document(self):
        print("</body></html>")
    def start_paragraph(self):
        # modified there, I think the display should given by outer css
        print('<p>')
    def end_pargraph(self):
        print('</p>')
    def start_heading(self):
        print('<h2>')
    def end_heading(self):
        print('</h2>')
    def start_list(self):
        print('<ul>')
    def end_list(self):
        print('</ul>')
    def start_listitem(self):
        print('<li>')
    def end_listitem(self):
        print('</li>')
    def start_title(self):
        print('<h1>')
    def end_title(self):
        print('</h1>')
    def sub_emphasis(self,match):
        return '<em>{}</em>'.format(match.group(1))
    def sub_url(self,match):
        return '<a target="_blank" href="{}">{}</a>'.format(match.group(1),match.group(1))
    def sub_mail(self,match):
        return '<a href="mailto:{}">{}</a>'.format(match.group(1),match.group(1))
    def feed(self,data):
        print(data)