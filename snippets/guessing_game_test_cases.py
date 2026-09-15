def calculate_score(secret, guess):
    if guess == secret:
        return 100
    else:
        difference = secret - guess
        score = max(0, 100 - abs(difference) * 10)
        return score

def test_code():
    # Test Case 1: Full-score test
    # arrange
    secret_number = 42
    guessed_number = 42

    # act
    score = calculate_score(secret_number, guessed_number)

    # assert
    expected_score = 100
    print(score)
    if score == expected_score:
        print("test 1 passed")
    else:
        print("test 1 failed")

    # Test Case 2: Maximum difference:
    secret_number = 42
    guessed_number = 32

    # act
    score = calculate_score(secret_number, guessed_number)
    print(score)

    # assert
    expected_score = 0
    assert score == expected_score
    print("Test case 2 passed")

    # Test Case 3: Maximum difference + 1:
    secret_number = 42
    guessed_number = 31

    # act
    score = calculate_score(secret_number, guessed_number)
    print(score)

    # assert
    expected_score = 0
    if score == expected_score:
        print("test 3 passed")
    else:
        print("test 3 failed")

    # Test Case 4: Maximum larger difference:
    secret_number = 42
    guessed_number = 52

    # act
    score = calculate_score(secret_number, guessed_number)
    print(score)

    # assert
    expected_score = 0
    if score == expected_score:
        print("test 4 passed")
    else:
        print("test 4 failed")


test_code()
