# aspose_barcode_cloud.FolderApi

All URIs are relative to *https://api.aspose.cloud/v3.0*

Method | HTTP request | Description
------ | ------------ | -----------
[**copy_folder**](FolderApi.md#copy_folder) | **PUT** /barcode/storage/folder/copy/{srcPath} | Copy folder
[**create_folder**](FolderApi.md#create_folder) | **PUT** /barcode/storage/folder/{path} | Create the folder
[**delete_folder**](FolderApi.md#delete_folder) | **DELETE** /barcode/storage/folder/{path} | Delete folder
[**get_files_list**](FolderApi.md#get_files_list) | **GET** /barcode/storage/folder/{path} | Get all files and folders within a folder
[**move_folder**](FolderApi.md#move_folder) | **PUT** /barcode/storage/folder/move/{srcPath} | Move folder


# **copy_folder**
> copy_folder(src_path, dest_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name)

Copy folder

### Example
```python
from __future__ import division, print_function
import time
import aspose_barcode_cloud
from aspose_barcode_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = aspose_barcode_cloud.Configuration(access_token="YOUR_ACCESS_TOKEN")

# create an instance of the API class
api_instance = aspose_barcode_cloud.FolderApi(aspose_barcode_cloud.ApiClient(configuration))
src_path = 'src_path_example' # str | Source folder path e.g. '/src'
dest_path = 'dest_path_example' # str | Destination folder path e.g. '/dst'
src_storage_name = 'src_storage_name_example' # str | Source storage name (optional)
dest_storage_name = 'dest_storage_name_example' # str | Destination storage name (optional)

try:
    # Copy folder
    api_instance.copy_folder(src_path, dest_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name)
except ApiException as e:
    print("Exception when calling FolderApi->copy_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
---- | ---- | ------------ | -----
 **src_path** | **str**| Source folder path e.g. &#39;/src&#39; | 
 **dest_path** | **str**| Destination folder path e.g. &#39;/dst&#39; | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_folder**
> create_folder(path, storage_name=storage_name)

Create the folder

### Example
```python
from __future__ import division, print_function
import time
import aspose_barcode_cloud
from aspose_barcode_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = aspose_barcode_cloud.Configuration(access_token="YOUR_ACCESS_TOKEN")

# create an instance of the API class
api_instance = aspose_barcode_cloud.FolderApi(aspose_barcode_cloud.ApiClient(configuration))
path = 'path_example' # str | Folder path to create e.g. 'folder_1/folder_2/'
storage_name = 'storage_name_example' # str | Storage name (optional)

try:
    # Create the folder
    api_instance.create_folder(path, storage_name=storage_name)
except ApiException as e:
    print("Exception when calling FolderApi->create_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
---- | ---- | ------------ | -----
 **path** | **str**| Folder path to create e.g. &#39;folder_1/folder_2/&#39; | 
 **storage_name** | **str**| Storage name | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_folder**
> delete_folder(path, storage_name=storage_name, recursive=recursive)

Delete folder

### Example
```python
from __future__ import division, print_function
import time
import aspose_barcode_cloud
from aspose_barcode_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = aspose_barcode_cloud.Configuration(access_token="YOUR_ACCESS_TOKEN")

# create an instance of the API class
api_instance = aspose_barcode_cloud.FolderApi(aspose_barcode_cloud.ApiClient(configuration))
path = 'path_example' # str | Folder path e.g. '/folder'
storage_name = 'storage_name_example' # str | Storage name (optional)
recursive = False # bool | Enable to delete folders, subfolders and files (optional) (default to False)

try:
    # Delete folder
    api_instance.delete_folder(path, storage_name=storage_name, recursive=recursive)
except ApiException as e:
    print("Exception when calling FolderApi->delete_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
---- | ---- | ------------ | -----
 **path** | **str**| Folder path e.g. &#39;/folder&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **recursive** | **bool**| Enable to delete folders, subfolders and files | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_files_list**
> FilesList get_files_list(path, storage_name=storage_name)

Get all files and folders within a folder

### Example
```python
from __future__ import division, print_function
import time
import aspose_barcode_cloud
from aspose_barcode_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = aspose_barcode_cloud.Configuration(access_token="YOUR_ACCESS_TOKEN")

# create an instance of the API class
api_instance = aspose_barcode_cloud.FolderApi(aspose_barcode_cloud.ApiClient(configuration))
path = 'path_example' # str | Folder path e.g. '/folder'
storage_name = 'storage_name_example' # str | Storage name (optional)

try:
    # Get all files and folders within a folder
    api_response = api_instance.get_files_list(path, storage_name=storage_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FolderApi->get_files_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
---- | ---- | ------------ | -----
 **path** | **str**| Folder path e.g. &#39;/folder&#39; | 
 **storage_name** | **str**| Storage name | [optional] 

### Return type

[**FilesList**](FilesList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_folder**
> move_folder(src_path, dest_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name)

Move folder

### Example
```python
from __future__ import division, print_function
import time
import aspose_barcode_cloud
from aspose_barcode_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = aspose_barcode_cloud.Configuration(access_token="YOUR_ACCESS_TOKEN")

# create an instance of the API class
api_instance = aspose_barcode_cloud.FolderApi(aspose_barcode_cloud.ApiClient(configuration))
src_path = 'src_path_example' # str | Folder path to move e.g. '/folder'
dest_path = 'dest_path_example' # str | Destination folder path to move to e.g '/dst'
src_storage_name = 'src_storage_name_example' # str | Source storage name (optional)
dest_storage_name = 'dest_storage_name_example' # str | Destination storage name (optional)

try:
    # Move folder
    api_instance.move_folder(src_path, dest_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name)
except ApiException as e:
    print("Exception when calling FolderApi->move_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
---- | ---- | ------------ | -----
 **src_path** | **str**| Folder path to move e.g. &#39;/folder&#39; | 
 **dest_path** | **str**| Destination folder path to move to e.g &#39;/dst&#39; | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

