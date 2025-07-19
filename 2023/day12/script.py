from pathlib import Path


ROOT_DIR = Path(__file__).parent.parent


def part1():
    with open(ROOT_DIR / "data" / "day12_input.txt", "r") as f:
        input_lines = f.readlines()


def part2():
    pass


if __name__ == "__main__":
    part1()
    part2()
