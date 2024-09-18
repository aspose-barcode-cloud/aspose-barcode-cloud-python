# aspose_barcode_cloud.RecognizeApi

All URIs are relative to *https://barcode.qa.aspose.cloud/v4.0*

Method | HTTP request | Description
------ | ------------ | -----------
[**barcode_recognize_barcode_type_get**](RecognizeApi.md#barcode_recognize_barcode_type_get) | **GET** /barcode/recognize/{barcodeType} | Recognize barcode from file on server using GET requests with parameters in route and query string.
[**barcode_recognize_body_post**](RecognizeApi.md#barcode_recognize_body_post) | **POST** /barcode/recognize-body | Recognize barcode from file in request body using POST requests with parameters in body in json or xml format.
[**barcode_recognize_form_post**](RecognizeApi.md#barcode_recognize_form_post) | **POST** /barcode/recognize-form | Recognize barcode from file in request body using POST requests with parameters in multipart form.


# **barcode_recognize_barcode_type_get**
> BarcodeResponseList barcode_recognize_barcode_type_get(barcode_type, file_url, recognition_mode=recognition_mode, image_kind=image_kind)

Recognize barcode from file on server using GET requests with parameters in route and query string.

### Example
```python
import time
import aspose_barcode_cloud
from aspose_barcode_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose_barcode_cloud.RecognizeApi()
barcode_type = aspose_barcode_cloud.DecodeBarcodeType() # DecodeBarcodeType | Type of barcode to recognize
file_url = 'file_url_example' # str | Url to barcode image
recognition_mode = aspose_barcode_cloud.RecognitionMode() # RecognitionMode | Recognition mode (optional)
image_kind = aspose_barcode_cloud.RecognitionImageKind() # RecognitionImageKind | Image kind (optional)

try:
    # Recognize barcode from file on server using GET requests with parameters in route and query string.
    api_response = api_instance.barcode_recognize_barcode_type_get(barcode_type, file_url, recognition_mode=recognition_mode, image_kind=image_kind)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecognizeApi->barcode_recognize_barcode_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
---- | ---- | ------------ | -----
 **barcode_type** | [**DecodeBarcodeType**](.md)| Type of barcode to recognize | 
 **file_url** | **str**| Url to barcode image | 
 **recognition_mode** | [**RecognitionMode**](.md)| Recognition mode | [optional] 
 **image_kind** | [**RecognitionImageKind**](.md)| Image kind | [optional] 

### Return type

[**BarcodeResponseList**](BarcodeResponseList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **barcode_recognize_body_post**
> BarcodeResponseList barcode_recognize_body_post(recognize_base64_request)

Recognize barcode from file in request body using POST requests with parameters in body in json or xml format.

### Example
```python
import time
import aspose_barcode_cloud
from aspose_barcode_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose_barcode_cloud.RecognizeApi()
recognize_base64_request = aspose_barcode_cloud.RecognizeBase64Request() # RecognizeBase64Request | Barcode recognition request

try:
    # Recognize barcode from file in request body using POST requests with parameters in body in json or xml format.
    api_response = api_instance.barcode_recognize_body_post(recognize_base64_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecognizeApi->barcode_recognize_body_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
---- | ---- | ------------ | -----
 **recognize_base64_request** | [**RecognizeBase64Request**](RecognizeBase64Request.md)| Barcode recognition request | 

### Return type

[**BarcodeResponseList**](BarcodeResponseList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **barcode_recognize_form_post**
> BarcodeResponseList barcode_recognize_form_post(barcode_type, file, recognition_mode=recognition_mode, image_kind=image_kind)

Recognize barcode from file in request body using POST requests with parameters in multipart form.

### Example
```python
import time
import aspose_barcode_cloud
from aspose_barcode_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose_barcode_cloud.RecognizeApi()
barcode_type = aspose_barcode_cloud.DecodeBarcodeType() # DecodeBarcodeType | 
file = None # bytearray | 
recognition_mode = aspose_barcode_cloud.RecognitionMode() # RecognitionMode |  (optional)
image_kind = aspose_barcode_cloud.RecognitionImageKind() # RecognitionImageKind |  (optional)

try:
    # Recognize barcode from file in request body using POST requests with parameters in multipart form.
    api_response = api_instance.barcode_recognize_form_post(barcode_type, file, recognition_mode=recognition_mode, image_kind=image_kind)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecognizeApi->barcode_recognize_form_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
---- | ---- | ------------ | -----
 **barcode_type** | [**DecodeBarcodeType**](DecodeBarcodeType.md)|  | 
 **file** | **bytearray**|  | 
 **recognition_mode** | [**RecognitionMode**](RecognitionMode.md)|  | [optional] 
 **image_kind** | [**RecognitionImageKind**](RecognitionImageKind.md)|  | [optional] 

### Return type

[**BarcodeResponseList**](BarcodeResponseList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

