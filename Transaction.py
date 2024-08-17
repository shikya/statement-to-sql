from dataclasses import dataclass

from Total import Total


@dataclass
class Transaction:
    transaction_date: str
    settlement_date: str
    description: str
    transaction: float
    balance: float
    is_debit: bool

@dataclass
class PDFData:
    transactions: [Transaction]
    total: Total
    balance_forward: float
