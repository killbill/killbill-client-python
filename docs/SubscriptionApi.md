# killbill.SubscriptionApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_subscription_blocking_state**](SubscriptionApi.md#add_subscription_blocking_state) | **PUT** /1.0/kb/subscriptions/{subscriptionId}/block | Block a subscription
[**cancel_subscription_plan**](SubscriptionApi.md#cancel_subscription_plan) | **DELETE** /1.0/kb/subscriptions/{subscriptionId} | Cancel an entitlement plan
[**change_subscription_plan**](SubscriptionApi.md#change_subscription_plan) | **PUT** /1.0/kb/subscriptions/{subscriptionId} | Change entitlement plan
[**create_subscription**](SubscriptionApi.md#create_subscription) | **POST** /1.0/kb/subscriptions | Create an subscription
[**create_subscription_custom_fields**](SubscriptionApi.md#create_subscription_custom_fields) | **POST** /1.0/kb/subscriptions/{subscriptionId}/customFields | Add custom fields to subscription
[**create_subscription_tags**](SubscriptionApi.md#create_subscription_tags) | **POST** /1.0/kb/subscriptions/{subscriptionId}/tags | Add tags to subscription
[**create_subscription_with_add_ons**](SubscriptionApi.md#create_subscription_with_add_ons) | **POST** /1.0/kb/subscriptions/createSubscriptionWithAddOns | Create an entitlement with addOn products
[**create_subscriptions_with_add_ons**](SubscriptionApi.md#create_subscriptions_with_add_ons) | **POST** /1.0/kb/subscriptions/createSubscriptionsWithAddOns | Create multiple entitlements with addOn products
[**delete_subscription_custom_fields**](SubscriptionApi.md#delete_subscription_custom_fields) | **DELETE** /1.0/kb/subscriptions/{subscriptionId}/customFields | Remove custom fields from subscription
[**delete_subscription_tags**](SubscriptionApi.md#delete_subscription_tags) | **DELETE** /1.0/kb/subscriptions/{subscriptionId}/tags | Remove tags from subscription
[**get_subscription**](SubscriptionApi.md#get_subscription) | **GET** /1.0/kb/subscriptions/{subscriptionId} | Retrieve a subscription by id
[**get_subscription_custom_fields**](SubscriptionApi.md#get_subscription_custom_fields) | **GET** /1.0/kb/subscriptions/{subscriptionId}/customFields | Retrieve subscription custom fields
[**get_subscription_tags**](SubscriptionApi.md#get_subscription_tags) | **GET** /1.0/kb/subscriptions/{subscriptionId}/tags | Retrieve subscription tags
[**modify_subscription_custom_fields**](SubscriptionApi.md#modify_subscription_custom_fields) | **PUT** /1.0/kb/subscriptions/{subscriptionId}/customFields | Modify custom fields to subscription
[**uncancel_subscription_plan**](SubscriptionApi.md#uncancel_subscription_plan) | **PUT** /1.0/kb/subscriptions/{subscriptionId}/uncancel | Un-cancel an entitlement
[**undo_change_subscription_plan**](SubscriptionApi.md#undo_change_subscription_plan) | **PUT** /1.0/kb/subscriptions/{subscriptionId}/undoChangePlan | Undo a pending change plan on an entitlement
[**update_subscription_bcd**](SubscriptionApi.md#update_subscription_bcd) | **PUT** /1.0/kb/subscriptions/{subscriptionId}/bcd | Update the BCD associated to a subscription


# **add_subscription_blocking_state**
> add_subscription_blocking_state(subscription_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, requested_date=requested_date, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Block a subscription



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
api_instance = killbill.SubscriptionApi(killbill.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
body = killbill.BlockingState() # BlockingState | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
requested_date = '2013-10-20' # date |  (optional)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Block a subscription
    api_instance.add_subscription_blocking_state(subscription_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, requested_date=requested_date, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling SubscriptionApi->add_subscription_blocking_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)|  | 
 **body** | [**BlockingState**](BlockingState.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **requested_date** | **date**|  | [optional] 
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 
 **x_killbill_reason** | **str**|  | [optional] 
 **x_killbill_comment** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_subscription_plan**
> cancel_subscription_plan(subscription_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, requested_date=requested_date, call_completion=call_completion, call_timeout_sec=call_timeout_sec, entitlement_policy=entitlement_policy, billing_policy=billing_policy, use_requested_date_for_billing=use_requested_date_for_billing, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Cancel an entitlement plan



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
api_instance = killbill.SubscriptionApi(killbill.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
requested_date = '2013-10-20' # date |  (optional)
call_completion = false # bool |  (optional) (default to false)
call_timeout_sec = 5 # int |  (optional) (default to 5)
entitlement_policy = 'entitlement_policy_example' # str |  (optional)
billing_policy = 'billing_policy_example' # str |  (optional)
use_requested_date_for_billing = false # bool |  (optional) (default to false)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Cancel an entitlement plan
    api_instance.cancel_subscription_plan(subscription_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, requested_date=requested_date, call_completion=call_completion, call_timeout_sec=call_timeout_sec, entitlement_policy=entitlement_policy, billing_policy=billing_policy, use_requested_date_for_billing=use_requested_date_for_billing, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling SubscriptionApi->cancel_subscription_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **requested_date** | **date**|  | [optional] 
 **call_completion** | **bool**|  | [optional] [default to false]
 **call_timeout_sec** | **int**|  | [optional] [default to 5]
 **entitlement_policy** | **str**|  | [optional] 
 **billing_policy** | **str**|  | [optional] 
 **use_requested_date_for_billing** | **bool**|  | [optional] [default to false]
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

# **change_subscription_plan**
> change_subscription_plan(subscription_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, requested_date=requested_date, call_completion=call_completion, call_timeout_sec=call_timeout_sec, billing_policy=billing_policy, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Change entitlement plan



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
api_instance = killbill.SubscriptionApi(killbill.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
body = killbill.Subscription() # Subscription | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
requested_date = '2013-10-20' # date |  (optional)
call_completion = false # bool |  (optional) (default to false)
call_timeout_sec = 3 # int |  (optional) (default to 3)
billing_policy = 'billing_policy_example' # str |  (optional)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Change entitlement plan
    api_instance.change_subscription_plan(subscription_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, requested_date=requested_date, call_completion=call_completion, call_timeout_sec=call_timeout_sec, billing_policy=billing_policy, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling SubscriptionApi->change_subscription_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)|  | 
 **body** | [**Subscription**](Subscription.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **requested_date** | **date**|  | [optional] 
 **call_completion** | **bool**|  | [optional] [default to false]
 **call_timeout_sec** | **int**|  | [optional] [default to 3]
 **billing_policy** | **str**|  | [optional] 
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

# **create_subscription**
> Subscription create_subscription(body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, entitlement_date=entitlement_date, billing_date=billing_date, rename_key_if_exists_and_unused=rename_key_if_exists_and_unused, migrated=migrated, bcd=bcd, call_completion=call_completion, call_timeout_sec=call_timeout_sec, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Create an subscription



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
api_instance = killbill.SubscriptionApi(killbill.ApiClient(configuration))
body = killbill.Subscription() # Subscription | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
entitlement_date = '2013-10-20' # date |  (optional)
billing_date = '2013-10-20' # date |  (optional)
rename_key_if_exists_and_unused = true # bool |  (optional) (default to true)
migrated = false # bool |  (optional) (default to false)
bcd = 56 # int |  (optional)
call_completion = false # bool |  (optional) (default to false)
call_timeout_sec = 3 # int |  (optional) (default to 3)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Create an subscription
    api_response = api_instance.create_subscription(body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, entitlement_date=entitlement_date, billing_date=billing_date, rename_key_if_exists_and_unused=rename_key_if_exists_and_unused, migrated=migrated, bcd=bcd, call_completion=call_completion, call_timeout_sec=call_timeout_sec, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->create_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Subscription**](Subscription.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **entitlement_date** | **date**|  | [optional] 
 **billing_date** | **date**|  | [optional] 
 **rename_key_if_exists_and_unused** | **bool**|  | [optional] [default to true]
 **migrated** | **bool**|  | [optional] [default to false]
 **bcd** | **int**|  | [optional] 
 **call_completion** | **bool**|  | [optional] [default to false]
 **call_timeout_sec** | **int**|  | [optional] [default to 3]
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 
 **x_killbill_reason** | **str**|  | [optional] 
 **x_killbill_comment** | **str**|  | [optional] 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subscription_custom_fields**
> create_subscription_custom_fields(subscription_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Add custom fields to subscription



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
api_instance = killbill.SubscriptionApi(killbill.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
body = [killbill.CustomField()] # list[CustomField] | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Add custom fields to subscription
    api_instance.create_subscription_custom_fields(subscription_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling SubscriptionApi->create_subscription_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)|  | 
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

# **create_subscription_tags**
> list[Tag] create_subscription_tags(subscription_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, tag_def=tag_def, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Add tags to subscription



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
api_instance = killbill.SubscriptionApi(killbill.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
tag_def = ['tag_def_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Add tags to subscription
    api_response = api_instance.create_subscription_tags(subscription_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, tag_def=tag_def, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->create_subscription_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)|  | 
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

# **create_subscription_with_add_ons**
> Bundle create_subscription_with_add_ons(body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, entitlement_date=entitlement_date, billing_date=billing_date, migrated=migrated, rename_key_if_exists_and_unused=rename_key_if_exists_and_unused, call_completion=call_completion, call_timeout_sec=call_timeout_sec, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Create an entitlement with addOn products



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
api_instance = killbill.SubscriptionApi(killbill.ApiClient(configuration))
body = [killbill.Subscription()] # list[Subscription] | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
entitlement_date = '2013-10-20' # date |  (optional)
billing_date = '2013-10-20' # date |  (optional)
migrated = false # bool |  (optional) (default to false)
rename_key_if_exists_and_unused = true # bool |  (optional) (default to true)
call_completion = false # bool |  (optional) (default to false)
call_timeout_sec = 3 # int |  (optional) (default to 3)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Create an entitlement with addOn products
    api_response = api_instance.create_subscription_with_add_ons(body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, entitlement_date=entitlement_date, billing_date=billing_date, migrated=migrated, rename_key_if_exists_and_unused=rename_key_if_exists_and_unused, call_completion=call_completion, call_timeout_sec=call_timeout_sec, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->create_subscription_with_add_ons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Subscription]**](Subscription.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **entitlement_date** | **date**|  | [optional] 
 **billing_date** | **date**|  | [optional] 
 **migrated** | **bool**|  | [optional] [default to false]
 **rename_key_if_exists_and_unused** | **bool**|  | [optional] [default to true]
 **call_completion** | **bool**|  | [optional] [default to false]
 **call_timeout_sec** | **int**|  | [optional] [default to 3]
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 
 **x_killbill_reason** | **str**|  | [optional] 
 **x_killbill_comment** | **str**|  | [optional] 

### Return type

[**Bundle**](Bundle.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subscriptions_with_add_ons**
> list[Bundle] create_subscriptions_with_add_ons(body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, entitlement_date=entitlement_date, billing_date=billing_date, rename_key_if_exists_and_unused=rename_key_if_exists_and_unused, migrated=migrated, call_completion=call_completion, call_timeout_sec=call_timeout_sec, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Create multiple entitlements with addOn products



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
api_instance = killbill.SubscriptionApi(killbill.ApiClient(configuration))
body = [killbill.BulkSubscriptionsBundle()] # list[BulkSubscriptionsBundle] | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
entitlement_date = '2013-10-20' # date |  (optional)
billing_date = '2013-10-20' # date |  (optional)
rename_key_if_exists_and_unused = true # bool |  (optional) (default to true)
migrated = false # bool |  (optional) (default to false)
call_completion = false # bool |  (optional) (default to false)
call_timeout_sec = 3 # int |  (optional) (default to 3)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Create multiple entitlements with addOn products
    api_response = api_instance.create_subscriptions_with_add_ons(body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, entitlement_date=entitlement_date, billing_date=billing_date, rename_key_if_exists_and_unused=rename_key_if_exists_and_unused, migrated=migrated, call_completion=call_completion, call_timeout_sec=call_timeout_sec, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->create_subscriptions_with_add_ons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[BulkSubscriptionsBundle]**](BulkSubscriptionsBundle.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **entitlement_date** | **date**|  | [optional] 
 **billing_date** | **date**|  | [optional] 
 **rename_key_if_exists_and_unused** | **bool**|  | [optional] [default to true]
 **migrated** | **bool**|  | [optional] [default to false]
 **call_completion** | **bool**|  | [optional] [default to false]
 **call_timeout_sec** | **int**|  | [optional] [default to 3]
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 
 **x_killbill_reason** | **str**|  | [optional] 
 **x_killbill_comment** | **str**|  | [optional] 

### Return type

[**list[Bundle]**](Bundle.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscription_custom_fields**
> delete_subscription_custom_fields(subscription_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, custom_field=custom_field, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Remove custom fields from subscription



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
api_instance = killbill.SubscriptionApi(killbill.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
custom_field = ['custom_field_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Remove custom fields from subscription
    api_instance.delete_subscription_custom_fields(subscription_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, custom_field=custom_field, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling SubscriptionApi->delete_subscription_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)|  | 
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

# **delete_subscription_tags**
> delete_subscription_tags(subscription_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, tag_def=tag_def, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Remove tags from subscription



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
api_instance = killbill.SubscriptionApi(killbill.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
tag_def = ['tag_def_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Remove tags from subscription
    api_instance.delete_subscription_tags(subscription_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, tag_def=tag_def, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling SubscriptionApi->delete_subscription_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)|  | 
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

# **get_subscription**
> Subscription get_subscription(subscription_id, x_killbill_api_key, x_killbill_api_secret, audit=audit)

Retrieve a subscription by id



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
api_instance = killbill.SubscriptionApi(killbill.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # Retrieve a subscription by id
    api_response = api_instance.get_subscription(subscription_id, x_killbill_api_key, x_killbill_api_secret, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->get_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **audit** | **str**|  | [optional] [default to NONE]

### Return type

[**Subscription**](Subscription.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_custom_fields**
> list[CustomField] get_subscription_custom_fields(subscription_id, x_killbill_api_key, x_killbill_api_secret, audit=audit)

Retrieve subscription custom fields



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
api_instance = killbill.SubscriptionApi(killbill.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # Retrieve subscription custom fields
    api_response = api_instance.get_subscription_custom_fields(subscription_id, x_killbill_api_key, x_killbill_api_secret, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->get_subscription_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)|  | 
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

# **get_subscription_tags**
> list[Tag] get_subscription_tags(subscription_id, x_killbill_api_key, x_killbill_api_secret, included_deleted=included_deleted, audit=audit)

Retrieve subscription tags



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
api_instance = killbill.SubscriptionApi(killbill.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
included_deleted = false # bool |  (optional) (default to false)
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # Retrieve subscription tags
    api_response = api_instance.get_subscription_tags(subscription_id, x_killbill_api_key, x_killbill_api_secret, included_deleted=included_deleted, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->get_subscription_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)|  | 
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

# **modify_subscription_custom_fields**
> modify_subscription_custom_fields(subscription_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Modify custom fields to subscription



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
api_instance = killbill.SubscriptionApi(killbill.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
body = [killbill.CustomField()] # list[CustomField] | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Modify custom fields to subscription
    api_instance.modify_subscription_custom_fields(subscription_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling SubscriptionApi->modify_subscription_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)|  | 
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

# **uncancel_subscription_plan**
> uncancel_subscription_plan(subscription_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Un-cancel an entitlement



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
api_instance = killbill.SubscriptionApi(killbill.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Un-cancel an entitlement
    api_instance.uncancel_subscription_plan(subscription_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling SubscriptionApi->uncancel_subscription_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
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

# **undo_change_subscription_plan**
> undo_change_subscription_plan(subscription_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Undo a pending change plan on an entitlement



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
api_instance = killbill.SubscriptionApi(killbill.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Undo a pending change plan on an entitlement
    api_instance.undo_change_subscription_plan(subscription_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling SubscriptionApi->undo_change_subscription_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
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

# **update_subscription_bcd**
> update_subscription_bcd(subscription_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, effective_from_date=effective_from_date, force_new_bcd_with_past_effective_date=force_new_bcd_with_past_effective_date, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Update the BCD associated to a subscription



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
api_instance = killbill.SubscriptionApi(killbill.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
body = killbill.Subscription() # Subscription | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
effective_from_date = '2013-10-20' # date |  (optional)
force_new_bcd_with_past_effective_date = false # bool |  (optional) (default to false)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Update the BCD associated to a subscription
    api_instance.update_subscription_bcd(subscription_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, effective_from_date=effective_from_date, force_new_bcd_with_past_effective_date=force_new_bcd_with_past_effective_date, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling SubscriptionApi->update_subscription_bcd: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)|  | 
 **body** | [**Subscription**](Subscription.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **effective_from_date** | **date**|  | [optional] 
 **force_new_bcd_with_past_effective_date** | **bool**|  | [optional] [default to false]
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

