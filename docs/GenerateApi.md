# aspose_barcode_cloud.GenerateApi

All URIs are relative to *https://api.aspose.cloud/v4.0*

Method | HTTP request | Description
------ | ------------ | -----------
[**generate**](GenerateApi.md#generate) | **GET** /barcode/generate/{barcodeType} | Generate barcode using GET request with parameters in route and query string.
[**generate_body**](GenerateApi.md#generate_body) | **POST** /barcode/generate-body | Generate barcode using POST request with parameters in body in json or xml format.
[**generate_multipart**](GenerateApi.md#generate_multipart) | **POST** /barcode/generate-multipart | Generate barcode using POST request with parameters in multipart form.


# **generate**
> bytearray generate(barcode_type, data, data_type=data_type, image_format=image_format, text_location=text_location, foreground_color=foreground_color, background_color=background_color, units=units, resolution=resolution, image_height=image_height, image_width=image_width, rotation_angle=rotation_angle)

Generate barcode using GET request with parameters in route and query string.

### Example
```python
import time
import aspose_barcode_cloud
from aspose_barcode_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = aspose_barcode_cloud.Configuration(access_token="YOUR_ACCESS_TOKEN")

# create an instance of the API class
api_instance = aspose_barcode_cloud.GenerateApi(aspose_barcode_cloud.ApiClient(configuration))
barcode_type = aspose_barcode_cloud.EncodeBarcodeType() # EncodeBarcodeType | Type of barcode to generate.
data = 'data_example' # str | String represents data to encode
data_type = aspose_barcode_cloud.EncodeDataType() # EncodeDataType | Type of data to encode. Default value: StringData. (optional)
image_format = aspose_barcode_cloud.BarcodeImageFormat() # BarcodeImageFormat | Barcode output image format. Default value: png (optional)
text_location = aspose_barcode_cloud.CodeLocation() # CodeLocation | Specify the displaying Text Location, set to CodeLocation.None to hide CodeText. Default value: Depends on BarcodeType. CodeLocation.Below for 1D Barcodes. CodeLocation.None for 2D Barcodes. (optional)
foreground_color = 'Black' # str | Specify the displaying bars and content Color. Value: Color name from https://reference.aspose.com/drawing/net/system.drawing/color/ or ARGB value started with #. For example: AliceBlue or #FF000000 Default value: Black. (optional) (default to 'Black')
background_color = 'White' # str | Background color of the barcode image. Value: Color name from https://reference.aspose.com/drawing/net/system.drawing/color/ or ARGB value started with #. For example: AliceBlue or #FF000000 Default value: White. (optional) (default to 'White')
units = aspose_barcode_cloud.GraphicsUnit() # GraphicsUnit | Common Units for all measuring in query. Default units: pixel. (optional)
resolution = 3.4 # float | Resolution of the BarCode image. One value for both dimensions. Default value: 96 dpi. Decimal separator is dot. (optional)
image_height = 3.4 # float | Height of the barcode image in given units. Default units: pixel. Decimal separator is dot. (optional)
image_width = 3.4 # float | Width of the barcode image in given units. Default units: pixel. Decimal separator is dot. (optional)
rotation_angle = 56 # int | BarCode image rotation angle, measured in degree, e.g. RotationAngle = 0 or RotationAngle = 360 means no rotation. If RotationAngle NOT equal to 90, 180, 270 or 0, it may increase the difficulty for the scanner to read the image. Default value: 0. (optional)

try:
    # Generate barcode using GET request with parameters in route and query string.
    api_response = api_instance.generate(barcode_type, data, data_type=data_type, image_format=image_format, text_location=text_location, foreground_color=foreground_color, background_color=background_color, units=units, resolution=resolution, image_height=image_height, image_width=image_width, rotation_angle=rotation_angle)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerateApi->generate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
---- | ---- | ------------ | -----
 **barcode_type** | [**EncodeBarcodeType**](.md)| Type of barcode to generate. | 
 **data** | **str**| String represents data to encode | 
 **data_type** | [**EncodeDataType**](.md)| Type of data to encode. Default value: StringData. | [optional] 
 **image_format** | [**BarcodeImageFormat**](.md)| Barcode output image format. Default value: png | [optional] 
 **text_location** | [**CodeLocation**](.md)| Specify the displaying Text Location, set to CodeLocation.None to hide CodeText. Default value: Depends on BarcodeType. CodeLocation.Below for 1D Barcodes. CodeLocation.None for 2D Barcodes. | [optional] 
 **foreground_color** | **str**| Specify the displaying bars and content Color. Value: Color name from https://reference.aspose.com/drawing/net/system.drawing/color/ or ARGB value started with #. For example: AliceBlue or #FF000000 Default value: Black. | [optional] [default to &#39;Black&#39;]
 **background_color** | **str**| Background color of the barcode image. Value: Color name from https://reference.aspose.com/drawing/net/system.drawing/color/ or ARGB value started with #. For example: AliceBlue or #FF000000 Default value: White. | [optional] [default to &#39;White&#39;]
 **units** | [**GraphicsUnit**](.md)| Common Units for all measuring in query. Default units: pixel. | [optional] 
 **resolution** | **float**| Resolution of the BarCode image. One value for both dimensions. Default value: 96 dpi. Decimal separator is dot. | [optional] 
 **image_height** | **float**| Height of the barcode image in given units. Default units: pixel. Decimal separator is dot. | [optional] 
 **image_width** | **float**| Width of the barcode image in given units. Default units: pixel. Decimal separator is dot. | [optional] 
 **rotation_angle** | **int**| BarCode image rotation angle, measured in degree, e.g. RotationAngle &#x3D; 0 or RotationAngle &#x3D; 360 means no rotation. If RotationAngle NOT equal to 90, 180, 270 or 0, it may increase the difficulty for the scanner to read the image. Default value: 0. | [optional] 

### Return type

**bytearray**

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png, image/bmp, image/gif, image/jpeg, image/svg+xml, image/tiff, application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_body**
> bytearray generate_body(generate_params)

Generate barcode using POST request with parameters in body in json or xml format.

### Example
```python
import time
import aspose_barcode_cloud
from aspose_barcode_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = aspose_barcode_cloud.Configuration(access_token="YOUR_ACCESS_TOKEN")

# create an instance of the API class
api_instance = aspose_barcode_cloud.GenerateApi(aspose_barcode_cloud.ApiClient(configuration))
generate_params = aspose_barcode_cloud.GenerateParams() # GenerateParams | Parameters of generation

try:
    # Generate barcode using POST request with parameters in body in json or xml format.
    api_response = api_instance.generate_body(generate_params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerateApi->generate_body: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
---- | ---- | ------------ | -----
 **generate_params** | [**GenerateParams**](GenerateParams.md)| Parameters of generation | 

### Return type

**bytearray**

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: image/png, image/bmp, image/gif, image/jpeg, image/svg+xml, image/tiff, application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_multipart**
> bytearray generate_multipart(barcode_type, data, data_type=data_type, image_format=image_format, text_location=text_location, foreground_color=foreground_color, background_color=background_color, units=units, resolution=resolution, image_height=image_height, image_width=image_width, rotation_angle=rotation_angle)

Generate barcode using POST request with parameters in multipart form.

### Example
```python
import time
import aspose_barcode_cloud
from aspose_barcode_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = aspose_barcode_cloud.Configuration(access_token="YOUR_ACCESS_TOKEN")

# create an instance of the API class
api_instance = aspose_barcode_cloud.GenerateApi(aspose_barcode_cloud.ApiClient(configuration))
barcode_type = aspose_barcode_cloud.EncodeBarcodeType() # EncodeBarcodeType | 
data = 'data_example' # str | String represents data to encode
data_type = aspose_barcode_cloud.EncodeDataType() # EncodeDataType |  (optional)
image_format = aspose_barcode_cloud.BarcodeImageFormat() # BarcodeImageFormat |  (optional)
text_location = aspose_barcode_cloud.CodeLocation() # CodeLocation |  (optional)
foreground_color = 'Black' # str | Specify the displaying bars and content Color. Value: Color name from https://reference.aspose.com/drawing/net/system.drawing/color/ or ARGB value started with #. For example: AliceBlue or #FF000000 Default value: Black. (optional) (default to 'Black')
background_color = 'White' # str | Background color of the barcode image. Value: Color name from https://reference.aspose.com/drawing/net/system.drawing/color/ or ARGB value started with #. For example: AliceBlue or #FF000000 Default value: White. (optional) (default to 'White')
units = aspose_barcode_cloud.GraphicsUnit() # GraphicsUnit |  (optional)
resolution = 3.4 # float | Resolution of the BarCode image. One value for both dimensions. Default value: 96 dpi. Decimal separator is dot. (optional)
image_height = 3.4 # float | Height of the barcode image in given units. Default units: pixel. Decimal separator is dot. (optional)
image_width = 3.4 # float | Width of the barcode image in given units. Default units: pixel. Decimal separator is dot. (optional)
rotation_angle = 56 # int | BarCode image rotation angle, measured in degree, e.g. RotationAngle = 0 or RotationAngle = 360 means no rotation. If RotationAngle NOT equal to 90, 180, 270 or 0, it may increase the difficulty for the scanner to read the image. Default value: 0. (optional)

try:
    # Generate barcode using POST request with parameters in multipart form.
    api_response = api_instance.generate_multipart(barcode_type, data, data_type=data_type, image_format=image_format, text_location=text_location, foreground_color=foreground_color, background_color=background_color, units=units, resolution=resolution, image_height=image_height, image_width=image_width, rotation_angle=rotation_angle)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerateApi->generate_multipart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
---- | ---- | ------------ | -----
 **barcode_type** | [**EncodeBarcodeType**](EncodeBarcodeType.md)|  | 
 **data** | **str**| String represents data to encode | 
 **data_type** | [**EncodeDataType**](EncodeDataType.md)|  | [optional] 
 **image_format** | [**BarcodeImageFormat**](BarcodeImageFormat.md)|  | [optional] 
 **text_location** | [**CodeLocation**](CodeLocation.md)|  | [optional] 
 **foreground_color** | **str**| Specify the displaying bars and content Color. Value: Color name from https://reference.aspose.com/drawing/net/system.drawing/color/ or ARGB value started with #. For example: AliceBlue or #FF000000 Default value: Black. | [optional] [default to &#39;Black&#39;]
 **background_color** | **str**| Background color of the barcode image. Value: Color name from https://reference.aspose.com/drawing/net/system.drawing/color/ or ARGB value started with #. For example: AliceBlue or #FF000000 Default value: White. | [optional] [default to &#39;White&#39;]
 **units** | [**GraphicsUnit**](GraphicsUnit.md)|  | [optional] 
 **resolution** | **float**| Resolution of the BarCode image. One value for both dimensions. Default value: 96 dpi. Decimal separator is dot. | [optional] 
 **image_height** | **float**| Height of the barcode image in given units. Default units: pixel. Decimal separator is dot. | [optional] 
 **image_width** | **float**| Width of the barcode image in given units. Default units: pixel. Decimal separator is dot. | [optional] 
 **rotation_angle** | **int**| BarCode image rotation angle, measured in degree, e.g. RotationAngle &#x3D; 0 or RotationAngle &#x3D; 360 means no rotation. If RotationAngle NOT equal to 90, 180, 270 or 0, it may increase the difficulty for the scanner to read the image. Default value: 0. | [optional] 

### Return type

**bytearray**

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: image/png, image/bmp, image/gif, image/jpeg, image/svg+xml, image/tiff, application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

