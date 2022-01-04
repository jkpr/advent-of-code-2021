from __future__ import annotations
from dataclasses import dataclass
from re import findall


@dataclass
class Cube:
    x0: int
    x1: int
    y0: int
    y1: int
    z0: int
    z1: int

    def is_proper(self) -> bool:
        return self.x0 <= self.x1 and self.y0 <= self.y1 and self.z0 <= self.z1

    @property
    def volume(self):
        if self.is_proper():
            return (
                (self.x1 - self.x0 + 1)
                * (self.y1 - self.y0 + 1)
                * (self.z1 - self.z0 + 1)
            )
        return 0

    def __bool__(self):
        return self.volume > 0

    def __and__(self, other: Cube) -> Cube:
        x0 = max(self.x0, other.x0)
        x1 = min(self.x1, other.x1)
        y0 = max(self.y0, other.y0)
        y1 = min(self.y1, other.y1)
        z0 = max(self.z0, other.z0)
        z1 = min(self.z1, other.z1)
        cube = Cube(x0, x1, y0, y1, z0, z1)
        if cube.is_proper():
            return cube
        return None

    def __sub__(self, other: Cube) -> list[Cube]:
        i = self & other
        if not i:
            return [self]
        cubes = []
        if self.x0 < i.x0:
            cubes.append(Cube(self.x0, i.x0 - 1, self.y0, self.y1, self.z0, self.z1))
        if self.x1 > i.x1:
            cubes.append(Cube(i.x1 + 1, self.x1, self.y0, self.y1, self.z0, self.z1))
        if self.y0 < i.y0:
            cubes.append(Cube(i.x0, i.x1, self.y0, i.y0 - 1, self.z0, self.z1))
        if self.y1 > i.y1:
            cubes.append(Cube(i.x0, i.x1, i.y1 + 1, self.y1, self.z0, self.z1))
        if self.z0 < i.z0:
            cubes.append(Cube(i.x0, i.x1, i.y0, i.y1, self.z0, i.z0 - 1))
        if self.z1 > i.z1:
            cubes.append(Cube(i.x0, i.x1, i.y0, i.y1, i.z1 + 1, self.z1))
        return cubes


def get_cube_count(lines: list[str], instructions: int = None) -> int:
    cubes: list[Cube] = []
    for line in lines[slice(0, instructions)]:
        off_on = line.split()[0]
        coords = [int(i) for i in findall(r"-?\d+", line)]
        cube = Cube(*coords)
        new_cubes = []
        for c in cubes:
            new_cubes.extend(c - cube)
        if off_on == "on":
            new_cubes.append(cube)
        cubes = new_cubes
    return sum(c.volume for c in cubes)


def part1(lines: list[str]):
    return get_cube_count(lines, 20)


def part2(lines: list[str]):
    return get_cube_count(lines)
