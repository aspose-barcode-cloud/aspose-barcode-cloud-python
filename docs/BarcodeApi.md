# aspose_barcode_cloud.BarcodeApi

All URIs are relative to *https://api.aspose.cloud/v3.0*

Method | HTTP request | Description
------ | ------------ | -----------
[**get_barcode_generate**](BarcodeApi.md#get_barcode_generate) | **GET** /barcode/generate | Generate barcode.
[**get_barcode_recognize**](BarcodeApi.md#get_barcode_recognize) | **GET** /barcode/{name}/recognize | Recognize barcode from a file on server.
[**post_barcode_recognize_from_url_or_content**](BarcodeApi.md#post_barcode_recognize_from_url_or_content) | **POST** /barcode/recognize | Recognize barcode from an url or from request body. Request body can contain raw data bytes of the image or encoded with base64.
[**post_generate_multiple**](BarcodeApi.md#post_generate_multiple) | **POST** /barcode/generateMultiple | Generate multiple barcodes and return in response stream
[**put_barcode_generate_file**](BarcodeApi.md#put_barcode_generate_file) | **PUT** /barcode/{name}/generate | Generate barcode and save on server (from query params or from file with json or xml content)
[**put_barcode_recognize_from_body**](BarcodeApi.md#put_barcode_recognize_from_body) | **PUT** /barcode/{name}/recognize | Recognition of a barcode from file on server with parameters in body.
[**put_generate_multiple**](BarcodeApi.md#put_generate_multiple) | **PUT** /barcode/{name}/generateMultiple | Generate image with multiple barcodes and put new file on server


# **get_barcode_generate**
> file get_barcode_generate(type, text, two_d_display_text=two_d_display_text, text_location=text_location, text_alignment=text_alignment, text_color=text_color, font_size_mode=font_size_mode, no_wrap=no_wrap, resolution=resolution, resolution_x=resolution_x, resolution_y=resolution_y, dimension_x=dimension_x, text_space=text_space, units=units, size_mode=size_mode, bar_height=bar_height, image_height=image_height, image_width=image_width, rotation_angle=rotation_angle, back_color=back_color, bar_color=bar_color, border_color=border_color, border_width=border_width, border_dash_style=border_dash_style, border_visible=border_visible, enable_checksum=enable_checksum, enable_escape=enable_escape, filled_bars=filled_bars, always_show_checksum=always_show_checksum, wide_narrow_ratio=wide_narrow_ratio, validate_text=validate_text, supplement_data=supplement_data, supplement_space=supplement_space, bar_width_reduction=bar_width_reduction, format=format)

Generate barcode.

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
api_instance = aspose_barcode_cloud.BarcodeApi(aspose_barcode_cloud.ApiClient(configuration))
type = 'type_example' # str | Type of barcode to generate.
text = 'text_example' # str | Text to encode.
two_d_display_text = 'two_d_display_text_example' # str | Text that will be displayed instead of codetext in 2D barcodes. Used for: Aztec, Pdf417, DataMatrix, QR, MaxiCode, DotCode (optional)
text_location = 'text_location_example' # str | Specify the displaying Text Location, set to CodeLocation.None to hide CodeText. Default value: CodeLocation.Below. (optional)
text_alignment = 'text_alignment_example' # str | Text alignment. (optional)
text_color = 'text_color_example' # str | Specify the displaying CodeText's Color. Default value: Color.Black. (optional)
font_size_mode = 'font_size_mode_example' # str | Specify FontSizeMode. If FontSizeMode is set to Auto, font size will be calculated automatically based on xDimension value. It is recommended to use FontSizeMode.Auto especially in AutoSizeMode.Nearest or AutoSizeMode.Interpolation. Default value: FontSizeMode.Auto. (optional)
no_wrap = True # bool | Specify word wraps (line breaks) within text. Default value: False. (optional)
resolution = 1.2 # float | Resolution of the BarCode image. One value for both dimensions. Default value: 96 dpi. (optional)
resolution_x = 1.2 # float | DEPRECATED: Use 'Resolution' instead. (optional)
resolution_y = 1.2 # float | DEPRECATED: Use 'Resolution' instead. (optional)
dimension_x = 1.2 # float | The smallest width of the unit of BarCode bars or spaces. Increase this will increase the whole barcode image width. Ignored if AutoSizeMode property is set to AutoSizeMode.Nearest or AutoSizeMode.Interpolation. (optional)
text_space = 1.2 # float | Space between the CodeText and the BarCode in Unit value. Default value: 2pt. Ignored for EAN8, EAN13, UPCE, UPCA, ISBN, ISMN, ISSN, UpcaGs1DatabarCoupon. (optional)
units = 'units_example' # str | Common Units for all measuring in query. Default units: pixel. (optional)
size_mode = 'size_mode_example' # str | Specifies the different types of automatic sizing modes. Default value: AutoSizeMode.None. (optional)
bar_height = 1.2 # float | Height of the barcode in given units. Default units: pixel. (optional)
image_height = 1.2 # float | Height of the barcode image in given units. Default units: pixel. (optional)
image_width = 1.2 # float | Width of the barcode image in given units. Default units: pixel. (optional)
rotation_angle = 1.2 # float | BarCode image rotation angle, measured in degree, e.g. RotationAngle = 0 or RotationAngle = 360 means no rotation. If RotationAngle NOT equal to 90, 180, 270 or 0, it may increase the difficulty for the scanner to read the image. Default value: 0. (optional)
back_color = 'back_color_example' # str | Background color of the barcode image. Default value: Color.White. (optional)
bar_color = 'bar_color_example' # str | Bars color. Default value: Color.Black. (optional)
border_color = 'border_color_example' # str | Border color. Default value: Color.Black. (optional)
border_width = 1.2 # float | Border width. Default value: 0. Ignored if Visible is set to False. (optional)
border_dash_style = 'border_dash_style_example' # str | Border dash style. Default value: BorderDashStyle.Solid. (optional)
border_visible = True # bool | Border visibility. If False than parameter Width is always ignored (0). Default value: False. (optional)
enable_checksum = 'enable_checksum_example' # str | Enable checksum during generation 1D barcodes. Default is treated as Yes for symbology which must contain checksum, as No where checksum only possible. Checksum is possible: Code39 Standard/Extended, Standard2of5, Interleaved2of5, Matrix2of5, ItalianPost25, DeutschePostIdentcode, DeutschePostLeitcode, VIN, Codabar Checksum always used: Rest symbology (optional)
enable_escape = True # bool | Indicates whether explains the character \"\\\" as an escape character in CodeText property. Used for Pdf417, DataMatrix, Code128 only If the EnableEscape is True, \"\\\" will be explained as a special escape character. Otherwise, \"\\\" acts as normal characters. Aspose.BarCode supports input decimal ascii code and mnemonic for ASCII control-code characters. For example, \\013 and \\\\CR stands for CR. (optional)
filled_bars = True # bool | Value indicating whether bars are filled. Only for 1D barcodes. Default value: True. (optional)
always_show_checksum = True # bool | Always display checksum digit in the human readable text for Code128 and GS1Code128 barcodes. (optional)
wide_narrow_ratio = 1.2 # float | Wide bars to Narrow bars ratio. Default value: 3, that is, wide bars are 3 times as wide as narrow bars. Used for ITF, PZN, PharmaCode, Standard2of5, Interleaved2of5, Matrix2of5, ItalianPost25, IATA2of5, VIN, DeutschePost, OPC, Code32, DataLogic2of5, PatchCode, Code39Extended, Code39Standard (optional)
validate_text = True # bool | Only for 1D barcodes. If codetext is incorrect and value set to True - exception will be thrown. Otherwise codetext will be corrected to match barcode's specification. Exception always will be thrown for: Databar symbology if codetext is incorrect. Exception always will not be thrown for: AustraliaPost, SingaporePost, Code39Extended, Code93Extended, Code16K, Code128 symbology if codetext is incorrect. (optional)
supplement_data = 'supplement_data_example' # str | Supplement parameters. Used for Interleaved2of5, Standard2of5, EAN13, EAN8, UPCA, UPCE, ISBN, ISSN, ISMN. (optional)
supplement_space = 1.2 # float | Space between main the BarCode and supplement BarCode. (optional)
bar_width_reduction = 1.2 # float | Bars reduction value that is used to compensate ink spread while printing. (optional)
format = 'format_example' # str | Result image format. (optional)

try:
    # Generate barcode.
    api_response = api_instance.get_barcode_generate(type, text, two_d_display_text=two_d_display_text, text_location=text_location, text_alignment=text_alignment, text_color=text_color, font_size_mode=font_size_mode, no_wrap=no_wrap, resolution=resolution, resolution_x=resolution_x, resolution_y=resolution_y, dimension_x=dimension_x, text_space=text_space, units=units, size_mode=size_mode, bar_height=bar_height, image_height=image_height, image_width=image_width, rotation_angle=rotation_angle, back_color=back_color, bar_color=bar_color, border_color=border_color, border_width=border_width, border_dash_style=border_dash_style, border_visible=border_visible, enable_checksum=enable_checksum, enable_escape=enable_escape, filled_bars=filled_bars, always_show_checksum=always_show_checksum, wide_narrow_ratio=wide_narrow_ratio, validate_text=validate_text, supplement_data=supplement_data, supplement_space=supplement_space, bar_width_reduction=bar_width_reduction, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BarcodeApi->get_barcode_generate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
---- | ---- | ------------ | -----
 **type** | **str**| Type of barcode to generate. | 
 **text** | **str**| Text to encode. | 
 **two_d_display_text** | **str**| Text that will be displayed instead of codetext in 2D barcodes. Used for: Aztec, Pdf417, DataMatrix, QR, MaxiCode, DotCode | [optional] 
 **text_location** | **str**| Specify the displaying Text Location, set to CodeLocation.None to hide CodeText. Default value: CodeLocation.Below. | [optional] 
 **text_alignment** | **str**| Text alignment. | [optional] 
 **text_color** | **str**| Specify the displaying CodeText&#39;s Color. Default value: Color.Black. | [optional] 
 **font_size_mode** | **str**| Specify FontSizeMode. If FontSizeMode is set to Auto, font size will be calculated automatically based on xDimension value. It is recommended to use FontSizeMode.Auto especially in AutoSizeMode.Nearest or AutoSizeMode.Interpolation. Default value: FontSizeMode.Auto. | [optional] 
 **no_wrap** | **bool**| Specify word wraps (line breaks) within text. Default value: False. | [optional] 
 **resolution** | **float**| Resolution of the BarCode image. One value for both dimensions. Default value: 96 dpi. | [optional] 
 **resolution_x** | **float**| DEPRECATED: Use &#39;Resolution&#39; instead. | [optional] 
 **resolution_y** | **float**| DEPRECATED: Use &#39;Resolution&#39; instead. | [optional] 
 **dimension_x** | **float**| The smallest width of the unit of BarCode bars or spaces. Increase this will increase the whole barcode image width. Ignored if AutoSizeMode property is set to AutoSizeMode.Nearest or AutoSizeMode.Interpolation. | [optional] 
 **text_space** | **float**| Space between the CodeText and the BarCode in Unit value. Default value: 2pt. Ignored for EAN8, EAN13, UPCE, UPCA, ISBN, ISMN, ISSN, UpcaGs1DatabarCoupon. | [optional] 
 **units** | **str**| Common Units for all measuring in query. Default units: pixel. | [optional] 
 **size_mode** | **str**| Specifies the different types of automatic sizing modes. Default value: AutoSizeMode.None. | [optional] 
 **bar_height** | **float**| Height of the barcode in given units. Default units: pixel. | [optional] 
 **image_height** | **float**| Height of the barcode image in given units. Default units: pixel. | [optional] 
 **image_width** | **float**| Width of the barcode image in given units. Default units: pixel. | [optional] 
 **rotation_angle** | **float**| BarCode image rotation angle, measured in degree, e.g. RotationAngle &#x3D; 0 or RotationAngle &#x3D; 360 means no rotation. If RotationAngle NOT equal to 90, 180, 270 or 0, it may increase the difficulty for the scanner to read the image. Default value: 0. | [optional] 
 **back_color** | **str**| Background color of the barcode image. Default value: Color.White. | [optional] 
 **bar_color** | **str**| Bars color. Default value: Color.Black. | [optional] 
 **border_color** | **str**| Border color. Default value: Color.Black. | [optional] 
 **border_width** | **float**| Border width. Default value: 0. Ignored if Visible is set to False. | [optional] 
 **border_dash_style** | **str**| Border dash style. Default value: BorderDashStyle.Solid. | [optional] 
 **border_visible** | **bool**| Border visibility. If False than parameter Width is always ignored (0). Default value: False. | [optional] 
 **enable_checksum** | **str**| Enable checksum during generation 1D barcodes. Default is treated as Yes for symbology which must contain checksum, as No where checksum only possible. Checksum is possible: Code39 Standard/Extended, Standard2of5, Interleaved2of5, Matrix2of5, ItalianPost25, DeutschePostIdentcode, DeutschePostLeitcode, VIN, Codabar Checksum always used: Rest symbology | [optional] 
 **enable_escape** | **bool**| Indicates whether explains the character \&quot;\\\&quot; as an escape character in CodeText property. Used for Pdf417, DataMatrix, Code128 only If the EnableEscape is True, \&quot;\\\&quot; will be explained as a special escape character. Otherwise, \&quot;\\\&quot; acts as normal characters. Aspose.BarCode supports input decimal ascii code and mnemonic for ASCII control-code characters. For example, \\013 and \\\\CR stands for CR. | [optional] 
 **filled_bars** | **bool**| Value indicating whether bars are filled. Only for 1D barcodes. Default value: True. | [optional] 
 **always_show_checksum** | **bool**| Always display checksum digit in the human readable text for Code128 and GS1Code128 barcodes. | [optional] 
 **wide_narrow_ratio** | **float**| Wide bars to Narrow bars ratio. Default value: 3, that is, wide bars are 3 times as wide as narrow bars. Used for ITF, PZN, PharmaCode, Standard2of5, Interleaved2of5, Matrix2of5, ItalianPost25, IATA2of5, VIN, DeutschePost, OPC, Code32, DataLogic2of5, PatchCode, Code39Extended, Code39Standard | [optional] 
 **validate_text** | **bool**| Only for 1D barcodes. If codetext is incorrect and value set to True - exception will be thrown. Otherwise codetext will be corrected to match barcode&#39;s specification. Exception always will be thrown for: Databar symbology if codetext is incorrect. Exception always will not be thrown for: AustraliaPost, SingaporePost, Code39Extended, Code93Extended, Code16K, Code128 symbology if codetext is incorrect. | [optional] 
 **supplement_data** | **str**| Supplement parameters. Used for Interleaved2of5, Standard2of5, EAN13, EAN8, UPCA, UPCE, ISBN, ISSN, ISMN. | [optional] 
 **supplement_space** | **float**| Space between main the BarCode and supplement BarCode. | [optional] 
 **bar_width_reduction** | **float**| Bars reduction value that is used to compensate ink spread while printing. | [optional] 
 **format** | **str**| Result image format. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: image/png, image/bmp, image/gif, image/jpeg, image/svg+xml, image/tiff

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_barcode_recognize**
> BarcodeResponseList get_barcode_recognize(name, type=type, checksum_validation=checksum_validation, detect_encoding=detect_encoding, preset=preset, rect_x=rect_x, rect_y=rect_y, rect_width=rect_width, rect_height=rect_height, strip_fnc=strip_fnc, timeout=timeout, median_smoothing_window_size=median_smoothing_window_size, allow_median_smoothing=allow_median_smoothing, allow_complex_background=allow_complex_background, allow_datamatrix_industrial_barcodes=allow_datamatrix_industrial_barcodes, allow_decreased_image=allow_decreased_image, allow_detect_scan_gap=allow_detect_scan_gap, allow_incorrect_barcodes=allow_incorrect_barcodes, allow_invert_image=allow_invert_image, allow_micro_white_spots_removing=allow_micro_white_spots_removing, allow_one_d_fast_barcodes_detector=allow_one_d_fast_barcodes_detector, allow_one_d_wiped_bars_restoration=allow_one_d_wiped_bars_restoration, allow_qr_micro_qr_restoration=allow_qr_micro_qr_restoration, allow_regular_image=allow_regular_image, allow_salt_and_pepper_filtering=allow_salt_and_pepper_filtering, allow_white_spots_removing=allow_white_spots_removing, check_more1_d_variants=check_more1_d_variants, fast_scan_only=fast_scan_only, region_likelihood_threshold_percent=region_likelihood_threshold_percent, scan_window_sizes=scan_window_sizes, similarity=similarity, skip_diagonal_search=skip_diagonal_search, read_tiny_barcodes=read_tiny_barcodes, australian_post_encoding_table=australian_post_encoding_table, ignore_ending_filling_patterns_for_c_table=ignore_ending_filling_patterns_for_c_table, rectangle_region=rectangle_region, storage=storage, folder=folder)

Recognize barcode from a file on server.

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
api_instance = aspose_barcode_cloud.BarcodeApi(aspose_barcode_cloud.ApiClient(configuration))
name = 'name_example' # str | The image file name.
type = 'type_example' # str | The type of barcode to read. (optional)
checksum_validation = 'checksum_validation_example' # str | Enable checksum validation during recognition for 1D barcodes. Default is treated as Yes for symbologies which must contain checksum, as No where checksum only possible. Checksum never used: Codabar Checksum is possible: Code39 Standard/Extended, Standard2of5, Interleaved2of5, Matrix2of5, ItalianPost25, DeutschePostIdentcode, DeutschePostLeitcode, VIN Checksum always used: Rest symbologies (optional)
detect_encoding = True # bool | A flag which force engine to detect codetext encoding for Unicode. (optional)
preset = 'preset_example' # str | Preset allows to configure recognition quality and speed manually. You can quickly set up Preset by embedded presets: HighPerformance, NormalQuality, HighQuality, MaxBarCodes or you can manually configure separate options. Default value of Preset is NormalQuality. (optional)
rect_x = 56 # int | Set X for area for recognition. (optional)
rect_y = 56 # int | Set Y for area for recognition. (optional)
rect_width = 56 # int | Set Width of area for recognition. (optional)
rect_height = 56 # int | Set Height of area for recognition. (optional)
strip_fnc = True # bool | Value indicating whether FNC symbol strip must be done. (optional)
timeout = 56 # int | Timeout of recognition process. (optional)
median_smoothing_window_size = 56 # int | Window size for median smoothing. Typical values are 3 or 4. Default value is 3. AllowMedianSmoothing must be set. (optional)
allow_median_smoothing = True # bool | Allows engine to enable median smoothing as additional scan. Mode helps to recognize noised barcodes. (optional)
allow_complex_background = True # bool | Allows engine to recognize color barcodes on color background as additional scan. Extremely slow mode. (optional)
allow_datamatrix_industrial_barcodes = True # bool | Allows engine for Datamatrix to recognize dashed industrial Datamatrix barcodes. Slow mode which helps only for dashed barcodes which consist from spots. (optional)
allow_decreased_image = True # bool | Allows engine to recognize decreased image as additional scan. Size for decreasing is selected by internal engine algorithms. Mode helps to recognize barcodes which are noised and blurred but captured with high resolution. (optional)
allow_detect_scan_gap = True # bool | Allows engine to use gap between scans to increase recognition speed. Mode can make recognition problems with low height barcodes. (optional)
allow_incorrect_barcodes = True # bool | Allows engine to recognize barcodes which has incorrect checksum or incorrect values. Mode can be used to recognize damaged barcodes with incorrect text. (optional)
allow_invert_image = True # bool | Allows engine to recognize inverse color image as additional scan. Mode can be used when barcode is white on black background. (optional)
allow_micro_white_spots_removing = True # bool | Allows engine for Postal barcodes to recognize slightly noised images. Mode helps to recognize slightly damaged Postal barcodes. (optional)
allow_one_d_fast_barcodes_detector = True # bool | Allows engine for 1D barcodes to quickly recognize high quality barcodes which fill almost whole image. Mode helps to quickly recognize generated barcodes from Internet. (optional)
allow_one_d_wiped_bars_restoration = True # bool | Allows engine for 1D barcodes to recognize barcodes with single wiped/glued bars in pattern. (optional)
allow_qr_micro_qr_restoration = True # bool | Allows engine for QR/MicroQR to recognize damaged MicroQR barcodes. (optional)
allow_regular_image = True # bool | Allows engine to recognize regular image without any restorations as main scan. Mode to recognize image as is. (optional)
allow_salt_and_pepper_filtering = True # bool | Allows engine to recognize barcodes with salt and pepper noise type. Mode can remove small noise with white and black dots. (optional)
allow_white_spots_removing = True # bool | Allows engine to recognize image without small white spots as additional scan. Mode helps to recognize noised image as well as median smoothing filtering. (optional)
check_more1_d_variants = True # bool | Allows engine to recognize 1D barcodes with checksum by checking more recognition variants. Default value: False. (optional)
fast_scan_only = True # bool | Allows engine for 1D barcodes to quickly recognize middle slice of an image and return result without using any time-consuming algorithms. Default value: False. (optional)
region_likelihood_threshold_percent = 1.2 # float | Sets threshold for detected regions that may contain barcodes. Value 0.7 means that bottom 70% of possible regions are filtered out and not processed further. Region likelihood threshold must be between [0.05, 0.9] Use high values for clear images with few barcodes. Use low values for images with many barcodes or for noisy images. Low value may lead to a bigger recognition time. (optional)
scan_window_sizes = [56] # list[int] | Scan window sizes in pixels. Allowed sizes are 10, 15, 20, 25, 30. Scanning with small window size takes more time and provides more accuracy but may fail in detecting very big barcodes. Combining of several window sizes can improve detection quality. (optional)
similarity = 1.2 # float | Similarity coefficient depends on how homogeneous barcodes are. Use high value for for clear barcodes. Use low values to detect barcodes that ara partly damaged or not lighten evenly. Similarity coefficient must be between [0.5, 0.9] (optional)
skip_diagonal_search = True # bool | Allows detector to skip search for diagonal barcodes. Setting it to False will increase detection time but allow to find diagonal barcodes that can be missed otherwise. Enabling of diagonal search leads to a bigger detection time. (optional)
read_tiny_barcodes = True # bool | Allows engine to recognize tiny barcodes on large images. Ignored if AllowIncorrectBarcodes is set to True. Default value: False. (optional)
australian_post_encoding_table = 'australian_post_encoding_table_example' # str | Interpreting Type for the Customer Information of AustralianPost BarCode.Default is CustomerInformationInterpretingType.Other. (optional)
ignore_ending_filling_patterns_for_c_table = True # bool | The flag which force AustraliaPost decoder to ignore last filling patterns in Customer Information Field during decoding as CTable method. CTable encoding method does not have any gaps in encoding table and sequnce \"333\" of filling paterns is decoded as letter \"z\". (optional)
rectangle_region = 'rectangle_region_example' # str |  (optional)
storage = 'storage_example' # str | The image storage. (optional)
folder = 'folder_example' # str | The image folder. (optional)

try:
    # Recognize barcode from a file on server.
    api_response = api_instance.get_barcode_recognize(name, type=type, checksum_validation=checksum_validation, detect_encoding=detect_encoding, preset=preset, rect_x=rect_x, rect_y=rect_y, rect_width=rect_width, rect_height=rect_height, strip_fnc=strip_fnc, timeout=timeout, median_smoothing_window_size=median_smoothing_window_size, allow_median_smoothing=allow_median_smoothing, allow_complex_background=allow_complex_background, allow_datamatrix_industrial_barcodes=allow_datamatrix_industrial_barcodes, allow_decreased_image=allow_decreased_image, allow_detect_scan_gap=allow_detect_scan_gap, allow_incorrect_barcodes=allow_incorrect_barcodes, allow_invert_image=allow_invert_image, allow_micro_white_spots_removing=allow_micro_white_spots_removing, allow_one_d_fast_barcodes_detector=allow_one_d_fast_barcodes_detector, allow_one_d_wiped_bars_restoration=allow_one_d_wiped_bars_restoration, allow_qr_micro_qr_restoration=allow_qr_micro_qr_restoration, allow_regular_image=allow_regular_image, allow_salt_and_pepper_filtering=allow_salt_and_pepper_filtering, allow_white_spots_removing=allow_white_spots_removing, check_more1_d_variants=check_more1_d_variants, fast_scan_only=fast_scan_only, region_likelihood_threshold_percent=region_likelihood_threshold_percent, scan_window_sizes=scan_window_sizes, similarity=similarity, skip_diagonal_search=skip_diagonal_search, read_tiny_barcodes=read_tiny_barcodes, australian_post_encoding_table=australian_post_encoding_table, ignore_ending_filling_patterns_for_c_table=ignore_ending_filling_patterns_for_c_table, rectangle_region=rectangle_region, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BarcodeApi->get_barcode_recognize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
---- | ---- | ------------ | -----
 **name** | **str**| The image file name. | 
 **type** | **str**| The type of barcode to read. | [optional] 
 **checksum_validation** | **str**| Enable checksum validation during recognition for 1D barcodes. Default is treated as Yes for symbologies which must contain checksum, as No where checksum only possible. Checksum never used: Codabar Checksum is possible: Code39 Standard/Extended, Standard2of5, Interleaved2of5, Matrix2of5, ItalianPost25, DeutschePostIdentcode, DeutschePostLeitcode, VIN Checksum always used: Rest symbologies | [optional] 
 **detect_encoding** | **bool**| A flag which force engine to detect codetext encoding for Unicode. | [optional] 
 **preset** | **str**| Preset allows to configure recognition quality and speed manually. You can quickly set up Preset by embedded presets: HighPerformance, NormalQuality, HighQuality, MaxBarCodes or you can manually configure separate options. Default value of Preset is NormalQuality. | [optional] 
 **rect_x** | **int**| Set X for area for recognition. | [optional] 
 **rect_y** | **int**| Set Y for area for recognition. | [optional] 
 **rect_width** | **int**| Set Width of area for recognition. | [optional] 
 **rect_height** | **int**| Set Height of area for recognition. | [optional] 
 **strip_fnc** | **bool**| Value indicating whether FNC symbol strip must be done. | [optional] 
 **timeout** | **int**| Timeout of recognition process. | [optional] 
 **median_smoothing_window_size** | **int**| Window size for median smoothing. Typical values are 3 or 4. Default value is 3. AllowMedianSmoothing must be set. | [optional] 
 **allow_median_smoothing** | **bool**| Allows engine to enable median smoothing as additional scan. Mode helps to recognize noised barcodes. | [optional] 
 **allow_complex_background** | **bool**| Allows engine to recognize color barcodes on color background as additional scan. Extremely slow mode. | [optional] 
 **allow_datamatrix_industrial_barcodes** | **bool**| Allows engine for Datamatrix to recognize dashed industrial Datamatrix barcodes. Slow mode which helps only for dashed barcodes which consist from spots. | [optional] 
 **allow_decreased_image** | **bool**| Allows engine to recognize decreased image as additional scan. Size for decreasing is selected by internal engine algorithms. Mode helps to recognize barcodes which are noised and blurred but captured with high resolution. | [optional] 
 **allow_detect_scan_gap** | **bool**| Allows engine to use gap between scans to increase recognition speed. Mode can make recognition problems with low height barcodes. | [optional] 
 **allow_incorrect_barcodes** | **bool**| Allows engine to recognize barcodes which has incorrect checksum or incorrect values. Mode can be used to recognize damaged barcodes with incorrect text. | [optional] 
 **allow_invert_image** | **bool**| Allows engine to recognize inverse color image as additional scan. Mode can be used when barcode is white on black background. | [optional] 
 **allow_micro_white_spots_removing** | **bool**| Allows engine for Postal barcodes to recognize slightly noised images. Mode helps to recognize slightly damaged Postal barcodes. | [optional] 
 **allow_one_d_fast_barcodes_detector** | **bool**| Allows engine for 1D barcodes to quickly recognize high quality barcodes which fill almost whole image. Mode helps to quickly recognize generated barcodes from Internet. | [optional] 
 **allow_one_d_wiped_bars_restoration** | **bool**| Allows engine for 1D barcodes to recognize barcodes with single wiped/glued bars in pattern. | [optional] 
 **allow_qr_micro_qr_restoration** | **bool**| Allows engine for QR/MicroQR to recognize damaged MicroQR barcodes. | [optional] 
 **allow_regular_image** | **bool**| Allows engine to recognize regular image without any restorations as main scan. Mode to recognize image as is. | [optional] 
 **allow_salt_and_pepper_filtering** | **bool**| Allows engine to recognize barcodes with salt and pepper noise type. Mode can remove small noise with white and black dots. | [optional] 
 **allow_white_spots_removing** | **bool**| Allows engine to recognize image without small white spots as additional scan. Mode helps to recognize noised image as well as median smoothing filtering. | [optional] 
 **check_more1_d_variants** | **bool**| Allows engine to recognize 1D barcodes with checksum by checking more recognition variants. Default value: False. | [optional] 
 **fast_scan_only** | **bool**| Allows engine for 1D barcodes to quickly recognize middle slice of an image and return result without using any time-consuming algorithms. Default value: False. | [optional] 
 **region_likelihood_threshold_percent** | **float**| Sets threshold for detected regions that may contain barcodes. Value 0.7 means that bottom 70% of possible regions are filtered out and not processed further. Region likelihood threshold must be between [0.05, 0.9] Use high values for clear images with few barcodes. Use low values for images with many barcodes or for noisy images. Low value may lead to a bigger recognition time. | [optional] 
 **scan_window_sizes** | [**list[int]**](int.md)| Scan window sizes in pixels. Allowed sizes are 10, 15, 20, 25, 30. Scanning with small window size takes more time and provides more accuracy but may fail in detecting very big barcodes. Combining of several window sizes can improve detection quality. | [optional] 
 **similarity** | **float**| Similarity coefficient depends on how homogeneous barcodes are. Use high value for for clear barcodes. Use low values to detect barcodes that ara partly damaged or not lighten evenly. Similarity coefficient must be between [0.5, 0.9] | [optional] 
 **skip_diagonal_search** | **bool**| Allows detector to skip search for diagonal barcodes. Setting it to False will increase detection time but allow to find diagonal barcodes that can be missed otherwise. Enabling of diagonal search leads to a bigger detection time. | [optional] 
 **read_tiny_barcodes** | **bool**| Allows engine to recognize tiny barcodes on large images. Ignored if AllowIncorrectBarcodes is set to True. Default value: False. | [optional] 
 **australian_post_encoding_table** | **str**| Interpreting Type for the Customer Information of AustralianPost BarCode.Default is CustomerInformationInterpretingType.Other. | [optional] 
 **ignore_ending_filling_patterns_for_c_table** | **bool**| The flag which force AustraliaPost decoder to ignore last filling patterns in Customer Information Field during decoding as CTable method. CTable encoding method does not have any gaps in encoding table and sequnce \&quot;333\&quot; of filling paterns is decoded as letter \&quot;z\&quot;. | [optional] 
 **rectangle_region** | **str**|  | [optional] 
 **storage** | **str**| The image storage. | [optional] 
 **folder** | **str**| The image folder. | [optional] 

### Return type

[**BarcodeResponseList**](BarcodeResponseList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_barcode_recognize_from_url_or_content**
> BarcodeResponseList post_barcode_recognize_from_url_or_content(type=type, checksum_validation=checksum_validation, detect_encoding=detect_encoding, preset=preset, rect_x=rect_x, rect_y=rect_y, rect_width=rect_width, rect_height=rect_height, strip_fnc=strip_fnc, timeout=timeout, median_smoothing_window_size=median_smoothing_window_size, allow_median_smoothing=allow_median_smoothing, allow_complex_background=allow_complex_background, allow_datamatrix_industrial_barcodes=allow_datamatrix_industrial_barcodes, allow_decreased_image=allow_decreased_image, allow_detect_scan_gap=allow_detect_scan_gap, allow_incorrect_barcodes=allow_incorrect_barcodes, allow_invert_image=allow_invert_image, allow_micro_white_spots_removing=allow_micro_white_spots_removing, allow_one_d_fast_barcodes_detector=allow_one_d_fast_barcodes_detector, allow_one_d_wiped_bars_restoration=allow_one_d_wiped_bars_restoration, allow_qr_micro_qr_restoration=allow_qr_micro_qr_restoration, allow_regular_image=allow_regular_image, allow_salt_and_pepper_filtering=allow_salt_and_pepper_filtering, allow_white_spots_removing=allow_white_spots_removing, check_more1_d_variants=check_more1_d_variants, fast_scan_only=fast_scan_only, region_likelihood_threshold_percent=region_likelihood_threshold_percent, scan_window_sizes=scan_window_sizes, similarity=similarity, skip_diagonal_search=skip_diagonal_search, read_tiny_barcodes=read_tiny_barcodes, australian_post_encoding_table=australian_post_encoding_table, ignore_ending_filling_patterns_for_c_table=ignore_ending_filling_patterns_for_c_table, rectangle_region=rectangle_region, url=url, image=image)

Recognize barcode from an url or from request body. Request body can contain raw data bytes of the image or encoded with base64.

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
api_instance = aspose_barcode_cloud.BarcodeApi(aspose_barcode_cloud.ApiClient(configuration))
type = 'type_example' # str | The type of barcode to read. (optional)
checksum_validation = 'checksum_validation_example' # str | Enable checksum validation during recognition for 1D barcodes. Default is treated as Yes for symbologies which must contain checksum, as No where checksum only possible. Checksum never used: Codabar Checksum is possible: Code39 Standard/Extended, Standard2of5, Interleaved2of5, Matrix2of5, ItalianPost25, DeutschePostIdentcode, DeutschePostLeitcode, VIN Checksum always used: Rest symbologies (optional)
detect_encoding = True # bool | A flag which force engine to detect codetext encoding for Unicode. (optional)
preset = 'preset_example' # str | Preset allows to configure recognition quality and speed manually. You can quickly set up Preset by embedded presets: HighPerformance, NormalQuality, HighQuality, MaxBarCodes or you can manually configure separate options. Default value of Preset is NormalQuality. (optional)
rect_x = 56 # int | Set X for area for recognition. (optional)
rect_y = 56 # int | Set Y for area for recognition. (optional)
rect_width = 56 # int | Set Width of area for recognition. (optional)
rect_height = 56 # int | Set Height of area for recognition. (optional)
strip_fnc = True # bool | Value indicating whether FNC symbol strip must be done. (optional)
timeout = 56 # int | Timeout of recognition process. (optional)
median_smoothing_window_size = 56 # int | Window size for median smoothing. Typical values are 3 or 4. Default value is 3. AllowMedianSmoothing must be set. (optional)
allow_median_smoothing = True # bool | Allows engine to enable median smoothing as additional scan. Mode helps to recognize noised barcodes. (optional)
allow_complex_background = True # bool | Allows engine to recognize color barcodes on color background as additional scan. Extremely slow mode. (optional)
allow_datamatrix_industrial_barcodes = True # bool | Allows engine for Datamatrix to recognize dashed industrial Datamatrix barcodes. Slow mode which helps only for dashed barcodes which consist from spots. (optional)
allow_decreased_image = True # bool | Allows engine to recognize decreased image as additional scan. Size for decreasing is selected by internal engine algorithms. Mode helps to recognize barcodes which are noised and blurred but captured with high resolution. (optional)
allow_detect_scan_gap = True # bool | Allows engine to use gap between scans to increase recognition speed. Mode can make recognition problems with low height barcodes. (optional)
allow_incorrect_barcodes = True # bool | Allows engine to recognize barcodes which has incorrect checksum or incorrect values. Mode can be used to recognize damaged barcodes with incorrect text. (optional)
allow_invert_image = True # bool | Allows engine to recognize inverse color image as additional scan. Mode can be used when barcode is white on black background. (optional)
allow_micro_white_spots_removing = True # bool | Allows engine for Postal barcodes to recognize slightly noised images. Mode helps to recognize slightly damaged Postal barcodes. (optional)
allow_one_d_fast_barcodes_detector = True # bool | Allows engine for 1D barcodes to quickly recognize high quality barcodes which fill almost whole image. Mode helps to quickly recognize generated barcodes from Internet. (optional)
allow_one_d_wiped_bars_restoration = True # bool | Allows engine for 1D barcodes to recognize barcodes with single wiped/glued bars in pattern. (optional)
allow_qr_micro_qr_restoration = True # bool | Allows engine for QR/MicroQR to recognize damaged MicroQR barcodes. (optional)
allow_regular_image = True # bool | Allows engine to recognize regular image without any restorations as main scan. Mode to recognize image as is. (optional)
allow_salt_and_pepper_filtering = True # bool | Allows engine to recognize barcodes with salt and pepper noise type. Mode can remove small noise with white and black dots. (optional)
allow_white_spots_removing = True # bool | Allows engine to recognize image without small white spots as additional scan. Mode helps to recognize noised image as well as median smoothing filtering. (optional)
check_more1_d_variants = True # bool | Allows engine to recognize 1D barcodes with checksum by checking more recognition variants. Default value: False. (optional)
fast_scan_only = True # bool | Allows engine for 1D barcodes to quickly recognize middle slice of an image and return result without using any time-consuming algorithms. Default value: False. (optional)
region_likelihood_threshold_percent = 1.2 # float | Sets threshold for detected regions that may contain barcodes. Value 0.7 means that bottom 70% of possible regions are filtered out and not processed further. Region likelihood threshold must be between [0.05, 0.9] Use high values for clear images with few barcodes. Use low values for images with many barcodes or for noisy images. Low value may lead to a bigger recognition time. (optional)
scan_window_sizes = [56] # list[int] | Scan window sizes in pixels. Allowed sizes are 10, 15, 20, 25, 30. Scanning with small window size takes more time and provides more accuracy but may fail in detecting very big barcodes. Combining of several window sizes can improve detection quality. (optional)
similarity = 1.2 # float | Similarity coefficient depends on how homogeneous barcodes are. Use high value for for clear barcodes. Use low values to detect barcodes that ara partly damaged or not lighten evenly. Similarity coefficient must be between [0.5, 0.9] (optional)
skip_diagonal_search = True # bool | Allows detector to skip search for diagonal barcodes. Setting it to False will increase detection time but allow to find diagonal barcodes that can be missed otherwise. Enabling of diagonal search leads to a bigger detection time. (optional)
read_tiny_barcodes = True # bool | Allows engine to recognize tiny barcodes on large images. Ignored if AllowIncorrectBarcodes is set to True. Default value: False. (optional)
australian_post_encoding_table = 'australian_post_encoding_table_example' # str | Interpreting Type for the Customer Information of AustralianPost BarCode.Default is CustomerInformationInterpretingType.Other. (optional)
ignore_ending_filling_patterns_for_c_table = True # bool | The flag which force AustraliaPost decoder to ignore last filling patterns in Customer Information Field during decoding as CTable method. CTable encoding method does not have any gaps in encoding table and sequnce \"333\" of filling paterns is decoded as letter \"z\". (optional)
rectangle_region = 'rectangle_region_example' # str |  (optional)
url = 'url_example' # str | The image file url. (optional)
image = '/path/to/file.txt' # file | Image data (optional)

try:
    # Recognize barcode from an url or from request body. Request body can contain raw data bytes of the image or encoded with base64.
    api_response = api_instance.post_barcode_recognize_from_url_or_content(type=type, checksum_validation=checksum_validation, detect_encoding=detect_encoding, preset=preset, rect_x=rect_x, rect_y=rect_y, rect_width=rect_width, rect_height=rect_height, strip_fnc=strip_fnc, timeout=timeout, median_smoothing_window_size=median_smoothing_window_size, allow_median_smoothing=allow_median_smoothing, allow_complex_background=allow_complex_background, allow_datamatrix_industrial_barcodes=allow_datamatrix_industrial_barcodes, allow_decreased_image=allow_decreased_image, allow_detect_scan_gap=allow_detect_scan_gap, allow_incorrect_barcodes=allow_incorrect_barcodes, allow_invert_image=allow_invert_image, allow_micro_white_spots_removing=allow_micro_white_spots_removing, allow_one_d_fast_barcodes_detector=allow_one_d_fast_barcodes_detector, allow_one_d_wiped_bars_restoration=allow_one_d_wiped_bars_restoration, allow_qr_micro_qr_restoration=allow_qr_micro_qr_restoration, allow_regular_image=allow_regular_image, allow_salt_and_pepper_filtering=allow_salt_and_pepper_filtering, allow_white_spots_removing=allow_white_spots_removing, check_more1_d_variants=check_more1_d_variants, fast_scan_only=fast_scan_only, region_likelihood_threshold_percent=region_likelihood_threshold_percent, scan_window_sizes=scan_window_sizes, similarity=similarity, skip_diagonal_search=skip_diagonal_search, read_tiny_barcodes=read_tiny_barcodes, australian_post_encoding_table=australian_post_encoding_table, ignore_ending_filling_patterns_for_c_table=ignore_ending_filling_patterns_for_c_table, rectangle_region=rectangle_region, url=url, image=image)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BarcodeApi->post_barcode_recognize_from_url_or_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
---- | ---- | ------------ | -----
 **type** | **str**| The type of barcode to read. | [optional] 
 **checksum_validation** | **str**| Enable checksum validation during recognition for 1D barcodes. Default is treated as Yes for symbologies which must contain checksum, as No where checksum only possible. Checksum never used: Codabar Checksum is possible: Code39 Standard/Extended, Standard2of5, Interleaved2of5, Matrix2of5, ItalianPost25, DeutschePostIdentcode, DeutschePostLeitcode, VIN Checksum always used: Rest symbologies | [optional] 
 **detect_encoding** | **bool**| A flag which force engine to detect codetext encoding for Unicode. | [optional] 
 **preset** | **str**| Preset allows to configure recognition quality and speed manually. You can quickly set up Preset by embedded presets: HighPerformance, NormalQuality, HighQuality, MaxBarCodes or you can manually configure separate options. Default value of Preset is NormalQuality. | [optional] 
 **rect_x** | **int**| Set X for area for recognition. | [optional] 
 **rect_y** | **int**| Set Y for area for recognition. | [optional] 
 **rect_width** | **int**| Set Width of area for recognition. | [optional] 
 **rect_height** | **int**| Set Height of area for recognition. | [optional] 
 **strip_fnc** | **bool**| Value indicating whether FNC symbol strip must be done. | [optional] 
 **timeout** | **int**| Timeout of recognition process. | [optional] 
 **median_smoothing_window_size** | **int**| Window size for median smoothing. Typical values are 3 or 4. Default value is 3. AllowMedianSmoothing must be set. | [optional] 
 **allow_median_smoothing** | **bool**| Allows engine to enable median smoothing as additional scan. Mode helps to recognize noised barcodes. | [optional] 
 **allow_complex_background** | **bool**| Allows engine to recognize color barcodes on color background as additional scan. Extremely slow mode. | [optional] 
 **allow_datamatrix_industrial_barcodes** | **bool**| Allows engine for Datamatrix to recognize dashed industrial Datamatrix barcodes. Slow mode which helps only for dashed barcodes which consist from spots. | [optional] 
 **allow_decreased_image** | **bool**| Allows engine to recognize decreased image as additional scan. Size for decreasing is selected by internal engine algorithms. Mode helps to recognize barcodes which are noised and blurred but captured with high resolution. | [optional] 
 **allow_detect_scan_gap** | **bool**| Allows engine to use gap between scans to increase recognition speed. Mode can make recognition problems with low height barcodes. | [optional] 
 **allow_incorrect_barcodes** | **bool**| Allows engine to recognize barcodes which has incorrect checksum or incorrect values. Mode can be used to recognize damaged barcodes with incorrect text. | [optional] 
 **allow_invert_image** | **bool**| Allows engine to recognize inverse color image as additional scan. Mode can be used when barcode is white on black background. | [optional] 
 **allow_micro_white_spots_removing** | **bool**| Allows engine for Postal barcodes to recognize slightly noised images. Mode helps to recognize slightly damaged Postal barcodes. | [optional] 
 **allow_one_d_fast_barcodes_detector** | **bool**| Allows engine for 1D barcodes to quickly recognize high quality barcodes which fill almost whole image. Mode helps to quickly recognize generated barcodes from Internet. | [optional] 
 **allow_one_d_wiped_bars_restoration** | **bool**| Allows engine for 1D barcodes to recognize barcodes with single wiped/glued bars in pattern. | [optional] 
 **allow_qr_micro_qr_restoration** | **bool**| Allows engine for QR/MicroQR to recognize damaged MicroQR barcodes. | [optional] 
 **allow_regular_image** | **bool**| Allows engine to recognize regular image without any restorations as main scan. Mode to recognize image as is. | [optional] 
 **allow_salt_and_pepper_filtering** | **bool**| Allows engine to recognize barcodes with salt and pepper noise type. Mode can remove small noise with white and black dots. | [optional] 
 **allow_white_spots_removing** | **bool**| Allows engine to recognize image without small white spots as additional scan. Mode helps to recognize noised image as well as median smoothing filtering. | [optional] 
 **check_more1_d_variants** | **bool**| Allows engine to recognize 1D barcodes with checksum by checking more recognition variants. Default value: False. | [optional] 
 **fast_scan_only** | **bool**| Allows engine for 1D barcodes to quickly recognize middle slice of an image and return result without using any time-consuming algorithms. Default value: False. | [optional] 
 **region_likelihood_threshold_percent** | **float**| Sets threshold for detected regions that may contain barcodes. Value 0.7 means that bottom 70% of possible regions are filtered out and not processed further. Region likelihood threshold must be between [0.05, 0.9] Use high values for clear images with few barcodes. Use low values for images with many barcodes or for noisy images. Low value may lead to a bigger recognition time. | [optional] 
 **scan_window_sizes** | [**list[int]**](int.md)| Scan window sizes in pixels. Allowed sizes are 10, 15, 20, 25, 30. Scanning with small window size takes more time and provides more accuracy but may fail in detecting very big barcodes. Combining of several window sizes can improve detection quality. | [optional] 
 **similarity** | **float**| Similarity coefficient depends on how homogeneous barcodes are. Use high value for for clear barcodes. Use low values to detect barcodes that ara partly damaged or not lighten evenly. Similarity coefficient must be between [0.5, 0.9] | [optional] 
 **skip_diagonal_search** | **bool**| Allows detector to skip search for diagonal barcodes. Setting it to False will increase detection time but allow to find diagonal barcodes that can be missed otherwise. Enabling of diagonal search leads to a bigger detection time. | [optional] 
 **read_tiny_barcodes** | **bool**| Allows engine to recognize tiny barcodes on large images. Ignored if AllowIncorrectBarcodes is set to True. Default value: False. | [optional] 
 **australian_post_encoding_table** | **str**| Interpreting Type for the Customer Information of AustralianPost BarCode.Default is CustomerInformationInterpretingType.Other. | [optional] 
 **ignore_ending_filling_patterns_for_c_table** | **bool**| The flag which force AustraliaPost decoder to ignore last filling patterns in Customer Information Field during decoding as CTable method. CTable encoding method does not have any gaps in encoding table and sequnce \&quot;333\&quot; of filling paterns is decoded as letter \&quot;z\&quot;. | [optional] 
 **rectangle_region** | **str**|  | [optional] 
 **url** | **str**| The image file url. | [optional] 
 **image** | **file**| Image data | [optional] 

### Return type

[**BarcodeResponseList**](BarcodeResponseList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded, application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_generate_multiple**
> file post_generate_multiple(generator_params_list, format=format)

Generate multiple barcodes and return in response stream

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
api_instance = aspose_barcode_cloud.BarcodeApi(aspose_barcode_cloud.ApiClient(configuration))
generator_params_list = aspose_barcode_cloud.GeneratorParamsList() # GeneratorParamsList | List of barcodes
format = 'png' # str | Format to return stream in (optional) (default to png)

try:
    # Generate multiple barcodes and return in response stream
    api_response = api_instance.post_generate_multiple(generator_params_list, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BarcodeApi->post_generate_multiple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
---- | ---- | ------------ | -----
 **generator_params_list** | [**GeneratorParamsList**](GeneratorParamsList.md)| List of barcodes | 
 **format** | **str**| Format to return stream in | [optional] [default to png]

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: image/png, image/bmp, image/gif, image/jpeg, image/svg+xml, image/tiff

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_barcode_generate_file**
> ResultImageInfo put_barcode_generate_file(name, type, text, two_d_display_text=two_d_display_text, text_location=text_location, text_alignment=text_alignment, text_color=text_color, font_size_mode=font_size_mode, no_wrap=no_wrap, resolution=resolution, resolution_x=resolution_x, resolution_y=resolution_y, dimension_x=dimension_x, text_space=text_space, units=units, size_mode=size_mode, bar_height=bar_height, image_height=image_height, image_width=image_width, rotation_angle=rotation_angle, back_color=back_color, bar_color=bar_color, border_color=border_color, border_width=border_width, border_dash_style=border_dash_style, border_visible=border_visible, enable_checksum=enable_checksum, enable_escape=enable_escape, filled_bars=filled_bars, always_show_checksum=always_show_checksum, wide_narrow_ratio=wide_narrow_ratio, validate_text=validate_text, supplement_data=supplement_data, supplement_space=supplement_space, bar_width_reduction=bar_width_reduction, storage=storage, folder=folder, format=format)

Generate barcode and save on server (from query params or from file with json or xml content)

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
api_instance = aspose_barcode_cloud.BarcodeApi(aspose_barcode_cloud.ApiClient(configuration))
name = 'name_example' # str | The image file name.
type = 'type_example' # str | Type of barcode to generate.
text = 'text_example' # str | Text to encode.
two_d_display_text = 'two_d_display_text_example' # str | Text that will be displayed instead of codetext in 2D barcodes. Used for: Aztec, Pdf417, DataMatrix, QR, MaxiCode, DotCode (optional)
text_location = 'text_location_example' # str | Specify the displaying Text Location, set to CodeLocation.None to hide CodeText. Default value: CodeLocation.Below. (optional)
text_alignment = 'text_alignment_example' # str | Text alignment. (optional)
text_color = 'text_color_example' # str | Specify the displaying CodeText's Color. Default value: Color.Black. (optional)
font_size_mode = 'font_size_mode_example' # str | Specify FontSizeMode. If FontSizeMode is set to Auto, font size will be calculated automatically based on xDimension value. It is recommended to use FontSizeMode.Auto especially in AutoSizeMode.Nearest or AutoSizeMode.Interpolation. Default value: FontSizeMode.Auto. (optional)
no_wrap = True # bool | Specify word wraps (line breaks) within text. Default value: False. (optional)
resolution = 1.2 # float | Resolution of the BarCode image. One value for both dimensions. Default value: 96 dpi. (optional)
resolution_x = 1.2 # float | DEPRECATED: Use 'Resolution' instead. (optional)
resolution_y = 1.2 # float | DEPRECATED: Use 'Resolution' instead. (optional)
dimension_x = 1.2 # float | The smallest width of the unit of BarCode bars or spaces. Increase this will increase the whole barcode image width. Ignored if AutoSizeMode property is set to AutoSizeMode.Nearest or AutoSizeMode.Interpolation. (optional)
text_space = 1.2 # float | Space between the CodeText and the BarCode in Unit value. Default value: 2pt. Ignored for EAN8, EAN13, UPCE, UPCA, ISBN, ISMN, ISSN, UpcaGs1DatabarCoupon. (optional)
units = 'units_example' # str | Common Units for all measuring in query. Default units: pixel. (optional)
size_mode = 'size_mode_example' # str | Specifies the different types of automatic sizing modes. Default value: AutoSizeMode.None. (optional)
bar_height = 1.2 # float | Height of the barcode in given units. Default units: pixel. (optional)
image_height = 1.2 # float | Height of the barcode image in given units. Default units: pixel. (optional)
image_width = 1.2 # float | Width of the barcode image in given units. Default units: pixel. (optional)
rotation_angle = 1.2 # float | BarCode image rotation angle, measured in degree, e.g. RotationAngle = 0 or RotationAngle = 360 means no rotation. If RotationAngle NOT equal to 90, 180, 270 or 0, it may increase the difficulty for the scanner to read the image. Default value: 0. (optional)
back_color = 'back_color_example' # str | Background color of the barcode image. Default value: Color.White. (optional)
bar_color = 'bar_color_example' # str | Bars color. Default value: Color.Black. (optional)
border_color = 'border_color_example' # str | Border color. Default value: Color.Black. (optional)
border_width = 1.2 # float | Border width. Default value: 0. Ignored if Visible is set to False. (optional)
border_dash_style = 'border_dash_style_example' # str | Border dash style. Default value: BorderDashStyle.Solid. (optional)
border_visible = True # bool | Border visibility. If False than parameter Width is always ignored (0). Default value: False. (optional)
enable_checksum = 'enable_checksum_example' # str | Enable checksum during generation 1D barcodes. Default is treated as Yes for symbology which must contain checksum, as No where checksum only possible. Checksum is possible: Code39 Standard/Extended, Standard2of5, Interleaved2of5, Matrix2of5, ItalianPost25, DeutschePostIdentcode, DeutschePostLeitcode, VIN, Codabar Checksum always used: Rest symbology (optional)
enable_escape = True # bool | Indicates whether explains the character \"\\\" as an escape character in CodeText property. Used for Pdf417, DataMatrix, Code128 only If the EnableEscape is True, \"\\\" will be explained as a special escape character. Otherwise, \"\\\" acts as normal characters. Aspose.BarCode supports input decimal ascii code and mnemonic for ASCII control-code characters. For example, \\013 and \\\\CR stands for CR. (optional)
filled_bars = True # bool | Value indicating whether bars are filled. Only for 1D barcodes. Default value: True. (optional)
always_show_checksum = True # bool | Always display checksum digit in the human readable text for Code128 and GS1Code128 barcodes. (optional)
wide_narrow_ratio = 1.2 # float | Wide bars to Narrow bars ratio. Default value: 3, that is, wide bars are 3 times as wide as narrow bars. Used for ITF, PZN, PharmaCode, Standard2of5, Interleaved2of5, Matrix2of5, ItalianPost25, IATA2of5, VIN, DeutschePost, OPC, Code32, DataLogic2of5, PatchCode, Code39Extended, Code39Standard (optional)
validate_text = True # bool | Only for 1D barcodes. If codetext is incorrect and value set to True - exception will be thrown. Otherwise codetext will be corrected to match barcode's specification. Exception always will be thrown for: Databar symbology if codetext is incorrect. Exception always will not be thrown for: AustraliaPost, SingaporePost, Code39Extended, Code93Extended, Code16K, Code128 symbology if codetext is incorrect. (optional)
supplement_data = 'supplement_data_example' # str | Supplement parameters. Used for Interleaved2of5, Standard2of5, EAN13, EAN8, UPCA, UPCE, ISBN, ISSN, ISMN. (optional)
supplement_space = 1.2 # float | Space between main the BarCode and supplement BarCode. (optional)
bar_width_reduction = 1.2 # float | Bars reduction value that is used to compensate ink spread while printing. (optional)
storage = 'storage_example' # str | Image's storage. (optional)
folder = 'folder_example' # str | Image's folder. (optional)
format = 'format_example' # str | The image format. (optional)

try:
    # Generate barcode and save on server (from query params or from file with json or xml content)
    api_response = api_instance.put_barcode_generate_file(name, type, text, two_d_display_text=two_d_display_text, text_location=text_location, text_alignment=text_alignment, text_color=text_color, font_size_mode=font_size_mode, no_wrap=no_wrap, resolution=resolution, resolution_x=resolution_x, resolution_y=resolution_y, dimension_x=dimension_x, text_space=text_space, units=units, size_mode=size_mode, bar_height=bar_height, image_height=image_height, image_width=image_width, rotation_angle=rotation_angle, back_color=back_color, bar_color=bar_color, border_color=border_color, border_width=border_width, border_dash_style=border_dash_style, border_visible=border_visible, enable_checksum=enable_checksum, enable_escape=enable_escape, filled_bars=filled_bars, always_show_checksum=always_show_checksum, wide_narrow_ratio=wide_narrow_ratio, validate_text=validate_text, supplement_data=supplement_data, supplement_space=supplement_space, bar_width_reduction=bar_width_reduction, storage=storage, folder=folder, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BarcodeApi->put_barcode_generate_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
---- | ---- | ------------ | -----
 **name** | **str**| The image file name. | 
 **type** | **str**| Type of barcode to generate. | 
 **text** | **str**| Text to encode. | 
 **two_d_display_text** | **str**| Text that will be displayed instead of codetext in 2D barcodes. Used for: Aztec, Pdf417, DataMatrix, QR, MaxiCode, DotCode | [optional] 
 **text_location** | **str**| Specify the displaying Text Location, set to CodeLocation.None to hide CodeText. Default value: CodeLocation.Below. | [optional] 
 **text_alignment** | **str**| Text alignment. | [optional] 
 **text_color** | **str**| Specify the displaying CodeText&#39;s Color. Default value: Color.Black. | [optional] 
 **font_size_mode** | **str**| Specify FontSizeMode. If FontSizeMode is set to Auto, font size will be calculated automatically based on xDimension value. It is recommended to use FontSizeMode.Auto especially in AutoSizeMode.Nearest or AutoSizeMode.Interpolation. Default value: FontSizeMode.Auto. | [optional] 
 **no_wrap** | **bool**| Specify word wraps (line breaks) within text. Default value: False. | [optional] 
 **resolution** | **float**| Resolution of the BarCode image. One value for both dimensions. Default value: 96 dpi. | [optional] 
 **resolution_x** | **float**| DEPRECATED: Use &#39;Resolution&#39; instead. | [optional] 
 **resolution_y** | **float**| DEPRECATED: Use &#39;Resolution&#39; instead. | [optional] 
 **dimension_x** | **float**| The smallest width of the unit of BarCode bars or spaces. Increase this will increase the whole barcode image width. Ignored if AutoSizeMode property is set to AutoSizeMode.Nearest or AutoSizeMode.Interpolation. | [optional] 
 **text_space** | **float**| Space between the CodeText and the BarCode in Unit value. Default value: 2pt. Ignored for EAN8, EAN13, UPCE, UPCA, ISBN, ISMN, ISSN, UpcaGs1DatabarCoupon. | [optional] 
 **units** | **str**| Common Units for all measuring in query. Default units: pixel. | [optional] 
 **size_mode** | **str**| Specifies the different types of automatic sizing modes. Default value: AutoSizeMode.None. | [optional] 
 **bar_height** | **float**| Height of the barcode in given units. Default units: pixel. | [optional] 
 **image_height** | **float**| Height of the barcode image in given units. Default units: pixel. | [optional] 
 **image_width** | **float**| Width of the barcode image in given units. Default units: pixel. | [optional] 
 **rotation_angle** | **float**| BarCode image rotation angle, measured in degree, e.g. RotationAngle &#x3D; 0 or RotationAngle &#x3D; 360 means no rotation. If RotationAngle NOT equal to 90, 180, 270 or 0, it may increase the difficulty for the scanner to read the image. Default value: 0. | [optional] 
 **back_color** | **str**| Background color of the barcode image. Default value: Color.White. | [optional] 
 **bar_color** | **str**| Bars color. Default value: Color.Black. | [optional] 
 **border_color** | **str**| Border color. Default value: Color.Black. | [optional] 
 **border_width** | **float**| Border width. Default value: 0. Ignored if Visible is set to False. | [optional] 
 **border_dash_style** | **str**| Border dash style. Default value: BorderDashStyle.Solid. | [optional] 
 **border_visible** | **bool**| Border visibility. If False than parameter Width is always ignored (0). Default value: False. | [optional] 
 **enable_checksum** | **str**| Enable checksum during generation 1D barcodes. Default is treated as Yes for symbology which must contain checksum, as No where checksum only possible. Checksum is possible: Code39 Standard/Extended, Standard2of5, Interleaved2of5, Matrix2of5, ItalianPost25, DeutschePostIdentcode, DeutschePostLeitcode, VIN, Codabar Checksum always used: Rest symbology | [optional] 
 **enable_escape** | **bool**| Indicates whether explains the character \&quot;\\\&quot; as an escape character in CodeText property. Used for Pdf417, DataMatrix, Code128 only If the EnableEscape is True, \&quot;\\\&quot; will be explained as a special escape character. Otherwise, \&quot;\\\&quot; acts as normal characters. Aspose.BarCode supports input decimal ascii code and mnemonic for ASCII control-code characters. For example, \\013 and \\\\CR stands for CR. | [optional] 
 **filled_bars** | **bool**| Value indicating whether bars are filled. Only for 1D barcodes. Default value: True. | [optional] 
 **always_show_checksum** | **bool**| Always display checksum digit in the human readable text for Code128 and GS1Code128 barcodes. | [optional] 
 **wide_narrow_ratio** | **float**| Wide bars to Narrow bars ratio. Default value: 3, that is, wide bars are 3 times as wide as narrow bars. Used for ITF, PZN, PharmaCode, Standard2of5, Interleaved2of5, Matrix2of5, ItalianPost25, IATA2of5, VIN, DeutschePost, OPC, Code32, DataLogic2of5, PatchCode, Code39Extended, Code39Standard | [optional] 
 **validate_text** | **bool**| Only for 1D barcodes. If codetext is incorrect and value set to True - exception will be thrown. Otherwise codetext will be corrected to match barcode&#39;s specification. Exception always will be thrown for: Databar symbology if codetext is incorrect. Exception always will not be thrown for: AustraliaPost, SingaporePost, Code39Extended, Code93Extended, Code16K, Code128 symbology if codetext is incorrect. | [optional] 
 **supplement_data** | **str**| Supplement parameters. Used for Interleaved2of5, Standard2of5, EAN13, EAN8, UPCA, UPCE, ISBN, ISSN, ISMN. | [optional] 
 **supplement_space** | **float**| Space between main the BarCode and supplement BarCode. | [optional] 
 **bar_width_reduction** | **float**| Bars reduction value that is used to compensate ink spread while printing. | [optional] 
 **storage** | **str**| Image&#39;s storage. | [optional] 
 **folder** | **str**| Image&#39;s folder. | [optional] 
 **format** | **str**| The image format. | [optional] 

### Return type

[**ResultImageInfo**](ResultImageInfo.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded, application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_barcode_recognize_from_body**
> BarcodeResponseList put_barcode_recognize_from_body(name, reader_params, type=type, storage=storage, folder=folder)

Recognition of a barcode from file on server with parameters in body.

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
api_instance = aspose_barcode_cloud.BarcodeApi(aspose_barcode_cloud.ApiClient(configuration))
name = 'name_example' # str | The image file name.
reader_params = aspose_barcode_cloud.ReaderParams() # ReaderParams | BarcodeReader object with parameters.
type = 'type_example' # str |  (optional)
storage = 'storage_example' # str | The storage name (optional)
folder = 'folder_example' # str | The image folder. (optional)

try:
    # Recognition of a barcode from file on server with parameters in body.
    api_response = api_instance.put_barcode_recognize_from_body(name, reader_params, type=type, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BarcodeApi->put_barcode_recognize_from_body: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
---- | ---- | ------------ | -----
 **name** | **str**| The image file name. | 
 **reader_params** | [**ReaderParams**](ReaderParams.md)| BarcodeReader object with parameters. | 
 **type** | **str**|  | [optional] 
 **storage** | **str**| The storage name | [optional] 
 **folder** | **str**| The image folder. | [optional] 

### Return type

[**BarcodeResponseList**](BarcodeResponseList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_generate_multiple**
> ResultImageInfo put_generate_multiple(name, generator_params_list, format=format, folder=folder, storage=storage)

Generate image with multiple barcodes and put new file on server

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
api_instance = aspose_barcode_cloud.BarcodeApi(aspose_barcode_cloud.ApiClient(configuration))
name = 'name_example' # str | New filename
generator_params_list = aspose_barcode_cloud.GeneratorParamsList() # GeneratorParamsList | List of barcodes
format = 'png' # str | Format of file (optional) (default to png)
folder = 'folder_example' # str | Folder to place file to (optional)
storage = 'storage_example' # str | The storage name (optional)

try:
    # Generate image with multiple barcodes and put new file on server
    api_response = api_instance.put_generate_multiple(name, generator_params_list, format=format, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BarcodeApi->put_generate_multiple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
---- | ---- | ------------ | -----
 **name** | **str**| New filename | 
 **generator_params_list** | [**GeneratorParamsList**](GeneratorParamsList.md)| List of barcodes | 
 **format** | **str**| Format of file | [optional] [default to png]
 **folder** | **str**| Folder to place file to | [optional] 
 **storage** | **str**| The storage name | [optional] 

### Return type

[**ResultImageInfo**](ResultImageInfo.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

