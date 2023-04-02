class Stack():
    '''빈 스택 하나 생성'''
    def __init__(self, size=0):
        self.mystack =  [0] * size
        self.top = 0
        self.size = size
    '''스택이 꽉 차있는지 검사'''
    def isStackFull(self):
        if (self.top - 1) >= self.size:
            return True
        else:
            return False
    
    '''스택이 완전히 비어있는지 검사'''
    def isStackEmpty(self):
        if (self.top <= -1):
            return True
        else:
            return False
        
    '''스택에 요소를 추가'''
    def push(self):
        if self.isStackFull():
            print("스택이 꽉 찼습니다.")
            return
        top += 1
        self.mystack[self.top] = self.data

    '''가장 마지막에 들어온 요소를 반환하고 제거'''
    def pop(self):
        if self.isStackEmpty:
            print("스택이 비었습니다.")
            return None
        data = self.mystack[top]
        self.mystack[top] = None
        top -= 1
        return data
    
    '''스택에 저장된 모든 요소를 출력'''
    def printStack(self):
        print(self.mystack)
