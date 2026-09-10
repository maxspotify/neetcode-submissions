class TextProcessor:
    # Implement method overloading for format_text method
    def format_text(self, arg1, arg2=None):
        if not arg2:
            return arg1.upper()
        return arg1 + arg2



# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
