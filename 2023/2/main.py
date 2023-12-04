from typing import Self, NamedTuple
import re
import operator
import functools

gid_regex = re.compile("Game ([0-9]+)")
vals_regex = re.compile("([0-9]+) ([a-z]+)")


class Observation(NamedTuple):
    red: int = 0
    blue: int = 0
    green: int = 0

    def __add__(self, other: Self) -> Self:
        return Observation(*(max(x) for x in zip(self, other)))

    @property
    def power(self) -> int:
        return functools.reduce(operator.mul, self)


def test_possible(reference: Observation, testee: Observation) -> bool:
    return all(y <= x for x, y in zip(reference, testee))


def parse_line(line: str):
    game_section, value_section = line.split(":")
    game_id = gid_regex.match(game_section).group(1)
    game_id = int(game_id)
    observations = [
        Observation(**{k: int(v) for v, k in vals_regex.findall(part)})
        for part in value_section.split(";")
    ]
    return (game_id, functools.reduce(operator.add, observations))


def main():
    reference = Observation(red=12, blue=14, green=13)
    possible_ids_sum = 0
    power_sum = 0
    with open("input", encoding="utf-8") as f:
        for line in f:
            game_id, obs = parse_line(line)
            pos = test_possible(reference, obs)
            print(
                f"total for game {game_id}: {obs}. Power {obs.power}. Possible: {pos}"
            )
            power_sum += obs.power
            if pos:
                possible_ids_sum += game_id
    print(f"{possible_ids_sum}; power sum: {power_sum}")


if __name__ == "__main__":
    main()
