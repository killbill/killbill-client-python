# killbill.PluginInfoApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_plugins_info**](PluginInfoApi.md#get_plugins_info) | **GET** /1.0/kb/pluginsInfo | Retrieve the list of registered plugins


# **get_plugins_info**
> list[PluginInfo] get_plugins_info(x_killbill_api_key, x_killbill_api_secret)

Retrieve the list of registered plugins



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
api_instance = killbill.PluginInfoApi(killbill.ApiClient(configuration))
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 

try:
    # Retrieve the list of registered plugins
    api_response = api_instance.get_plugins_info(x_killbill_api_key, x_killbill_api_secret)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginInfoApi->get_plugins_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 

### Return type

[**list[PluginInfo]**](PluginInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

