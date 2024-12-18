from abc import ABC, abstractmethod

# Step 1: Define the base Plugin class
class Plugin(ABC):
    """
    Abstract base class for all plugins.
    All plugins must implement the `run` method.
    """
    @abstractmethod
    def run(self, *args, **kwargs):
        pass


# Step 2: Create the PluginManager class
class PluginManager:
    """
    Manages the registration and execution of plugins.
    """
    def __init__(self):
        self.plugins = {}

    def register_plugin(self, name, plugin):
        """
        Registers a plugin with a unique name.
        """
        if not issubclass(type(plugin), Plugin):
            raise TypeError(f"Plugin must inherit from Plugin base class.")
        self.plugins[name] = plugin

    def run_plugin(self, name, *args, **kwargs):
        """
        Executes a registered plugin by its name.
        """
        if name not in self.plugins:
            raise ValueError(f"No plugin registered with name: {name}")
        plugin = self.plugins[name]
        print(f"Running plugin: {name}")
        return plugin.run(*args, **kwargs)

    def list_plugins(self):
        """
        Lists all registered plugins.
        """
        return list(self.plugins.keys())


# Step 3: Implement example plugins
class HelloWorldPlugin(Plugin):
    """
    A simple plugin that prints a hello message.
    """
    def run(self, *args, **kwargs):
        return "Hello, World!"


class AddNumbersPlugin(Plugin):
    """
    A plugin that adds two numbers.
    """
    def run(self, a, b):
        return f"The sum of {a} and {b} is {a + b}"


class ReverseStringPlugin(Plugin):
    """
    A plugin that reverses a string.
    """
    def run(self, string):
        return f"Reversed string: {string[::-1]}"


# Step 4: Demonstrate the Plugin System
if __name__ == "__main__":
    # Create the PluginManager
    manager = PluginManager()

    # Register plugins
    manager.register_plugin("hello_world", HelloWorldPlugin())
    manager.register_plugin("add_numbers", AddNumbersPlugin())
    manager.register_plugin("reverse_string", ReverseStringPlugin())

    # List available plugins
    print("Available plugins:", manager.list_plugins())

    # Run the plugins
    print(manager.run_plugin("hello_world"))
    print(manager.run_plugin("add_numbers", 5, 7))
    print(manager.run_plugin("reverse_string", "Python"))
