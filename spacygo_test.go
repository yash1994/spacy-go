package spacygo

import (
	"math"
	"strings"
	"testing"
)

func TestLoadModelError(t *testing.T) {
	var modelName string = "dummy_model_name"
	var errSubs string = "Can't find model 'dummy_model_name'"
	r, err := Load(modelName)

	if r == nil {
		if strings.Contains(err.Error(), errSubs) {
			t.Logf("passed testLoadModelError: %v", errSubs)
		} else {
			t.Errorf("failed testLoadModelError: %v", err.Error())
		}
	}
}

func TestNlpProcessError(t *testing.T) {
	var text string = "This is error test."
	var errSubs string = "'NoneType' object is not callable"
	r, err := Nlp(text)

	if r == nil {
		if strings.Contains(err.Error(), errSubs) {
			t.Logf("passed testNlpProcessError: %v", errSubs)
		} else {
			t.Errorf("failed testNlpProcessError: %v", err.Error())
		}
	}
}

func TestDocSimilarityError(t *testing.T) {
	var texta string = "I like apples"
	var textb string = "I like oranges"
	var errSubs string = "'NoneType' object is not callable"

	r, err := Similarity(texta, textb)

	if r == nil {
		if strings.Contains(err.Error(), errSubs) {
			t.Logf("passed testDocSimilarityError: %v", errSubs)
		} else {
			t.Errorf("failed testDocSimilarityError: %v", err.Error())
		}
	}
}

func TestLoadModelDefault(t *testing.T) {
	var modelName string = ""
	r, err := Load(modelName)

	if r.GetMessage() == "Model loaded 'en_core_web_sm'" {
		t.Logf("passed testLoadModelDefault.load: %v == Model loaded 'en_core_web_sm'", r.GetMessage())
	} else {
		t.Errorf("failed testLoadModelDefault.load: %v != Model loaded 'en_core_web_sm'", r.GetMessage())
	}

	if err != nil {
		t.Errorf("failed testLoadModelDefault: %v", err.Error())
	}

}

func TestLoadModel(t *testing.T) {
	var modelName string = "en_core_web_sm"
	r, err := Load(modelName)

	if r.GetMessage() == "Model loaded 'en_core_web_sm'" {
		t.Logf("passed testLoadModel.load: %v == Model loaded 'en_core_web_sm'", r.GetMessage())
	} else {
		t.Errorf("failed testLoadModel.load: %v != Model loaded 'en_core_web_sm'", r.GetMessage())
	}

	if err != nil {
		t.Errorf("failed testLoadModel: %v", err.Error())
	}

}

func TestNlpProcessDoc(t *testing.T) {
	var text string = "Apple is looking at buying U.K. startup for $1 billion"
	r, err := Nlp(text)

	if r.GetDoc().GetText() == text {
		t.Logf("passed testNlpProcess.doc.text: %v == %v", r.GetDoc().GetText(), text)
	} else {
		t.Errorf("failed testNlpProcess.doc.text: %v != %v", r.GetDoc().GetText(), text)
	}

	if r.GetDoc().GetTextWithWs() == text {
		t.Logf("passed testNlpProcess.doc.text_with_ws: %v == %v", r.GetDoc().GetTextWithWs(), text)
	} else {
		t.Errorf("failed testNlpProcess.doc.text_with_ws: %v != %v", r.GetDoc().GetTextWithWs(), text)
	}

	if r.GetDoc().GetIsTagged() == true {
		t.Logf("passed testNlpProcess.doc.is_tagged: %v == %v", r.GetDoc().GetIsTagged(), true)
	} else {
		t.Errorf("failed testNlpProcess.doc.is_tagged: %v != %v", r.GetDoc().GetIsTagged(), false)
	}

	if r.GetDoc().GetIsParsed() == true {
		t.Logf("passed testNlpProcess.doc.is_parsed: %v == %v", r.GetDoc().GetIsParsed(), true)
	} else {
		t.Errorf("failed testNlpProcess.doc.is_parsed: %v != %v", r.GetDoc().GetIsParsed(), false)
	}

	if r.GetDoc().GetIsNered() == true {
		t.Logf("passed testNlpProcess.doc.is_nered: %v == %v", r.GetDoc().GetIsNered(), true)
	} else {
		t.Errorf("failed testNlpProcess.doc.is_nered: %v != %v", r.GetDoc().GetIsNered(), false)
	}

	if r.GetDoc().GetIsSentenced() == true {
		t.Logf("passed testNlpProcess.doc.is_sentenced: %v == %v", r.GetDoc().GetIsSentenced(), true)
	} else {
		t.Errorf("failed testNlpProcess.doc.is_sentenced: %v != %v", r.GetDoc().GetIsSentenced(), false)
	}

	if err != nil {
		t.Errorf("failed TestNlpProcessDoc: %v", err.Error())
	}
}

func TestNlpProcessEnts(t *testing.T) {
	var text string = "Apple is looking at buying U.K. startup for $1 billion"
	r, err := Nlp(text)

	if r.GetEnts()[0].GetLabel() == "ORG" && r.GetEnts()[0].GetStart() == 0 && r.GetEnts()[0].GetEnd() == 1 {
		t.Logf("passed testNlpProcess.ents[0].label_: %v == %v", r.GetEnts()[0].GetLabel(), "ORG")
		t.Logf("passed testNlpProcess.ents[0].start: %v == %v", r.GetEnts()[0].GetStart(), 0)
		t.Logf("passed testNlpProcess.ents[0].end: %v == %v", r.GetEnts()[0].GetEnd(), 1)
	} else {
		t.Errorf("failed testNlpProcess.ents[0].label_: %v != %v", r.GetEnts()[0].GetLabel(), "ORG")
		t.Errorf("failed testNlpProcess.ents[0].start: %v != %v", r.GetEnts()[0].GetStart(), 0)
		t.Errorf("failed testNlpProcess.ents[0].end: %v != %v", r.GetEnts()[0].GetEnd(), 1)
	}

	if r.GetEnts()[1].GetLabel() == "GPE" && r.GetEnts()[1].GetStart() == 5 && r.GetEnts()[1].GetEnd() == 6 {
		t.Logf("passed testNlpProcess.ents[1].label_: %v == %v", r.GetEnts()[1].GetLabel(), "GPE")
		t.Logf("passed testNlpProcess.ents[1].start: %v == %v", r.GetEnts()[1].GetStart(), 5)
		t.Logf("passed testNlpProcess.ents[1].end: %v == %v", r.GetEnts()[1].GetEnd(), 6)
	} else {
		t.Errorf("failed testNlpProcess.ents[1].label_: %v != %v", r.GetEnts()[1].GetLabel(), "GPE")
		t.Errorf("failed testNlpProcess.ents[1].start: %v != %v", r.GetEnts()[1].GetStart(), 5)
		t.Errorf("failed testNlpProcess.ents[1].end: %v != %v", r.GetEnts()[1].GetEnd(), 6)
	}

	if err != nil {
		t.Errorf("failed TestNlpProcessEnts: %v", err.Error())
	}
}

func TestNlpProcessSents(t *testing.T) {
	var text string = "Systems based on automatically learning the rules can be made more accurate simply by supplying more input data. However, systems based on handwritten rules can only be made more accurate by increasing the complexity of the rules, which is a much more difficult task."

	r, err := Nlp(text)

	if r.GetSents()[0].GetStart() == 0 && r.GetSents()[0].GetEnd() == 19 {
		t.Logf("passed testNlpProcess.sents[0].start: %v == %v", r.GetSents()[0].GetStart(), 0)
		t.Logf("passed testNlpProcess.sents[0].end: %v == %v", r.GetSents()[0].GetEnd(), 19)
	} else {
		t.Errorf("failed testNlpProcess.sents[0].start: %v != %v", r.GetSents()[0].GetStart(), 0)
		t.Errorf("failed testNlpProcess.sents[0].end: %v != %v", r.GetSents()[0].GetEnd(), 19)
	}

	if err != nil {
		t.Errorf("failed TestNlpProcessSents: %v", err.Error())
	}
}

func TestNlpProcessNounChunks(t *testing.T) {
	var text string = "Systems based on automatically learning the rules can be made more accurate simply by supplying more input data."

	r, err := Nlp(text)

	if r.GetNounChunks()[0].GetStart() == 0 && r.GetNounChunks()[0].GetEnd() == 1 {
		t.Logf("passed testNlpProcess.noun_chunks[0].start: %v == %v", r.GetNounChunks()[0].GetStart(), 0)
		t.Logf("passed testNlpProcess.noun_chunks[0].end: %v == %v", r.GetNounChunks()[0].GetEnd(), 1)
	} else {
		t.Errorf("failed testNlpProcess.noun_chunks[0].start: %v != %v", r.GetNounChunks()[0].GetStart(), 0)
		t.Errorf("failed testNlpProcess.noun_chunks[0].end: %v != %v", r.GetNounChunks()[0].GetEnd(), 1)
	}

	if r.GetNounChunks()[2].GetStart() == 15 && r.GetNounChunks()[2].GetEnd() == 18 {
		t.Logf("passed testNlpProcess.noun_chunks[2].start: %v == %v", r.GetNounChunks()[2].GetStart(), 15)
		t.Logf("passed testNlpProcess.noun_chunks[2].end: %v == %v", r.GetNounChunks()[2].GetEnd(), 18)
	} else {
		t.Errorf("failed testNlpProcess.noun_chunks[2].start: %v != %v", r.GetNounChunks()[2].GetStart(), 15)
		t.Errorf("failed testNlpProcess.noun_chunks[2].end: %v != %v", r.GetNounChunks()[2].GetEnd(), 18)
	}

	if err != nil {
		t.Errorf("failed TestNlpProcessNounChunks: %v", err.Error())
	}
}

func TestNlpProcessTokens(t *testing.T) {
	var text string = "Apple is looking at buying U.K. startup for $1 billion"
	r, err := Nlp(text)

	if r.GetTokens()[0].GetText() == "Apple" {
		t.Logf("passed testNlpProcess.tokens[0].text: %v == %v", r.GetTokens()[0].GetText(), "Apple")
	} else {
		t.Errorf("failed testNlpProcess.tokens[0].text: %v != %v", r.GetTokens()[0].GetText(), "Apple")
	}

	if r.GetTokens()[0].GetTextWithWs() == "Apple " {
		t.Logf("passed testNlpProcess.tokens[0].text_with_ws: %v == %v", r.GetTokens()[0].GetTextWithWs(), "Apple ")
	} else {
		t.Errorf("failed testNlpProcess.tokens[0].text_with_ws: %v != %v", r.GetTokens()[0].GetTextWithWs(), "Apple ")
	}

	if r.GetTokens()[1].GetWhitespace() == " " {
		t.Logf("passed testNlpProcess.tokens[1].whitespace_: %v == %v", r.GetTokens()[1].GetWhitespace(), " ")
	} else {
		t.Errorf("failed testNlpProcess.tokens[1].whitespace_: %v != %v", r.GetTokens()[1].GetWhitespace(), " ")
	}

	if r.GetTokens()[1].GetEntType() == "" {
		t.Logf("passed testNlpProcess.tokens[1].ent_type_: %v == %v", r.GetTokens()[1].GetEntType(), "")
	} else {
		t.Errorf("failed testNlpProcess.tokens[1].ent_type_: %v != %v", r.GetTokens()[1].GetEntType(), "")
	}

	if r.GetTokens()[2].GetEntIob() == "O" {
		t.Logf("passed testNlpProcess.tokens[2].ent_iob_: %v == %v", r.GetTokens()[2].GetEntIob(), "O")
	} else {
		t.Errorf("failed testNlpProcess.tokens[2].ent_iob_: %v != %v", r.GetTokens()[2].GetEntIob(), "O")
	}

	if r.GetTokens()[2].GetLemma() == "look" {
		t.Logf("passed testNlpProcess.tokens[2].lemma_: %v == %v", r.GetTokens()[2].GetLemma(), "look")
	} else {
		t.Errorf("failed testNlpProcess.tokens[2].lemma_: %v != %v", r.GetTokens()[2].GetLemma(), "look")
	}

	if r.GetTokens()[2].GetNorm() == "looking" {
		t.Logf("passed testNlpProcess.tokens[2].norm_: %v == %v", r.GetTokens()[2].GetNorm(), "looking")
	} else {
		t.Errorf("failed testNlpProcess.tokens[2].norm_: %v != %v", r.GetTokens()[2].GetNorm(), "looking")
	}

	if r.GetTokens()[3].GetLower() == "at" {
		t.Logf("passed testNlpProcess.tokens[3].lower_: %v == %v", r.GetTokens()[3].GetLower(), "at")
	} else {
		t.Errorf("failed testNlpProcess.tokens[3].lower_: %v != %v", r.GetTokens()[3].GetLower(), "at")
	}

	if r.GetTokens()[3].GetShape() == "xx" {
		t.Logf("passed testNlpProcess.tokens[3].shape_: %v == %v", r.GetTokens()[3].GetShape(), "xx")
	} else {
		t.Errorf("failed testNlpProcess.tokens[3].shape_: %v != %v", r.GetTokens()[3].GetShape(), "xx")
	}

	if r.GetTokens()[3].GetPrefix() == "a" {
		t.Logf("passed testNlpProcess.tokens[3].prefix_: %v == %v", r.GetTokens()[3].GetPrefix(), "a")
	} else {
		t.Errorf("failed testNlpProcess.tokens[3].prefix_: %v != %v", r.GetTokens()[3].GetPrefix(), "a")
	}

	if r.GetTokens()[3].GetSuffix() == "at" {
		t.Logf("passed testNlpProcess.tokens[3].suffix_: %v == %v", r.GetTokens()[3].GetSuffix(), "at")
	} else {
		t.Errorf("failed testNlpProcess.tokens[3].suffix_: %v != %v", r.GetTokens()[3].GetSuffix(), "at")
	}

	if r.GetTokens()[4].GetPos() == "VERB" {
		t.Logf("passed testNlpProcess.tokens[4].pos_: %v == %v", r.GetTokens()[4].GetPos(), "VERB")
	} else {
		t.Errorf("failed testNlpProcess.tokens[4].pos_: %v != %v", r.GetTokens()[4].GetPos(), "VERB")
	}

	if r.GetTokens()[4].GetTag() == "VBG" {
		t.Logf("passed testNlpProcess.tokens[4].tag_: %v == %v", r.GetTokens()[4].GetTag(), "VBG")
	} else {
		t.Errorf("failed testNlpProcess.tokens[4].tag_: %v != %v", r.GetTokens()[4].GetTag(), "VBG")
	}

	if r.GetTokens()[4].GetDep() == "pcomp" {
		t.Logf("passed testNlpProcess.tokens[4].dep_: %v == %v", r.GetTokens()[4].GetDep(), "pcomp")
	} else {
		t.Errorf("failed testNlpProcess.tokens[4].dep_: %v != %v", r.GetTokens()[4].GetDep(), "pcomp")
	}

	if r.GetTokens()[4].GetIsAlpha() == true {
		t.Logf("passed testNlpProcess.tokens[4].is_alpha: %v == %v", r.GetTokens()[4].GetIsAlpha(), true)
	} else {
		t.Errorf("failed testNlpProcess.tokens[4].is_alpha: %v != %v", r.GetTokens()[4].GetIsAlpha(), true)
	}

	if r.GetTokens()[4].GetIsAscii() == true {
		t.Logf("passed testNlpProcess.tokens[4].is_ascii: %v == %v", r.GetTokens()[4].GetIsAscii(), true)
	} else {
		t.Errorf("failed testNlpProcess.tokens[4].is_ascii: %v != %v", r.GetTokens()[4].GetIsAscii(), true)
	}

	if r.GetTokens()[5].GetIsDigit() == false {
		t.Logf("passed testNlpProcess.tokens[5].is_digit: %v == %v", r.GetTokens()[5].GetIsDigit(), false)
	} else {
		t.Errorf("failed testNlpProcess.tokens[5].is_digit: %v != %v", r.GetTokens()[5].GetIsDigit(), false)
	}

	if r.GetTokens()[5].GetIsLower() == false {
		t.Logf("passed testNlpProcess.tokens[5].is_lower: %v == %v", r.GetTokens()[5].GetIsLower(), false)
	} else {
		t.Errorf("failed testNlpProcess.tokens[5].is_lower: %v != %v", r.GetTokens()[5].GetIsLower(), false)
	}

	if r.GetTokens()[5].GetIsUpper() == true {
		t.Logf("passed testNlpProcess.tokens[5].is_upper: %v == %v", r.GetTokens()[5].GetIsUpper(), true)
	} else {
		t.Errorf("failed testNlpProcess.tokens[5].is_upper: %v != %v", r.GetTokens()[5].GetIsUpper(), true)
	}

	if r.GetTokens()[5].GetIsTitle() == true {
		t.Logf("passed testNlpProcess.tokens[5].is_title: %v == %v", r.GetTokens()[5].GetIsTitle(), true)
	} else {
		t.Errorf("failed testNlpProcess.tokens[5].is_title: %v != %v", r.GetTokens()[5].GetIsTitle(), true)
	}

	if r.GetTokens()[5].GetIsPunct() == false {
		t.Logf("passed testNlpProcess.tokens[5].is_punct: %v == %v", r.GetTokens()[5].GetIsPunct(), false)
	} else {
		t.Errorf("failed testNlpProcess.tokens[5].is_punct: %v != %v", r.GetTokens()[5].GetIsPunct(), false)
	}

	if r.GetTokens()[5].GetIsLeftPunct() == false {
		t.Logf("passed testNlpProcess.tokens[5].is_left_punct: %v == %v", r.GetTokens()[5].GetIsLeftPunct(), false)
	} else {
		t.Errorf("failed testNlpProcess.tokens[5].is_left_punct: %v != %v", r.GetTokens()[5].GetIsLeftPunct(), false)
	}

	if r.GetTokens()[6].GetIsRightPunct() == false {
		t.Logf("passed testNlpProcess.tokens[6].is_right_punct: %v == %v", r.GetTokens()[6].GetIsRightPunct(), false)
	} else {
		t.Errorf("failed testNlpProcess.tokens[6].is_right_punct: %v != %v", r.GetTokens()[6].GetIsRightPunct(), false)
	}

	if r.GetTokens()[6].GetIsSpace() == false {
		t.Logf("passed testNlpProcess.tokens[6].is_space: %v == %v", r.GetTokens()[6].GetIsSpace(), false)
	} else {
		t.Errorf("failed testNlpProcess.tokens[6].is_space: %v != %v", r.GetTokens()[6].GetIsSpace(), false)
	}

	if r.GetTokens()[6].GetIsBracket() == false {
		t.Logf("passed testNlpProcess.tokens[6].is_bracket: %v == %v", r.GetTokens()[6].GetIsBracket(), false)
	} else {
		t.Errorf("failed testNlpProcess.tokens[6].is_bracket: %v != %v", r.GetTokens()[6].GetIsBracket(), false)
	}

	if r.GetTokens()[6].GetIsCurrency() == false {
		t.Logf("passed testNlpProcess.tokens[6].is_currency: %v == %v", r.GetTokens()[6].GetIsCurrency(), false)
	} else {
		t.Errorf("failed testNlpProcess.tokens[6].is_currency: %v != %v", r.GetTokens()[6].GetIsCurrency(), false)
	}

	if r.GetTokens()[6].GetLikeUrl() == false {
		t.Logf("passed testNlpProcess.tokens[6].like_url: %v == %v", r.GetTokens()[6].GetLikeUrl(), false)
	} else {
		t.Errorf("failed testNlpProcess.tokens[6].like_url: %v != %v", r.GetTokens()[6].GetLikeUrl(), false)
	}

	if r.GetTokens()[6].GetLikeNum() == false {
		t.Logf("passed testNlpProcess.tokens[6].like_num: %v == %v", r.GetTokens()[6].GetLikeNum(), false)
	} else {
		t.Errorf("failed testNlpProcess.tokens[6].like_num: %v != %v", r.GetTokens()[6].GetLikeNum(), false)
	}

	if r.GetTokens()[6].GetLikeEmail() == false {
		t.Logf("passed testNlpProcess.tokens[6].like_email: %v == %v", r.GetTokens()[6].GetLikeEmail(), false)
	} else {
		t.Errorf("failed testNlpProcess.tokens[6].like_email: %v != %v", r.GetTokens()[6].GetLikeEmail(), false)
	}

	if r.GetTokens()[7].GetIsOov() == true {
		t.Logf("passed testNlpProcess.tokens[7].is_oov: %v == %v", r.GetTokens()[7].GetIsOov(), true)
	} else {
		t.Errorf("failed testNlpProcess.tokens[7].is_oov: %v != %v", r.GetTokens()[7].GetIsOov(), true)
	}

	if r.GetTokens()[7].GetIsStop() == true {
		t.Logf("passed testNlpProcess.tokens[7].is_stop: %v == %v", r.GetTokens()[7].GetIsStop(), true)
	} else {
		t.Errorf("failed testNlpProcess.tokens[7].is_stop: %v != %v", r.GetTokens()[7].GetIsStop(), true)
	}

	if r.GetTokens()[8].GetIsSentStart() == false {
		t.Logf("passed testNlpProcess.tokens[8].is_sent_start: %v == %v", r.GetTokens()[8].GetIsSentStart(), false)
	} else {
		t.Errorf("failed testNlpProcess.tokens[8].is_sent_start: %v != %v", r.GetTokens()[8].GetIsSentStart(), false)
	}

	if r.GetTokens()[8].GetHead() == 10 {
		t.Logf("passed testNlpProcess.tokens[8].head.i: %v == %v", r.GetTokens()[8].GetHead(), 10)
	} else {
		t.Errorf("failed testNlpProcess.tokens[8].head.i: %v != %v", r.GetTokens()[8].GetHead(), 10)
	}

	if err != nil {
		t.Errorf("failed TestNlpProcessTokens: %v", err.Error())
	}
}

func TestDocSimilarity(t *testing.T) {
	var texta string = "I like apples"
	var textb string = "I like oranges"
	var actualSimi float64 = 0.837
	var tolerance float64 = 0.001
	r, err := Similarity(texta, textb)

	if math.Abs(float64(r.GetSimilarity())-actualSimi) < tolerance {
		t.Logf("passed TestDocSimilarity: %v ~= %v", r.GetSimilarity(), actualSimi)
	} else {
		t.Errorf("failed TestDocSimilarity: %v", r.GetSimilarity())
	}

	if err != nil {
		t.Errorf("failed TestDocSimilarity: %v", err.Error())
	}
}

func TestMatcher(t *testing.T) {
	var testRules []rule
	var testRule rule
	testRule.id = "HelloWorld"
	var testPattern1, testPattern2 pattern
	testPattern1.key = "LOWER"
	testPattern1.value = "hello"
	testPattern2.key = "LOWER"
	testPattern2.value = "world"

	testRule.patterns = append(testRule.patterns, testPattern1, testPattern2)
	testRules = append(testRules, testRule)

	r, err := PatternMatch(testRules, "HELLO WORLD on Google Maps.")

	if r.GetMatches()[0].GetStart() == 0 {
		t.Logf("passed patternMatch.matches[0].start: %v == %v", r.GetMatches()[0].GetStart(), 0)
	} else {
		t.Errorf("failed patternMatch.matches[0].start: %v != %v", r.GetMatches()[0].GetStart(), 0)
	}

	if r.GetMatches()[0].GetEnd() == 2 {
		t.Logf("passed patternMatch.matches[0].end: %v == %v", r.GetMatches()[0].GetEnd(), 2)
	} else {
		t.Errorf("failed patternMatch.matches[0].end: %v != %v", r.GetMatches()[0].GetEnd(), 2)
	}

	if err != nil {
		t.Errorf("failed TestMatcher: %v", err.Error())
	}

}
