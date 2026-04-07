class ActionQueue:
    def __init__(self):
        self.queue = []
        self.current_action = None
    
    def add(self, action):
        self.queue.append(action)
    
    def update(self):
        if self.queue and self.current_action is None:
            self.current_action = self.queue.pop(0)
            self.current_action.begin()
        
        if self.current_action:
            self.current_action.execute()
            
            if self.current_action.is_done:
                self.current_action = None
    
    def is_empty(self):
        return len(self.queue) == 0 and self.current_action is None