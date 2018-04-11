# PaymentAttempt

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**payment_method_id** | **str** |  | [optional] 
**payment_external_key** | **str** |  | [optional] 
**transaction_id** | **str** |  | [optional] 
**transaction_external_key** | **str** |  | [optional] 
**transaction_type** | **str** |  | [optional] 
**effective_date** | **datetime** |  | [optional] 
**state_name** | **str** |  | [optional] 
**amount** | **float** | Transaction amount, required except for void operations | [optional] 
**currency** | **str** | Amount currency (account currency unless specified) | [optional] 
**plugin_name** | **str** |  | [optional] 
**plugin_properties** | [**list[PluginProperty]**](PluginProperty.md) |  | [optional] 
**audit_logs** | [**list[AuditLog]**](AuditLog.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


