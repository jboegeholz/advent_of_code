# Day 04 Part 2

## Ausgangspunkt
Pointer Karte   Anzahl  Gewinne
        1       1       4
        2       1       2
        3       1       2
        4       1       2
        5       1       0
        6       1       0
## Erster Durchlauf
Pointer Karte   Anzahl  Gewinne
 ->     1       1       4
        2       1+1     2
        3       1+1     2
        4       1+1     2
        5       1+1     0
        6       1       0

Pointer Karte   Anzahl  Gewinne
 ->     1       1       4
        2       2       2
        3       2       2
        4       2       2
        5       2       0
        6       1       0

## Zweiter Durchlauf
Pointer Karte   Anzahl  Gewinne
        1       1       4
->      2       2       2
        3       2+2     2
        4       2+2     2
        5       2       0
        6       1       0

Pointer Karte   Anzahl  Gewinne
        1       1       4
->      2       2       2
        3       4       2
        4       4       2
        5       2       0
        6       1       0

## Dritter Durchlauf
Pointer Karte   Anzahl  Gewinne
        1       1       4
        2       2       2
->      3       4       2
        4       4+4     2
        5       2+4     0
        6       1       0

Pointer Karte   Anzahl  Gewinne
        1       1       4
        2       2       2
->      3       4       2
        4       8       2
        5       6       0
        6       1       0

## Vierter Durchlauf
Pointer Karte   Anzahl  Gewinne
        1       1       4
        2       2       2
        3       4       2
->      4       8       2
        5       6+8     0
        6       1       0

Pointer Karte   Anzahl  Gewinne
        1       1       4
        2       2       2
        3       4       2
->      4       8       2
        5       14      0
        6       1       0