# coding: utf-8

from __future__ import absolute_import, division

import contextlib
import copy
import json
import logging
import multiprocessing
import sys
import urllib3
import http.client

from aspose_barcode_cloud.rest import RESTClientObject


class Configuration(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Ref: https://github.com/swagger-api/swagger-codegen
    Do not edit the class manually.
    """

    _default = None

    def __init__(
        self,
        client_id=None,
        client_secret=None,
        access_token=None,
        host=None,
        token_url="https://api.aspose.cloud/connect/token",
    ):
        """Constructor"""
        if self._default:
            for key in self._default.__dict__:
                self.__dict__[key] = copy.copy(self._default.__dict__[key])
            return

        # Default Base url
        self.host = host or "https://api.aspose.cloud/v3.0"
        # Temp file folder for downloading files
        self.temp_folder_path = None

        # Authentication Settings
        # dict to store API key(s)
        self.api_key = {}
        # dict to store API prefix (e.g. Bearer)
        self.api_key_prefix = {}
        # function to refresh API key if expired
        self.refresh_api_key_hook = None
        # Username for HTTP basic authentication
        self.username = ""
        # Password for HTTP basic authentication
        self.password = ""

        # access token for OAuth
        self._access_token = access_token
        self._client_id = client_id
        self._client_secret = client_secret
        self._token_url = token_url

        # Logging Settings
        self.logger = {
            "package_logger": logging.getLogger("aspose_barcode_cloud"),
            "urllib3_logger": logging.getLogger("urllib3"),
        }
        # Log format
        self.logger_format = "%(asctime)s %(levelname)s %(message)s"
        # Log stream handler
        self.logger_stream_handler = None
        # Log file handler
        self.logger_file_handler = None
        # Debug file location
        self.logger_file = None
        # Debug switch
        self.debug = False

        # SSL/TLS verification
        # Set this to false to skip verifying SSL certificate when calling API
        # from https server.
        self.verify_ssl = True
        # Set this to customize the certificate file to verify the peer.
        self.ssl_ca_cert = None
        # client certificate file
        self.cert_file = None
        # client key file
        self.key_file = None
        # Set this to True/False to enable/disable SSL hostname verification.
        self.assert_hostname = None

        # urllib3 connection pool's maximum number of connections saved
        # per pool. urllib3 uses 1 connection as default value, but this is
        # not the best value when you are making a lot of possibly parallel
        # requests to the same host, which is often the case here.
        # cpu_count * 5 is used as default value to increase performance.
        self.connection_pool_maxsize = multiprocessing.cpu_count() * 5

        # Proxy URL
        self.proxy = None
        # Safe chars for path_param
        self.safe_chars_for_path_param = "/"

    @property
    def access_token(self):
        if self._access_token:
            return self._access_token

        if self._client_id and self._client_secret and self._token_url:
            self._access_token = self.fetch_token(self._client_id, self._client_secret, self._token_url)
            return self._access_token

        raise ValueError("No access_token or client_id and client_secret specified")

    @property
    def token_url(self):
        return self._token_url

    @classmethod
    def set_default(cls, default):
        cls._default = default

    @property
    def logger_file(self):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :return: The logger_file path.
        :type: str
        """
        return self.__logger_file

    @logger_file.setter
    def logger_file(self, value):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        self.__logger_file = value
        if self.__logger_file:
            # If set logging file,
            # then add file handler and remove stream handler.
            self.logger_file_handler = logging.FileHandler(self.__logger_file)
            self.logger_file_handler.setFormatter(self.logger_formatter)
            for logger in self.logger.values():
                logger.addHandler(self.logger_file_handler)
                if self.logger_stream_handler:
                    logger.removeHandler(self.logger_stream_handler)
        else:
            # If not set logging file,
            # then add stream handler and remove file handler.
            self.logger_stream_handler = logging.StreamHandler()
            self.logger_stream_handler.setFormatter(self.logger_formatter)
            for logger in self.logger.values():
                logger.addHandler(self.logger_stream_handler)
                if self.logger_file_handler:
                    logger.removeHandler(self.logger_file_handler)

    @property
    def debug(self):
        """Debug status

        :return: The debug status, True or False.
        :type: bool
        """
        return self.__debug

    @debug.setter
    def debug(self, value):
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        self.__debug = value
        if self.__debug:
            # if debug status is True, turn on debug logging
            for logger in self.logger.values():
                logger.setLevel(logging.DEBUG)
            # turn on http.client debug
            http.client.HTTPConnection.debuglevel = 1
        else:
            # if debug status is False, turn off debug logging,
            # setting log level to default `logging.WARNING`
            for logger in self.logger.values():
                logger.setLevel(logging.WARNING)
            # turn off http.client debug
            http.client.HTTPConnection.debuglevel = 0

    @property
    def logger_format(self):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :return: The format string.
        :type: str
        """
        return self.__logger_format

    @logger_format.setter
    def logger_format(self, value):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        self.__logger_format = value
        self.logger_formatter = logging.Formatter(self.__logger_format)

    def get_api_key_with_prefix(self, identifier):
        """Gets API key (with prefix if set).

        :param identifier: The identifier of apiKey.
        :return: The token for api key authentication.
        """

        if self.refresh_api_key_hook:
            self.refresh_api_key_hook(self)

        key = self.api_key.get(identifier)
        if key:
            prefix = self.api_key_prefix.get(identifier)
            if prefix:
                return "%s %s" % (prefix, key)
            else:
                return key

    def get_basic_auth_token(self):
        """Gets HTTP basic authentication header (string).

        :return: The token for basic HTTP authentication.
        """
        return urllib3.util.make_headers(basic_auth=self.username + ":" + self.password).get("authorization")

    def auth_settings(self):
        """Gets Auth Settings dict for api client.

        :return: The Auth Settings information dict.
        """
        return {
            "JWT": {"type": "oauth2", "in": "header", "key": "Authorization", "value": "Bearer " + self.access_token},
        }

    def to_debug_report(self):
        """Gets the essential information for debugging.

        :return: The report for debugging.
        """
        return (
            "Python SDK Debug Report:\n"
            "OS: {env}\n"
            "Python Version: {pyversion}\n"
            "Version of the API: 3.0\n"
            "SDK Package Version: 24.6.0".format(env=sys.platform, pyversion=sys.version)
        )

    @staticmethod
    def fetch_token(client_id, client_secret, token_url):
        with contextlib.closing(
            RESTClientObject(Configuration(client_id=client_id, client_secret=client_secret, token_url=token_url))
        ) as client:
            response = client.POST(
                token_url,
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                post_params={
                    "grant_type": "client_credentials",
                    "client_id": client_id,
                    "client_secret": client_secret,
                },
            )
            js_data = json.loads(response.data)

        access_token = js_data["access_token"]

        return access_token
