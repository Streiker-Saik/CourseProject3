from abc import ABC, abstractmethod
from typing import Any, Dict, List


class AbsApi(ABC):
    """
    Абстрактный класс работы с API
        connect(self) -> Dict[Any, Any]:
            Метод подключения к API
    """

    @abstractmethod
    def connect(self) -> Dict[Any, Any]:
        """Метод подключения к API"""
        pass
