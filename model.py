import random
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Tuple, Union, Iterable


class ClassifierModel(ABC):

    @abstractmethod
    def fit(self, X: Iterable, y= Iterable) -> None:
        pass

    @abstractmethod
    def predict(self, X: Iterable) -> List:
        pass


class RandomBinaryClassifierModel(ClassifierModel):
    
    def __init__(self, random_state: Optional[int] = None) -> None:
        self.random_state = random_state
    
    def fit(self, X: Iterable, y: Iterable) -> ClassifierModel:
        return self
    
    def predict(self, X: Iterable) -> List:
        random.setstate(self.random_state)
        return [random.choice([0, 1]) for _ in range(len(X))]