"""Test your functions from Week 2 assignment.
"""
import preclass_assignment.functions as fxn


def test_greet(capsys):
    """Check that the greet function prints as expected"""
    # given
    name = 'world'  # who should we greet?
    # when
    fxn.greet(name)  # greet them
    captured = capsys.readouterr()  # capture what would have been printed to screen
    # then
    assert captured.out == 'Hello, world!\n'  # check that the greeting was what we expect


def test_goldilocks(capsys):
    """Check goldilocks returns expected output"""
    # given
    # when
    # then
    assert False  # TODO! Update the contents of this function so it correctly tests goldilocks


def test_square_list():
    """Check square_list returns expected output"""
    # given
    inp = [1, 2, 3]  # test input to function
    exp_out = [1, 4, 9]  # expected output
    # when
    out = fxn.square_list(inp)  # actual output
    # then
    assert exp_out == out  # throw error if actual and expected output don't match
    
    
def test_fibonacci_stop():
    """Check fibonacci functions works as expected."""
    # given
    inp = 6
    # when
    exp_fib = [1,1,2,3,5]
    # then
    out = fxn.fibonacci_stop(inp)
    assert exp_fib == out
     # TODO! Update the contents of this function so it correctly tests fibonacci_stop


def test_clean_pitch():
    """Check clean_pitch works as expected."""
    # given
    inp_meas = [1, 2, -45, 7]
    # given
    inp_sig = [0, 0 , 1, 0]
    # when
    exp_meas_out = [1, 2, -999, 7]
    # then
    assert exp_meas_out == fxn.clean_pitch(inp_meas,inp_sig)
