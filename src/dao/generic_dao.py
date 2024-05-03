from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

T = TypeVar('T')


class GenericDao(Generic[T], ABC):

    @abstractmethod
    def save(self, t: T) -> T:
        pass
    
    @abstractmethod
    def find_by_id(self, id) -> Optional[T]:
        pass
