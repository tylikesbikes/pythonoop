"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=1):
        """
        initialize class w/starting value
        """
        self.start = start
        self.current = start-1

    def reset(self):
        """
        reset class's 'current' value based on the original start parameter provided in __init__
        """
        self.current=self.start-1

    def generate(self):
        """
        return 'current', increment by one for next iteration
        """
        self.current += 1
        return self.current

    def __repr__(self):
        """describe this object"""
        return f"SerialGenerator:  start = {self.start}, current = {current}"
        
        