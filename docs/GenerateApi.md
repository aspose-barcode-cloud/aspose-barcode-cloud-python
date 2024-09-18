# aspose_barcode_cloud.GenerateApi

All URIs are relative to *https://barcode.qa.aspose.cloud/v4.0*

Method | HTTP request | Description
------ | ------------ | -----------
[**barcode_generate_barcode_type_get**](GenerateApi.md#barcode_generate_barcode_type_get) | **GET** /barcode/generate/{barcodeType} | Generate barcode using GET request with parameters in route and query string.
[**barcode_generate_body_post**](GenerateApi.md#barcode_generate_body_post) | **POST** /barcode/generate-body | Generate barcode using POST request with parameters in body in json or xml format.
[**barcode_generate_form_post**](GenerateApi.md#barcode_generate_form_post) | **POST** /barcode/generate-form | Generate barcode using POST request with parameters in url ecncoded form.


# **barcode_generate_barcode_type_get**
> bytearray barcode_generate_barcode_type_get(barcode_type, data, data_type=data_type, image_format=image_format, two_d_display_text=two_d_display_text, text_location=text_location, text_alignment=text_alignment, foreground_color=foreground_color, background_color=background_color, units=units, resolution=resolution, image_height=image_height, image_width=image_width, rotation_angle=rotation_angle)

Generate barcode using GET request with parameters in route and query string.

### Example
```python
import time
import aspose_barcode_cloud
from aspose_barcode_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose_barcode_cloud.GenerateApi()
barcode_type = aspose_barcode_cloud.EncodeBarcodeType() # EncodeBarcodeType | Type of barcode to generate.
data = 'data_example' # str | String represents data to encode
data_type = aspose_barcode_cloud.EncodeDataType() # EncodeDataType | Type of data to encode.  Default value:  EncodeDataType.StringData. (optional)
image_format = aspose_barcode_cloud.AvailableBarCodeImageFormat() # AvailableBarCodeImageFormat | Barcode output image format.  Default value: png (optional)
two_d_display_text = 'two_d_display_text_example' # str | Text that will be displayed instead of codetext in 2D barcodes.  Used for: Aztec, Pdf417, DataMatrix, QR, MaxiCode, DotCode (optional)
text_location = aspose_barcode_cloud.CodeLocation() # CodeLocation | Specify the displaying Text Location, set to CodeLocation.None to hide CodeText.  Default value: CodeLocation.Below. (optional)
text_alignment = aspose_barcode_cloud.TextAlignment() # TextAlignment | Text alignment.  Default value: TextAligment.Left (optional)
foreground_color = 'foreground_color_example' # str | Specify the displaying bars and content Color.   Value: Color name from https://reference.aspose.com/drawing/net/system.drawing/color/ or ARGB value started with #.   For example: Color.AliceBlue or #FF000000  Default value: Color.Black. (optional)
background_color = 'background_color_example' # str | Background color of the barcode image.  Value: Color name from https://reference.aspose.com/drawing/net/system.drawing/color/ or ARGB value started with #.   For example: Color.AliceBlue or #FF000000  Default value: Color.White. (optional)
units = aspose_barcode_cloud.AvailableGraphicsUnit() # AvailableGraphicsUnit | Common Units for all measuring in query. Default units: pixel. (optional)
resolution = 3.4 # float | Resolution of the BarCode image.  One value for both dimensions.  Default value: 96 dpi. (optional)
image_height = 3.4 # float | Height of the barcode image in given units. Default units: pixel. (optional)
image_width = 3.4 # float | Width of the barcode image in given units. Default units: pixel. (optional)
rotation_angle = 56 # int | BarCode image rotation angle, measured in degree, e.g. RotationAngle = 0 or RotationAngle = 360 means no rotation.  If RotationAngle NOT equal to 90, 180, 270 or 0, it may increase the difficulty for the scanner to read the image.  Default value: 0. (optional)

try:
    # Generate barcode using GET request with parameters in route and query string.
    api_response = api_instance.barcode_generate_barcode_type_get(barcode_type, data, data_type=data_type, image_format=image_format, two_d_display_text=two_d_display_text, text_location=text_location, text_alignment=text_alignment, foreground_color=foreground_color, background_color=background_color, units=units, resolution=resolution, image_height=image_height, image_width=image_width, rotation_angle=rotation_angle)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerateApi->barcode_generate_barcode_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
---- | ---- | ------------ | -----
 **barcode_type** | [**EncodeBarcodeType**](.md)| Type of barcode to generate. | 
 **data** | **str**| String represents data to encode | 
 **data_type** | [**EncodeDataType**](.md)| Type of data to encode.  Default value:  EncodeDataType.StringData. | [optional] 
 **image_format** | [**AvailableBarCodeImageFormat**](.md)| Barcode output image format.  Default value: png | [optional] 
 **two_d_display_text** | **str**| Text that will be displayed instead of codetext in 2D barcodes.  Used for: Aztec, Pdf417, DataMatrix, QR, MaxiCode, DotCode | [optional] 
 **text_location** | [**CodeLocation**](.md)| Specify the displaying Text Location, set to CodeLocation.None to hide CodeText.  Default value: CodeLocation.Below. | [optional] 
 **text_alignment** | [**TextAlignment**](.md)| Text alignment.  Default value: TextAligment.Left | [optional] 
 **foreground_color** | **str**| Specify the displaying bars and content Color.   Value: Color name from https://reference.aspose.com/drawing/net/system.drawing/color/ or ARGB value started with #.   For example: Color.AliceBlue or #FF000000  Default value: Color.Black. | [optional] 
 **background_color** | **str**| Background color of the barcode image.  Value: Color name from https://reference.aspose.com/drawing/net/system.drawing/color/ or ARGB value started with #.   For example: Color.AliceBlue or #FF000000  Default value: Color.White. | [optional] 
 **units** | [**AvailableGraphicsUnit**](.md)| Common Units for all measuring in query. Default units: pixel. | [optional] 
 **resolution** | **float**| Resolution of the BarCode image.  One value for both dimensions.  Default value: 96 dpi. | [optional] 
 **image_height** | **float**| Height of the barcode image in given units. Default units: pixel. | [optional] 
 **image_width** | **float**| Width of the barcode image in given units. Default units: pixel. | [optional] 
 **rotation_angle** | **int**| BarCode image rotation angle, measured in degree, e.g. RotationAngle &#x3D; 0 or RotationAngle &#x3D; 360 means no rotation.  If RotationAngle NOT equal to 90, 180, 270 or 0, it may increase the difficulty for the scanner to read the image.  Default value: 0. | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png, image/bmp, image/gif, image/jpeg, image/svg+xml, image/tiff, application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **barcode_generate_body_post**
> bytearray barcode_generate_body_post(generate_params)

Generate barcode using POST request with parameters in body in json or xml format.

### Example
```python
import time
import aspose_barcode_cloud
from aspose_barcode_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose_barcode_cloud.GenerateApi()
generate_params = aspose_barcode_cloud.GenerateParams() # GenerateParams | Parameters of generation

try:
    # Generate barcode using POST request with parameters in body in json or xml format.
    api_response = api_instance.barcode_generate_body_post(generate_params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerateApi->barcode_generate_body_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
---- | ---- | ------------ | -----
 **generate_params** | [**GenerateParams**](GenerateParams.md)| Parameters of generation | 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: image/png, image/bmp, image/gif, image/jpeg, image/svg+xml, image/tiff, application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **barcode_generate_form_post**
> bytearray barcode_generate_form_post(barcode_type, data, data_type=data_type, image_format=image_format, two_d_display_text=two_d_display_text, text_location=text_location, text_alignment=text_alignment, foreground_color=foreground_color, background_color=background_color, units=units, resolution=resolution, image_height=image_height, image_width=image_width, rotation_angle=rotation_angle)

Generate barcode using POST request with parameters in url ecncoded form.

### Example
```python
import time
import aspose_barcode_cloud
from aspose_barcode_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aspose_barcode_cloud.GenerateApi()
barcode_type = aspose_barcode_cloud.EncodeBarcodeType() # EncodeBarcodeType | 
data = 'data_example' # str | String represents data to encode
data_type = aspose_barcode_cloud.EncodeDataType() # EncodeDataType |  (optional)
image_format = aspose_barcode_cloud.AvailableBarCodeImageFormat() # AvailableBarCodeImageFormat |  (optional)
two_d_display_text = 'two_d_display_text_example' # str | Text that will be displayed instead of codetext in 2D barcodes.  Used for: Aztec, Pdf417, DataMatrix, QR, MaxiCode, DotCode (optional)
text_location = aspose_barcode_cloud.CodeLocation() # CodeLocation |  (optional)
text_alignment = aspose_barcode_cloud.TextAlignment() # TextAlignment |  (optional)
foreground_color = 'foreground_color_example' # str | Specify the displaying bars and content Color.   Value: Color name from https://reference.aspose.com/drawing/net/system.drawing/color/ or ARGB value started with #.   For example: Color.AliceBlue or #FF000000  Default value: Color.Black. (optional)
background_color = 'background_color_example' # str | Background color of the barcode image.  Value: Color name from https://reference.aspose.com/drawing/net/system.drawing/color/ or ARGB value started with #.   For example: Color.AliceBlue or #FF000000  Default value: Color.White. (optional)
units = aspose_barcode_cloud.AvailableGraphicsUnit() # AvailableGraphicsUnit |  (optional)
resolution = 3.4 # float | Resolution of the BarCode image.  One value for both dimensions.  Default value: 96 dpi. (optional)
image_height = 3.4 # float | Height of the barcode image in given units. Default units: pixel. (optional)
image_width = 3.4 # float | Width of the barcode image in given units. Default units: pixel. (optional)
rotation_angle = 56 # int | BarCode image rotation angle, measured in degree, e.g. RotationAngle = 0 or RotationAngle = 360 means no rotation.  If RotationAngle NOT equal to 90, 180, 270 or 0, it may increase the difficulty for the scanner to read the image.  Default value: 0. (optional)

try:
    # Generate barcode using POST request with parameters in url ecncoded form.
    api_response = api_instance.barcode_generate_form_post(barcode_type, data, data_type=data_type, image_format=image_format, two_d_display_text=two_d_display_text, text_location=text_location, text_alignment=text_alignment, foreground_color=foreground_color, background_color=background_color, units=units, resolution=resolution, image_height=image_height, image_width=image_width, rotation_angle=rotation_angle)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerateApi->barcode_generate_form_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
---- | ---- | ------------ | -----
 **barcode_type** | [**EncodeBarcodeType**](EncodeBarcodeType.md)|  | 
 **data** | **str**| String represents data to encode | 
 **data_type** | [**EncodeDataType**](EncodeDataType.md)|  | [optional] 
 **image_format** | [**AvailableBarCodeImageFormat**](AvailableBarCodeImageFormat.md)|  | [optional] 
 **two_d_display_text** | **str**| Text that will be displayed instead of codetext in 2D barcodes.  Used for: Aztec, Pdf417, DataMatrix, QR, MaxiCode, DotCode | [optional] 
 **text_location** | [**CodeLocation**](CodeLocation.md)|  | [optional] 
 **text_alignment** | [**TextAlignment**](TextAlignment.md)|  | [optional] 
 **foreground_color** | **str**| Specify the displaying bars and content Color.   Value: Color name from https://reference.aspose.com/drawing/net/system.drawing/color/ or ARGB value started with #.   For example: Color.AliceBlue or #FF000000  Default value: Color.Black. | [optional] 
 **background_color** | **str**| Background color of the barcode image.  Value: Color name from https://reference.aspose.com/drawing/net/system.drawing/color/ or ARGB value started with #.   For example: Color.AliceBlue or #FF000000  Default value: Color.White. | [optional] 
 **units** | [**AvailableGraphicsUnit**](AvailableGraphicsUnit.md)|  | [optional] 
 **resolution** | **float**| Resolution of the BarCode image.  One value for both dimensions.  Default value: 96 dpi. | [optional] 
 **image_height** | **float**| Height of the barcode image in given units. Default units: pixel. | [optional] 
 **image_width** | **float**| Width of the barcode image in given units. Default units: pixel. | [optional] 
 **rotation_angle** | **int**| BarCode image rotation angle, measured in degree, e.g. RotationAngle &#x3D; 0 or RotationAngle &#x3D; 360 means no rotation.  If RotationAngle NOT equal to 90, 180, 270 or 0, it may increase the difficulty for the scanner to read the image.  Default value: 0. | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: image/png, image/bmp, image/gif, image/jpeg, image/svg+xml, image/tiff, application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

