import itertools
def test_comb():
    comb = list(itertools.combinations([i for i in range(2, 15) ], 5))
    assert len(comb) == 1287

def test_perm():
    comb = list(itertools.permutations([i for i in range(2, 15) ], 5))
    assert len(comb) == 154440