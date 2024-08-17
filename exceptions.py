class MultipleTotalMentionedError(BaseException):
    pass


class PDFVerificationError(BaseException):
    pass


class CalculationMismatchError(BaseException):
    pass

class BalenceVerificationFailedError(PDFVerificationError):
    pass


class WithDrawalVerificationFailedError(PDFVerificationError):
    pass


class DepositeVerificationFailedError(PDFVerificationError):
    pass
