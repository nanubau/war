from rest_framework import status


class ErrorMessage(Exception):

    def __init__(self, msg):
        self.value = msg

    def __str__(self):
        return repr(self.value)


class ResponseException(Exception):

    def __init__(self, meta, response, status):
        self.response = response
        self.status = status
        self.meta = meta
        super(Exception, self).__init__(
            meta + ". Status Code: " + str(status))

    def __str__(self):
        return ("Response: {response}, Meta: {meta}, Status: {status}".format(response=self.response, meta=self.meta, status=self.status))


class BadRequestError(ResponseException):

    def __init__(self, param, param_value, response={}):
        meta = '%s : %s Not Found' % (str(param), str(param_value))
        super(BadRequestError, self).__init__(
            meta, response, status.HTTP_400_BAD_REQUEST)