from abc import ABC, abstractmethod


class IIocContainerConfigInfrastructure(ABC):
    @classmethod
    @abstractmethod
    def build_ioc_container(cls):
        pass
