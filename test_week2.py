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
    bed_size=180
    # when
    fxn.goldilocks(bed_size)
    captured=capsys.readouterr()
    # then
    assert captured.out == "Too large!\n"
    #assert False  # TODO! Update the contents of this function so it correctly tests goldilocks


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
    result = fxn.fibonacci_stop(50)
    # when
    exp_out=[1, 1, 2, 3, 5, 8, 13, 21, 34]
    # then
    assert result==exp_out  # TODO! Update the contents of this function so it correctly tests fibonacci_stop


def test_clean_pitch():
    """Check clean_pitch works as expected."""
    # given
    pitch_angles = [30, 95, -10, 60, 45]
    status_signals = [0, 1, 1, 0, 0]
    # when
    result = fxn.clean_pitch(pitch_angles, status_signals)
    # then
    exp_out = [30, -999, -999, 60, 45]
    assert result == exp_out
    # assert False  # TODO! Update the contents of this function so it correctly tests clean_pitch
