from num2word import num2word

def test_baseline():

    assert num2word('The pump is 536 deep underground.') == 'five hundred and thirty-six'

    assert num2word('We processed 9121 records.') == 'nine thousand, one hundred and twenty-one'

    assert num2word('Variables reported as having a missing type #65678.') == 'number invalid'

    assert num2word('Interactive and printable 10022 ZIP code.') == 'ten thousand and twenty-two'

    assert num2word('The database has 66723107008 records.') == 'sixty-six billion, seven hundred and twenty-three million, one hundred and seven thousand and eight'
    
    assert num2word('I received 23 456,9 KGs.') == 'number invalid'


def test_some_edge_cases():

    assert num2word('0') == 'zero'

    assert num2word('00000') == 'zero'

    assert num2word('1') == 'one'

    assert num2word('001') == 'one'

    assert num2word('001') == 'one'

    assert num2word('00100') == 'one hundred'

    assert num2word('100') == 'one hundred'

    assert num2word('100100') == 'one hundred thousand and one hundred'