import os


class CleanUpFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        # This method is called when entering the 'with' block.
        # You can optionally open the file here if needed.
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # This method is called when exiting the 'with' block.
        # Remove the file if it exists.
        if os.path.exists(self.filename):
            os.remove(self.filename)


# Example usage:
with CleanUpFile("file.txt"):
    with open("file.txt", "w") as file:
        file.write("Hello Mate!")

# After the 'with' block, the file "file.txt" will be removed.
