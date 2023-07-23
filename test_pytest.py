import pytest


def calculate_sum(a, b):
    return a + b


def test_calculate_sum():
    assert calculate_sum(2, 3) == 5
    assert calculate_sum(-5, 8) == 3
    assert calculate_sum(0, 0) == 0

    assert calculate_sum(1000000, 2000000) == 3000000
    assert calculate_sum(-999999, 999999) == 0

    assert calculate_sum(-5, -10) == -15
    assert calculate_sum(-100, -200) == -300

    assert calculate_sum(7, 9) == calculate_sum(9, 7)

    with pytest.raises(TypeError):
        calculate_sum(10, "20")
    with pytest.raises(TypeError):
        calculate_sum("30", 40)

    assert calculate_sum(3.5, 2.5) == 6.0
    assert calculate_sum(0.1, 0.2) == pytest.approx(0.3, rel=1e-6)
    
