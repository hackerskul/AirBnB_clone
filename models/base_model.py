#!/usr/bin/env python
import uuid
from datetime import datetime

class BaseModel:
    """A base class for all models"""
    def __init__(self, *args **kwargs):
        from models import storage
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        def __str__(self):
            return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"            
        def save(self):
            self.updated_at = datetime.now()

        def to_dict(self):
            dict_rep = self.__dict__copy()
            dict_rep['__class__'] = self.__class__.name__
            dict_rep['created_at'] = self.created_at.isoformat()
            dict_rep['updated_at'] = self.updated_at.isoformat()
        
            return dict_rep

