from api.foo.foo import Foo
from domain.domain_printer import DomainPrinter


def main() -> None:
    DomainPrinter().print()
    Foo()


if __name__ == "__main__":
    main()
