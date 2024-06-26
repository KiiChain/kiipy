<a id="kiipy.aerial.urls"></a>

# kiipy.aerial.urls

Parsing the URL.

<a id="kiipy.aerial.urls.Protocol"></a>

## Protocol Objects

```python
class Protocol(Enum)
```

Protocol Enum.

**Arguments**:

- `Enum`: Enum

<a id="kiipy.aerial.urls.ParsedUrl"></a>

## ParsedUrl Objects

```python
@dataclass
class ParsedUrl()
```

Parse URL.

**Returns**:

Parsed URL

<a id="kiipy.aerial.urls.ParsedUrl.host_and_port"></a>

#### host`_`and`_`port

```python
@property
def host_and_port() -> str
```

Get the host and port of the url.

**Returns**:

host and port

<a id="kiipy.aerial.urls.ParsedUrl.rest_url"></a>

#### rest`_`url

```python
@property
def rest_url() -> str
```

Get the rest url.

**Returns**:

rest url

<a id="kiipy.aerial.urls.parse_url"></a>

#### parse`_`url

```python
def parse_url(url: str) -> ParsedUrl
```

Initialize.

**Arguments**:

- `url`: url

**Raises**:

- `RuntimeError`: If url scheme is unsupported

**Returns**:

Parsed URL

