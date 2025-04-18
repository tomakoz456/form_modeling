class body_line:
    orientation = "horizontal"
    description = "A line of text in the body of a document."
    
    def __init__(self, line):
        self.line = line

    def __repr__(self):
        return f"body_line({self.line})"

    def __str__(self):
        return self.line