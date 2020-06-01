# aspose_barcode_cloud.FileApi

All URIs are relative to *https://api.aspose.cloud/v3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copy_file**](FileApi.md#copy_file) | **PUT** /barcode/storage/file/copy/{srcPath} | Copy file
[**delete_file**](FileApi.md#delete_file) | **DELETE** /barcode/storage/file/{path} | Delete file
[**download_file**](FileApi.md#download_file) | **GET** /barcode/storage/file/{path} | Download file
[**move_file**](FileApi.md#move_file) | **PUT** /barcode/storage/file/move/{srcPath} | Move file
[**upload_file**](FileApi.md#upload_file) | **PUT** /barcode/storage/file/{path} | Upload file


# **copy_file**
> copy_file(src_path, dest_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name, version_id=version_id)

Copy file

### Example
```python
from __future__ import print_function
import time
import aspose_barcode_cloud
from aspose_barcode_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = aspose_barcode_cloud.Configuration(access_token='YOUR_ACCESS_TOKEN')

# create an instance of the API class
api_instance = aspose_barcode_cloud.FileApi(aspose_barcode_cloud.ApiClient(configuration))
src_path = 'src_path_example' # str | Source file path e.g. '/folder/file.ext'
dest_path = 'dest_path_example' # str | Destination file path
src_storage_name = 'src_storage_name_example' # str | Source storage name (optional)
dest_storage_name = 'dest_storage_name_example' # str | Destination storage name (optional)
version_id = 'version_id_example' # str | File version ID to copy (optional)

try:
    # Copy file
    api_instance.copy_file(src_path, dest_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name, version_id=version_id)
except ApiException as e:
    print("Exception when calling FileApi->copy_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Source file path e.g. &#39;/folder/file.ext&#39; | 
 **dest_path** | **str**| Destination file path | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 
 **version_id** | **str**| File version ID to copy | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file**
> delete_file(path, storage_name=storage_name, version_id=version_id)

Delete file

### Example
```python
from __future__ import print_function
import time
import aspose_barcode_cloud
from aspose_barcode_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = aspose_barcode_cloud.Configuration(access_token='YOUR_ACCESS_TOKEN')

# create an instance of the API class
api_instance = aspose_barcode_cloud.FileApi(aspose_barcode_cloud.ApiClient(configuration))
path = 'path_example' # str | File path e.g. '/folder/file.ext'
storage_name = 'storage_name_example' # str | Storage name (optional)
version_id = 'version_id_example' # str | File version ID to delete (optional)

try:
    # Delete file
    api_instance.delete_file(path, storage_name=storage_name, version_id=version_id)
except ApiException as e:
    print("Exception when calling FileApi->delete_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File path e.g. &#39;/folder/file.ext&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **version_id** | **str**| File version ID to delete | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_file**
> file download_file(path, storage_name=storage_name, version_id=version_id)

Download file

### Example
```python
from __future__ import print_function
import time
import aspose_barcode_cloud
from aspose_barcode_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = aspose_barcode_cloud.Configuration(access_token='YOUR_ACCESS_TOKEN')

# create an instance of the API class
api_instance = aspose_barcode_cloud.FileApi(aspose_barcode_cloud.ApiClient(configuration))
path = 'path_example' # str | File path e.g. '/folder/file.ext'
storage_name = 'storage_name_example' # str | Storage name (optional)
version_id = 'version_id_example' # str | File version ID to download (optional)

try:
    # Download file
    api_response = api_instance.download_file(path, storage_name=storage_name, version_id=version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->download_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File path e.g. &#39;/folder/file.ext&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **version_id** | **str**| File version ID to download | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_file**
> move_file(src_path, dest_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name, version_id=version_id)

Move file

### Example
```python
from __future__ import print_function
import time
import aspose_barcode_cloud
from aspose_barcode_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = aspose_barcode_cloud.Configuration(access_token='YOUR_ACCESS_TOKEN')

# create an instance of the API class
api_instance = aspose_barcode_cloud.FileApi(aspose_barcode_cloud.ApiClient(configuration))
src_path = 'src_path_example' # str | Source file path e.g. '/src.ext'
dest_path = 'dest_path_example' # str | Destination file path e.g. '/dest.ext'
src_storage_name = 'src_storage_name_example' # str | Source storage name (optional)
dest_storage_name = 'dest_storage_name_example' # str | Destination storage name (optional)
version_id = 'version_id_example' # str | File version ID to move (optional)

try:
    # Move file
    api_instance.move_file(src_path, dest_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name, version_id=version_id)
except ApiException as e:
    print("Exception when calling FileApi->move_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Source file path e.g. &#39;/src.ext&#39; | 
 **dest_path** | **str**| Destination file path e.g. &#39;/dest.ext&#39; | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 
 **version_id** | **str**| File version ID to move | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> FilesUploadResult upload_file(path, file, storage_name=storage_name)

Upload file

### Example
```python
from __future__ import print_function
import time
import aspose_barcode_cloud
from aspose_barcode_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = aspose_barcode_cloud.Configuration(access_token='YOUR_ACCESS_TOKEN')

# create an instance of the API class
api_instance = aspose_barcode_cloud.FileApi(aspose_barcode_cloud.ApiClient(configuration))
path = 'path_example' # str | Path where to upload including filename and extension e.g. /file.ext or /Folder 1/file.ext             If the content is multipart and path does not contains the file name it tries to get them from filename parameter             from Content-Disposition header.             
file = '/path/to/file.txt' # file | File to upload
storage_name = 'storage_name_example' # str | Storage name (optional)

try:
    # Upload file
    api_response = api_instance.upload_file(path, file, storage_name=storage_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->upload_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Path where to upload including filename and extension e.g. /file.ext or /Folder 1/file.ext             If the content is multipart and path does not contains the file name it tries to get them from filename parameter             from Content-Disposition header.              | 
 **file** | **file**| File to upload | 
 **storage_name** | **str**| Storage name | [optional] 

### Return type

[**FilesUploadResult**](FilesUploadResult.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

