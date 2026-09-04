import pytest

from flight_calculator import calculate_flight_time


def test_zero_payload_returns_base_flight_time():
    assert calculate_flight_time(0) == 180


@pytest.mark.parametrize(
    ("weight_grams", "expected_flight_time"),
    [
        (100, 170),
        (500, 130),
        (123.5, 167.65),
    ],
)
def test_calculates_flight_time_for_valid_weights(
    weight_grams, expected_flight_time
):
    assert calculate_flight_time(weight_grams) == pytest.approx(
        expected_flight_time
    )


def test_flight_time_is_zero_at_weight_limit():
    assert calculate_flight_time(1800) == 0


def test_flight_time_does_not_become_negative():
    assert calculate_flight_time(2000) == 0


def test_negative_weight_raises_value_error():
    with pytest.raises(
        ValueError,
        match="Weight cannot be negative",
    ):
        calculate_flight_time(-1)