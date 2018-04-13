# killbill
Kill Bill is an open-source billing and payments platform

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import killbill 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import killbill
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import killbill
from killbill.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
killbill.configuration.username = 'YOUR_USERNAME'
killbill.configuration.password = 'YOUR_PASSWORD'
# create an instance of the API class
api_instance = killbill.AccountApi()
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

## How to generate using [Killbill Swagger Codegen](https://github.com/killbill/killbill-swagger-coden)

First install Killbill Swagger Codegen
```sh
git clone https://github.com/killbill/killbill-swagger-coden.git
cd killbill-swagger-coden
mvn package
```

Then to generate the client enter the following:
```sh
java -jar swagger-codegen-cli.jar generate \
--invoker-package="client" \
--api-package="api" \
--model-package="models" \
--http-user-agent="killbill/python-client" \
--lang=python \
-i kbswagger.yaml \
-t src/main/resources/killbill-python \
-o ../killbill-client-python -DpackageName=killbill
```
Note: If you don't want to generate the API docs and `git_push.hs` file just create a file named `.swagger-codegen-ignore` in the output directory.
with the following:
```
docs/*.md
git_push.sh
```
[Reff: How to skip certain files during code generation?](https://github.com/swagger-api/swagger-codegen/wiki/FAQ#how-to-skip-certain-files-during-code-generation)
