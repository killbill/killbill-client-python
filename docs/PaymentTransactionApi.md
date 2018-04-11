# killbill.PaymentTransactionApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transaction_custom_fields**](PaymentTransactionApi.md#create_transaction_custom_fields) | **POST** /1.0/kb/paymentTransactions/{transactionId}/customFields | Add custom fields to payment transaction
[**create_transaction_tags**](PaymentTransactionApi.md#create_transaction_tags) | **POST** /1.0/kb/paymentTransactions/{transactionId}/tags | Add tags to payment transaction
[**delete_transaction_custom_fields**](PaymentTransactionApi.md#delete_transaction_custom_fields) | **DELETE** /1.0/kb/paymentTransactions/{transactionId}/customFields | Remove custom fields from payment transaction
[**delete_transaction_tags**](PaymentTransactionApi.md#delete_transaction_tags) | **DELETE** /1.0/kb/paymentTransactions/{transactionId}/tags | Remove tags from payment transaction
[**get_payment_by_transaction_id**](PaymentTransactionApi.md#get_payment_by_transaction_id) | **GET** /1.0/kb/paymentTransactions/{transactionId} | Retrieve a payment by transaction id
[**get_transaction_custom_fields**](PaymentTransactionApi.md#get_transaction_custom_fields) | **GET** /1.0/kb/paymentTransactions/{transactionId}/customFields | Retrieve payment transaction custom fields
[**get_transaction_tags**](PaymentTransactionApi.md#get_transaction_tags) | **GET** /1.0/kb/paymentTransactions/{transactionId}/tags | Retrieve payment transaction tags
[**modify_transaction_custom_fields**](PaymentTransactionApi.md#modify_transaction_custom_fields) | **PUT** /1.0/kb/paymentTransactions/{transactionId}/customFields | Modify custom fields to payment transaction
[**notify_state_changed**](PaymentTransactionApi.md#notify_state_changed) | **POST** /1.0/kb/paymentTransactions/{transactionId} | Mark a pending payment transaction as succeeded or failed


# **create_transaction_custom_fields**
> list[CustomField] create_transaction_custom_fields(transaction_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Add custom fields to payment transaction



### Example
```python
from __future__ import print_function
import time
import killbill
from killbill.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = killbill.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = killbill.PaymentTransactionApi(killbill.ApiClient(configuration))
transaction_id = 'transaction_id_example' # str | 
body = [killbill.CustomField()] # list[CustomField] | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Add custom fields to payment transaction
    api_response = api_instance.create_transaction_custom_fields(transaction_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentTransactionApi->create_transaction_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | [**str**](.md)|  | 
 **body** | [**list[CustomField]**](CustomField.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **x_killbill_reason** | **str**|  | [optional] 
 **x_killbill_comment** | **str**|  | [optional] 

### Return type

[**list[CustomField]**](CustomField.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_transaction_tags**
> list[Tag] create_transaction_tags(transaction_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, tag_def=tag_def, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Add tags to payment transaction



### Example
```python
from __future__ import print_function
import time
import killbill
from killbill.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = killbill.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = killbill.PaymentTransactionApi(killbill.ApiClient(configuration))
transaction_id = 'transaction_id_example' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
tag_def = ['tag_def_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Add tags to payment transaction
    api_response = api_instance.create_transaction_tags(transaction_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, tag_def=tag_def, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentTransactionApi->create_transaction_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | [**str**](.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **tag_def** | [**list[str]**](str.md)|  | [optional] 
 **x_killbill_reason** | **str**|  | [optional] 
 **x_killbill_comment** | **str**|  | [optional] 

### Return type

[**list[Tag]**](Tag.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transaction_custom_fields**
> delete_transaction_custom_fields(transaction_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, custom_field=custom_field, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Remove custom fields from payment transaction



### Example
```python
from __future__ import print_function
import time
import killbill
from killbill.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = killbill.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = killbill.PaymentTransactionApi(killbill.ApiClient(configuration))
transaction_id = 'transaction_id_example' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
custom_field = ['custom_field_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Remove custom fields from payment transaction
    api_instance.delete_transaction_custom_fields(transaction_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, custom_field=custom_field, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling PaymentTransactionApi->delete_transaction_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | [**str**](.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **custom_field** | [**list[str]**](str.md)|  | [optional] 
 **x_killbill_reason** | **str**|  | [optional] 
 **x_killbill_comment** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transaction_tags**
> delete_transaction_tags(transaction_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, tag_def=tag_def, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Remove tags from payment transaction



### Example
```python
from __future__ import print_function
import time
import killbill
from killbill.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = killbill.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = killbill.PaymentTransactionApi(killbill.ApiClient(configuration))
transaction_id = 'transaction_id_example' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
tag_def = ['tag_def_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Remove tags from payment transaction
    api_instance.delete_transaction_tags(transaction_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, tag_def=tag_def, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling PaymentTransactionApi->delete_transaction_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | [**str**](.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **tag_def** | [**list[str]**](str.md)|  | [optional] 
 **x_killbill_reason** | **str**|  | [optional] 
 **x_killbill_comment** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_by_transaction_id**
> Payment get_payment_by_transaction_id(transaction_id, x_killbill_api_key, x_killbill_api_secret, with_plugin_info=with_plugin_info, with_attempts=with_attempts, plugin_property=plugin_property, audit=audit)

Retrieve a payment by transaction id



### Example
```python
from __future__ import print_function
import time
import killbill
from killbill.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = killbill.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = killbill.PaymentTransactionApi(killbill.ApiClient(configuration))
transaction_id = 'transaction_id_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
with_plugin_info = false # bool |  (optional) (default to false)
with_attempts = false # bool |  (optional) (default to false)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # Retrieve a payment by transaction id
    api_response = api_instance.get_payment_by_transaction_id(transaction_id, x_killbill_api_key, x_killbill_api_secret, with_plugin_info=with_plugin_info, with_attempts=with_attempts, plugin_property=plugin_property, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentTransactionApi->get_payment_by_transaction_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | [**str**](.md)|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **with_plugin_info** | **bool**|  | [optional] [default to false]
 **with_attempts** | **bool**|  | [optional] [default to false]
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 
 **audit** | **str**|  | [optional] [default to NONE]

### Return type

[**Payment**](Payment.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_custom_fields**
> list[CustomField] get_transaction_custom_fields(transaction_id, x_killbill_api_key, x_killbill_api_secret, audit=audit)

Retrieve payment transaction custom fields



### Example
```python
from __future__ import print_function
import time
import killbill
from killbill.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = killbill.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = killbill.PaymentTransactionApi(killbill.ApiClient(configuration))
transaction_id = 'transaction_id_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # Retrieve payment transaction custom fields
    api_response = api_instance.get_transaction_custom_fields(transaction_id, x_killbill_api_key, x_killbill_api_secret, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentTransactionApi->get_transaction_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | [**str**](.md)|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **audit** | **str**|  | [optional] [default to NONE]

### Return type

[**list[CustomField]**](CustomField.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_tags**
> list[Tag] get_transaction_tags(transaction_id, x_killbill_api_key, x_killbill_api_secret, included_deleted=included_deleted, audit=audit)

Retrieve payment transaction tags



### Example
```python
from __future__ import print_function
import time
import killbill
from killbill.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = killbill.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = killbill.PaymentTransactionApi(killbill.ApiClient(configuration))
transaction_id = 'transaction_id_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
included_deleted = false # bool |  (optional) (default to false)
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # Retrieve payment transaction tags
    api_response = api_instance.get_transaction_tags(transaction_id, x_killbill_api_key, x_killbill_api_secret, included_deleted=included_deleted, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentTransactionApi->get_transaction_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | [**str**](.md)|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **included_deleted** | **bool**|  | [optional] [default to false]
 **audit** | **str**|  | [optional] [default to NONE]

### Return type

[**list[Tag]**](Tag.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_transaction_custom_fields**
> modify_transaction_custom_fields(transaction_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Modify custom fields to payment transaction



### Example
```python
from __future__ import print_function
import time
import killbill
from killbill.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = killbill.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = killbill.PaymentTransactionApi(killbill.ApiClient(configuration))
transaction_id = 'transaction_id_example' # str | 
body = [killbill.CustomField()] # list[CustomField] | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Modify custom fields to payment transaction
    api_instance.modify_transaction_custom_fields(transaction_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling PaymentTransactionApi->modify_transaction_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | [**str**](.md)|  | 
 **body** | [**list[CustomField]**](CustomField.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **x_killbill_reason** | **str**|  | [optional] 
 **x_killbill_comment** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notify_state_changed**
> Payment notify_state_changed(transaction_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, control_plugin_name=control_plugin_name, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Mark a pending payment transaction as succeeded or failed



### Example
```python
from __future__ import print_function
import time
import killbill
from killbill.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = killbill.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = killbill.PaymentTransactionApi(killbill.ApiClient(configuration))
transaction_id = 'transaction_id_example' # str | 
body = killbill.PaymentTransaction() # PaymentTransaction | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
control_plugin_name = ['control_plugin_name_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Mark a pending payment transaction as succeeded or failed
    api_response = api_instance.notify_state_changed(transaction_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, control_plugin_name=control_plugin_name, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentTransactionApi->notify_state_changed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | [**str**](.md)|  | 
 **body** | [**PaymentTransaction**](PaymentTransaction.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **control_plugin_name** | [**list[str]**](str.md)|  | [optional] 
 **x_killbill_reason** | **str**|  | [optional] 
 **x_killbill_comment** | **str**|  | [optional] 

### Return type

[**Payment**](Payment.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

