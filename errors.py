class Error(Exception):
    """
        Base class for other errors.
    """
    pass


class ValueTooLargeError(Error):
    """
        Raised when the parameter or input value is too large.
    """

    def __init__(self, errorCausingVariableName, errorCausingVariableValue, maximumValue):
        # Contains the error causing variable name
        self.errorCausingVariableName = errorCausingVariableName

        # Contains the error causing variable.
        self.errorCausingVariableValue = errorCausingVariableValue

        # Contains the maximum value that is allowed.
        self.maximumValue = maximumValue


class ValueTooSmallError(Error):
    """
        Raised when parameter or input value is too small.
    """

    def __init__(self, errorCausingVariableName, errorCausingVariableValue, minimumValue):
        # Contains the error causing variable name
        self.errorCausingVariableName = errorCausingVariableName

        # Contains the error causing variable.
        self.errorCausingVariableValue = errorCausingVariableValue

        # Contains the maximum value that is allowed.
        self.minimumValue = minimumValue


class ExpectsIntError(Error):
    """
        Raised when parameter or input value should be an integer but isn't.
    """

    def __init__(self, errorCausingVariableName, errorCausingVariableValue):
        # Contains the error causing variable name
        self.errorCausingVariableName = errorCausingVariableName

        # Contains the error causing variable.
        self.errorCausingVariableValue = errorCausingVariableValue


class ExpectsStringError(Error):
    """
        Raised when parameter or input value should be a string but isn't.
    """

    def __init__(self, errorCausingVariableName, errorCausingVariableValue):
        # Contains the error causing variable name
        self.errorCausingVariableName = errorCausingVariableName

        # Contains the error causing variable.
        self.errorCausingVariableValue = errorCausingVariableValue


class HexStringTooShortError(Error):
    """
        Raised when parameter or input hex string is too short.
    """

    def __init__(self, errorCausingVariableName, errorCausingVariableValue, minimumLength):
        # Contains the error causing variable name
        self.errorCausingVariableName = errorCausingVariableName

        # Contains the error causing variable.
        self.errorCausingVariableValue = errorCausingVariableValue

        # Contains the maximum value that is allowed.
        self.minimumLength = minimumLength


class HexStringTooLongError(Error):
    """
        Raised when parameter or input hex string is too long.
    """

    def __init__(self, errorCausingVariableName, errorCausingVariableValue, maximumLength):
        # Contains the error causing variable name
        self.errorCausingVariableName = errorCausingVariableName

        # Contains the error causing variable.
        self.errorCausingVariableValue = errorCausingVariableValue

        # Contains the maximum value that is allowed.
        self.maximumLength = maximumLength


class HexStringFormatError(Error):
    """
        Raised when hex string hasn't the right format.
    """

    def __init__(self, errorCausingVariableName, errorCausingVariableValue):
        # Contains the error causing variable name
        self.errorCausingVariableName = errorCausingVariableName

        # Contains the error causing variable.
        self.errorCausingVariableValue = errorCausingVariableValue
