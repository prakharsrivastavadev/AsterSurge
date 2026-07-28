"""
AsterSurge Loader

Version: 0.2.0
"""

import importlib
import pkgutil


class Loader:
    """
    Dynamic module loader.
    """

    @staticmethod
    def import_module(module_name: str):
        """
        Import a module by name.
        """
        return importlib.import_module(module_name)

    @staticmethod
    def load_package(package):
        """
        Load all modules in a package.
        """

        modules = {}

        for _, name, _ in pkgutil.iter_modules(package.__path__):
            full_name = f"{package.__name__}.{name}"
            modules[name] = importlib.import_module(full_name)

        return modules

    @staticmethod
    def load_class(module_name: str, class_name: str):
        """
        Load a class from a module.
        """

        module = importlib.import_module(module_name)

        return getattr(module, class_name)

    @staticmethod
    def exists(module_name: str):
        """
        Check whether a module exists.
        """

        try:
            importlib.import_module(module_name)
            return True
        except ModuleNotFoundError:
            return False
