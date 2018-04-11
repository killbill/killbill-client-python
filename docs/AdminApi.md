# killbill.AdminApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invalidates_cache**](AdminApi.md#invalidates_cache) | **DELETE** /1.0/kb/admin/cache | Invalidates the given Cache if specified, otherwise invalidates all caches
[**invalidates_cache_by_account**](AdminApi.md#invalidates_cache_by_account) | **DELETE** /1.0/kb/admin/cache/accounts/{accountId} | Invalidates Caches per account level
[**invalidates_cache_by_tenant**](AdminApi.md#invalidates_cache_by_tenant) | **DELETE** /1.0/kb/admin/cache/tenants | Invalidates Caches per tenant level
[**put_in_rotation**](AdminApi.md#put_in_rotation) | **PUT** /1.0/kb/admin/healthcheck | Put the host back into rotation
[**put_out_of_rotation**](AdminApi.md#put_out_of_rotation) | **DELETE** /1.0/kb/admin/healthcheck | Put the host out of rotation
[**trigger_invoice_generation_for_parked_accounts**](AdminApi.md#trigger_invoice_generation_for_parked_accounts) | **POST** /1.0/kb/admin/invoices | Trigger an invoice generation for all parked accounts
[**update_payment_transaction_state**](AdminApi.md#update_payment_transaction_state) | **PUT** /1.0/kb/admin/payments/{paymentId}/transactions/{paymentTransactionId} | Update existing paymentTransaction and associated payment state


# **invalidates_cache**
> invalidates_cache(x_killbill_api_key, x_killbill_api_secret, cache_name=cache_name)

Invalidates the given Cache if specified, otherwise invalidates all caches



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
api_instance = killbill.AdminApi(killbill.ApiClient(configuration))
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
cache_name = 'cache_name_example' # str |  (optional)

try:
    # Invalidates the given Cache if specified, otherwise invalidates all caches
    api_instance.invalidates_cache(x_killbill_api_key, x_killbill_api_secret, cache_name=cache_name)
except ApiException as e:
    print("Exception when calling AdminApi->invalidates_cache: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **cache_name** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invalidates_cache_by_account**
> invalidates_cache_by_account(account_id, x_killbill_api_key, x_killbill_api_secret)

Invalidates Caches per account level



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
api_instance = killbill.AdminApi(killbill.ApiClient(configuration))
account_id = 'account_id_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 

try:
    # Invalidates Caches per account level
    api_instance.invalidates_cache_by_account(account_id, x_killbill_api_key, x_killbill_api_secret)
except ApiException as e:
    print("Exception when calling AdminApi->invalidates_cache_by_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invalidates_cache_by_tenant**
> invalidates_cache_by_tenant(x_killbill_api_key, x_killbill_api_secret)

Invalidates Caches per tenant level



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
api_instance = killbill.AdminApi(killbill.ApiClient(configuration))
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 

try:
    # Invalidates Caches per tenant level
    api_instance.invalidates_cache_by_tenant(x_killbill_api_key, x_killbill_api_secret)
except ApiException as e:
    print("Exception when calling AdminApi->invalidates_cache_by_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_in_rotation**
> put_in_rotation(x_killbill_api_key, x_killbill_api_secret)

Put the host back into rotation



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
api_instance = killbill.AdminApi(killbill.ApiClient(configuration))
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 

try:
    # Put the host back into rotation
    api_instance.put_in_rotation(x_killbill_api_key, x_killbill_api_secret)
except ApiException as e:
    print("Exception when calling AdminApi->put_in_rotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_out_of_rotation**
> put_out_of_rotation(x_killbill_api_key, x_killbill_api_secret)

Put the host out of rotation



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
api_instance = killbill.AdminApi(killbill.ApiClient(configuration))
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 

try:
    # Put the host out of rotation
    api_instance.put_out_of_rotation(x_killbill_api_key, x_killbill_api_secret)
except ApiException as e:
    print("Exception when calling AdminApi->put_out_of_rotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_invoice_generation_for_parked_accounts**
> trigger_invoice_generation_for_parked_accounts(x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, offset=offset, limit=limit, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Trigger an invoice generation for all parked accounts



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
api_instance = killbill.AdminApi(killbill.ApiClient(configuration))
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Trigger an invoice generation for all parked accounts
    api_instance.trigger_invoice_generation_for_parked_accounts(x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, offset=offset, limit=limit, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling AdminApi->trigger_invoice_generation_for_parked_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]
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

# **update_payment_transaction_state**
> update_payment_transaction_state(payment_id, payment_transaction_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Update existing paymentTransaction and associated payment state



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
api_instance = killbill.AdminApi(killbill.ApiClient(configuration))
payment_id = 'payment_id_example' # str | 
payment_transaction_id = 'payment_transaction_id_example' # str | 
body = killbill.AdminPayment() # AdminPayment | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Update existing paymentTransaction and associated payment state
    api_instance.update_payment_transaction_state(payment_id, payment_transaction_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling AdminApi->update_payment_transaction_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | [**str**](.md)|  | 
 **payment_transaction_id** | [**str**](.md)|  | 
 **body** | [**AdminPayment**](AdminPayment.md)|  | 
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

