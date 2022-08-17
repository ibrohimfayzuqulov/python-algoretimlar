from queue import Empty


class Stack:
        """Stack obyekti"""
        def __init__(self):
            self.stack = []

        def isEmpty(self):
            """bo'sh ekanligii tekshirish"""
            return len(self.stack)==0

        def push(self,data):
            """elementni qo'shish"""
            self.stack.append(data)
            return True

        def pop(self):
            """elementni sug'urib olish"""
            if self.isEmpty():
                return "Stck is Empty"
            else:
                return self.stack.pop()

        def peek(self):
            """eng ustki elementni ko'rish"""
            if self.isEmpty()