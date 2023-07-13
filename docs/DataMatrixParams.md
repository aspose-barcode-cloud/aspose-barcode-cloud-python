# DataMatrixParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aspect_ratio** | **float** | Height/Width ratio of 2D BarCode module | [optional] 
**text_encoding** | **str** | Encoding of codetext. | [optional] 
**columns** | **int** | DEPRECATED: Will be replaced with &#39;DataMatrix.Version&#39; in the next release  Columns count. | [optional] 
**data_matrix_ecc** | [**DataMatrixEccType**](DataMatrixEccType.md) | Datamatrix ECC type. Default value: DataMatrixEccType.Ecc200. | [optional] 
**data_matrix_encode_mode** | [**DataMatrixEncodeMode**](DataMatrixEncodeMode.md) | Encode mode of Datamatrix barcode. Default value: DataMatrixEncodeMode.Auto. | [optional] 
**rows** | **int** | DEPRECATED: Will be replaced with &#39;DataMatrix.Version&#39; in the next release  Rows count. | [optional] 
**macro_characters** | [**MacroCharacter**](MacroCharacter.md) | Macro Characters 05 and 06 values are used to obtain more compact encoding in special modes. Can be used only with DataMatrixEccType.Ecc200 or DataMatrixEccType.EccAuto. Cannot be used with EncodeTypes.GS1DataMatrix Default value: MacroCharacters.None. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


