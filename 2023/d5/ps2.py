"""
Puzzle input has info for:
    Seeds that need to be planted
    Type of soil to be used with each kind of seed
    Type of fertilizer to be used with each kind of soil
    Type of water to be used with each kind of fertilizer
    And a bunch more stuff

Same numbers from one category can mean a diffrent thing in another category
    soil 123 and fertilizer 123 aren't necessarily related to each other

Puzzle input info:
    1) listing which seeds need to be planted: seeds 79, 14, 55, and 13
    2) The rest of almanac contains a list of maps which describe how to convert numbers
       from a source category(x) into numbers in a destination category(Y)
       Ex -> How to convert seed number to soil number and so on
    3) X(source)-to-Y(destination) map:
        means -> type of Y needed for X
    4) Each line within a map contains three numbers
        destination range start(DRS)
        source range start(SRS)
        range length(RL)
        [DRS + i for i in range(0, RL)]
        [SRS + i for i in range(0, RL)]

        [(SRS[i], DRS[i]) for i in range(len(DRS))]
    Any source numbers that aren't mapped correspond to the same destination number
    So, seed number 10 corresponds to soil number 10

Every type of seed, soil, fertilizer etc is identified with a number

Goal -> Find the lowest location Number
Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
func(map: str, required_values: list) -> mapping for required values
seeds = []
a = seeds
while(!location, i)
    a = func(i, a)
ans = seed[a.find(min(a))]
"""
