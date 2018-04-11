# Invoice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**credit_adj** | **float** |  | [optional] 
**refund_adj** | **float** |  | [optional] 
**invoice_id** | **str** |  | [optional] 
**invoice_date** | **date** |  | [optional] 
**target_date** | **date** |  | [optional] 
**invoice_number** | **str** |  | [optional] 
**balance** | **float** |  | [optional] 
**account_id** | **str** |  | [optional] 
**bundle_keys** | **str** |  | [optional] 
**credits** | [**list[Credit]**](Credit.md) |  | [optional] 
**items** | [**list[InvoiceItem]**](InvoiceItem.md) |  | [optional] 
**is_parent_invoice** | **bool** |  | [optional] [default to False]
**parent_invoice_id** | **str** |  | [optional] 
**parent_account_id** | **str** |  | [optional] 
**audit_logs** | [**list[AuditLog]**](AuditLog.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


