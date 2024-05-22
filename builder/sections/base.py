from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass(kw_only=True)
class BaseTexDataClass(ABC):


    @abstractmethod
    def to_tex(self):
        raise NotImplementedError()