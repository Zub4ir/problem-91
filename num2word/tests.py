from num2word import num2word

def test_baseline():

    assert num2word('The pump is 536 deep underground.') == 'five hundred and thirty-six'

    assert num2word('We processed 9121 records. ') == 'nine thousand, one hundred and twenty-one'


def test_additional():

    assert 2 == 2
