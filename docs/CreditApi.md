# killbill.CreditApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_credit**](CreditApi.md#create_credit) | **POST** /1.0/kb/credits | Create a credit
[**get_credit**](CreditApi.md#get_credit) | **GET** /1.0/kb/credits/{creditId} | Retrieve a credit by id


# **create_credit**
> Credit create_credit(body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, auto_commit=auto_commit, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Create a credit



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
api_instance = killbill.CreditApi(killbill.ApiClient(configuration))
body = killbill.Credit() # Credit | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
auto_commit = false # bool |  (optional) (default to false)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Create a credit
    api_response = api_instance.create_credit(body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, auto_commit=auto_commit, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditApi->create_credit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Credit**](Credit.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **auto_commit** | **bool**|  | [optional] [default to false]
 **x_killbill_reason** | **str**|  | [optional] 
 **x_killbill_comment** | **str**|  | [optional] 

### Return type

[**Credit**](Credit.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit**
> Credit get_credit(credit_id, x_killbill_api_key, x_killbill_api_secret)

Retrieve a credit by id



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
api_instance = killbill.CreditApi(killbill.ApiClient(configuration))
credit_id = 'credit_id_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 

try:
    # Retrieve a credit by id
    api_response = api_instance.get_credit(credit_id, x_killbill_api_key, x_killbill_api_secret)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditApi->get_credit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_id** | [**str**](.md)|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 

### Return type

[**Credit**](Credit.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

