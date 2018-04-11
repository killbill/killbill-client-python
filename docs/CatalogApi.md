# killbill.CatalogApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_simple_plan**](CatalogApi.md#add_simple_plan) | **POST** /1.0/kb/catalog/simplePlan | Add a simple plan entry in the current version of the catalog
[**delete_catalog**](CatalogApi.md#delete_catalog) | **DELETE** /1.0/kb/catalog | Delete all versions for a per tenant catalog
[**get_available_addons**](CatalogApi.md#get_available_addons) | **GET** /1.0/kb/catalog/availableAddons | Retrieve available add-ons for a given product
[**get_available_base_plans**](CatalogApi.md#get_available_base_plans) | **GET** /1.0/kb/catalog/availableBasePlans | Retrieve available base plans
[**get_catalog_json**](CatalogApi.md#get_catalog_json) | **GET** /1.0/kb/catalog | Retrieve the catalog as JSON
[**get_catalog_versions**](CatalogApi.md#get_catalog_versions) | **GET** /1.0/kb/catalog/versions | Retrieve a list of catalog versions
[**get_catalog_xml**](CatalogApi.md#get_catalog_xml) | **GET** /1.0/kb/catalog/xml | Retrieve the full catalog as XML
[**get_phase_for_subscription_and_date**](CatalogApi.md#get_phase_for_subscription_and_date) | **GET** /1.0/kb/catalog/phase | Retrieve phase for a given subscription and date
[**get_plan_for_subscription_and_date**](CatalogApi.md#get_plan_for_subscription_and_date) | **GET** /1.0/kb/catalog/plan | Retrieve plan for a given subscription and date
[**get_price_list_for_subscription_and_date**](CatalogApi.md#get_price_list_for_subscription_and_date) | **GET** /1.0/kb/catalog/priceList | Retrieve priceList for a given subscription and date
[**get_product_for_subscription_and_date**](CatalogApi.md#get_product_for_subscription_and_date) | **GET** /1.0/kb/catalog/product | Retrieve product for a given subscription and date
[**upload_catalog_xml**](CatalogApi.md#upload_catalog_xml) | **POST** /1.0/kb/catalog/xml | Upload the full catalog as XML


# **add_simple_plan**
> add_simple_plan(body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Add a simple plan entry in the current version of the catalog



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
api_instance = killbill.CatalogApi(killbill.ApiClient(configuration))
body = killbill.SimplePlan() # SimplePlan | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Add a simple plan entry in the current version of the catalog
    api_instance.add_simple_plan(body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling CatalogApi->add_simple_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SimplePlan**](SimplePlan.md)|  | 
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

# **delete_catalog**
> delete_catalog(x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Delete all versions for a per tenant catalog



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
api_instance = killbill.CatalogApi(killbill.ApiClient(configuration))
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Delete all versions for a per tenant catalog
    api_instance.delete_catalog(x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling CatalogApi->delete_catalog: %s\n" % e)
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

# **get_available_addons**
> list[PlanDetail] get_available_addons(x_killbill_api_key, x_killbill_api_secret, base_product_name=base_product_name, price_list_name=price_list_name)

Retrieve available add-ons for a given product



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
api_instance = killbill.CatalogApi(killbill.ApiClient(configuration))
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
base_product_name = 'base_product_name_example' # str |  (optional)
price_list_name = 'price_list_name_example' # str |  (optional)

try:
    # Retrieve available add-ons for a given product
    api_response = api_instance.get_available_addons(x_killbill_api_key, x_killbill_api_secret, base_product_name=base_product_name, price_list_name=price_list_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogApi->get_available_addons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **base_product_name** | **str**|  | [optional] 
 **price_list_name** | **str**|  | [optional] 

### Return type

[**list[PlanDetail]**](PlanDetail.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_base_plans**
> list[PlanDetail] get_available_base_plans(x_killbill_api_key, x_killbill_api_secret)

Retrieve available base plans



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
api_instance = killbill.CatalogApi(killbill.ApiClient(configuration))
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 

try:
    # Retrieve available base plans
    api_response = api_instance.get_available_base_plans(x_killbill_api_key, x_killbill_api_secret)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogApi->get_available_base_plans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 

### Return type

[**list[PlanDetail]**](PlanDetail.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_catalog_json**
> list[Catalog] get_catalog_json(x_killbill_api_key, x_killbill_api_secret, requested_date=requested_date)

Retrieve the catalog as JSON



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
api_instance = killbill.CatalogApi(killbill.ApiClient(configuration))
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
requested_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    # Retrieve the catalog as JSON
    api_response = api_instance.get_catalog_json(x_killbill_api_key, x_killbill_api_secret, requested_date=requested_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogApi->get_catalog_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **requested_date** | **datetime**|  | [optional] 

### Return type

[**list[Catalog]**](Catalog.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_catalog_versions**
> list[datetime] get_catalog_versions(x_killbill_api_key, x_killbill_api_secret)

Retrieve a list of catalog versions



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
api_instance = killbill.CatalogApi(killbill.ApiClient(configuration))
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 

try:
    # Retrieve a list of catalog versions
    api_response = api_instance.get_catalog_versions(x_killbill_api_key, x_killbill_api_secret)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogApi->get_catalog_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 

### Return type

**list[datetime]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_catalog_xml**
> str get_catalog_xml(x_killbill_api_key, x_killbill_api_secret, requested_date=requested_date)

Retrieve the full catalog as XML



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
api_instance = killbill.CatalogApi(killbill.ApiClient(configuration))
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
requested_date = '2013-10-20' # date |  (optional)

try:
    # Retrieve the full catalog as XML
    api_response = api_instance.get_catalog_xml(x_killbill_api_key, x_killbill_api_secret, requested_date=requested_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogApi->get_catalog_xml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **requested_date** | **date**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_phase_for_subscription_and_date**
> Phase get_phase_for_subscription_and_date(x_killbill_api_key, x_killbill_api_secret, subscription_id=subscription_id, requested_date=requested_date)

Retrieve phase for a given subscription and date



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
api_instance = killbill.CatalogApi(killbill.ApiClient(configuration))
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
subscription_id = 'subscription_id_example' # str |  (optional)
requested_date = '2013-10-20' # date |  (optional)

try:
    # Retrieve phase for a given subscription and date
    api_response = api_instance.get_phase_for_subscription_and_date(x_killbill_api_key, x_killbill_api_secret, subscription_id=subscription_id, requested_date=requested_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogApi->get_phase_for_subscription_and_date: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **subscription_id** | [**str**](.md)|  | [optional] 
 **requested_date** | **date**|  | [optional] 

### Return type

[**Phase**](Phase.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plan_for_subscription_and_date**
> Plan get_plan_for_subscription_and_date(x_killbill_api_key, x_killbill_api_secret, subscription_id=subscription_id, requested_date=requested_date)

Retrieve plan for a given subscription and date



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
api_instance = killbill.CatalogApi(killbill.ApiClient(configuration))
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
subscription_id = 'subscription_id_example' # str |  (optional)
requested_date = '2013-10-20' # date |  (optional)

try:
    # Retrieve plan for a given subscription and date
    api_response = api_instance.get_plan_for_subscription_and_date(x_killbill_api_key, x_killbill_api_secret, subscription_id=subscription_id, requested_date=requested_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogApi->get_plan_for_subscription_and_date: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **subscription_id** | [**str**](.md)|  | [optional] 
 **requested_date** | **date**|  | [optional] 

### Return type

[**Plan**](Plan.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_list_for_subscription_and_date**
> PriceList get_price_list_for_subscription_and_date(x_killbill_api_key, x_killbill_api_secret, subscription_id=subscription_id, requested_date=requested_date)

Retrieve priceList for a given subscription and date



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
api_instance = killbill.CatalogApi(killbill.ApiClient(configuration))
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
subscription_id = 'subscription_id_example' # str |  (optional)
requested_date = '2013-10-20' # date |  (optional)

try:
    # Retrieve priceList for a given subscription and date
    api_response = api_instance.get_price_list_for_subscription_and_date(x_killbill_api_key, x_killbill_api_secret, subscription_id=subscription_id, requested_date=requested_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogApi->get_price_list_for_subscription_and_date: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **subscription_id** | [**str**](.md)|  | [optional] 
 **requested_date** | **date**|  | [optional] 

### Return type

[**PriceList**](PriceList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_for_subscription_and_date**
> Product get_product_for_subscription_and_date(x_killbill_api_key, x_killbill_api_secret, subscription_id=subscription_id, requested_date=requested_date)

Retrieve product for a given subscription and date



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
api_instance = killbill.CatalogApi(killbill.ApiClient(configuration))
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
subscription_id = 'subscription_id_example' # str |  (optional)
requested_date = '2013-10-20' # date |  (optional)

try:
    # Retrieve product for a given subscription and date
    api_response = api_instance.get_product_for_subscription_and_date(x_killbill_api_key, x_killbill_api_secret, subscription_id=subscription_id, requested_date=requested_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogApi->get_product_for_subscription_and_date: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_killbill_api_key** | **str**|  | 
 **x_killbill_api_secret** | **str**|  | 
 **subscription_id** | [**str**](.md)|  | [optional] 
 **requested_date** | **date**|  | [optional] 

### Return type

[**Product**](Product.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_catalog_xml**
> upload_catalog_xml(body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Upload the full catalog as XML



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
api_instance = killbill.CatalogApi(killbill.ApiClient(configuration))
body = 'body_example' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_api_key = 'x_killbill_api_key_example' # str | 
x_killbill_api_secret = 'x_killbill_api_secret_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Upload the full catalog as XML
    api_instance.upload_catalog_xml(body, x_killbill_created_by, x_killbill_api_key, x_killbill_api_secret, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling CatalogApi->upload_catalog_xml: %s\n" % e)
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

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

