import sys
from logic_oop import Container


class Main:
    def start(self):
        if len(sys.argv) != 3:
            return print("Вы не ввели нужные аргументы.")

        input_name = sys.argv[1]
        output_name = sys.argv[2]

        c = Container()
        c.input_shapes(input_name)
        c.output(output_name)


if __name__ == '__main__':
    print("START")
    m = Main()
    m.start()
    print("STOP")
