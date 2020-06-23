package spacygo

import "testing"

func TestLoadModel(t *testing.T) {
	var modelName string = "en_core_web_sm"
	resp := load(modelName)

	if resp == "Model loaded en_core_web_sm" {
		t.Logf("passed testLoadModel")
	}

}
