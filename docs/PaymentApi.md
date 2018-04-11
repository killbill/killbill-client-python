# killbill.PaymentApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_scheduled_payment_transaction_by_external_key**](PaymentApi.md#cancel_scheduled_payment_transaction_by_external_key) | **DELETE** /1.0/kb/payments/cancelScheduledPaymentTransaction | Cancels a scheduled payment attempt retry
[**cancel_scheduled_payment_transaction_by_id**](PaymentApi.md#cancel_scheduled_payment_transaction_by_id) | **DELETE** /1.0/kb/payments/{paymentTransactionId}/cancelScheduledPaymentTransaction | Cancels a scheduled payment attempt retry
[**capture_authorization**](PaymentApi.md#capture_authorization) | **POST** /1.0/kb/payments/{paymentId} | Capture an existing authorization
[**capture_authorization_by_external_key**](PaymentApi.md#capture_authorization_by_external_key) | **POST** /1.0/kb/payments | Capture an existing authorization
[**chargeback_payment**](PaymentApi.md#chargeback_payment) | **POST** /1.0/kb/payments/{paymentId}/chargebacks | Record a chargeback
[**chargeback_payment_by_external_key**](PaymentApi.md#chargeback_payment_by_external_key) | **POST** /1.0/kb/payments/chargebacks | Record a chargeback
[**chargeback_reversal_payment**](PaymentApi.md#chargeback_reversal_payment) | **POST** /1.0/kb/payments/{paymentId}/chargebackReversals | Record a chargeback reversal
[**chargeback_reversal_payment_by_external_key**](PaymentApi.md#chargeback_reversal_payment_by_external_key) | **POST** /1.0/kb/payments/chargebackReversals | Record a chargeback reversal
[**complete_transaction**](PaymentApi.md#complete_transaction) | **PUT** /1.0/kb/payments/{paymentId} | Complete an existing transaction
[**complete_transaction_by_external_key**](PaymentApi.md#complete_transaction_by_external_key) | **PUT** /1.0/kb/payments | Complete an existing transaction
[**create_combo_payment**](PaymentApi.md#create_combo_payment) | **POST** /1.0/kb/payments/combo | Combo api to create a new payment transaction on a existing (or not) account 
[**create_payment_custom_fields**](PaymentApi.md#create_payment_custom_fields) | **POST** /1.0/kb/payments/{paymentId}/customFields | Add custom fields to payment
[**create_payment_tags**](PaymentApi.md#create_payment_tags) | **POST** /1.0/kb/payments/{paymentId}/tags | Add tags to payment payment
[**delete_payment_custom_fields**](PaymentApi.md#delete_payment_custom_fields) | **DELETE** /1.0/kb/payments/{paymentId}/customFields | Remove custom fields from payment payment
[**delete_payment_tags**](PaymentApi.md#delete_payment_tags) | **DELETE** /1.0/kb/payments/{paymentId}/tags | Remove tags from payment payment
[**get_payment**](PaymentApi.md#get_payment) | **GET** /1.0/kb/payments/{paymentId} | Retrieve a payment by id
[**get_payment_by_external_key**](PaymentApi.md#get_payment_by_external_key) | **GET** /1.0/kb/payments | Retrieve a payment by external key
[**get_payment_custom_fields**](PaymentApi.md#get_payment_custom_fields) | **GET** /1.0/kb/payments/{paymentId}/customFields | Retrieve payment custom fields
[**get_payment_tags**](PaymentApi.md#get_payment_tags) | **GET** /1.0/kb/payments/{paymentId}/tags | Retrieve payment payment tags
[**get_payments**](PaymentApi.md#get_payments) | **GET** /1.0/kb/payments/pagination | Get payments
[**modify_payment_custom_fields**](PaymentApi.md#modify_payment_custom_fields) | **PUT** /1.0/kb/payments/{paymentId}/customFields | Modify custom fields to payment
[**refund_payment**](PaymentApi.md#refund_payment) | **POST** /1.0/kb/payments/{paymentId}/refunds | Refund an existing payment
[**refund_payment_by_external_key**](PaymentApi.md#refund_payment_by_external_key) | **POST** /1.0/kb/payments/refunds | Refund an existing payment
[**search_payments**](PaymentApi.md#search_payments) | **GET** /1.0/kb/payments/search/{searchKey} | Search payments
[**void_payment**](PaymentApi.md#void_payment) | **DELETE** /1.0/kb/payments/{paymentId} | Void an existing payment
[**void_payment_by_external_key**](PaymentApi.md#void_payment_by_external_key) | **DELETE** /1.0/kb/payments | Void an existing payment


# **cancel_scheduled_payment_transaction_by_external_key**
> cancel_scheduled_payment_transaction_by_external_key(transaction_external_key, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Cancels a scheduled payment attempt retry



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
api_instance = killbill.PaymentApi(killbill.ApiClient(configuration))
transaction_external_key = 'transaction_external_key_example' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Cancels a scheduled payment attempt retry
    api_instance.cancel_scheduled_payment_transaction_by_external_key(transaction_external_key, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling PaymentApi->cancel_scheduled_payment_transaction_by_external_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_external_key** | **str**|  | 
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

# **cancel_scheduled_payment_transaction_by_id**
> cancel_scheduled_payment_transaction_by_id(payment_transaction_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Cancels a scheduled payment attempt retry



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
api_instance = killbill.PaymentApi(killbill.ApiClient(configuration))
payment_transaction_id = 'payment_transaction_id_example' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Cancels a scheduled payment attempt retry
    api_instance.cancel_scheduled_payment_transaction_by_id(payment_transaction_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling PaymentApi->cancel_scheduled_payment_transaction_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_transaction_id** | [**str**](.md)|  | 
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

# **capture_authorization**
> Payment capture_authorization(payment_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, control_plugin_name=control_plugin_name, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Capture an existing authorization



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
api_instance = killbill.PaymentApi(killbill.ApiClient(configuration))
payment_id = 'payment_id_example' # str | 
body = killbill.PaymentTransaction() # PaymentTransaction | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
control_plugin_name = ['control_plugin_name_example'] # list[str] |  (optional)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Capture an existing authorization
    api_response = api_instance.capture_authorization(payment_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, control_plugin_name=control_plugin_name, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->capture_authorization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | [**str**](.md)|  | 
 **body** | [**PaymentTransaction**](PaymentTransaction.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **control_plugin_name** | [**list[str]**](str.md)|  | [optional] 
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 
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

# **capture_authorization_by_external_key**
> Payment capture_authorization_by_external_key(body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, control_plugin_name=control_plugin_name, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Capture an existing authorization



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
api_instance = killbill.PaymentApi(killbill.ApiClient(configuration))
body = killbill.PaymentTransaction() # PaymentTransaction | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
control_plugin_name = ['control_plugin_name_example'] # list[str] |  (optional)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Capture an existing authorization
    api_response = api_instance.capture_authorization_by_external_key(body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, control_plugin_name=control_plugin_name, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->capture_authorization_by_external_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PaymentTransaction**](PaymentTransaction.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **control_plugin_name** | [**list[str]**](str.md)|  | [optional] 
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 
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

# **chargeback_payment**
> Payment chargeback_payment(payment_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, control_plugin_name=control_plugin_name, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Record a chargeback



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
api_instance = killbill.PaymentApi(killbill.ApiClient(configuration))
payment_id = 'payment_id_example' # str | 
body = killbill.PaymentTransaction() # PaymentTransaction | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
control_plugin_name = ['control_plugin_name_example'] # list[str] |  (optional)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Record a chargeback
    api_response = api_instance.chargeback_payment(payment_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, control_plugin_name=control_plugin_name, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->chargeback_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | [**str**](.md)|  | 
 **body** | [**PaymentTransaction**](PaymentTransaction.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **control_plugin_name** | [**list[str]**](str.md)|  | [optional] 
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 
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

# **chargeback_payment_by_external_key**
> Payment chargeback_payment_by_external_key(body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, control_plugin_name=control_plugin_name, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Record a chargeback



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
api_instance = killbill.PaymentApi(killbill.ApiClient(configuration))
body = killbill.PaymentTransaction() # PaymentTransaction | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
control_plugin_name = ['control_plugin_name_example'] # list[str] |  (optional)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Record a chargeback
    api_response = api_instance.chargeback_payment_by_external_key(body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, control_plugin_name=control_plugin_name, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->chargeback_payment_by_external_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PaymentTransaction**](PaymentTransaction.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **control_plugin_name** | [**list[str]**](str.md)|  | [optional] 
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 
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

# **chargeback_reversal_payment**
> Payment chargeback_reversal_payment(payment_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, control_plugin_name=control_plugin_name, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Record a chargeback reversal



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
api_instance = killbill.PaymentApi(killbill.ApiClient(configuration))
payment_id = 'payment_id_example' # str | 
body = killbill.PaymentTransaction() # PaymentTransaction | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
control_plugin_name = ['control_plugin_name_example'] # list[str] |  (optional)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Record a chargeback reversal
    api_response = api_instance.chargeback_reversal_payment(payment_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, control_plugin_name=control_plugin_name, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->chargeback_reversal_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | [**str**](.md)|  | 
 **body** | [**PaymentTransaction**](PaymentTransaction.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **control_plugin_name** | [**list[str]**](str.md)|  | [optional] 
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 
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

# **chargeback_reversal_payment_by_external_key**
> Payment chargeback_reversal_payment_by_external_key(body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, control_plugin_name=control_plugin_name, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Record a chargeback reversal



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
api_instance = killbill.PaymentApi(killbill.ApiClient(configuration))
body = killbill.PaymentTransaction() # PaymentTransaction | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
control_plugin_name = ['control_plugin_name_example'] # list[str] |  (optional)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Record a chargeback reversal
    api_response = api_instance.chargeback_reversal_payment_by_external_key(body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, control_plugin_name=control_plugin_name, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->chargeback_reversal_payment_by_external_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PaymentTransaction**](PaymentTransaction.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **control_plugin_name** | [**list[str]**](str.md)|  | [optional] 
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 
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

# **complete_transaction**
> complete_transaction(payment_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, control_plugin_name=control_plugin_name, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Complete an existing transaction



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
api_instance = killbill.PaymentApi(killbill.ApiClient(configuration))
payment_id = 'payment_id_example' # str | 
body = killbill.PaymentTransaction() # PaymentTransaction | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
control_plugin_name = ['control_plugin_name_example'] # list[str] |  (optional)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Complete an existing transaction
    api_instance.complete_transaction(payment_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, control_plugin_name=control_plugin_name, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling PaymentApi->complete_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | [**str**](.md)|  | 
 **body** | [**PaymentTransaction**](PaymentTransaction.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **control_plugin_name** | [**list[str]**](str.md)|  | [optional] 
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 
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

# **complete_transaction_by_external_key**
> complete_transaction_by_external_key(body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, control_plugin_name=control_plugin_name, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Complete an existing transaction



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
api_instance = killbill.PaymentApi(killbill.ApiClient(configuration))
body = killbill.PaymentTransaction() # PaymentTransaction | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
control_plugin_name = ['control_plugin_name_example'] # list[str] |  (optional)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Complete an existing transaction
    api_instance.complete_transaction_by_external_key(body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, control_plugin_name=control_plugin_name, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling PaymentApi->complete_transaction_by_external_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PaymentTransaction**](PaymentTransaction.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **control_plugin_name** | [**list[str]**](str.md)|  | [optional] 
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 
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

# **create_combo_payment**
> Payment create_combo_payment(body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, control_plugin_name=control_plugin_name, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Combo api to create a new payment transaction on a existing (or not) account 



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
api_instance = killbill.PaymentApi(killbill.ApiClient(configuration))
body = killbill.ComboPaymentTransaction() # ComboPaymentTransaction | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
control_plugin_name = ['control_plugin_name_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Combo api to create a new payment transaction on a existing (or not) account 
    api_response = api_instance.create_combo_payment(body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, control_plugin_name=control_plugin_name, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->create_combo_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComboPaymentTransaction**](ComboPaymentTransaction.md)|  | 
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

# **create_payment_custom_fields**
> list[CustomField] create_payment_custom_fields(payment_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Add custom fields to payment



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
api_instance = killbill.PaymentApi(killbill.ApiClient(configuration))
payment_id = 'payment_id_example' # str | 
body = [killbill.CustomField()] # list[CustomField] | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Add custom fields to payment
    api_response = api_instance.create_payment_custom_fields(payment_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->create_payment_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | [**str**](.md)|  | 
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

# **create_payment_tags**
> list[Tag] create_payment_tags(payment_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, tag_def=tag_def, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Add tags to payment payment



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
api_instance = killbill.PaymentApi(killbill.ApiClient(configuration))
payment_id = 'payment_id_example' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
tag_def = ['tag_def_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Add tags to payment payment
    api_response = api_instance.create_payment_tags(payment_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, tag_def=tag_def, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->create_payment_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | [**str**](.md)|  | 
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

# **delete_payment_custom_fields**
> delete_payment_custom_fields(payment_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, custom_field=custom_field, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Remove custom fields from payment payment



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
api_instance = killbill.PaymentApi(killbill.ApiClient(configuration))
payment_id = 'payment_id_example' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
custom_field = ['custom_field_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Remove custom fields from payment payment
    api_instance.delete_payment_custom_fields(payment_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, custom_field=custom_field, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling PaymentApi->delete_payment_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | [**str**](.md)|  | 
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

# **delete_payment_tags**
> delete_payment_tags(payment_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, tag_def=tag_def, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Remove tags from payment payment



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
api_instance = killbill.PaymentApi(killbill.ApiClient(configuration))
payment_id = 'payment_id_example' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
tag_def = ['tag_def_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Remove tags from payment payment
    api_instance.delete_payment_tags(payment_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, tag_def=tag_def, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling PaymentApi->delete_payment_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | [**str**](.md)|  | 
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

# **get_payment**
> Payment get_payment(payment_id, x_killbill_api_key, x_killbill_api_secret, with_plugin_info=with_plugin_info, with_attempts=with_attempts, plugin_property=plugin_property, audit=audit)

Retrieve a payment by id



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
api_instance = killbill.PaymentApi(killbill.ApiClient(configuration))
payment_id = 'payment_id_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
with_plugin_info = false # bool |  (optional) (default to false)
with_attempts = false # bool |  (optional) (default to false)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # Retrieve a payment by id
    api_response = api_instance.get_payment(payment_id, x_killbill_api_key, x_killbill_api_secret, with_plugin_info=with_plugin_info, with_attempts=with_attempts, plugin_property=plugin_property, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->get_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | [**str**](.md)|  | 
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

# **get_payment_by_external_key**
> Payment get_payment_by_external_key(external_key, x_killbill_api_key, x_killbill_api_secret, with_plugin_info=with_plugin_info, with_attempts=with_attempts, plugin_property=plugin_property, audit=audit)

Retrieve a payment by external key



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
api_instance = killbill.PaymentApi(killbill.ApiClient(configuration))
external_key = 'external_key_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
with_plugin_info = false # bool |  (optional) (default to false)
with_attempts = false # bool |  (optional) (default to false)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # Retrieve a payment by external key
    api_response = api_instance.get_payment_by_external_key(external_key, x_killbill_api_key, x_killbill_api_secret, with_plugin_info=with_plugin_info, with_attempts=with_attempts, plugin_property=plugin_property, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->get_payment_by_external_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_key** | **str**|  | 
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

# **get_payment_custom_fields**
> list[CustomField] get_payment_custom_fields(payment_id, x_killbill_api_key, x_killbill_api_secret, audit=audit)

Retrieve payment custom fields



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
api_instance = killbill.PaymentApi(killbill.ApiClient(configuration))
payment_id = 'payment_id_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # Retrieve payment custom fields
    api_response = api_instance.get_payment_custom_fields(payment_id, x_killbill_api_key, x_killbill_api_secret, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->get_payment_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | [**str**](.md)|  | 
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

# **get_payment_tags**
> list[Tag] get_payment_tags(payment_id, x_killbill_api_key, x_killbill_api_secret, included_deleted=included_deleted, audit=audit)

Retrieve payment payment tags



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
api_instance = killbill.PaymentApi(killbill.ApiClient(configuration))
payment_id = 'payment_id_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
included_deleted = false # bool |  (optional) (default to false)
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # Retrieve payment payment tags
    api_response = api_instance.get_payment_tags(payment_id, x_killbill_api_key, x_killbill_api_secret, included_deleted=included_deleted, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->get_payment_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | [**str**](.md)|  | 
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

# **get_payments**
> list[Payment] get_payments(x_killbill_api_key, x_killbill_api_secret, offset=offset, limit=limit, plugin_name=plugin_name, with_plugin_info=with_plugin_info, with_attempts=with_attempts, plugin_property=plugin_property, audit=audit)

Get payments



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
api_instance = killbill.PaymentApi(killbill.ApiClient(configuration))
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)
plugin_name = 'plugin_name_example' # str |  (optional)
with_plugin_info = false # bool |  (optional) (default to false)
with_attempts = false # bool |  (optional) (default to false)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # Get payments
    api_response = api_instance.get_payments(x_killbill_api_key, x_killbill_api_secret, offset=offset, limit=limit, plugin_name=plugin_name, with_plugin_info=with_plugin_info, with_attempts=with_attempts, plugin_property=plugin_property, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->get_payments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]
 **plugin_name** | **str**|  | [optional] 
 **with_plugin_info** | **bool**|  | [optional] [default to false]
 **with_attempts** | **bool**|  | [optional] [default to false]
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 
 **audit** | **str**|  | [optional] [default to NONE]

### Return type

[**list[Payment]**](Payment.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_payment_custom_fields**
> modify_payment_custom_fields(payment_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Modify custom fields to payment



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
api_instance = killbill.PaymentApi(killbill.ApiClient(configuration))
payment_id = 'payment_id_example' # str | 
body = [killbill.CustomField()] # list[CustomField] | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Modify custom fields to payment
    api_instance.modify_payment_custom_fields(payment_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling PaymentApi->modify_payment_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | [**str**](.md)|  | 
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

# **refund_payment**
> Payment refund_payment(payment_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, control_plugin_name=control_plugin_name, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Refund an existing payment



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
api_instance = killbill.PaymentApi(killbill.ApiClient(configuration))
payment_id = 'payment_id_example' # str | 
body = killbill.PaymentTransaction() # PaymentTransaction | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
control_plugin_name = ['control_plugin_name_example'] # list[str] |  (optional)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Refund an existing payment
    api_response = api_instance.refund_payment(payment_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, control_plugin_name=control_plugin_name, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->refund_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | [**str**](.md)|  | 
 **body** | [**PaymentTransaction**](PaymentTransaction.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **control_plugin_name** | [**list[str]**](str.md)|  | [optional] 
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 
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

# **refund_payment_by_external_key**
> Payment refund_payment_by_external_key(body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, control_plugin_name=control_plugin_name, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Refund an existing payment



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
api_instance = killbill.PaymentApi(killbill.ApiClient(configuration))
body = killbill.PaymentTransaction() # PaymentTransaction | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
control_plugin_name = ['control_plugin_name_example'] # list[str] |  (optional)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Refund an existing payment
    api_response = api_instance.refund_payment_by_external_key(body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, control_plugin_name=control_plugin_name, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->refund_payment_by_external_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PaymentTransaction**](PaymentTransaction.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **control_plugin_name** | [**list[str]**](str.md)|  | [optional] 
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 
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

# **search_payments**
> list[Payment] search_payments(search_key, x_killbill_api_key, x_killbill_api_secret, offset=offset, limit=limit, with_plugin_info=with_plugin_info, with_attempts=with_attempts, plugin_name=plugin_name, plugin_property=plugin_property, audit=audit)

Search payments



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
api_instance = killbill.PaymentApi(killbill.ApiClient(configuration))
search_key = 'search_key_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)
with_plugin_info = false # bool |  (optional) (default to false)
with_attempts = false # bool |  (optional) (default to false)
plugin_name = 'plugin_name_example' # str |  (optional)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # Search payments
    api_response = api_instance.search_payments(search_key, x_killbill_api_key, x_killbill_api_secret, offset=offset, limit=limit, with_plugin_info=with_plugin_info, with_attempts=with_attempts, plugin_name=plugin_name, plugin_property=plugin_property, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->search_payments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_key** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]
 **with_plugin_info** | **bool**|  | [optional] [default to false]
 **with_attempts** | **bool**|  | [optional] [default to false]
 **plugin_name** | **str**|  | [optional] 
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 
 **audit** | **str**|  | [optional] [default to NONE]

### Return type

[**list[Payment]**](Payment.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **void_payment**
> void_payment(payment_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, control_plugin_name=control_plugin_name, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Void an existing payment



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
api_instance = killbill.PaymentApi(killbill.ApiClient(configuration))
payment_id = 'payment_id_example' # str | 
body = killbill.PaymentTransaction() # PaymentTransaction | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
control_plugin_name = ['control_plugin_name_example'] # list[str] |  (optional)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Void an existing payment
    api_instance.void_payment(payment_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, control_plugin_name=control_plugin_name, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling PaymentApi->void_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | [**str**](.md)|  | 
 **body** | [**PaymentTransaction**](PaymentTransaction.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **control_plugin_name** | [**list[str]**](str.md)|  | [optional] 
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 
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

# **void_payment_by_external_key**
> void_payment_by_external_key(body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, control_plugin_name=control_plugin_name, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Void an existing payment



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
api_instance = killbill.PaymentApi(killbill.ApiClient(configuration))
body = killbill.PaymentTransaction() # PaymentTransaction | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
control_plugin_name = ['control_plugin_name_example'] # list[str] |  (optional)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Void an existing payment
    api_instance.void_payment_by_external_key(body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, control_plugin_name=control_plugin_name, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling PaymentApi->void_payment_by_external_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PaymentTransaction**](PaymentTransaction.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **control_plugin_name** | [**list[str]**](str.md)|  | [optional] 
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 
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

