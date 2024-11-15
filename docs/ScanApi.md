# aspose_barcode_cloud.ScanApi

All URIs are relative to *https://barcode.qa.aspose.cloud/v4.0*

Method | HTTP request | Description
------ | ------------ | -----------
[**barcode_scan_body_post**](ScanApi.md#barcode_scan_body_post) | **POST** /barcode/scan-body | Scan barcode from file in request body using POST requests with parameter in body in json or xml format.
[**barcode_scan_get**](ScanApi.md#barcode_scan_get) | **GET** /barcode/scan | Scan barcode from file on server using GET requests with parameter in query string.
[**barcode_scan_multipart_post**](ScanApi.md#barcode_scan_multipart_post) | **POST** /barcode/scan-multipart | Scan barcode from file in request body using POST requests with parameter in multipart form.


# **barcode_scan_body_post**
> BarcodeResponseList barcode_scan_body_post(scan_base64_request)

Scan barcode from file in request body using POST requests with parameter in body in json or xml format.

### Example
```python
import time
import aspose_barcode_cloud
from aspose_barcode_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = aspose_barcode_cloud.Configuration(access_token="YOUR_ACCESS_TOKEN")

# create an instance of the API class
api_instance = aspose_barcode_cloud.ScanApi(aspose_barcode_cloud.ApiClient(configuration))
scan_base64_request = aspose_barcode_cloud.ScanBase64Request() # ScanBase64Request | Barcode scan request

try:
    # Scan barcode from file in request body using POST requests with parameter in body in json or xml format.
    api_response = api_instance.barcode_scan_body_post(scan_base64_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanApi->barcode_scan_body_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
---- | ---- | ------------ | -----
 **scan_base64_request** | [**ScanBase64Request**](ScanBase64Request.md)| Barcode scan request | 

### Return type

[**BarcodeResponseList**](BarcodeResponseList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **barcode_scan_get**
> BarcodeResponseList barcode_scan_get(file_url)

Scan barcode from file on server using GET requests with parameter in query string.

### Example
```python
import time
import aspose_barcode_cloud
from aspose_barcode_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = aspose_barcode_cloud.Configuration(access_token="YOUR_ACCESS_TOKEN")

# create an instance of the API class
api_instance = aspose_barcode_cloud.ScanApi(aspose_barcode_cloud.ApiClient(configuration))
file_url = 'file_url_example' # str | Url to barcode image

try:
    # Scan barcode from file on server using GET requests with parameter in query string.
    api_response = api_instance.barcode_scan_get(file_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanApi->barcode_scan_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
---- | ---- | ------------ | -----
 **file_url** | **str**| Url to barcode image | 

### Return type

[**BarcodeResponseList**](BarcodeResponseList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **barcode_scan_multipart_post**
> BarcodeResponseList barcode_scan_multipart_post(file)

Scan barcode from file in request body using POST requests with parameter in multipart form.

### Example
```python
import time
import aspose_barcode_cloud
from aspose_barcode_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = aspose_barcode_cloud.Configuration(access_token="YOUR_ACCESS_TOKEN")

# create an instance of the API class
api_instance = aspose_barcode_cloud.ScanApi(aspose_barcode_cloud.ApiClient(configuration))
file = None # bytearray | Barcode image file

try:
    # Scan barcode from file in request body using POST requests with parameter in multipart form.
    api_response = api_instance.barcode_scan_multipart_post(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanApi->barcode_scan_multipart_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
---- | ---- | ------------ | -----
 **file** | **bytearray**| Barcode image file | 

### Return type

[**BarcodeResponseList**](BarcodeResponseList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

