# killbill.SecurityApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_role_definition**](SecurityApi.md#add_role_definition) | **POST** /1.0/kb/security/roles | Add a new role definition)
[**add_user_roles**](SecurityApi.md#add_user_roles) | **POST** /1.0/kb/security/users | Add a new user with roles (to make api requests)
[**get_current_user_permissions**](SecurityApi.md#get_current_user_permissions) | **GET** /1.0/kb/security/permissions | List user permissions
[**get_current_user_subject**](SecurityApi.md#get_current_user_subject) | **GET** /1.0/kb/security/subject | Get user information
[**get_user_roles**](SecurityApi.md#get_user_roles) | **GET** /1.0/kb/security/users/{username}/roles | Get roles associated to a user
[**invalidate_user**](SecurityApi.md#invalidate_user) | **DELETE** /1.0/kb/security/users/{username} | Invalidate an existing user
[**update_role_definition**](SecurityApi.md#update_role_definition) | **PUT** /1.0/kb/security/roles | Update a new role definition)
[**update_user_password**](SecurityApi.md#update_user_password) | **PUT** /1.0/kb/security/users/{username}/password | Update a user password
[**update_user_roles**](SecurityApi.md#update_user_roles) | **PUT** /1.0/kb/security/users/{username}/roles | Update roles associated to a user


# **add_role_definition**
> add_role_definition(body, x_killbill_created_by, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Add a new role definition)



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
api_instance = killbill.SecurityApi(killbill.ApiClient(configuration))
body = killbill.RoleDefinition() # RoleDefinition | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Add a new role definition)
    api_instance.add_role_definition(body, x_killbill_created_by, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling SecurityApi->add_role_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoleDefinition**](RoleDefinition.md)|  | 
 **x_killbill_created_by** | **str**|  | 
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

# **add_user_roles**
> add_user_roles(body, x_killbill_created_by, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Add a new user with roles (to make api requests)



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
api_instance = killbill.SecurityApi(killbill.ApiClient(configuration))
body = killbill.UserRoles() # UserRoles | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Add a new user with roles (to make api requests)
    api_instance.add_user_roles(body, x_killbill_created_by, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling SecurityApi->add_user_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserRoles**](UserRoles.md)|  | 
 **x_killbill_created_by** | **str**|  | 
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

# **get_current_user_permissions**
> list[str] get_current_user_permissions()

List user permissions



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
api_instance = killbill.SecurityApi(killbill.ApiClient(configuration))

try:
    # List user permissions
    api_response = api_instance.get_current_user_permissions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->get_current_user_permissions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user_subject**
> Subject get_current_user_subject()

Get user information



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
api_instance = killbill.SecurityApi(killbill.ApiClient(configuration))

try:
    # Get user information
    api_response = api_instance.get_current_user_subject()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->get_current_user_subject: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Subject**](Subject.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_roles**
> UserRoles get_user_roles(username)

Get roles associated to a user



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
api_instance = killbill.SecurityApi(killbill.ApiClient(configuration))
username = 'username_example' # str | 

try:
    # Get roles associated to a user
    api_response = api_instance.get_user_roles(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->get_user_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

### Return type

[**UserRoles**](UserRoles.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invalidate_user**
> invalidate_user(username, x_killbill_created_by, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Invalidate an existing user



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
api_instance = killbill.SecurityApi(killbill.ApiClient(configuration))
username = 'username_example' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Invalidate an existing user
    api_instance.invalidate_user(username, x_killbill_created_by, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling SecurityApi->invalidate_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **x_killbill_created_by** | **str**|  | 
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

# **update_role_definition**
> update_role_definition(body, x_killbill_created_by, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Update a new role definition)



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
api_instance = killbill.SecurityApi(killbill.ApiClient(configuration))
body = killbill.RoleDefinition() # RoleDefinition | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Update a new role definition)
    api_instance.update_role_definition(body, x_killbill_created_by, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling SecurityApi->update_role_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoleDefinition**](RoleDefinition.md)|  | 
 **x_killbill_created_by** | **str**|  | 
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

# **update_user_password**
> update_user_password(username, body, x_killbill_created_by, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Update a user password



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
api_instance = killbill.SecurityApi(killbill.ApiClient(configuration))
username = 'username_example' # str | 
body = killbill.UserRoles() # UserRoles | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Update a user password
    api_instance.update_user_password(username, body, x_killbill_created_by, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling SecurityApi->update_user_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **body** | [**UserRoles**](UserRoles.md)|  | 
 **x_killbill_created_by** | **str**|  | 
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

# **update_user_roles**
> update_user_roles(username, body, x_killbill_created_by, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Update roles associated to a user



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
api_instance = killbill.SecurityApi(killbill.ApiClient(configuration))
username = 'username_example' # str | 
body = killbill.UserRoles() # UserRoles | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Update roles associated to a user
    api_instance.update_user_roles(username, body, x_killbill_created_by, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling SecurityApi->update_user_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **body** | [**UserRoles**](UserRoles.md)|  | 
 **x_killbill_created_by** | **str**|  | 
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

