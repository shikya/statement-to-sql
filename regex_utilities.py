import re

from Total import Total
from constants import BALANCE_FORWARD, TOTAL
from exceptions import MultipleTotalMentionedError


def get_balance_forwards(pdf_text) -> float:
    """Takes the pdf text and returns the last balence forward in number"""

    bf_express = re.finditer(BALANCE_FORWARD, pdf_text)
    bf_string = ""
    for bf in bf_express:
        bf_string = bf.groupdict()['balance']
    bf_string = bf_string.replace(',', '')
    balance_forward = float(bf_string)
    return balance_forward


def get_total_balance(pdf_text) -> Total:
    """Takes the pdf text and returns the total balance in number"""

    total_express = re.finditer(TOTAL, pdf_text)
    index = 0
    for tb in total_express:
        if index > 0:
            raise MultipleTotalMentionedError()
        deposit_string = tb.groupdict()['deposit'].replace(',', '')
        withdrawal_string = tb.groupdict()['withdrawal'].replace(',', '')
        balance_string = tb.groupdict()['balance'].replace(',', '')
        index += 1
    return Total(float(deposit_string), float(withdrawal_string), float(balance_string))
