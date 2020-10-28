# Pdf417Params

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aspect_ratio** | **float** | Height/Width ratio of 2D BarCode module. | [optional] 
**text_encoding** | **str** | Encoding of codetext. | [optional] 
**columns** | **int** | Columns count. | [optional] 
**compaction_mode** | [**Pdf417CompactionMode**](Pdf417CompactionMode.md) | Pdf417 symbology type of BarCode&#39;s compaction mode. Default value: Pdf417CompactionMode.Auto. | [optional] 
**error_level** | [**Pdf417ErrorLevel**](Pdf417ErrorLevel.md) | Pdf417 symbology type of BarCode&#39;s error correction level ranging from level0 to level8, level0 means no error correction info, level8 means best error correction which means a larger picture. | [optional] 
**macro_file_id** | **int** | Macro Pdf417 barcode&#39;s file ID. Used for MacroPdf417. | [optional] 
**macro_segment_id** | **int** | Macro Pdf417 barcode&#39;s segment ID, which starts from 0, to MacroSegmentsCount - 1. | [optional] 
**macro_segments_count** | **int** | Macro Pdf417 barcode segments count. | [optional] 
**rows** | **int** | Rows count. | [optional] 
**truncate** | **bool** | Whether Pdf417 symbology type of BarCode is truncated (to reduce space). | [optional] 
**pdf417_eci_encoding** | [**ECIEncodings**](ECIEncodings.md) | Extended Channel Interpretation Identifiers. It is used to tell the barcode reader details about the used references for encoding the data in the symbol. Current implementation consists all well known charset encodings. | [optional] 
**is_reader_initialization** | **bool** | Used to instruct the reader to interpret the data contained within the symbol as programming for reader initialization | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


