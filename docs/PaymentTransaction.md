# PaymentTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** |  | [optional] 
**transaction_external_key** | **str** |  | [optional] 
**payment_id** | **str** | Associated payment id, required when notifying state transitions | [optional] 
**payment_external_key** | **str** |  | [optional] 
**transaction_type** | **str** |  | [optional] 
**amount** | **float** | Transaction amount, required except for void operations | [optional] 
**currency** | **str** | Amount currency (account currency unless specified) | [optional] 
**effective_date** | **datetime** |  | [optional] 
**processed_amount** | **float** |  | [optional] 
**processed_currency** | **str** |  | [optional] 
**status** | **str** | Transaction status, required for state change notifications | [optional] 
**gateway_error_code** | **str** |  | [optional] 
**gateway_error_msg** | **str** |  | [optional] 
**first_payment_reference_id** | **str** |  | [optional] 
**second_payment_reference_id** | **str** |  | [optional] 
**properties** | [**list[PluginProperty]**](PluginProperty.md) |  | [optional] 
**audit_logs** | [**list[AuditLog]**](AuditLog.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


