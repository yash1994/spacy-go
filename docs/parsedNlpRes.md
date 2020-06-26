# ParsedNLPRes

ParsedNLPRes is type of `struct` returned when `Nlp` method is called.

## Attributes and Access Methods

| Name | Type | Access Method | Return Type | Description |
| ---- | -----| ------------- | ----------- | ----------- |
| `Model` | `string` | `GetModel()` | `string` | Contains name of loaded language model. |
| `Doc` | `Doc` | `GetDoc()` | [`Doc`](https://github.com/yash1994/spacy-go/blob/master/docs/parsedNlpRes.md#doc) | Contains `Doc` of type `struct`. |
| `Ents` | `Array` | `GetEnts()` | `Array` of [`Ent`](https://github.com/yash1994/spacy-go/blob/master/docs/parsedNlpRes.md#ent) | Contains `Array` of type [`Ent`](https://github.com/yash1994/spacy-go/blob/master/docs/parsedNlpRes.md#ent) (list of entities from nered text). |
| `Sents` | `Array` | `GetSents()` | `Array` of [`Sent`](https://github.com/yash1994/spacy-go/blob/master/docs/parsedNlpRes.md#sent) | Contains `Array` of type [`Sent`](https://github.com/yash1994/spacy-go/blob/master/docs/parsedNlpRes.md#sent) (list of sentences from processed text). |
| `NounChunks` | `Array` | `GetNounChunks()` | `Array` of [`NounChunk`](https://github.com/yash1994/spacy-go/blob/master/docs/parsedNlpRes.md#nounchunk) | Contains `Array` of type [`NounChunk`](https://github.com/yash1994/spacy-go/blob/master/docs/parsedNlpRes.md#nounchunk) ((list of Noun Chunks from processed text)). |
| `Tokens` | `Array` | `GetTokens()` | `Array` of [`Token`](https://github.com/yash1994/spacy-go/blob/master/docs/parsedNlpRes.md#token) | Contains `Array` of type [`Token`](https://github.com/yash1994/spacy-go/blob/master/docs/parsedNlpRes.md#token) (list of tokens from processed text). |

# Doc

Doc is type of `struct` returned when `GetModel()` method is called on `ParsedNLPRes`.

## Attributes and Access Methods

| Name | Type | Access Method | Return Type | Description |
| ---- | -----| ------------- | ----------- | ----------- |
| `Text` | `string` | `GetText()` | `string` | A unicode representation of the document text. |
| `TextWithWs` | `string` | `GetTextWithWs()` | `string` | An alias of Doc.Text, provided for duck-type compatibility with Span and Token. |
| `IsTagged` | `bool` | `GetIsTagged()` | `bool` | A flag indicating that the document has been part-of-speech tagged. Returns True if the Doc is empty. |
| `IsParsed` | `bool` | `GetIsParsed()` | `bool` | A flag indicating that the document has been part-of-speech tagged. Returns True if the Doc is empty.A flag indicating that the document has been syntactically parsed. Returns True if the Doc is empty. |
| `IsNered` | `bool` | `GetIsNered()` | `bool` | A flag indicating that named entities have been set. Will return True if the Doc is empty, or if any of the tokens has an entity tag set, even if the others are unknown. |
| `IsSentenced` | `bool` | `GetIsSentenced()` | `bool` | A flag indicating that sentence boundaries have been applied to the document. Returns True if the Doc is empty. |

# Ent

Ent is type of `struct` returned as array element when `GetEnts()` method is called on `ParsedNLPRes`.

## Attributes and Access Methods

| Name | Type | Access Method | Return Type | Description |
| ---- | -----| ------------- | ----------- | ----------- |
| `Start` | `int32` | `GetStart()` | `int32` | Starting index of entity in processed text. |
| `End` | `int32` | `GetEnd()` | `int32` | Ending index of entity in processed text. |
| `Label` | `string` | `GetLabel()` | `string` | Entity label. |

# Sent

Sent is type of `struct` returned as array element when `GetSents()` method is called on `ParsedNLPRes`.

## Attributes and Access Methods

| Name | Type | Access Method | Return Type | Description |
| ---- | -----| ------------- | ----------- | ----------- |
| `Start` | `int32` | `GetStart()` | `int32` | Starting index of sentence in processed text. |
| `End` | `int32` | `GetEnd()` | `int32` | Ending index of sentence in processed text. |

# NounChunk

NounChunk is type of `struct` returned as array element when `GetNounChunks()` method is called on `ParsedNLPRes`.

## Attributes and Access Methods

| Name | Type | Access Method | Return Type | Description |
| ---- | -----| ------------- | ----------- | ----------- |
| `Start` | `int32` | `GetStart()` | `int32` | Starting index of Noun Chunk in processed text. |
| `End` | `int32` | `GetEnd()` | `int32` | Ending index of Noun Chunk in processed text. |

# Token

Token is type of `struct` returned as array element when `GetTokens()` method is called on `ParsedNLPRes`.

## Attributes and Access Methods

| Name | Type | Access Method | Return Type | Description |
| ---- | -----| ------------- | ----------- | ----------- |
| `Text` | `string` | `GetText()` | `string` | Verbatim text content. |
| `TextWithWs` | `string` | `GetTextWithWs()` | `string` | Text content, with trailing space character if present. |
| `Whitespace` | `string` | `GetWhitespace()` | `string` | Trailing space character if present. |
| `EntType` | `string` | `GetEntType()` | `string` | Named entity type. |
| `EntIob` | `string` | `GetEntIob()` | `string` | Named entity type. |
| `Lemma` | `string` | `GetLemma()` | `string` | Base form of the token, with no inflectional suffixes. |
| `Norm` | `string` | `GetNorm()` | `string` | The token’s norm, i.e. a normalized form of the token text. |
| `Lower` | `string` | `GetLower()` | `string` | Lowercase form of the token. |
| `Shape` | `string` | `GetShape()` | `string` | Transform of the tokens’s string, to show orthographic features. Alphabetic characters are replaced by x or X, and numeric characters are replaced by d, and sequences of the same character are truncated after length 4. For example,"Xxxx"or"dd". |
| `Prefix` | `string` | `GetPrefix()` | `string` | A length-N substring from the start of the token. |
| `Suffix` | `string` | `GetSuffix()` | `string` | Hash value of a length-N substring from the end of the token. |
| `Pos` | `string` | `GetPos()` | `string` | Coarse-grained part-of-speech from the Universal POS tag set. |
| `Tag` | `string` | `GetTag()` | `string` | Fine-grained part-of-speech. |
| `Dep` | `string` | `GetDep()` | `string` | Syntactic dependency relation. |
| `IsAlpha` | `bool` | `GetIsAlpha()` | `bool` | Does the token consist of alphabetic characters? |
| `IsAscii` | `bool` | `GetIsAscii()` | `bool` | Does the token consist of ASCII characters? | 
| `IsDigit` | `bool` | `GetIsDigit()` | `bool` | Does the token consist of digits?  |
| `IsLower` | `bool` | `GetIsLower()` | `bool` | Is the token in lowercase? |
| `IsUpper` | `bool` | `GetIsUpper()` | `bool` | Is the token in uppercase? |
| `IsTitle` | `bool` | `GetIsTitle()` | `bool` | Is the token in titlecase? |
| `IsPunct` | `bool` | `GetIsPunct()` | `bool` | Is the token punctuation? |
| `IsLeftPunct` | `bool` | `GetIsLeftPunct()` | `bool` | Is the token a left punctuation mark, e.g. '(' ? |
| `IsRightPunct` | `bool` | `GetIsRightPunct()` | `bool` | Is the token a right punctuation mark, e.g. ')' ? |
| `IsSpace` | `bool` | `GetIsSpace()` | `bool` | Does the token consist of whitespace characters? |
| `IsBracket` | `bool` | `GetIsBracket()` | `bool` | Is the token a bracket? |
| `IsCurrency` | `bool` | `GetIsCurrency()` | `bool` | Is the token a currency symbol? |
| `LikeUrl` | `bool` | `GetLikeUrl()` | `bool` | Does the token resemble a URL? |
| `LikeNum` | `bool` | `GetLikeNum()` | `bool` | Does the token represent a number? e.g. “10.9”, “10”, “ten”, etc. |
| `LikeEmail` | `bool` | `GetLikeEmail()` | `bool` | Does the token resemble an email address? |
| `IsOov` | `bool` | `GetIsOov()` | `bool` | Does the token have a word vector? |
| `IsStop` | `bool` | `GetIsStop()` | `bool` | Is the token part of a “stop list”? |
| `IsSentStart` | `bool` | `GetIsSentStart()` | `bool` | A boolean value indicating whether the token starts a sentence. |
| `Head` | `int32` | `GetHead()` | `int32` | The syntactic parent, or “governor”, of this token. |
