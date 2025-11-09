import Lab2.bmi as bmi

# Follow the same nameing convention
def test_bmi_normal_weight():
    result = bmi.calculate_bmi(1.75, 70)
    assert result == 0

def test_bmi_over_weight():
    result = bmi.calculate_bmi(1.75, 85)
    assert result == 1

def test_bmi_under_weight():
    result = bmi.calculate_bmi(1.75, 50)
    assert result == -1


# The AAA pattern in Testing

# The Three Phases

# 1. Arrange 
# Set up the test conditions
# Prepare the input data and prerequisites

# 2. Act
# Call the function/method you want to test
# This is usually a single line

# 3. Assert
# Verify the results
# Check the actual output matches the expected output
# Use assertions to confirm correctness.