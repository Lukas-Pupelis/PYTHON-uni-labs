from line import Line

def create_line(x1, y1, x2, y2):
    return Line(x1, y1, x2, y2)

def get_line_length(line):
    return line.length()

if __name__ == "__main__":
    line = create_line(0, 0, 3, 4)
    print(f"The length of the line is: {get_line_length(line)}")
