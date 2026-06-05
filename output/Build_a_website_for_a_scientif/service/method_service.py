python
# service/method_service.py

from abc import ABC, abstractmethod
from typing import List
from dataclasses import dataclass

@dataclass
class MathMethod:
    id: int
    formula_id: int
    name: str
    description: str

class MathMethodService(ABC):
    @abstractmethod
    def create_math_method(self, formula_id: int, name: str, description: str) -> int:
        pass

    @abstractmethod
    def get_math_method(self, math_method_id: int) -> MathMethod:
        pass

    @abstractmethod
    def get_math_methods(self, formula_id: int = None) -> List[MathMethod]:
        pass

    @abstractmethod
    def update_math_method(self, math_method_id: int, name: str, description: str):
        pass

    @abstractmethod
    def delete_math_method(self, math_method_id: int):
        pass

class DefaultMathMethodService(MathMethodService):
    def __init__(self, db_session):
        self.db_session = db_session
        self.methods = {}

    def create_math_method(self, formula_id: int, name: str, description: str) -> int:
        method = MathMethod(len(self.methods) + 1, formula_id, name, description)
        self.methods[method.id] = method
        self.db_session.add(method)
        self.db_session.commit()
        return method.id

    def get_math_method(self, math_method_id: int) -> MathMethod:
        return self.methods.get(math_method_id)

    def get_math_methods(self, formula_id: int = None) -> List[MathMethod]:
        if formula_id:
            return [method for method in self.methods.values() if method.formula_id == formula_id]
        return list(self.methods.values())

    def update_math_method(self, math_method_id: int, name: str, description: str):
        method = self.get_math_method(math_method_id)
        if method:
            method.name = name
            method.description = description
            self.db_session.commit()

    def delete_math_method(self, math_method_id: int):
        method = self.get_math_method(math_method_id)
        if method:
            self.db_session.delete(method)
            self.db_session.commit()
            del self.methods[method.id]
