from leave import leave_status

def test_sufficient_leave():
    assert leave_status(20, 5) == "Sufficient Leave"

def test_low_leave():
    assert leave_status(20, 15) == "Low Leave Balance"

def test_no_leave():
    assert leave_status(10, 10) == "No Leave Available"