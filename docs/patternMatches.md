# PatternMatches

Matches is type of `struct` returned when `PatternMatch` method is called.

## Attributes and Access Methods

| Name | Type | Access Method | Return Type | Description |
| ---- | -----| ------------- | ----------- | ----------- |
| `Matches` | `Array` | `GetMatches()` | `Array` of [`Match`](https://github.com/yash1994/spacy-go/blob/master/docs/patternMatches.md#match) | Contains `Array` of type [`Match`](https://github.com/yash1994/spacy-go/blob/master/docs/patternMatches.md#match) (list of matched tokens). |

# Match

Match is type of `struct` returned as array element when `GetMatches()` method is called on `Matches`.

## Attributes and Access Methods

| Name | Type | Access Method | Return Type | Description |
| ---- | -----| ------------- | ----------- | ----------- |
| `Start` | `int32` | `GetStart()` | `int32` | Starting index of matched token in processed text. |
| `End` | `int32` | `GetEnd()` | `int32` | Ending index of matched token in processed text. |
| `Id` | `string` | `GetId()` | `string` | Unique match id for matched pattern in text. |