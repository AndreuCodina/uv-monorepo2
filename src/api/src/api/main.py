import os

from api.foo.foo import Foo
from domain.domain_printer import DomainPrinter


def main() -> None:
    print(f"Current directory: {os.getcwd()}")
    DomainPrinter().print()
    Foo().print()


if __name__ == "__main__":
    main()
