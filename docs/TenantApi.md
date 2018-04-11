# killbill.TenantApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tenant**](TenantApi.md#create_tenant) | **POST** /1.0/kb/tenants | Create a tenant
[**delete_per_tenant_configuration**](TenantApi.md#delete_per_tenant_configuration) | **DELETE** /1.0/kb/tenants/uploadPerTenantConfig | Delete a per tenant configuration (system properties)
[**delete_plugin_configuration**](TenantApi.md#delete_plugin_configuration) | **DELETE** /1.0/kb/tenants/uploadPluginConfig/{pluginName} | Delete a per tenant configuration for a plugin
[**delete_plugin_payment_state_machine_config**](TenantApi.md#delete_plugin_payment_state_machine_config) | **DELETE** /1.0/kb/tenants/uploadPluginPaymentStateMachineConfig/{pluginName} | Delete a per tenant payment state machine for a plugin
[**delete_push_notification_callbacks**](TenantApi.md#delete_push_notification_callbacks) | **DELETE** /1.0/kb/tenants/registerNotificationCallback | Delete a push notification
[**delete_user_key_value**](TenantApi.md#delete_user_key_value) | **DELETE** /1.0/kb/tenants/userKeyValue/{keyName} | Delete  a per tenant user key/value
[**get_all_plugin_configuration**](TenantApi.md#get_all_plugin_configuration) | **GET** /1.0/kb/tenants/uploadPerTenantConfig/{keyPrefix}/search | Retrieve a per tenant key value based on key prefix
[**get_per_tenant_configuration**](TenantApi.md#get_per_tenant_configuration) | **GET** /1.0/kb/tenants/uploadPerTenantConfig | Retrieve a per tenant configuration (system properties)
[**get_plugin_configuration**](TenantApi.md#get_plugin_configuration) | **GET** /1.0/kb/tenants/uploadPluginConfig/{pluginName} | Retrieve a per tenant configuration for a plugin
[**get_plugin_payment_state_machine_config**](TenantApi.md#get_plugin_payment_state_machine_config) | **GET** /1.0/kb/tenants/uploadPluginPaymentStateMachineConfig/{pluginName} | Retrieve a per tenant payment state machine for a plugin
[**get_push_notification_callbacks**](TenantApi.md#get_push_notification_callbacks) | **GET** /1.0/kb/tenants/registerNotificationCallback | Retrieve a push notification
[**get_tenant**](TenantApi.md#get_tenant) | **GET** /1.0/kb/tenants/{tenantId} | Retrieve a tenant by id
[**get_tenant_by_api_key**](TenantApi.md#get_tenant_by_api_key) | **GET** /1.0/kb/tenants | Retrieve a tenant by its API key
[**get_user_key_value**](TenantApi.md#get_user_key_value) | **GET** /1.0/kb/tenants/userKeyValue/{keyName} | Retrieve a per tenant user key/value
[**insert_user_key_value**](TenantApi.md#insert_user_key_value) | **POST** /1.0/kb/tenants/userKeyValue/{keyName} | Add a per tenant user key/value
[**register_push_notification_callback**](TenantApi.md#register_push_notification_callback) | **POST** /1.0/kb/tenants/registerNotificationCallback | Create a push notification
[**upload_per_tenant_configuration**](TenantApi.md#upload_per_tenant_configuration) | **POST** /1.0/kb/tenants/uploadPerTenantConfig | Add a per tenant configuration (system properties)
[**upload_plugin_configuration**](TenantApi.md#upload_plugin_configuration) | **POST** /1.0/kb/tenants/uploadPluginConfig/{pluginName} | Add a per tenant configuration for a plugin
[**upload_plugin_payment_state_machine_config**](TenantApi.md#upload_plugin_payment_state_machine_config) | **POST** /1.0/kb/tenants/uploadPluginPaymentStateMachineConfig/{pluginName} | Add a per tenant payment state machine for a plugin


# **create_tenant**
> Tenant create_tenant(body, x_killbill_created_by, use_global_default=use_global_default, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Create a tenant



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
api_instance = killbill.TenantApi(killbill.ApiClient(configuration))
body = killbill.Tenant() # Tenant | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
use_global_default = false # bool |  (optional) (default to false)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Create a tenant
    api_response = api_instance.create_tenant(body, x_killbill_created_by, use_global_default=use_global_default, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantApi->create_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Tenant**](Tenant.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **use_global_default** | **bool**|  | [optional] [default to false]
 **x_killbill_reason** | **str**|  | [optional] 
 **x_killbill_comment** | **str**|  | [optional] 

### Return type

[**Tenant**](Tenant.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_per_tenant_configuration**
> delete_per_tenant_configuration(x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Delete a per tenant configuration (system properties)



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
api_instance = killbill.TenantApi(killbill.ApiClient(configuration))
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Delete a per tenant configuration (system properties)
    api_instance.delete_per_tenant_configuration(x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling TenantApi->delete_per_tenant_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_plugin_configuration**
> delete_plugin_configuration(plugin_name, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Delete a per tenant configuration for a plugin



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
api_instance = killbill.TenantApi(killbill.ApiClient(configuration))
plugin_name = 'plugin_name_example' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Delete a per tenant configuration for a plugin
    api_instance.delete_plugin_configuration(plugin_name, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling TenantApi->delete_plugin_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_name** | **str**|  | 
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

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_plugin_payment_state_machine_config**
> delete_plugin_payment_state_machine_config(plugin_name, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Delete a per tenant payment state machine for a plugin



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
api_instance = killbill.TenantApi(killbill.ApiClient(configuration))
plugin_name = 'plugin_name_example' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Delete a per tenant payment state machine for a plugin
    api_instance.delete_plugin_payment_state_machine_config(plugin_name, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling TenantApi->delete_plugin_payment_state_machine_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_name** | **str**|  | 
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

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_push_notification_callbacks**
> delete_push_notification_callbacks(x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Delete a push notification



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
api_instance = killbill.TenantApi(killbill.ApiClient(configuration))
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Delete a push notification
    api_instance.delete_push_notification_callbacks(x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling TenantApi->delete_push_notification_callbacks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_key_value**
> delete_user_key_value(key_name, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Delete  a per tenant user key/value



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
api_instance = killbill.TenantApi(killbill.ApiClient(configuration))
key_name = 'key_name_example' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Delete  a per tenant user key/value
    api_instance.delete_user_key_value(key_name, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling TenantApi->delete_user_key_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_name** | **str**|  | 
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

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_plugin_configuration**
> TenantKeyValue get_all_plugin_configuration(key_prefix, x_killbill_api_key, x_killbill_api_secret)

Retrieve a per tenant key value based on key prefix



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
api_instance = killbill.TenantApi(killbill.ApiClient(configuration))
key_prefix = 'key_prefix_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 

try:
    # Retrieve a per tenant key value based on key prefix
    api_response = api_instance.get_all_plugin_configuration(key_prefix, x_killbill_api_key, x_killbill_api_secret)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantApi->get_all_plugin_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_prefix** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 

### Return type

[**TenantKeyValue**](TenantKeyValue.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_per_tenant_configuration**
> TenantKeyValue get_per_tenant_configuration(x_killbill_api_key, x_killbill_api_secret)

Retrieve a per tenant configuration (system properties)



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
api_instance = killbill.TenantApi(killbill.ApiClient(configuration))
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 

try:
    # Retrieve a per tenant configuration (system properties)
    api_response = api_instance.get_per_tenant_configuration(x_killbill_api_key, x_killbill_api_secret)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantApi->get_per_tenant_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 

### Return type

[**TenantKeyValue**](TenantKeyValue.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugin_configuration**
> TenantKeyValue get_plugin_configuration(plugin_name, x_killbill_api_key, x_killbill_api_secret)

Retrieve a per tenant configuration for a plugin



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
api_instance = killbill.TenantApi(killbill.ApiClient(configuration))
plugin_name = 'plugin_name_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 

try:
    # Retrieve a per tenant configuration for a plugin
    api_response = api_instance.get_plugin_configuration(plugin_name, x_killbill_api_key, x_killbill_api_secret)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantApi->get_plugin_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_name** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 

### Return type

[**TenantKeyValue**](TenantKeyValue.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugin_payment_state_machine_config**
> TenantKeyValue get_plugin_payment_state_machine_config(plugin_name, x_killbill_api_key, x_killbill_api_secret)

Retrieve a per tenant payment state machine for a plugin



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
api_instance = killbill.TenantApi(killbill.ApiClient(configuration))
plugin_name = 'plugin_name_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 

try:
    # Retrieve a per tenant payment state machine for a plugin
    api_response = api_instance.get_plugin_payment_state_machine_config(plugin_name, x_killbill_api_key, x_killbill_api_secret)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantApi->get_plugin_payment_state_machine_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_name** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 

### Return type

[**TenantKeyValue**](TenantKeyValue.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_push_notification_callbacks**
> TenantKeyValue get_push_notification_callbacks(x_killbill_api_key, x_killbill_api_secret)

Retrieve a push notification



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
api_instance = killbill.TenantApi(killbill.ApiClient(configuration))
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 

try:
    # Retrieve a push notification
    api_response = api_instance.get_push_notification_callbacks(x_killbill_api_key, x_killbill_api_secret)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantApi->get_push_notification_callbacks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 

### Return type

[**TenantKeyValue**](TenantKeyValue.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant**
> Tenant get_tenant(tenant_id, x_killbill_api_key, x_killbill_api_secret)

Retrieve a tenant by id



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
api_instance = killbill.TenantApi(killbill.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 

try:
    # Retrieve a tenant by id
    api_response = api_instance.get_tenant(tenant_id, x_killbill_api_key, x_killbill_api_secret)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantApi->get_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | [**str**](.md)|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 

### Return type

[**Tenant**](Tenant.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_by_api_key**
> Tenant get_tenant_by_api_key(api_key=api_key)

Retrieve a tenant by its API key



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
api_instance = killbill.TenantApi(killbill.ApiClient(configuration))
api_key = 'api_key_example' # str |  (optional)

try:
    # Retrieve a tenant by its API key
    api_response = api_instance.get_tenant_by_api_key(api_key=api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantApi->get_tenant_by_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | [optional] 

### Return type

[**Tenant**](Tenant.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_key_value**
> TenantKeyValue get_user_key_value(key_name, x_killbill_api_key, x_killbill_api_secret)

Retrieve a per tenant user key/value



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
api_instance = killbill.TenantApi(killbill.ApiClient(configuration))
key_name = 'key_name_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 

try:
    # Retrieve a per tenant user key/value
    api_response = api_instance.get_user_key_value(key_name, x_killbill_api_key, x_killbill_api_secret)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantApi->get_user_key_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_name** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 

### Return type

[**TenantKeyValue**](TenantKeyValue.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_user_key_value**
> TenantKeyValue insert_user_key_value(key_name, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Add a per tenant user key/value



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
api_instance = killbill.TenantApi(killbill.ApiClient(configuration))
key_name = 'key_name_example' # str | 
body = 'body_example' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Add a per tenant user key/value
    api_response = api_instance.insert_user_key_value(key_name, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantApi->insert_user_key_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_name** | **str**|  | 
 **body** | **str**|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **x_killbill_reason** | **str**|  | [optional] 
 **x_killbill_comment** | **str**|  | [optional] 

### Return type

[**TenantKeyValue**](TenantKeyValue.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_push_notification_callback**
> TenantKeyValue register_push_notification_callback(x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, cb=cb, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Create a push notification



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
api_instance = killbill.TenantApi(killbill.ApiClient(configuration))
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
cb = 'cb_example' # str |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Create a push notification
    api_response = api_instance.register_push_notification_callback(x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, cb=cb, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantApi->register_push_notification_callback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **cb** | **str**|  | [optional] 
 **x_killbill_reason** | **str**|  | [optional] 
 **x_killbill_comment** | **str**|  | [optional] 

### Return type

[**TenantKeyValue**](TenantKeyValue.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_per_tenant_configuration**
> TenantKeyValue upload_per_tenant_configuration(body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Add a per tenant configuration (system properties)



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
api_instance = killbill.TenantApi(killbill.ApiClient(configuration))
body = 'body_example' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Add a per tenant configuration (system properties)
    api_response = api_instance.upload_per_tenant_configuration(body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantApi->upload_per_tenant_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **x_killbill_reason** | **str**|  | [optional] 
 **x_killbill_comment** | **str**|  | [optional] 

### Return type

[**TenantKeyValue**](TenantKeyValue.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_plugin_configuration**
> TenantKeyValue upload_plugin_configuration(plugin_name, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Add a per tenant configuration for a plugin



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
api_instance = killbill.TenantApi(killbill.ApiClient(configuration))
plugin_name = 'plugin_name_example' # str | 
body = 'body_example' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Add a per tenant configuration for a plugin
    api_response = api_instance.upload_plugin_configuration(plugin_name, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantApi->upload_plugin_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_name** | **str**|  | 
 **body** | **str**|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **x_killbill_reason** | **str**|  | [optional] 
 **x_killbill_comment** | **str**|  | [optional] 

### Return type

[**TenantKeyValue**](TenantKeyValue.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_plugin_payment_state_machine_config**
> TenantKeyValue upload_plugin_payment_state_machine_config(plugin_name, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Add a per tenant payment state machine for a plugin



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
api_instance = killbill.TenantApi(killbill.ApiClient(configuration))
plugin_name = 'plugin_name_example' # str | 
body = 'body_example' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Add a per tenant payment state machine for a plugin
    api_response = api_instance.upload_plugin_payment_state_machine_config(plugin_name, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantApi->upload_plugin_payment_state_machine_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_name** | **str**|  | 
 **body** | **str**|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **x_killbill_reason** | **str**|  | [optional] 
 **x_killbill_comment** | **str**|  | [optional] 

### Return type

[**TenantKeyValue**](TenantKeyValue.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

