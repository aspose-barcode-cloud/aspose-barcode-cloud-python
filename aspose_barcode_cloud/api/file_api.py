# coding: utf-8

"""

    Copyright (c) 2020 Aspose.BarCode for Cloud

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.

"""


from __future__ import absolute_import, division

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from aspose_barcode_cloud.api_client import ApiClient


class FileApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def copy_file(
        self,
        src_path,
        dest_path,
        src_storage_name=None,
        dest_storage_name=None,
        version_id=None,
        async_req=False,
        **kwargs
    ):
        """Copy file

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = FileApi().copy_file(src_path, dest_path, async_req=True)
        >>> result = thread.get()

        :param str src_path: Source file path e.g. '/folder/file.ext' # noqa: E501
        :param str dest_path: Destination file path # noqa: E501
        :param str src_storage_name: Source storage name # noqa: E501
        :param str dest_storage_name: Destination storage name # noqa: E501
        :param str version_id: File version ID to copy # noqa: E501
        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if async_req:
            return self.copy_file_with_http_info(
                src_path,
                dest_path,
                src_storage_name=src_storage_name,
                dest_storage_name=dest_storage_name,
                version_id=version_id,
                **kwargs
            )
        else:
            (data) = self.copy_file_with_http_info(
                src_path,
                dest_path,
                src_storage_name=src_storage_name,
                dest_storage_name=dest_storage_name,
                version_id=version_id,
                **kwargs
            )
            return data

    def copy_file_with_http_info(self, src_path, dest_path, **kwargs):
        """Copy file

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = FileApi().copy_file_with_http_info(src_path, dest_path, async_req=True)
        >>> result = thread.get()

        :param str src_path: Source file path e.g. '/folder/file.ext' # noqa: E501
        :param str dest_path: Destination file path # noqa: E501
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = {"src_path", "dest_path", "src_storage_name", "dest_storage_name", "version_id"}
        all_params.add("async_req")
        all_params.add("_return_http_data_only")
        all_params.add("_preload_content")
        all_params.add("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method copy_file" % key)
            if val is None:
                continue

            params[key] = val
        del params["kwargs"]
        # verify the required parameter "src_path" is set
        if "src_path" not in params or params["src_path"] is None:
            raise ValueError("Missing the required parameter 'src_path' when calling 'copy_file'")
        # verify the required parameter "dest_path" is set
        if "dest_path" not in params or params["dest_path"] is None:
            raise ValueError("Missing the required parameter 'dest_path' when calling 'copy_file'")

        collection_formats = {}

        path_params = {}
        if "src_path" in params:
            path_params["srcPath"] = params["src_path"]

        query_params = []
        if "dest_path" in params:
            query_params.append(("destPath", params["dest_path"]))
        if "src_storage_name" in params:
            query_params.append(("srcStorageName", params["src_storage_name"]))
        if "dest_storage_name" in params:
            query_params.append(("destStorageName", params["dest_storage_name"]))
        if "version_id" in params:
            query_params.append(("versionId", params["version_id"]))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header "Accept"
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        # HTTP header "Content-Type"
        header_params["Content-Type"] = self.api_client.select_header_content_type(["application/json"])

        # Authentication setting
        auth_settings = ["JWT"]

        return self.api_client.call_api(
            "/barcode/storage/file/copy/{srcPath}",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def delete_file(self, path, storage_name=None, version_id=None, async_req=False, **kwargs):
        """Delete file

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = FileApi().delete_file(path, async_req=True)
        >>> result = thread.get()

        :param str path: File path e.g. '/folder/file.ext' # noqa: E501
        :param str storage_name: Storage name # noqa: E501
        :param str version_id: File version ID to delete # noqa: E501
        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if async_req:
            return self.delete_file_with_http_info(path, storage_name=storage_name, version_id=version_id, **kwargs)
        else:
            (data) = self.delete_file_with_http_info(path, storage_name=storage_name, version_id=version_id, **kwargs)
            return data

    def delete_file_with_http_info(self, path, **kwargs):
        """Delete file

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = FileApi().delete_file_with_http_info(path, async_req=True)
        >>> result = thread.get()

        :param str path: File path e.g. '/folder/file.ext' # noqa: E501
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = {"path", "storage_name", "version_id"}
        all_params.add("async_req")
        all_params.add("_return_http_data_only")
        all_params.add("_preload_content")
        all_params.add("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method delete_file" % key)
            if val is None:
                continue

            params[key] = val
        del params["kwargs"]
        # verify the required parameter "path" is set
        if "path" not in params or params["path"] is None:
            raise ValueError("Missing the required parameter 'path' when calling 'delete_file'")

        collection_formats = {}

        path_params = {}
        if "path" in params:
            path_params["path"] = params["path"]

        query_params = []
        if "storage_name" in params:
            query_params.append(("storageName", params["storage_name"]))
        if "version_id" in params:
            query_params.append(("versionId", params["version_id"]))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header "Accept"
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        # HTTP header "Content-Type"
        header_params["Content-Type"] = self.api_client.select_header_content_type(["application/json"])

        # Authentication setting
        auth_settings = ["JWT"]

        return self.api_client.call_api(
            "/barcode/storage/file/{path}",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def download_file(self, path, storage_name=None, version_id=None, async_req=False, **kwargs):
        """Download file

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = FileApi().download_file(path, async_req=True)
        >>> result = thread.get()

        :param str path: File path e.g. '/folder/file.ext' # noqa: E501
        :param str storage_name: Storage name # noqa: E501
        :param str version_id: File version ID to download # noqa: E501
        :param async_req bool
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if async_req:
            return self.download_file_with_http_info(path, storage_name=storage_name, version_id=version_id, **kwargs)
        else:
            (data) = self.download_file_with_http_info(path, storage_name=storage_name, version_id=version_id, **kwargs)
            return data

    def download_file_with_http_info(self, path, **kwargs):
        """Download file

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = FileApi().download_file_with_http_info(path, async_req=True)
        >>> result = thread.get()

        :param str path: File path e.g. '/folder/file.ext' # noqa: E501
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = {"path", "storage_name", "version_id"}
        all_params.add("async_req")
        all_params.add("_return_http_data_only")
        all_params.add("_preload_content")
        all_params.add("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method download_file" % key)
            if val is None:
                continue

            params[key] = val
        del params["kwargs"]
        # verify the required parameter "path" is set
        if "path" not in params or params["path"] is None:
            raise ValueError("Missing the required parameter 'path' when calling 'download_file'")

        collection_formats = {}

        path_params = {}
        if "path" in params:
            path_params["path"] = params["path"]

        query_params = []
        if "storage_name" in params:
            query_params.append(("storageName", params["storage_name"]))
        if "version_id" in params:
            query_params.append(("versionId", params["version_id"]))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header "Accept"
        header_params["Accept"] = self.api_client.select_header_accept(["multipart/form-data"])

        # HTTP header "Content-Type"
        header_params["Content-Type"] = self.api_client.select_header_content_type(["application/json"])

        # Authentication setting
        auth_settings = ["JWT"]

        return self.api_client.call_api(
            "/barcode/storage/file/{path}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="file",
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", False),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def move_file(
        self,
        src_path,
        dest_path,
        src_storage_name=None,
        dest_storage_name=None,
        version_id=None,
        async_req=False,
        **kwargs
    ):
        """Move file

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = FileApi().move_file(src_path, dest_path, async_req=True)
        >>> result = thread.get()

        :param str src_path: Source file path e.g. '/src.ext' # noqa: E501
        :param str dest_path: Destination file path e.g. '/dest.ext' # noqa: E501
        :param str src_storage_name: Source storage name # noqa: E501
        :param str dest_storage_name: Destination storage name # noqa: E501
        :param str version_id: File version ID to move # noqa: E501
        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if async_req:
            return self.move_file_with_http_info(
                src_path,
                dest_path,
                src_storage_name=src_storage_name,
                dest_storage_name=dest_storage_name,
                version_id=version_id,
                **kwargs
            )
        else:
            (data) = self.move_file_with_http_info(
                src_path,
                dest_path,
                src_storage_name=src_storage_name,
                dest_storage_name=dest_storage_name,
                version_id=version_id,
                **kwargs
            )
            return data

    def move_file_with_http_info(self, src_path, dest_path, **kwargs):
        """Move file

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = FileApi().move_file_with_http_info(src_path, dest_path, async_req=True)
        >>> result = thread.get()

        :param str src_path: Source file path e.g. '/src.ext' # noqa: E501
        :param str dest_path: Destination file path e.g. '/dest.ext' # noqa: E501
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = {"src_path", "dest_path", "src_storage_name", "dest_storage_name", "version_id"}
        all_params.add("async_req")
        all_params.add("_return_http_data_only")
        all_params.add("_preload_content")
        all_params.add("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method move_file" % key)
            if val is None:
                continue

            params[key] = val
        del params["kwargs"]
        # verify the required parameter "src_path" is set
        if "src_path" not in params or params["src_path"] is None:
            raise ValueError("Missing the required parameter 'src_path' when calling 'move_file'")
        # verify the required parameter "dest_path" is set
        if "dest_path" not in params or params["dest_path"] is None:
            raise ValueError("Missing the required parameter 'dest_path' when calling 'move_file'")

        collection_formats = {}

        path_params = {}
        if "src_path" in params:
            path_params["srcPath"] = params["src_path"]

        query_params = []
        if "dest_path" in params:
            query_params.append(("destPath", params["dest_path"]))
        if "src_storage_name" in params:
            query_params.append(("srcStorageName", params["src_storage_name"]))
        if "dest_storage_name" in params:
            query_params.append(("destStorageName", params["dest_storage_name"]))
        if "version_id" in params:
            query_params.append(("versionId", params["version_id"]))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header "Accept"
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        # HTTP header "Content-Type"
        header_params["Content-Type"] = self.api_client.select_header_content_type(["application/json"])

        # Authentication setting
        auth_settings = ["JWT"]

        return self.api_client.call_api(
            "/barcode/storage/file/move/{srcPath}",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def upload_file(self, path, file, storage_name=None, async_req=False, **kwargs):
        """Upload file

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = FileApi().upload_file(path, file, async_req=True)
        >>> result = thread.get()

        :param str path: Path where to upload including filename and extension e.g. /file.ext or /Folder 1/file.ext  If the content is multipart and path does not contains the file name it tries to get them from filename parameter  from Content-Disposition header. # noqa: E501
        :param file file: File to upload # noqa: E501
        :param str storage_name: Storage name # noqa: E501
        :param async_req bool
        :return: FilesUploadResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if async_req:
            return self.upload_file_with_http_info(path, file, storage_name=storage_name, **kwargs)
        else:
            (data) = self.upload_file_with_http_info(path, file, storage_name=storage_name, **kwargs)
            return data

    def upload_file_with_http_info(self, path, file, **kwargs):
        """Upload file

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = FileApi().upload_file_with_http_info(path, file, async_req=True)
        >>> result = thread.get()

        :param str path: Path where to upload including filename and extension e.g. /file.ext or /Folder 1/file.ext  If the content is multipart and path does not contains the file name it tries to get them from filename parameter  from Content-Disposition header. # noqa: E501
        :param file file: File to upload # noqa: E501
        :return: FilesUploadResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = {"path", "file", "storage_name"}
        all_params.add("async_req")
        all_params.add("_return_http_data_only")
        all_params.add("_preload_content")
        all_params.add("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method upload_file" % key)
            if val is None:
                continue

            params[key] = val
        del params["kwargs"]
        # verify the required parameter "path" is set
        if "path" not in params or params["path"] is None:
            raise ValueError("Missing the required parameter 'path' when calling 'upload_file'")
        # verify the required parameter "file" is set
        if "file" not in params or params["file"] is None:
            raise ValueError("Missing the required parameter 'file' when calling 'upload_file'")

        collection_formats = {}

        path_params = {}
        if "path" in params:
            path_params["path"] = params["path"]

        query_params = []
        if "storage_name" in params:
            query_params.append(("storageName", params["storage_name"]))

        header_params = {}

        form_params = []
        local_var_files = {}
        if "file" in params:
            local_var_files["File"] = params["file"]

        body_params = None
        # HTTP header "Accept"
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        # HTTP header "Content-Type"
        header_params["Content-Type"] = self.api_client.select_header_content_type(["multipart/form-data"])

        # Authentication setting
        auth_settings = ["JWT"]

        return self.api_client.call_api(
            "/barcode/storage/file/{path}",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="FilesUploadResult",
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
