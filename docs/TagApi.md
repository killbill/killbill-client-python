# killbill.TagApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tags**](TagApi.md#get_tags) | **GET** /1.0/kb/tags/pagination | List tags
[**search_tags**](TagApi.md#search_tags) | **GET** /1.0/kb/tags/search/{searchKey} | Search tags


# **get_tags**
> list[Tag] get_tags(x_killbill_api_key, x_killbill_api_secret, offset=offset, limit=limit, audit=audit)

List tags



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
api_instance = killbill.TagApi(killbill.ApiClient(configuration))
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # List tags
    api_response = api_instance.get_tags(x_killbill_api_key, x_killbill_api_secret, offset=offset, limit=limit, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->get_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]
 **audit** | **str**|  | [optional] [default to NONE]

### Return type

[**list[Tag]**](Tag.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_tags**
> list[Tag] search_tags(search_key, x_killbill_api_key, x_killbill_api_secret, offset=offset, limit=limit, audit=audit)

Search tags



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
api_instance = killbill.TagApi(killbill.ApiClient(configuration))
search_key = 'search_key_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # Search tags
    api_response = api_instance.search_tags(search_key, x_killbill_api_key, x_killbill_api_secret, offset=offset, limit=limit, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->search_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_key** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]
 **audit** | **str**|  | [optional] [default to NONE]

### Return type

[**list[Tag]**](Tag.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

