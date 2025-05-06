from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False


    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def draw_line(self, line, fill_color="black"):
            line.draw(self.__canvas, fill_color)

    def close(self):
        self.__running = False
    
    


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1, p2):
        self.__p1_x = p1.x
        self.__p1_y = p1.y
        self.__p2_x = p2.x
        self.__p2_y = p2.y
    
    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.__p1_x, self.__p1_y,
            self.__p2_x, self.__p2_y,
            fill=fill_color, width=2
        )

