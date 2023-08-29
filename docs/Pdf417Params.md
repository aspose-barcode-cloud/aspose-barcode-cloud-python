# Pdf417Params

PDF417 parameters.

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
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
**macro_time_stamp** | **datetime** | Macro Pdf417 barcode time stamp | [optional] 
**macro_sender** | **str** | Macro Pdf417 barcode sender name | [optional] 
**macro_file_size** | **int** | Macro Pdf417 file size. The file size field contains the size in bytes of the entire source file | [optional] 
**macro_checksum** | **int** | Macro Pdf417 barcode checksum. The checksum field contains the value of the 16-bit (2 bytes) CRC checksum using the CCITT-16 polynomial | [optional] 
**macro_file_name** | **str** | Macro Pdf417 barcode file name | [optional] 
**macro_addressee** | **str** | Macro Pdf417 barcode addressee name | [optional] 
**macro_eci_encoding** | [**ECIEncodings**](ECIEncodings.md) | Extended Channel Interpretation Identifiers. Applies for Macro PDF417 text fields. | [optional] 
**code128_emulation** | [**Code128Emulation**](Code128Emulation.md) | Function codeword for Code 128 emulation. Applied for MicroPDF417 only. Ignored for PDF417 and MacroPDF417 barcodes. | [optional] 
**pdf417_macro_terminator** | [**Pdf417MacroTerminator**](Pdf417MacroTerminator.md) | Used to tell the encoder whether to add Macro PDF417 Terminator (codeword 922) to the segment. Applied only for Macro PDF417. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
