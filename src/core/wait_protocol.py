from typing import Protocol, Tuple, Any

class WaitProtocol(Protocol):
    def until(self, condition: Any): ...


Locator = Tuple[Any, str]
