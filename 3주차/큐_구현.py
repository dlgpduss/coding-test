class CircularQueue:
    '''큐 생성 및 초기화'''
    def __init__(self, size = 0):
        self.myQueue = [0] * size
        self.size = size
        self.front = 0
        self.rear = 0

    '''큐가 완전히 비어있는지 검사'''
    def isQueueEmpty(self):
        return self.size == 0
        
    '''큐가 꽉 차있는가 검사'''
    def isQueueFull(self):
        if self.rear == None:
            return False
        else:
            return self.next_index(self.rear) == self.fornt
        
    '''데이터 삽입'''
    def enqueue(self, data):
        if self.isQueueFull():
            print('큐가 꽉 차있습니다.')
        
        if self.rear == None:
            self.rear = 0
        else:
            self.rear = self.next_index(self.rear)

        self.myQueue[self.rear] = data
        self.size += 1
        return self.myQueue[self.rear]
    
    '''데이터 삭제'''
    def deque(self):
        if self.isQueueEmpty():
            print("큐가 비어있습니다.")
        self.myQueue[self.front] = None
        self.front = self.next_index(self.front)
        return self.myQueue[self.front]
    
    '''데이터 출력'''
    def printQueue(self):
        print(self.myQueue)