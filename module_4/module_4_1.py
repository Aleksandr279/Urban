from fake_math import divide as fmd
from true_math import divide as tmd

if __name__ == "__main__":
    fmd(69, 3)
    fmd(3, 0)
    tmd(49, 7)
    tmd(15, 0)

print(fmd(69, 3))
print(fmd(3, 0))
print(tmd(49, 7))
print(tmd(15, 0))

