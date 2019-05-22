
function AnalyticEvents_ClickedDarkToggle (eventLabel) {
	eventAction = "Click";
	eventCategory = "Dark Toggle Buttons";
	
	eventData = {
		"event_category": eventCategory,
		"event_label": eventLabel
	};
	
	gtag("event", eventAction, eventData);
}

function AnalyticEvents_DarkPageDialogResponse (eventLabel) {
	eventAction = "Dialog Response";
	eventCategory = "Dark Page Dialog Response";
	
	eventData = {
		"event_category": eventCategory,
		"event_label": eventLabel
	};
	
	gtag("event", eventAction, eventData);
}

function AnalyticEvents_DarkEnableDialogResponse (eventLabel) {
	eventAction = "Dialog Response";
	eventCategory = "Dark Enable Dialog Response";
	
	eventData = {
		"event_category": eventCategory,
		"event_label": eventLabel
	};
	
	gtag("event", eventAction, eventData);
}

function AnalyticEvents_Mod_ClickedDownloadButton () {
	eventAction = "Click";
	eventCategory = "Mod Download Buttons";
	
	eventData = {
		"event_category": eventCategory
	};
	
	gtag("event", eventAction, eventData);
}

function AnalyticEvents_Mod_ChangedTab (eventLabel) {
	eventAction = "Change Tab";
	eventCategory = "Mod Tabs";
	
	eventData = {
		"event_category": eventCategory,
		"event_label": eventLabel
	};
	
	gtag("event", eventAction, eventData);
}











