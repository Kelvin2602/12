from datetime import datetime
from typing import Dict, List, Optional

class Break:
    def __init__(self, break_type: str, user_id: int):
        self.type = break_type
        self.user_id = user_id
        self.start_time = datetime.now()
        self.end_time: Optional[datetime] = None
        self.duration: Optional[float] = None

    def end(self) -> float:
        self.end_time = datetime.now()
        self.duration = (self.end_time - self.start_time).total_seconds() / 60
        return self.duration

class Shift:
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.start_time = datetime.now()
        self.end_time: Optional[datetime] = None
        self.breaks: List[Break] = []
        
    def end(self) -> float:
        self.end_time = datetime.now()
        return (self.end_time - self.start_time).total_seconds() / 3600

class UserManager:
    def __init__(self):
        self.active_shifts: Dict[int, Shift] = {}
        self.active_breaks: Dict[int, Break] = {}
        
    def start_shift(self, user_id: int) -> bool:
        if user_id in self.active_shifts:
            return False
        self.active_shifts[user_id] = Shift(user_id)
        return True
        
    def end_shift(self, user_id: int) -> Optional[float]:
        if user_id not in self.active_shifts:
            return None
        hours = self.active_shifts[user_id].end()
        del self.active_shifts[user_id]
        return hours