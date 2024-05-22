from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(kw_only=True)
class BaseTexDataClass(ABC):
    @abstractmethod
    def to_tex(self):
        raise NotImplementedError()
