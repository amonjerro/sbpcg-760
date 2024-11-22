from sbpcg import SanityTester


if __name__ == '__main__':
    cases = [
        [3,480,6,7,(20, 0),(10, 3),(11, 2),(14, 2)],
        [0,830,7,5,(17, 3),(15, 1),(13, 0),(11, 0)]
    ]
    opponent = [0,650,7,4,(30, 0),(10, 1),(10, 2),(13, 3)]
    tester = SanityTester(opponent, cases)
    tester.run_cases()