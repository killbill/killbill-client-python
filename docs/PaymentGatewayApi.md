# killbill.PaymentGatewayApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**build_combo_form_descriptor**](PaymentGatewayApi.md#build_combo_form_descriptor) | **POST** /1.0/kb/paymentGateways/hosted/form | Combo API to generate form data to redirect the customer to the gateway
[**build_form_descriptor**](PaymentGatewayApi.md#build_form_descriptor) | **POST** /1.0/kb/paymentGateways/hosted/form/{accountId} | Generate form data to redirect the customer to the gateway
[**process_notification**](PaymentGatewayApi.md#process_notification) | **POST** /1.0/kb/paymentGateways/notification/{pluginName} | Process a gateway notification


# **build_combo_form_descriptor**
> HostedPaymentPageFormDescriptor build_combo_form_descriptor(body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, control_plugin_name=control_plugin_name, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Combo API to generate form data to redirect the customer to the gateway



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
api_instance = killbill.PaymentGatewayApi(killbill.ApiClient(configuration))
body = killbill.ComboHostedPaymentPage() # ComboHostedPaymentPage | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
control_plugin_name = ['control_plugin_name_example'] # list[str] |  (optional)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Combo API to generate form data to redirect the customer to the gateway
    api_response = api_instance.build_combo_form_descriptor(body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, control_plugin_name=control_plugin_name, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentGatewayApi->build_combo_form_descriptor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComboHostedPaymentPage**](ComboHostedPaymentPage.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **control_plugin_name** | [**list[str]**](str.md)|  | [optional] 
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 
 **x_killbill_reason** | **str**|  | [optional] 
 **x_killbill_comment** | **str**|  | [optional] 

### Return type

[**HostedPaymentPageFormDescriptor**](HostedPaymentPageFormDescriptor.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **build_form_descriptor**
> HostedPaymentPageFormDescriptor build_form_descriptor(account_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, payment_method_id=payment_method_id, control_plugin_name=control_plugin_name, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Generate form data to redirect the customer to the gateway



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
api_instance = killbill.PaymentGatewayApi(killbill.ApiClient(configuration))
account_id = 'account_id_example' # str | 
body = killbill.HostedPaymentPageFields() # HostedPaymentPageFields | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
payment_method_id = 'payment_method_id_example' # str |  (optional)
control_plugin_name = ['control_plugin_name_example'] # list[str] |  (optional)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Generate form data to redirect the customer to the gateway
    api_response = api_instance.build_form_descriptor(account_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, payment_method_id=payment_method_id, control_plugin_name=control_plugin_name, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentGatewayApi->build_form_descriptor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)|  | 
 **body** | [**HostedPaymentPageFields**](HostedPaymentPageFields.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **payment_method_id** | [**str**](.md)|  | [optional] 
 **control_plugin_name** | [**list[str]**](str.md)|  | [optional] 
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 
 **x_killbill_reason** | **str**|  | [optional] 
 **x_killbill_comment** | **str**|  | [optional] 

### Return type

[**HostedPaymentPageFormDescriptor**](HostedPaymentPageFormDescriptor.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_notification**
> process_notification(plugin_name, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, control_plugin_name=control_plugin_name, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Process a gateway notification

The response is built by the appropriate plugin

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
api_instance = killbill.PaymentGatewayApi(killbill.ApiClient(configuration))
plugin_name = 'plugin_name_example' # str | 
body = 'body_example' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
control_plugin_name = ['control_plugin_name_example'] # list[str] |  (optional)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Process a gateway notification
    api_instance.process_notification(plugin_name, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, control_plugin_name=control_plugin_name, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling PaymentGatewayApi->process_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_name** | **str**|  | 
 **body** | **str**|  | 
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

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

