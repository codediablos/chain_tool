# 

### Overview
EVM chain tool

#### Source code
https://github.com/codediablos/chain_tool/

### Quick start
#### Prerequisites

`python version：>=3.9`

#### Step 1: register an account on OKX and apply for an API key
- Register for an account: https://www.okx.com/account/register
- Apply for an API key: https://www.okx.com/account/users/myApi

#### Step 2: install requirements

```python
pip install -r /path/to/requirements.txt
```

#### Step 3: Setup Env

- copy .env.dev to .env
```python
cp .env.dev .env
```

- Fill in API credentials
```python
API_KEY = replace_your_key_here
SECRET_KEY = replace_your_secret_here
PASSPHRASE = replace_your_passphrase_here
EVM_PRIVATE_KEY = replace_your_private_key
```

- you can use addr_generator.py if you don't have EVM address
```python
python addr_generator.py
```

#### Step 4: Add address list

- add address to addr_list.txt
