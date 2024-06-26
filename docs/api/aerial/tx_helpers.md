<a id="kiipy.aerial.tx_helpers"></a>

# kiipy.aerial.tx`_`helpers

Transaction helpers.

<a id="kiipy.aerial.tx_helpers.MessageLog"></a>

## MessageLog Objects

```python
@dataclass
class MessageLog()
```

Message Log.

<a id="kiipy.aerial.tx_helpers.TxResponse"></a>

## TxResponse Objects

```python
@dataclass
class TxResponse()
```

Transaction response.

**Raises**:

- `OutOfGasError`: Out of gas error
- `InsufficientFeesError`: Insufficient fees
- `BroadcastError`: Broadcast Exception

<a id="kiipy.aerial.tx_helpers.TxResponse.is_successful"></a>

#### is`_`successful

```python
def is_successful() -> bool
```

Check transaction is successful.

**Returns**:

transaction status

<a id="kiipy.aerial.tx_helpers.TxResponse.ensure_successful"></a>

#### ensure`_`successful

```python
def ensure_successful()
```

Ensure transaction is successful.

**Raises**:

- `OutOfGasError`: Out of gas error
- `InsufficientFeesError`: Insufficient fees
- `BroadcastError`: Broadcast Exception

<a id="kiipy.aerial.tx_helpers.SubmittedTx"></a>

## SubmittedTx Objects

```python
class SubmittedTx()
```

Submitted transaction.

<a id="kiipy.aerial.tx_helpers.SubmittedTx.__init__"></a>

#### `__`init`__`

```python
def __init__(client: "LedgerClient", tx_hash: str)
```

Init the Submitted transaction.

**Arguments**:

- `client`: Ledger client
- `tx_hash`: transaction hash

<a id="kiipy.aerial.tx_helpers.SubmittedTx.tx_hash"></a>

#### tx`_`hash

```python
@property
def tx_hash() -> str
```

Get the transaction hash.

**Returns**:

transaction hash

<a id="kiipy.aerial.tx_helpers.SubmittedTx.response"></a>

#### response

```python
@property
def response() -> Optional[TxResponse]
```

Get the transaction response.

**Returns**:

response

<a id="kiipy.aerial.tx_helpers.SubmittedTx.contract_code_id"></a>

#### contract`_`code`_`id

```python
@property
def contract_code_id() -> Optional[int]
```

Get the contract code id.

**Returns**:

return contract code id if exist else None

<a id="kiipy.aerial.tx_helpers.SubmittedTx.contract_address"></a>

#### contract`_`address

```python
@property
def contract_address() -> Optional[Address]
```

Get the contract address.

**Returns**:

return contract address if exist else None

<a id="kiipy.aerial.tx_helpers.SubmittedTx.wait_to_complete"></a>

#### wait`_`to`_`complete

```python
def wait_to_complete(
    timeout: Optional[Union[int, float, timedelta]] = None,
    poll_period: Optional[Union[int, float,
                                timedelta]] = None) -> "SubmittedTx"
```

Wait to complete the transaction.

**Arguments**:

- `timeout`: timeout, defaults to None
- `poll_period`: poll_period, defaults to None

**Returns**:

Submitted Transaction

