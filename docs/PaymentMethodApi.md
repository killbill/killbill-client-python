# killbill.PaymentMethodApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment_method_custom_fields**](PaymentMethodApi.md#create_payment_method_custom_fields) | **POST** /1.0/kb/paymentMethods/{paymentMethodId}/customFields | Add custom fields to payment method
[**delete_payment_method**](PaymentMethodApi.md#delete_payment_method) | **DELETE** /1.0/kb/paymentMethods/{paymentMethodId} | Delete a payment method
[**delete_payment_method_custom_fields**](PaymentMethodApi.md#delete_payment_method_custom_fields) | **DELETE** /1.0/kb/paymentMethods/{paymentMethodId}/customFields | Remove custom fields from payment method
[**get_payment_method**](PaymentMethodApi.md#get_payment_method) | **GET** /1.0/kb/paymentMethods/{paymentMethodId} | Retrieve a payment method by id
[**get_payment_method_by_key**](PaymentMethodApi.md#get_payment_method_by_key) | **GET** /1.0/kb/paymentMethods | Retrieve a payment method by external key
[**get_payment_method_custom_fields**](PaymentMethodApi.md#get_payment_method_custom_fields) | **GET** /1.0/kb/paymentMethods/{paymentMethodId}/customFields | Retrieve payment method custom fields
[**get_payment_methods**](PaymentMethodApi.md#get_payment_methods) | **GET** /1.0/kb/paymentMethods/pagination | List payment methods
[**modify_payment_method_custom_fields**](PaymentMethodApi.md#modify_payment_method_custom_fields) | **PUT** /1.0/kb/paymentMethods/{paymentMethodId}/customFields | Modify custom fields to payment method
[**search_payment_methods**](PaymentMethodApi.md#search_payment_methods) | **GET** /1.0/kb/paymentMethods/search/{searchKey} | Search payment methods


# **create_payment_method_custom_fields**
> list[CustomField] create_payment_method_custom_fields(payment_method_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Add custom fields to payment method



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
api_instance = killbill.PaymentMethodApi(killbill.ApiClient(configuration))
payment_method_id = 'payment_method_id_example' # str | 
body = [killbill.CustomField()] # list[CustomField] | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Add custom fields to payment method
    api_response = api_instance.create_payment_method_custom_fields(payment_method_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodApi->create_payment_method_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | [**str**](.md)|  | 
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

# **delete_payment_method**
> delete_payment_method(payment_method_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, delete_default_pm_with_auto_pay_off=delete_default_pm_with_auto_pay_off, force_default_pm_deletion=force_default_pm_deletion, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Delete a payment method



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
api_instance = killbill.PaymentMethodApi(killbill.ApiClient(configuration))
payment_method_id = 'payment_method_id_example' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
delete_default_pm_with_auto_pay_off = false # bool |  (optional) (default to false)
force_default_pm_deletion = false # bool |  (optional) (default to false)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Delete a payment method
    api_instance.delete_payment_method(payment_method_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, delete_default_pm_with_auto_pay_off=delete_default_pm_with_auto_pay_off, force_default_pm_deletion=force_default_pm_deletion, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling PaymentMethodApi->delete_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | [**str**](.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **delete_default_pm_with_auto_pay_off** | **bool**|  | [optional] [default to false]
 **force_default_pm_deletion** | **bool**|  | [optional] [default to false]
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 
 **x_killbill_reason** | **str**|  | [optional] 
 **x_killbill_comment** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_payment_method_custom_fields**
> delete_payment_method_custom_fields(payment_method_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, custom_field=custom_field, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Remove custom fields from payment method



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
api_instance = killbill.PaymentMethodApi(killbill.ApiClient(configuration))
payment_method_id = 'payment_method_id_example' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
custom_field = ['custom_field_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Remove custom fields from payment method
    api_instance.delete_payment_method_custom_fields(payment_method_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, custom_field=custom_field, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling PaymentMethodApi->delete_payment_method_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | [**str**](.md)|  | 
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

# **get_payment_method**
> PaymentMethod get_payment_method(payment_method_id, x_killbill_api_key, x_killbill_api_secret, included_deleted=included_deleted, with_plugin_info=with_plugin_info, plugin_property=plugin_property, audit=audit)

Retrieve a payment method by id



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
api_instance = killbill.PaymentMethodApi(killbill.ApiClient(configuration))
payment_method_id = 'payment_method_id_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
included_deleted = false # bool |  (optional) (default to false)
with_plugin_info = false # bool |  (optional) (default to false)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # Retrieve a payment method by id
    api_response = api_instance.get_payment_method(payment_method_id, x_killbill_api_key, x_killbill_api_secret, included_deleted=included_deleted, with_plugin_info=with_plugin_info, plugin_property=plugin_property, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodApi->get_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | [**str**](.md)|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **included_deleted** | **bool**|  | [optional] [default to false]
 **with_plugin_info** | **bool**|  | [optional] [default to false]
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 
 **audit** | **str**|  | [optional] [default to NONE]

### Return type

[**PaymentMethod**](PaymentMethod.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_method_by_key**
> PaymentMethod get_payment_method_by_key(external_key, x_killbill_api_key, x_killbill_api_secret, included_deleted=included_deleted, with_plugin_info=with_plugin_info, plugin_property=plugin_property, audit=audit)

Retrieve a payment method by external key



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
api_instance = killbill.PaymentMethodApi(killbill.ApiClient(configuration))
external_key = 'external_key_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
included_deleted = false # bool |  (optional) (default to false)
with_plugin_info = false # bool |  (optional) (default to false)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # Retrieve a payment method by external key
    api_response = api_instance.get_payment_method_by_key(external_key, x_killbill_api_key, x_killbill_api_secret, included_deleted=included_deleted, with_plugin_info=with_plugin_info, plugin_property=plugin_property, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodApi->get_payment_method_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_key** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **included_deleted** | **bool**|  | [optional] [default to false]
 **with_plugin_info** | **bool**|  | [optional] [default to false]
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 
 **audit** | **str**|  | [optional] [default to NONE]

### Return type

[**PaymentMethod**](PaymentMethod.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_method_custom_fields**
> list[CustomField] get_payment_method_custom_fields(payment_method_id, x_killbill_api_key, x_killbill_api_secret, audit=audit)

Retrieve payment method custom fields



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
api_instance = killbill.PaymentMethodApi(killbill.ApiClient(configuration))
payment_method_id = 'payment_method_id_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # Retrieve payment method custom fields
    api_response = api_instance.get_payment_method_custom_fields(payment_method_id, x_killbill_api_key, x_killbill_api_secret, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodApi->get_payment_method_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | [**str**](.md)|  | 
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

# **get_payment_methods**
> list[PaymentMethod] get_payment_methods(x_killbill_api_key, x_killbill_api_secret, offset=offset, limit=limit, plugin_name=plugin_name, with_plugin_info=with_plugin_info, plugin_property=plugin_property, audit=audit)

List payment methods



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
api_instance = killbill.PaymentMethodApi(killbill.ApiClient(configuration))
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)
plugin_name = 'plugin_name_example' # str |  (optional)
with_plugin_info = false # bool |  (optional) (default to false)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # List payment methods
    api_response = api_instance.get_payment_methods(x_killbill_api_key, x_killbill_api_secret, offset=offset, limit=limit, plugin_name=plugin_name, with_plugin_info=with_plugin_info, plugin_property=plugin_property, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodApi->get_payment_methods: %s\n" % e)
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
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 
 **audit** | **str**|  | [optional] [default to NONE]

### Return type

[**list[PaymentMethod]**](PaymentMethod.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_payment_method_custom_fields**
> modify_payment_method_custom_fields(payment_method_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Modify custom fields to payment method



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
api_instance = killbill.PaymentMethodApi(killbill.ApiClient(configuration))
payment_method_id = 'payment_method_id_example' # str | 
body = [killbill.CustomField()] # list[CustomField] | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Modify custom fields to payment method
    api_instance.modify_payment_method_custom_fields(payment_method_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling PaymentMethodApi->modify_payment_method_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | [**str**](.md)|  | 
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

# **search_payment_methods**
> list[PaymentMethod] search_payment_methods(search_key, x_killbill_api_key, x_killbill_api_secret, offset=offset, limit=limit, plugin_name=plugin_name, with_plugin_info=with_plugin_info, plugin_property=plugin_property, audit=audit)

Search payment methods



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
api_instance = killbill.PaymentMethodApi(killbill.ApiClient(configuration))
search_key = 'search_key_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)
plugin_name = 'plugin_name_example' # str |  (optional)
with_plugin_info = false # bool |  (optional) (default to false)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # Search payment methods
    api_response = api_instance.search_payment_methods(search_key, x_killbill_api_key, x_killbill_api_secret, offset=offset, limit=limit, plugin_name=plugin_name, with_plugin_info=with_plugin_info, plugin_property=plugin_property, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodApi->search_payment_methods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_key** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]
 **plugin_name** | **str**|  | [optional] 
 **with_plugin_info** | **bool**|  | [optional] [default to false]
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 
 **audit** | **str**|  | [optional] [default to NONE]

### Return type

[**list[PaymentMethod]**](PaymentMethod.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

