"""Module for currency exchange

This module provides several string parsing functions to implement a
simple currency exchange routine using an online currency service.
The primary function in this module is exchange."""

from urllib.request import urlopen
import string


def currency_response(currency_from, currency_to, amount_from):
    """Returns: a JSON string that is a response to a currency query.

    A currency query converts amount_from money in currency currency_from
    to the currency currency_to. The response should be a string of the form

        '{"from":"<old-amt>","to":"<new-amt>","success":true, "error":""}'

    where the values old-amount and new-amount contain the value and name
    for the original and new currencies. If the query is invalid, both
    old-amount and new-amount will be empty, while "success" will be followed
    by the value false.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""

    doc = urlopen('http://cs1110.cs.cornell.edu/2018fa/a1server.php?from=' +
                  currency_from + '&to=' + currency_to +
                  '&amt=' + str(amount_from))
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return jstr


def iscurrency(currency):
    """Returns: True if currency is a valid (3 letter code for a) currency.
    It returns False otherwise.

    Parameter currency: the currency code to verify
    Precondition: currency is a string."""

    list1 = list(currency)
    if type(currency) is not str:
        return False
    elif len(currency) != 3:
            return False
    else:
        for i in range(2):
            if list1[i] not in string.ascii_uppercase:
                return False
            else:
                return True


def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in
    currency currency_from to the currency currency_to. The value
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""

    j = currency_response(currency_from, currency_to, amount_from)
    stan = "0123456789."
    a = j.replace('"dst"', '!')
    b = ''

    for i in range(len(a)):
        if a[i] in stan:
            b = b + a[i]
        if a[i] is '!':
            b = b + ' '
        else:
            b = b

    listb = b.split(' ')
    amount_to = float(listb[1])
    return amount_to


def test_exchange():
    """test function exchange()"""
    assert exchange('USD', 'CAD', 1) == 1.30395
    assert exchange('USD', 'EUR', 1) == 0.886407


def test_iscurrency():
    """test function iscurrency()"""
    assert iscurrency('USD') is True
    assert iscurrency('usd') is False
    assert iscurrency('123') is False
    assert iscurrency('12345') is False


def test_currency_response():
    """test function currency_response"""
    assert currency_response('USD', 'CAD', 1) == \
        '{ "src" : "1 United States Dollar", \
        "dst" : "1.30395 Canadian Dollars", "valid" : true, "error" : "" }'
    assert currency_response('asd', 'cad', 1) == \
        '{ "src" : "", "dst" : "", "valid" : false, \
        "error" : "Source currency code is invalid." }'


def testAll():
    """test all cases"""
    test_exchange()
    test_iscurrency
    test_currency_response
    print("All tests passed")


def main():
    """main module"""
    testAll()
    currency_from = input()
    currency_to = input()
    amount_from = input()

if __name__ == '__main__':
    main()
