# aspose_barcode_cloud.StorageApi

All URIs are relative to *https://api.aspose.cloud/v3.0*

Method | HTTP request | Description
------ | ------------ | -----------
[**get_disc_usage**](StorageApi.md#get_disc_usage) | **GET** /barcode/storage/disc | Get disc usage
[**get_file_versions**](StorageApi.md#get_file_versions) | **GET** /barcode/storage/version/{path} | Get file versions
[**object_exists**](StorageApi.md#object_exists) | **GET** /barcode/storage/exist/{path} | Check if file or folder exists
[**storage_exists**](StorageApi.md#storage_exists) | **GET** /barcode/storage/{storageName}/exist | Check if storage exists


# **get_disc_usage**
> DiscUsage get_disc_usage(storage_name=storage_name)

Get disc usage

### Example
```python
import time
import aspose_barcode_cloud
from aspose_barcode_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = aspose_barcode_cloud.Configuration(access_token="YOUR_ACCESS_TOKEN")

# create an instance of the API class
api_instance = aspose_barcode_cloud.StorageApi(aspose_barcode_cloud.ApiClient(configuration))
storage_name = 'storage_name_example' # str | Storage name (optional)

try:
    # Get disc usage
    api_response = api_instance.get_disc_usage(storage_name=storage_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageApi->get_disc_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
---- | ---- | ------------ | -----
 **storage_name** | **str**| Storage name | [optional] 

### Return type

[**DiscUsage**](DiscUsage.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_versions**
> FileVersions get_file_versions(path, storage_name=storage_name)

Get file versions

### Example
```python
import time
import aspose_barcode_cloud
from aspose_barcode_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = aspose_barcode_cloud.Configuration(access_token="YOUR_ACCESS_TOKEN")

# create an instance of the API class
api_instance = aspose_barcode_cloud.StorageApi(aspose_barcode_cloud.ApiClient(configuration))
path = 'path_example' # str | File path e.g. '/file.ext'
storage_name = 'storage_name_example' # str | Storage name (optional)

try:
    # Get file versions
    api_response = api_instance.get_file_versions(path, storage_name=storage_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageApi->get_file_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
---- | ---- | ------------ | -----
 **path** | **str**| File path e.g. &#39;/file.ext&#39; | 
 **storage_name** | **str**| Storage name | [optional] 

### Return type

[**FileVersions**](FileVersions.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **object_exists**
> ObjectExist object_exists(path, storage_name=storage_name, version_id=version_id)

Check if file or folder exists

### Example
```python
import time
import aspose_barcode_cloud
from aspose_barcode_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = aspose_barcode_cloud.Configuration(access_token="YOUR_ACCESS_TOKEN")

# create an instance of the API class
api_instance = aspose_barcode_cloud.StorageApi(aspose_barcode_cloud.ApiClient(configuration))
path = 'path_example' # str | File or folder path e.g. '/file.ext' or '/folder'
storage_name = 'storage_name_example' # str | Storage name (optional)
version_id = 'version_id_example' # str | File version ID (optional)

try:
    # Check if file or folder exists
    api_response = api_instance.object_exists(path, storage_name=storage_name, version_id=version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageApi->object_exists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
---- | ---- | ------------ | -----
 **path** | **str**| File or folder path e.g. &#39;/file.ext&#39; or &#39;/folder&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **version_id** | **str**| File version ID | [optional] 

### Return type

[**ObjectExist**](ObjectExist.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_exists**
> StorageExist storage_exists(storage_name)

Check if storage exists

### Example
```python
import time
import aspose_barcode_cloud
from aspose_barcode_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = aspose_barcode_cloud.Configuration(access_token="YOUR_ACCESS_TOKEN")

# create an instance of the API class
api_instance = aspose_barcode_cloud.StorageApi(aspose_barcode_cloud.ApiClient(configuration))
storage_name = 'storage_name_example' # str | Storage name

try:
    # Check if storage exists
    api_response = api_instance.storage_exists(storage_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageApi->storage_exists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
---- | ---- | ------------ | -----
 **storage_name** | **str**| Storage name | 

### Return type

[**StorageExist**](StorageExist.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

