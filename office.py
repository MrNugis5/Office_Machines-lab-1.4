from abc import ABC, abstractmethod


# 🔹 LIIDESED
class Printer(ABC):
    @abstractmethod
    def print(self, dokument):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan(self, dokument):
        pass


# 🔹 SEADMED
class MyPrinter(Printer):
    """Printer class."""
    def print(self, dokument):
        for l in dokument:
            print(l)


class Photocopier(Printer, Scanner):
    """Photo"""
    def print(self, dokument):
        for l in dokument:
            print(l)
    
    def scan(self, dokument):
        print("scanning", dokument)


# 🔹 MULTIFUNKTSIONAALNE SEADE (PEAMINE PARANDUS)
class MultiFunctionMachine:
    """Multi printer"""
    def __init__(self, printer: Printer, scanner: Scanner):
        self.printer = printer
        self.scanner = scanner

    def print(self, dokument):
        return self.printer.print(dokument)
    
    def scan(self, dokument):
        return self.scanner.scan(dokument)


if __name__ == "__main__":

    printer = MyPrinter()
photocopier = Photocopier()

printer.print("Hello from printer")

photocopier.print("Copy this document")
photocopier.scan("Scanned document")

mfm = MultiFunctionMachine(printer, photocopier)
mfm.print("Delegated print")
mfm.scan("Delegated scan")
