
# Copyright (C) 2019-2023 Cognizant Digital Business, Evolutionary AI.
# All Rights Reserved.
# Issued under the Academic Public License.
#
# You can be released from the terms, and requirements of the Academic Public
# License by purchasing a commercial license.
# Purchase of a commercial license is mandatory for any use of the
# leaf-server-common SDK Software in commercial settings.
#
# END COPYRIGHT

class RequestLogger():
    """
    An interface defining an API for services to call for logging
    the beginning and end of servicing their requests.
    """

    def start_request(self, caller, requestor_id, context):
        """
        Called by services to mark the beginning of a request
        inside their request methods.
        :param caller: A String representing the method called
                Stats will be kept as to how many times each method is called.
        :param requestor_id: A String representing other information about
                the requestor which will be logged in a uniform fashion.
        :param context: a grpc.ServicerContext
        :return: The RequestLoggerAdapter to be used throughout the
                processing of the request
        """
        raise NotImplementedError()

    def finish_request(self, caller, requestor_id, request_log):
        """
        Called by client services to mark the end of a request
        inside their request methods.
        :param caller: A String representing the method called
        :param requestor_id: A String representing other information about
                the requestor which will be logged in a uniform fashion.
        :param request_log: The RequestLoggerAdapter to be used throughout the
                processing of the request
        """
        raise NotImplementedError()
