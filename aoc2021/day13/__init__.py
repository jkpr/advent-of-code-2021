from dataclasses import dataclass, replace


@dataclass(frozen=True)
class Point:
    x: int
    y: int


@dataclass
class Fold:
    orientation: str
    line_value: int

    def apply(self, point: Point) -> Point:
        point_placement = getattr(point, self.orientation)
        if point_placement < self.line_value:
            return point
        else:
            diff = point_placement - self.line_value
            return replace(point, **{self.orientation: point_placement - 2 * diff})


@dataclass
class Origami:
    points: set[Point]

    def do_fold(self, fold: Fold) -> "Origami":
        new_points = set(fold.apply(point) for point in self.points)
        return Origami(new_points)

    def display(self):
        max_x = max(point.x for point in self.points)
        max_y = max(point.y for point in self.points)
        for y in range(max_y + 1):
            for x in range(max_x + 1):
                if Point(x, y) in self.points:
                    print("#", end="")
                else:
                    print(" ", end="")
            print()

    def __len__(self):
        return len(self.points)


def setup(lines: list[str]) -> tuple[Origami, list[Fold]]:
    nums, rules = "\n".join(lines).split("\n\n")
    points = set()
    for num in nums.splitlines():
        point = Point(*[int(i) for i in num.split(",")])
        points.add(point)
    origami = Origami(points)

    folds = []
    for rule in rules.splitlines():
        direction, value = rule.split()[-1].split("=")
        fold = Fold(direction, int(value))
        folds.append(fold)

    return origami, folds


def part1(lines: list[str]):
    origami, folds = setup(lines)
    return len(origami.do_fold(folds[0]))


def part2(lines: list[str]):
    origami, folds = setup(lines)
    for fold in folds:
        origami = origami.do_fold(fold)
    origami.display()
