import base

EXPECTED = [
    """Hello world from user mode program!
Test hello_world OK!""",
    """3\^10000=5079
3\^20000=8202
3\^30000=8824
3\^40000=5750
3\^50000=3824
3\^60000=8516
3\^70000=2510
3\^80000=9379
3\^90000=2621
3\^100000=2749
Test power OK!""",
    """string from data section
strinstring from stack section
strin
Test write1 OK!""",
]

TEMP = [
    """Test write0 OK!""",
]

if __name__ == '__main__':
    base.test(EXPECTED + TEMP)
