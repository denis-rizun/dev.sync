from abc import ABC, abstractmethod


class ISSHService(ABC):

    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def run_commands(self, shell_script: str, timeout: int = 300) -> tuple[bool, str]:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

    @abstractmethod
    def execute(self, shell_script: str, timeout: int = 300) -> tuple[bool, str]:
        pass
