import calc


def test_load_data() :
    inputs, targets = load_data("./data.json")
    print(inputs)
    for i in targets:
        print(i)
        assert (0 <= i <= 9)


print("all test cases passed")
