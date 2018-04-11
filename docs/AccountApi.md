# killbill.AccountApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_account_blocking_state**](AccountApi.md#add_account_blocking_state) | **PUT** /1.0/kb/accounts/{accountId}/block | Block an account
[**add_email**](AccountApi.md#add_email) | **POST** /1.0/kb/accounts/{accountId}/emails | Add account email
[**close_account**](AccountApi.md#close_account) | **DELETE** /1.0/kb/accounts/{accountId} | Close account
[**create_account**](AccountApi.md#create_account) | **POST** /1.0/kb/accounts | Create account
[**create_account_custom_fields**](AccountApi.md#create_account_custom_fields) | **POST** /1.0/kb/accounts/{accountId}/customFields | Add custom fields to account
[**create_account_tags**](AccountApi.md#create_account_tags) | **POST** /1.0/kb/accounts/{accountId}/tags | Add tags to account
[**create_payment_method**](AccountApi.md#create_payment_method) | **POST** /1.0/kb/accounts/{accountId}/paymentMethods | Add a payment method
[**delete_account_custom_fields**](AccountApi.md#delete_account_custom_fields) | **DELETE** /1.0/kb/accounts/{accountId}/customFields | Remove custom fields from account
[**delete_account_tags**](AccountApi.md#delete_account_tags) | **DELETE** /1.0/kb/accounts/{accountId}/tags | Remove tags from account
[**get_account**](AccountApi.md#get_account) | **GET** /1.0/kb/accounts/{accountId} | Retrieve an account by id
[**get_account_bundles**](AccountApi.md#get_account_bundles) | **GET** /1.0/kb/accounts/{accountId}/bundles | Retrieve bundles for account
[**get_account_by_key**](AccountApi.md#get_account_by_key) | **GET** /1.0/kb/accounts | Retrieve an account by external key
[**get_account_custom_fields**](AccountApi.md#get_account_custom_fields) | **GET** /1.0/kb/accounts/{accountId}/customFields | Retrieve account custom fields
[**get_account_tags**](AccountApi.md#get_account_tags) | **GET** /1.0/kb/accounts/{accountId}/tags | Retrieve account tags
[**get_account_timeline**](AccountApi.md#get_account_timeline) | **GET** /1.0/kb/accounts/{accountId}/timeline | Retrieve account timeline
[**get_accounts**](AccountApi.md#get_accounts) | **GET** /1.0/kb/accounts/pagination | List accounts
[**get_all_custom_fields**](AccountApi.md#get_all_custom_fields) | **GET** /1.0/kb/accounts/{accountId}/allCustomFields | Retrieve account customFields
[**get_all_tags**](AccountApi.md#get_all_tags) | **GET** /1.0/kb/accounts/{accountId}/allTags | Retrieve account tags
[**get_blocking_states**](AccountApi.md#get_blocking_states) | **GET** /1.0/kb/accounts/{accountId}/block | Retrieve blocking states for account
[**get_children_accounts**](AccountApi.md#get_children_accounts) | **GET** /1.0/kb/accounts/{accountId}/children | List children accounts
[**get_email_notifications_for_account**](AccountApi.md#get_email_notifications_for_account) | **GET** /1.0/kb/accounts/{accountId}/emailNotifications | Retrieve account email notification
[**get_emails**](AccountApi.md#get_emails) | **GET** /1.0/kb/accounts/{accountId}/emails | Retrieve an account emails
[**get_invoice_payments**](AccountApi.md#get_invoice_payments) | **GET** /1.0/kb/accounts/{accountId}/invoicePayments | Retrieve account invoice payments
[**get_invoices_for_account**](AccountApi.md#get_invoices_for_account) | **GET** /1.0/kb/accounts/{accountId}/invoices | Retrieve account invoices
[**get_overdue_account**](AccountApi.md#get_overdue_account) | **GET** /1.0/kb/accounts/{accountId}/overdue | Retrieve overdue state for account
[**get_payment_methods_for_account**](AccountApi.md#get_payment_methods_for_account) | **GET** /1.0/kb/accounts/{accountId}/paymentMethods | Retrieve account payment methods
[**get_payments_for_account**](AccountApi.md#get_payments_for_account) | **GET** /1.0/kb/accounts/{accountId}/payments | Retrieve account payments
[**modify_account_custom_fields**](AccountApi.md#modify_account_custom_fields) | **PUT** /1.0/kb/accounts/{accountId}/customFields | Modify custom fields to account
[**pay_all_invoices**](AccountApi.md#pay_all_invoices) | **POST** /1.0/kb/accounts/{accountId}/invoicePayments | Trigger a payment for all unpaid invoices
[**process_payment**](AccountApi.md#process_payment) | **POST** /1.0/kb/accounts/{accountId}/payments | Trigger a payment (authorization, purchase or credit)
[**process_payment_by_external_key**](AccountApi.md#process_payment_by_external_key) | **POST** /1.0/kb/accounts/payments | Trigger a payment using the account external key (authorization, purchase or credit)
[**rebalance_existing_cba_on_account**](AccountApi.md#rebalance_existing_cba_on_account) | **PUT** /1.0/kb/accounts/{accountId}/cbaRebalancing | Rebalance account CBA
[**refresh_payment_methods**](AccountApi.md#refresh_payment_methods) | **PUT** /1.0/kb/accounts/{accountId}/paymentMethods/refresh | Refresh account payment methods
[**remove_email**](AccountApi.md#remove_email) | **DELETE** /1.0/kb/accounts/{accountId}/emails/{email} | Delete email from account
[**search_accounts**](AccountApi.md#search_accounts) | **GET** /1.0/kb/accounts/search/{searchKey} | Search accounts
[**set_default_payment_method**](AccountApi.md#set_default_payment_method) | **PUT** /1.0/kb/accounts/{accountId}/paymentMethods/{paymentMethodId}/setDefault | Set the default payment method
[**set_email_notifications_for_account**](AccountApi.md#set_email_notifications_for_account) | **PUT** /1.0/kb/accounts/{accountId}/emailNotifications | Set account email notification
[**transfer_child_credit_to_parent**](AccountApi.md#transfer_child_credit_to_parent) | **PUT** /1.0/kb/accounts/{childAccountId}/transferCredit | Move a given child credit to the parent level
[**update_account**](AccountApi.md#update_account) | **PUT** /1.0/kb/accounts/{accountId} | Update account


# **add_account_blocking_state**
> add_account_blocking_state(account_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, requested_date=requested_date, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Block an account



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
api_instance = killbill.AccountApi(killbill.ApiClient(configuration))
account_id = 'account_id_example' # str | 
body = killbill.BlockingState() # BlockingState | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
requested_date = '2013-10-20' # date |  (optional)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Block an account
    api_instance.add_account_blocking_state(account_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, requested_date=requested_date, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling AccountApi->add_account_blocking_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)|  | 
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

# **add_email**
> list[AccountEmail] add_email(account_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Add account email



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
api_instance = killbill.AccountApi(killbill.ApiClient(configuration))
account_id = 'account_id_example' # str | 
body = killbill.AccountEmail() # AccountEmail | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Add account email
    api_response = api_instance.add_email(account_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->add_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)|  | 
 **body** | [**AccountEmail**](AccountEmail.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **x_killbill_reason** | **str**|  | [optional] 
 **x_killbill_comment** | **str**|  | [optional] 

### Return type

[**list[AccountEmail]**](AccountEmail.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **close_account**
> close_account(account_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, cancel_all_subscriptions=cancel_all_subscriptions, write_off_unpaid_invoices=write_off_unpaid_invoices, item_adjust_unpaid_invoices=item_adjust_unpaid_invoices, remove_future_notifications=remove_future_notifications, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Close account



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
api_instance = killbill.AccountApi(killbill.ApiClient(configuration))
account_id = 'account_id_example' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
cancel_all_subscriptions = false # bool |  (optional) (default to false)
write_off_unpaid_invoices = false # bool |  (optional) (default to false)
item_adjust_unpaid_invoices = false # bool |  (optional) (default to false)
remove_future_notifications = true # bool |  (optional) (default to true)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Close account
    api_instance.close_account(account_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, cancel_all_subscriptions=cancel_all_subscriptions, write_off_unpaid_invoices=write_off_unpaid_invoices, item_adjust_unpaid_invoices=item_adjust_unpaid_invoices, remove_future_notifications=remove_future_notifications, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling AccountApi->close_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **cancel_all_subscriptions** | **bool**|  | [optional] [default to false]
 **write_off_unpaid_invoices** | **bool**|  | [optional] [default to false]
 **item_adjust_unpaid_invoices** | **bool**|  | [optional] [default to false]
 **remove_future_notifications** | **bool**|  | [optional] [default to true]
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

# **create_account**
> Account create_account(body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Create account



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
api_instance = killbill.AccountApi(killbill.ApiClient(configuration))
body = killbill.Account() # Account | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Create account
    api_response = api_instance.create_account(body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->create_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Account**](Account.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **x_killbill_reason** | **str**|  | [optional] 
 **x_killbill_comment** | **str**|  | [optional] 

### Return type

[**Account**](Account.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_account_custom_fields**
> list[CustomField] create_account_custom_fields(account_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Add custom fields to account



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
api_instance = killbill.AccountApi(killbill.ApiClient(configuration))
account_id = 'account_id_example' # str | 
body = [killbill.CustomField()] # list[CustomField] | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Add custom fields to account
    api_response = api_instance.create_account_custom_fields(account_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->create_account_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)|  | 
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

# **create_account_tags**
> list[Tag] create_account_tags(account_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, tag_def=tag_def, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Add tags to account



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
api_instance = killbill.AccountApi(killbill.ApiClient(configuration))
account_id = 'account_id_example' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
tag_def = ['tag_def_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Add tags to account
    api_response = api_instance.create_account_tags(account_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, tag_def=tag_def, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->create_account_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)|  | 
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_payment_method**
> PaymentMethod create_payment_method(account_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, is_default=is_default, pay_all_unpaid_invoices=pay_all_unpaid_invoices, control_plugin_name=control_plugin_name, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Add a payment method



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
api_instance = killbill.AccountApi(killbill.ApiClient(configuration))
account_id = 'account_id_example' # str | 
body = killbill.PaymentMethod() # PaymentMethod | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
is_default = false # bool |  (optional) (default to false)
pay_all_unpaid_invoices = false # bool |  (optional) (default to false)
control_plugin_name = ['control_plugin_name_example'] # list[str] |  (optional)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Add a payment method
    api_response = api_instance.create_payment_method(account_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, is_default=is_default, pay_all_unpaid_invoices=pay_all_unpaid_invoices, control_plugin_name=control_plugin_name, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->create_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)|  | 
 **body** | [**PaymentMethod**](PaymentMethod.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **is_default** | **bool**|  | [optional] [default to false]
 **pay_all_unpaid_invoices** | **bool**|  | [optional] [default to false]
 **control_plugin_name** | [**list[str]**](str.md)|  | [optional] 
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 
 **x_killbill_reason** | **str**|  | [optional] 
 **x_killbill_comment** | **str**|  | [optional] 

### Return type

[**PaymentMethod**](PaymentMethod.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account_custom_fields**
> delete_account_custom_fields(account_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, custom_field=custom_field, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Remove custom fields from account



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
api_instance = killbill.AccountApi(killbill.ApiClient(configuration))
account_id = 'account_id_example' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
custom_field = ['custom_field_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Remove custom fields from account
    api_instance.delete_account_custom_fields(account_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, custom_field=custom_field, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling AccountApi->delete_account_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)|  | 
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

# **delete_account_tags**
> delete_account_tags(account_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, tag_def=tag_def, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Remove tags from account



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
api_instance = killbill.AccountApi(killbill.ApiClient(configuration))
account_id = 'account_id_example' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
tag_def = ['tag_def_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Remove tags from account
    api_instance.delete_account_tags(account_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, tag_def=tag_def, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling AccountApi->delete_account_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)|  | 
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

# **get_account**
> Account get_account(account_id, x_killbill_api_key, x_killbill_api_secret, account_with_balance=account_with_balance, account_with_balance_and_cba=account_with_balance_and_cba, audit=audit)

Retrieve an account by id



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
api_instance = killbill.AccountApi(killbill.ApiClient(configuration))
account_id = 'account_id_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
account_with_balance = false # bool |  (optional) (default to false)
account_with_balance_and_cba = false # bool |  (optional) (default to false)
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # Retrieve an account by id
    api_response = api_instance.get_account(account_id, x_killbill_api_key, x_killbill_api_secret, account_with_balance=account_with_balance, account_with_balance_and_cba=account_with_balance_and_cba, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **account_with_balance** | **bool**|  | [optional] [default to false]
 **account_with_balance_and_cba** | **bool**|  | [optional] [default to false]
 **audit** | **str**|  | [optional] [default to NONE]

### Return type

[**Account**](Account.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_bundles**
> list[Bundle] get_account_bundles(account_id, x_killbill_api_key, x_killbill_api_secret, external_key=external_key, bundles_filter=bundles_filter, audit=audit)

Retrieve bundles for account



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
api_instance = killbill.AccountApi(killbill.ApiClient(configuration))
account_id = 'account_id_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
external_key = 'external_key_example' # str |  (optional)
bundles_filter = 'bundles_filter_example' # str |  (optional)
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # Retrieve bundles for account
    api_response = api_instance.get_account_bundles(account_id, x_killbill_api_key, x_killbill_api_secret, external_key=external_key, bundles_filter=bundles_filter, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_account_bundles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **external_key** | **str**|  | [optional] 
 **bundles_filter** | **str**|  | [optional] 
 **audit** | **str**|  | [optional] [default to NONE]

### Return type

[**list[Bundle]**](Bundle.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_by_key**
> Account get_account_by_key(external_key, x_killbill_api_key, x_killbill_api_secret, account_with_balance=account_with_balance, account_with_balance_and_cba=account_with_balance_and_cba, audit=audit)

Retrieve an account by external key



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
api_instance = killbill.AccountApi(killbill.ApiClient(configuration))
external_key = 'external_key_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
account_with_balance = false # bool |  (optional) (default to false)
account_with_balance_and_cba = false # bool |  (optional) (default to false)
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # Retrieve an account by external key
    api_response = api_instance.get_account_by_key(external_key, x_killbill_api_key, x_killbill_api_secret, account_with_balance=account_with_balance, account_with_balance_and_cba=account_with_balance_and_cba, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_account_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_key** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **account_with_balance** | **bool**|  | [optional] [default to false]
 **account_with_balance_and_cba** | **bool**|  | [optional] [default to false]
 **audit** | **str**|  | [optional] [default to NONE]

### Return type

[**Account**](Account.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_custom_fields**
> list[CustomField] get_account_custom_fields(account_id, x_killbill_api_key, x_killbill_api_secret, audit=audit)

Retrieve account custom fields



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
api_instance = killbill.AccountApi(killbill.ApiClient(configuration))
account_id = 'account_id_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # Retrieve account custom fields
    api_response = api_instance.get_account_custom_fields(account_id, x_killbill_api_key, x_killbill_api_secret, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_account_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)|  | 
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

# **get_account_tags**
> list[Tag] get_account_tags(account_id, x_killbill_api_key, x_killbill_api_secret, included_deleted=included_deleted, audit=audit)

Retrieve account tags



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
api_instance = killbill.AccountApi(killbill.ApiClient(configuration))
account_id = 'account_id_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
included_deleted = false # bool |  (optional) (default to false)
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # Retrieve account tags
    api_response = api_instance.get_account_tags(account_id, x_killbill_api_key, x_killbill_api_secret, included_deleted=included_deleted, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_account_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)|  | 
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

# **get_account_timeline**
> AccountTimeline get_account_timeline(account_id, x_killbill_api_key, x_killbill_api_secret, parallel=parallel, audit=audit)

Retrieve account timeline



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
api_instance = killbill.AccountApi(killbill.ApiClient(configuration))
account_id = 'account_id_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
parallel = false # bool |  (optional) (default to false)
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # Retrieve account timeline
    api_response = api_instance.get_account_timeline(account_id, x_killbill_api_key, x_killbill_api_secret, parallel=parallel, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_account_timeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **parallel** | **bool**|  | [optional] [default to false]
 **audit** | **str**|  | [optional] [default to NONE]

### Return type

[**AccountTimeline**](AccountTimeline.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts**
> list[Account] get_accounts(x_killbill_api_key, x_killbill_api_secret, offset=offset, limit=limit, account_with_balance=account_with_balance, account_with_balance_and_cba=account_with_balance_and_cba, audit=audit)

List accounts



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
api_instance = killbill.AccountApi(killbill.ApiClient(configuration))
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)
account_with_balance = false # bool |  (optional) (default to false)
account_with_balance_and_cba = false # bool |  (optional) (default to false)
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # List accounts
    api_response = api_instance.get_accounts(x_killbill_api_key, x_killbill_api_secret, offset=offset, limit=limit, account_with_balance=account_with_balance, account_with_balance_and_cba=account_with_balance_and_cba, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]
 **account_with_balance** | **bool**|  | [optional] [default to false]
 **account_with_balance_and_cba** | **bool**|  | [optional] [default to false]
 **audit** | **str**|  | [optional] [default to NONE]

### Return type

[**list[Account]**](Account.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_custom_fields**
> list[CustomField] get_all_custom_fields(account_id, x_killbill_api_key, x_killbill_api_secret, object_type=object_type, audit=audit)

Retrieve account customFields



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
api_instance = killbill.AccountApi(killbill.ApiClient(configuration))
account_id = 'account_id_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
object_type = 'object_type_example' # str |  (optional)
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # Retrieve account customFields
    api_response = api_instance.get_all_custom_fields(account_id, x_killbill_api_key, x_killbill_api_secret, object_type=object_type, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_all_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **object_type** | **str**|  | [optional] 
 **audit** | **str**|  | [optional] [default to NONE]

### Return type

[**list[CustomField]**](CustomField.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_tags**
> list[Tag] get_all_tags(account_id, x_killbill_api_key, x_killbill_api_secret, object_type=object_type, included_deleted=included_deleted, audit=audit)

Retrieve account tags



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
api_instance = killbill.AccountApi(killbill.ApiClient(configuration))
account_id = 'account_id_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
object_type = 'object_type_example' # str |  (optional)
included_deleted = false # bool |  (optional) (default to false)
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # Retrieve account tags
    api_response = api_instance.get_all_tags(account_id, x_killbill_api_key, x_killbill_api_secret, object_type=object_type, included_deleted=included_deleted, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_all_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **object_type** | **str**|  | [optional] 
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

# **get_blocking_states**
> list[BlockingState] get_blocking_states(account_id, x_killbill_api_key, x_killbill_api_secret, blocking_state_types=blocking_state_types, blocking_state_svcs=blocking_state_svcs, audit=audit)

Retrieve blocking states for account



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
api_instance = killbill.AccountApi(killbill.ApiClient(configuration))
account_id = 'account_id_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
blocking_state_types = ['blocking_state_types_example'] # list[str] |  (optional)
blocking_state_svcs = ['blocking_state_svcs_example'] # list[str] |  (optional)
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # Retrieve blocking states for account
    api_response = api_instance.get_blocking_states(account_id, x_killbill_api_key, x_killbill_api_secret, blocking_state_types=blocking_state_types, blocking_state_svcs=blocking_state_svcs, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_blocking_states: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **blocking_state_types** | [**list[str]**](str.md)|  | [optional] 
 **blocking_state_svcs** | [**list[str]**](str.md)|  | [optional] 
 **audit** | **str**|  | [optional] [default to NONE]

### Return type

[**list[BlockingState]**](BlockingState.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_children_accounts**
> list[Account] get_children_accounts(account_id, x_killbill_api_key, x_killbill_api_secret, account_with_balance=account_with_balance, account_with_balance_and_cba=account_with_balance_and_cba, audit=audit)

List children accounts



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
api_instance = killbill.AccountApi(killbill.ApiClient(configuration))
account_id = 'account_id_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
account_with_balance = false # bool |  (optional) (default to false)
account_with_balance_and_cba = false # bool |  (optional) (default to false)
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # List children accounts
    api_response = api_instance.get_children_accounts(account_id, x_killbill_api_key, x_killbill_api_secret, account_with_balance=account_with_balance, account_with_balance_and_cba=account_with_balance_and_cba, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_children_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **account_with_balance** | **bool**|  | [optional] [default to false]
 **account_with_balance_and_cba** | **bool**|  | [optional] [default to false]
 **audit** | **str**|  | [optional] [default to NONE]

### Return type

[**list[Account]**](Account.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_notifications_for_account**
> InvoiceEmail get_email_notifications_for_account(account_id, x_killbill_api_key, x_killbill_api_secret)

Retrieve account email notification



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
api_instance = killbill.AccountApi(killbill.ApiClient(configuration))
account_id = 'account_id_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 

try:
    # Retrieve account email notification
    api_response = api_instance.get_email_notifications_for_account(account_id, x_killbill_api_key, x_killbill_api_secret)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_email_notifications_for_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 

### Return type

[**InvoiceEmail**](InvoiceEmail.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_emails**
> list[AccountEmail] get_emails(account_id, x_killbill_api_key, x_killbill_api_secret)

Retrieve an account emails



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
api_instance = killbill.AccountApi(killbill.ApiClient(configuration))
account_id = 'account_id_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 

try:
    # Retrieve an account emails
    api_response = api_instance.get_emails(account_id, x_killbill_api_key, x_killbill_api_secret)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_emails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 

### Return type

[**list[AccountEmail]**](AccountEmail.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_payments**
> list[InvoicePayment] get_invoice_payments(account_id, x_killbill_api_key, x_killbill_api_secret, with_plugin_info=with_plugin_info, with_attempts=with_attempts, plugin_property=plugin_property, audit=audit)

Retrieve account invoice payments



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
api_instance = killbill.AccountApi(killbill.ApiClient(configuration))
account_id = 'account_id_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
with_plugin_info = false # bool |  (optional) (default to false)
with_attempts = false # bool |  (optional) (default to false)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # Retrieve account invoice payments
    api_response = api_instance.get_invoice_payments(account_id, x_killbill_api_key, x_killbill_api_secret, with_plugin_info=with_plugin_info, with_attempts=with_attempts, plugin_property=plugin_property, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_invoice_payments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **with_plugin_info** | **bool**|  | [optional] [default to false]
 **with_attempts** | **bool**|  | [optional] [default to false]
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 
 **audit** | **str**|  | [optional] [default to NONE]

### Return type

[**list[InvoicePayment]**](InvoicePayment.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices_for_account**
> list[Invoice] get_invoices_for_account(account_id, x_killbill_api_key, x_killbill_api_secret, with_items=with_items, with_migration_invoices=with_migration_invoices, unpaid_invoices_only=unpaid_invoices_only, include_voided_invoices=include_voided_invoices, audit=audit)

Retrieve account invoices



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
api_instance = killbill.AccountApi(killbill.ApiClient(configuration))
account_id = 'account_id_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
with_items = false # bool |  (optional) (default to false)
with_migration_invoices = false # bool |  (optional) (default to false)
unpaid_invoices_only = false # bool |  (optional) (default to false)
include_voided_invoices = false # bool |  (optional) (default to false)
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # Retrieve account invoices
    api_response = api_instance.get_invoices_for_account(account_id, x_killbill_api_key, x_killbill_api_secret, with_items=with_items, with_migration_invoices=with_migration_invoices, unpaid_invoices_only=unpaid_invoices_only, include_voided_invoices=include_voided_invoices, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_invoices_for_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **with_items** | **bool**|  | [optional] [default to false]
 **with_migration_invoices** | **bool**|  | [optional] [default to false]
 **unpaid_invoices_only** | **bool**|  | [optional] [default to false]
 **include_voided_invoices** | **bool**|  | [optional] [default to false]
 **audit** | **str**|  | [optional] [default to NONE]

### Return type

[**list[Invoice]**](Invoice.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_overdue_account**
> OverdueState get_overdue_account(account_id, x_killbill_api_key, x_killbill_api_secret)

Retrieve overdue state for account



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
api_instance = killbill.AccountApi(killbill.ApiClient(configuration))
account_id = 'account_id_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 

try:
    # Retrieve overdue state for account
    api_response = api_instance.get_overdue_account(account_id, x_killbill_api_key, x_killbill_api_secret)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_overdue_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 

### Return type

[**OverdueState**](OverdueState.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_methods_for_account**
> list[PaymentMethod] get_payment_methods_for_account(account_id, x_killbill_api_key, x_killbill_api_secret, with_plugin_info=with_plugin_info, included_deleted=included_deleted, plugin_property=plugin_property, audit=audit)

Retrieve account payment methods



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
api_instance = killbill.AccountApi(killbill.ApiClient(configuration))
account_id = 'account_id_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
with_plugin_info = false # bool |  (optional) (default to false)
included_deleted = false # bool |  (optional) (default to false)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # Retrieve account payment methods
    api_response = api_instance.get_payment_methods_for_account(account_id, x_killbill_api_key, x_killbill_api_secret, with_plugin_info=with_plugin_info, included_deleted=included_deleted, plugin_property=plugin_property, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_payment_methods_for_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **with_plugin_info** | **bool**|  | [optional] [default to false]
 **included_deleted** | **bool**|  | [optional] [default to false]
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

# **get_payments_for_account**
> list[Payment] get_payments_for_account(account_id, x_killbill_api_key, x_killbill_api_secret, with_attempts=with_attempts, with_plugin_info=with_plugin_info, plugin_property=plugin_property, audit=audit)

Retrieve account payments



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
api_instance = killbill.AccountApi(killbill.ApiClient(configuration))
account_id = 'account_id_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
with_attempts = false # bool |  (optional) (default to false)
with_plugin_info = false # bool |  (optional) (default to false)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # Retrieve account payments
    api_response = api_instance.get_payments_for_account(account_id, x_killbill_api_key, x_killbill_api_secret, with_attempts=with_attempts, with_plugin_info=with_plugin_info, plugin_property=plugin_property, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_payments_for_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **with_attempts** | **bool**|  | [optional] [default to false]
 **with_plugin_info** | **bool**|  | [optional] [default to false]
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

# **modify_account_custom_fields**
> modify_account_custom_fields(account_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Modify custom fields to account



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
api_instance = killbill.AccountApi(killbill.ApiClient(configuration))
account_id = 'account_id_example' # str | 
body = [killbill.CustomField()] # list[CustomField] | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Modify custom fields to account
    api_instance.modify_account_custom_fields(account_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling AccountApi->modify_account_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)|  | 
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

# **pay_all_invoices**
> pay_all_invoices(account_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, external_payment=external_payment, payment_amount=payment_amount, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Trigger a payment for all unpaid invoices



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
api_instance = killbill.AccountApi(killbill.ApiClient(configuration))
account_id = 'account_id_example' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
external_payment = false # bool |  (optional) (default to false)
payment_amount = 8.14 # float |  (optional)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Trigger a payment for all unpaid invoices
    api_instance.pay_all_invoices(account_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, external_payment=external_payment, payment_amount=payment_amount, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling AccountApi->pay_all_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **external_payment** | **bool**|  | [optional] [default to false]
 **payment_amount** | **float**|  | [optional] 
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

# **process_payment**
> Payment process_payment(account_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, payment_method_id=payment_method_id, control_plugin_name=control_plugin_name, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Trigger a payment (authorization, purchase or credit)



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
api_instance = killbill.AccountApi(killbill.ApiClient(configuration))
account_id = 'account_id_example' # str | 
body = killbill.PaymentTransaction() # PaymentTransaction | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
payment_method_id = 'payment_method_id_example' # str |  (optional)
control_plugin_name = ['control_plugin_name_example'] # list[str] |  (optional)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Trigger a payment (authorization, purchase or credit)
    api_response = api_instance.process_payment(account_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, payment_method_id=payment_method_id, control_plugin_name=control_plugin_name, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->process_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)|  | 
 **body** | [**PaymentTransaction**](PaymentTransaction.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **payment_method_id** | [**str**](.md)|  | [optional] 
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

# **process_payment_by_external_key**
> Payment process_payment_by_external_key(body, external_key, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, payment_method_id=payment_method_id, control_plugin_name=control_plugin_name, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Trigger a payment using the account external key (authorization, purchase or credit)



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
api_instance = killbill.AccountApi(killbill.ApiClient(configuration))
body = killbill.PaymentTransaction() # PaymentTransaction | 
external_key = 'external_key_example' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
payment_method_id = 'payment_method_id_example' # str |  (optional)
control_plugin_name = ['control_plugin_name_example'] # list[str] |  (optional)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Trigger a payment using the account external key (authorization, purchase or credit)
    api_response = api_instance.process_payment_by_external_key(body, external_key, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, payment_method_id=payment_method_id, control_plugin_name=control_plugin_name, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->process_payment_by_external_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PaymentTransaction**](PaymentTransaction.md)|  | 
 **external_key** | **str**|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **payment_method_id** | [**str**](.md)|  | [optional] 
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

# **rebalance_existing_cba_on_account**
> rebalance_existing_cba_on_account(account_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Rebalance account CBA



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
api_instance = killbill.AccountApi(killbill.ApiClient(configuration))
account_id = 'account_id_example' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Rebalance account CBA
    api_instance.rebalance_existing_cba_on_account(account_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling AccountApi->rebalance_existing_cba_on_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)|  | 
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

# **refresh_payment_methods**
> refresh_payment_methods(account_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, plugin_name=plugin_name, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Refresh account payment methods



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
api_instance = killbill.AccountApi(killbill.ApiClient(configuration))
account_id = 'account_id_example' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
plugin_name = 'plugin_name_example' # str |  (optional)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Refresh account payment methods
    api_instance.refresh_payment_methods(account_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, plugin_name=plugin_name, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling AccountApi->refresh_payment_methods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **plugin_name** | **str**|  | [optional] 
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

# **remove_email**
> remove_email(account_id, email, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Delete email from account



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
api_instance = killbill.AccountApi(killbill.ApiClient(configuration))
account_id = 'account_id_example' # str | 
email = 'email_example' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Delete email from account
    api_instance.remove_email(account_id, email, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling AccountApi->remove_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)|  | 
 **email** | **str**|  | 
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_accounts**
> list[Account] search_accounts(search_key, x_killbill_api_key, x_killbill_api_secret, offset=offset, limit=limit, account_with_balance=account_with_balance, account_with_balance_and_cba=account_with_balance_and_cba, audit=audit)

Search accounts



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
api_instance = killbill.AccountApi(killbill.ApiClient(configuration))
search_key = 'search_key_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)
account_with_balance = false # bool |  (optional) (default to false)
account_with_balance_and_cba = false # bool |  (optional) (default to false)
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # Search accounts
    api_response = api_instance.search_accounts(search_key, x_killbill_api_key, x_killbill_api_secret, offset=offset, limit=limit, account_with_balance=account_with_balance, account_with_balance_and_cba=account_with_balance_and_cba, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->search_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_key** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]
 **account_with_balance** | **bool**|  | [optional] [default to false]
 **account_with_balance_and_cba** | **bool**|  | [optional] [default to false]
 **audit** | **str**|  | [optional] [default to NONE]

### Return type

[**list[Account]**](Account.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_default_payment_method**
> set_default_payment_method(account_id, payment_method_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, pay_all_unpaid_invoices=pay_all_unpaid_invoices, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Set the default payment method



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
api_instance = killbill.AccountApi(killbill.ApiClient(configuration))
account_id = 'account_id_example' # str | 
payment_method_id = 'payment_method_id_example' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
pay_all_unpaid_invoices = false # bool |  (optional) (default to false)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Set the default payment method
    api_instance.set_default_payment_method(account_id, payment_method_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, pay_all_unpaid_invoices=pay_all_unpaid_invoices, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling AccountApi->set_default_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)|  | 
 **payment_method_id** | [**str**](.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **pay_all_unpaid_invoices** | **bool**|  | [optional] [default to false]
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

# **set_email_notifications_for_account**
> set_email_notifications_for_account(account_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Set account email notification



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
api_instance = killbill.AccountApi(killbill.ApiClient(configuration))
account_id = 'account_id_example' # str | 
body = killbill.InvoiceEmail() # InvoiceEmail | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Set account email notification
    api_instance.set_email_notifications_for_account(account_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling AccountApi->set_email_notifications_for_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)|  | 
 **body** | [**InvoiceEmail**](InvoiceEmail.md)|  | 
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

# **transfer_child_credit_to_parent**
> transfer_child_credit_to_parent(child_account_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Move a given child credit to the parent level



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
api_instance = killbill.AccountApi(killbill.ApiClient(configuration))
child_account_id = 'child_account_id_example' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Move a given child credit to the parent level
    api_instance.transfer_child_credit_to_parent(child_account_id, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling AccountApi->transfer_child_credit_to_parent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **child_account_id** | [**str**](.md)|  | 
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

# **update_account**
> update_account(account_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, treat_null_as_reset=treat_null_as_reset, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Update account



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
api_instance = killbill.AccountApi(killbill.ApiClient(configuration))
account_id = 'account_id_example' # str | 
body = killbill.Account() # Account | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
treat_null_as_reset = false # bool |  (optional) (default to false)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Update account
    api_instance.update_account(account_id, body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, treat_null_as_reset=treat_null_as_reset, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling AccountApi->update_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)|  | 
 **body** | [**Account**](Account.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **treat_null_as_reset** | **bool**|  | [optional] [default to false]
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

