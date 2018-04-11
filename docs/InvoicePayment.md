# InvoicePayment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_invoice_id** | **str** |  | [optional] 
**account_id** | **str** |  | [optional] 
**payment_id** | **str** |  | [optional] 
**payment_number** | **str** |  | [optional] 
**payment_external_key** | **str** |  | [optional] 
**auth_amount** | **float** |  | [optional] 
**captured_amount** | **float** |  | [optional] 
**purchased_amount** | **float** |  | [optional] 
**refunded_amount** | **float** |  | [optional] 
**credited_amount** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 
**payment_method_id** | **str** |  | [optional] 
**transactions** | [**list[PaymentTransaction]**](PaymentTransaction.md) |  | [optional] 
**payment_attempts** | [**list[PaymentAttempt]**](PaymentAttempt.md) |  | [optional] 
**audit_logs** | [**list[AuditLog]**](AuditLog.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


