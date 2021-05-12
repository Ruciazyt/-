from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractFactory:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractFactory:
        pass


class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractFactory:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractFactory:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractFactory:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractFactory:
        return ConcreteProductB2()


class AbstractProductA(ABC):
    @abstractmethod
    def useful_function_a(self) -> str:
        pass


class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        return 'This is product A1'


class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return 'This is product A2'


class AbstractProductB(ABC):
    @abstractmethod
    def useful_function_b(self) -> str:
        pass


class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self) -> str:
        return 'This is product B1'


class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return 'This is product B2'


def client_code(factory: AbstractFactory) -> None:
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    print(product_a.useful_function_a())
    print(product_b.useful_function_b())


if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteFactory2())
