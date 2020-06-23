package spacygo

import (
	"testing"
)

func TestLoadModel(t *testing.T) {
	var modelName string = "en_core_web_sm"
	r, err := load(modelName)

	if r.GetMessage() == "Model loaded en_core_web_sm" {
		t.Logf("passed testLoadModel")
	}

	if err != nil {
		t.Errorf("failed testLoadModel")
	}

}

func TestNlpProcess(t *testing.T) {
	var text string = "Apple is looking at buying U.K. startup for $1 billion"
	r, err := nlp(text)

	if r.GetDoc().GetText() == text {
		t.Logf("passed testNlpProcess.doc.text")
	}

	if err != nil {
		t.Errorf("failed testNlpProcess")
	}
}
