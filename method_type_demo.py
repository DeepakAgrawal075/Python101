class MyClass:
    # Instance method
    def instance_method(self):
        return f'Instance method called. self: {self}'

    # Class method
    @classmethod
    def class_method(cls):
        return f'Class method called. cls: {cls}'

    # Static method
    @staticmethod
    def static_method():
        return 'Static method called.'


# Create an instance of MyClass
obj = MyClass()

# Call the instance method
print(obj.instance_method())  # Output: Instance method called. self: <__main__.MyClass object at 0x...>

# Call the class method using the class
print(MyClass.class_method())  # Output: Class method called. cls: <class '__main__.MyClass'>

# Call the class method using the instance
print(obj.class_method())  # Output: Class method called. cls: <class '__main__.MyClass'>

# Call the static method using the class
print(MyClass.static_method())  # Output: Static method called.

# Call the static method using the instance
print(obj.static_method())  # Output: Static method called.
