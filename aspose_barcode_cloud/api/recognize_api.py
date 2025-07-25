# coding: utf-8

import re  # noqa: F401
import warnings  # noqa: F401

from aspose_barcode_cloud.api_client import ApiClient


class RecognizeApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/OpenAPITools/openapi-generator
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        # Authentication setting
        self.auth_settings = ["JWT"]

    def recognize(
        self, barcode_type, file_url, recognition_mode=None, recognition_image_kind=None, async_req=False, **kwargs
    ):
        """Recognize barcode from file on server in the Internet using GET requests with parameter in query string. For recognizing files from your hard drive use `recognize-body` or `recognize-multipart` endpoints instead.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = RecognizeApi().recognize(barcode_type, file_url, async_req=True)
        >>> result = thread.get()

        :param DecodeBarcodeType barcode_type: Type of barcode to recognize # noqa: E501
        :param str file_url: Url to barcode image # noqa: E501
        :param RecognitionMode recognition_mode: Recognition mode # noqa: E501
        :param RecognitionImageKind recognition_image_kind: Image kind for recognition # noqa: E501
        :param async_req bool
        :return: BarcodeResponseList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if async_req:
            return self.recognize_with_http_info(
                barcode_type,
                file_url,
                recognition_mode=recognition_mode,
                recognition_image_kind=recognition_image_kind,
                **kwargs
            )
        else:
            (data) = self.recognize_with_http_info(
                barcode_type,
                file_url,
                recognition_mode=recognition_mode,
                recognition_image_kind=recognition_image_kind,
                **kwargs
            )
            return data

    def recognize_with_http_info(self, barcode_type, file_url, **kwargs):
        """Recognize barcode from file on server in the Internet using GET requests with parameter in query string. For recognizing files from your hard drive use `recognize-body` or `recognize-multipart` endpoints instead.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = RecognizeApi().recognize_with_http_info(barcode_type, file_url, async_req=True)
        >>> result = thread.get()

        :param DecodeBarcodeType barcode_type: Type of barcode to recognize # noqa: E501
        :param str file_url: Url to barcode image # noqa: E501
        :return: BarcodeResponseList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = {"barcode_type", "file_url", "recognition_mode", "recognition_image_kind"}
        all_params.add("async_req")
        all_params.add("_return_http_data_only")
        all_params.add("_preload_content")
        all_params.add("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method recognize" % key)
            if val is None:
                continue

            params[key] = val
        del params["kwargs"]
        # verify the required parameter "barcode_type" is set
        if "barcode_type" not in params or params["barcode_type"] is None:
            raise ValueError("Missing the required parameter 'barcode_type' when calling 'recognize'")
        # verify the required parameter "file_url" is set
        if "file_url" not in params or params["file_url"] is None:
            raise ValueError("Missing the required parameter 'file_url' when calling 'recognize'")

        collection_formats = {}

        path_params = {}

        query_params = []
        if "barcode_type" in params:
            query_params.append(("barcodeType", params["barcode_type"]))
        if "file_url" in params:
            query_params.append(("fileUrl", params["file_url"]))
        if "recognition_mode" in params:
            query_params.append(("recognitionMode", params["recognition_mode"]))
        if "recognition_image_kind" in params:
            query_params.append(("recognitionImageKind", params["recognition_image_kind"]))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header "Accept"
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "application/xml"])

        return self.api_client.call_api(
            "/barcode/recognize",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="BarcodeResponseList",
            auth_settings=self.auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def recognize_base64(self, recognize_base64_request, async_req=False, **kwargs):
        """Recognize barcode from file in request body using POST requests with parameters in body in json or xml format.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = RecognizeApi().recognize_base64(recognize_base64_request, async_req=True)
        >>> result = thread.get()

        :param RecognizeBase64Request recognize_base64_request: Barcode recognition request # noqa: E501
        :param async_req bool
        :return: BarcodeResponseList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if async_req:
            return self.recognize_base64_with_http_info(recognize_base64_request, **kwargs)
        else:
            (data) = self.recognize_base64_with_http_info(recognize_base64_request, **kwargs)
            return data

    def recognize_base64_with_http_info(self, recognize_base64_request, **kwargs):
        """Recognize barcode from file in request body using POST requests with parameters in body in json or xml format.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = RecognizeApi().recognize_base64_with_http_info(recognize_base64_request, async_req=True)
        >>> result = thread.get()

        :param RecognizeBase64Request recognize_base64_request: Barcode recognition request # noqa: E501
        :return: BarcodeResponseList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = {"recognize_base64_request"}
        all_params.add("async_req")
        all_params.add("_return_http_data_only")
        all_params.add("_preload_content")
        all_params.add("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method recognize_base64" % key)
            if val is None:
                continue

            params[key] = val
        del params["kwargs"]
        # verify the required parameter "recognize_base64_request" is set
        if "recognize_base64_request" not in params or params["recognize_base64_request"] is None:
            raise ValueError(
                "Missing the required parameter 'recognize_base64_request' when calling 'recognize_base64'"
            )

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "recognize_base64_request" in params:
            body_params = params["recognize_base64_request"]
        # HTTP header "Accept"
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "application/xml"])

        # HTTP header "Content-Type"
        header_params["Content-Type"] = self.api_client.select_header_content_type(
            ["application/json", "application/xml"]
        )

        return self.api_client.call_api(
            "/barcode/recognize-body",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="BarcodeResponseList",
            auth_settings=self.auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def recognize_multipart(
        self, barcode_type, file, recognition_mode=None, recognition_image_kind=None, async_req=False, **kwargs
    ):
        """Recognize barcode from file in request body using POST requests with parameters in multipart form.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = RecognizeApi().recognize_multipart(barcode_type, file, async_req=True)
        >>> result = thread.get()

        :param DecodeBarcodeType barcode_type: # noqa: E501
        :param bytearray file: Barcode image file # noqa: E501
        :param RecognitionMode recognition_mode: # noqa: E501
        :param RecognitionImageKind recognition_image_kind: # noqa: E501
        :param async_req bool
        :return: BarcodeResponseList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if async_req:
            return self.recognize_multipart_with_http_info(
                barcode_type,
                file,
                recognition_mode=recognition_mode,
                recognition_image_kind=recognition_image_kind,
                **kwargs
            )
        else:
            (data) = self.recognize_multipart_with_http_info(
                barcode_type,
                file,
                recognition_mode=recognition_mode,
                recognition_image_kind=recognition_image_kind,
                **kwargs
            )
            return data

    def recognize_multipart_with_http_info(self, barcode_type, file, **kwargs):
        """Recognize barcode from file in request body using POST requests with parameters in multipart form.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = RecognizeApi().recognize_multipart_with_http_info(barcode_type, file, async_req=True)
        >>> result = thread.get()

        :param DecodeBarcodeType barcode_type: # noqa: E501
        :param bytearray file: Barcode image file # noqa: E501
        :return: BarcodeResponseList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = {"barcode_type", "file", "recognition_mode", "recognition_image_kind"}
        all_params.add("async_req")
        all_params.add("_return_http_data_only")
        all_params.add("_preload_content")
        all_params.add("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method recognize_multipart" % key)
            if val is None:
                continue

            params[key] = val
        del params["kwargs"]
        # verify the required parameter "barcode_type" is set
        if "barcode_type" not in params or params["barcode_type"] is None:
            raise ValueError("Missing the required parameter 'barcode_type' when calling 'recognize_multipart'")
        # verify the required parameter "file" is set
        if "file" not in params or params["file"] is None:
            raise ValueError("Missing the required parameter 'file' when calling 'recognize_multipart'")

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if "barcode_type" in params:
            form_params.append(("barcodeType", params["barcode_type"]))
        if "file" in params:
            local_var_files["file"] = params["file"]
        if "recognition_mode" in params:
            form_params.append(("recognitionMode", params["recognition_mode"]))
        if "recognition_image_kind" in params:
            form_params.append(("recognitionImageKind", params["recognition_image_kind"]))

        body_params = None
        # HTTP header "Accept"
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "application/xml"])

        # HTTP header "Content-Type"
        header_params["Content-Type"] = self.api_client.select_header_content_type(["multipart/form-data"])

        return self.api_client.call_api(
            "/barcode/recognize-multipart",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="BarcodeResponseList",
            auth_settings=self.auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
