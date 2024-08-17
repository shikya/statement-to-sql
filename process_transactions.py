import re

from Transaction import Transaction, PDFData
from constants import TRANSACTION
from exceptions import MultipleTotalMentionedError, BalenceVerificationFailedError, WithDrawalVerificationFailedError, \
    DepositeVerificationFailedError, CalculationMismatchError

from regex_utilities import get_balance_forwards, get_total_balance

PRECISION = 2

def process_transactions(text_elements_single) -> dict:
    bank_tran = re.finditer(TRANSACTION, text_elements_single)
    balance_forward = get_balance_forwards(text_elements_single)
    total_balance = get_total_balance(text_elements_single)
    all_transactions = []
    # print(get_balance_forwards(text_elements_single))
    # print(get_total_balance(text_elements_single))

    balance = balance_forward
    index = 0
    _all_debit = 0
    _all_credit = 0

    for t in bank_tran:
        transaction_dict = t.groupdict()
        # print(transaction_dict)
        _transaction = float(transaction_dict['transaction'].replace(',', ''))
        _balance = float(transaction_dict['balance'].replace(',', ''))
        # print(f"balance: {balance}, _transaction: {_transaction}, _balance: {_balance}")
        # print(f"difference: {round(balance - _transaction, PRECISION)}, addition: {round(balance + _transaction, PRECISION)}")
        if round(balance - _transaction, 3) == _balance:
            _all_debit = round(_all_debit + _transaction, PRECISION)
            balance = _balance
            _tran = Transaction(transaction_date=transaction_dict['valuedate'],
                                settlement_date=transaction_dict['date'],
                                description=transaction_dict['description'],
                                transaction=transaction_dict['transaction'],
                                balance=transaction_dict['balance'], is_debit=True)
            all_transactions.append(_tran)
        elif round(balance + _transaction, 2) == _balance:
            _all_credit = round(_all_credit + _transaction, PRECISION)
            balance = _balance
            # print("credit")
            _tran = Transaction(transaction_date=transaction_dict['valuedate'],
                                settlement_date=transaction_dict['date'],
                                description=transaction_dict['description'],
                                transaction=transaction_dict['transaction'],
                                balance=transaction_dict['balance'], is_debit=False)
            all_transactions.append(_tran)
        else:
            raise CalculationMismatchError()

    # print(f"balance: {balance}, _all_debit: {_all_debit}, _all_credit: {_all_credit}")
    # print(f"total_balance: {total_balance}")

    if balance != total_balance.balance:
        raise BalenceVerificationFailedError()
    if _all_debit != total_balance.withdrawal:
        raise WithDrawalVerificationFailedError()
    if _all_credit != total_balance.deposit:
        raise DepositeVerificationFailedError()

    return PDFData(transactions=all_transactions, total=total_balance, balance_forward=balance_forward)

