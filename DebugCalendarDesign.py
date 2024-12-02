from typing import List

class Calendar:
    def __init__(self):
        self.events: List[List[int]] = []

    def schedule(self, start: int, end: int) -> bool:
        for s, e in self.events:
            if max(s, start) < min(e, end):
                return False
        self.events.append([start, end])
        return True

calendar = Calendar()
print(calendar.schedule(5, 10))  
print(calendar.schedule(8, 13)) 
print(calendar.schedule(10, 15))  
