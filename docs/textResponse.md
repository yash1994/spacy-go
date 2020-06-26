# TextResponse

TextResponse is type of `struct` returned when `Load` method is called.

## Attributes and Access Methods

| Name | Type | Access Method | Return Type | Description |
| ---- | -----| ------------- | ----------- | ----------- |
| `message` | `string` | `GetMessage()` | `string` | Holds message from gRPC NLP server for model getting loaded i.e. "Model loaded 'en_core_web_sm'" |