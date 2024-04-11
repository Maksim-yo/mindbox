from abc import ABC, abstractmethod


class IFigure(ABC):

    @abstractmethod
    def calculate_square(self):
        pass

