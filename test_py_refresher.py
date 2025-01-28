from py_refresher import smallest_positive

def test_smallest_positive_when_float():
  # given
  input = [.2, 5, 3, -.1, 7, 7, 6]
  # when
  result = smallest_positive(input)
  # then
  assert result == 0.2


def test_smallest_positive_when_integer():
  # given
  input = [4, -6, 7, 2, -4, 10]
  # when
  result = smallest_positive(input)
  # then
  assert result == 2

