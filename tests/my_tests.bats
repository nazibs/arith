load harness

@test "test-1" {
  check '2 * 7 + 3' '17'
}

@test "test-2" {
  check '3 + 7 * 2' '17'
}

@test "no-space" {
  check '2+3' '5'
}

@test "single-space-neg-num" {
  check '3 + -2' '1'
}

@test "multiple-space" {
  check '3   +       2' '5'
}

@test "sub-neg-num" {
  check '-1 - -3' '2'
}

@test "multiple-digits" {
  check '11 + 3' '14'
}

@test "multiple-operations-1" {
  check '9 - 5 + 3 + 11' '18'
}

@test "multiple-operations-2" {
  check '10 + 1 + 2 - 3 + 4 + 6 - 15' '5'
}

@test "multiple-operations-divide-1" {
  check '10 * 4  * 2 * 3 / 8' '30.0'
}

@test "multiple-operations-divide-2" {
  check '14 + 2 * 3 - 6 / 2' '17.0'
}

@test "multiple-operations-divide-3" {
  check '4 + 2 * 3 - 6 / 2' '7.0'
}

