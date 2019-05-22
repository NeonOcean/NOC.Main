Dark_EnableDialogIdentifier = "Dark_Enable_Dialog";
Dark_PageDialogIdentifier = "Dark_Page_Dialog";

Dark_EnabledCheckboxIdentifier = "Header_Dark_Checkbox_Enabled";
Dark_DisableCheckboxdIdentifier = "Header_Dark_Checkbox_Disabled";

Dark_PageAttribute = "dark_page";
Dark_ModeBehaviourAttribute = "data-dark_mode_behaviour";

Dark_ModeCookieKey = "dark_mode";

function Dark_OnPageLoad () {
	if(!Dark_IsDarkModeActive()) {
		if(Dark_IsPageDarkOnly()) {
			Dark_ShowPageDialog();
		}
		
		Dark_Disable();
	} else {	
		Dark_Enable();
	}
}

function Dark_IsPageDarkOnly () {
	metaElements = document.getElementsByTagName("meta");
	
	for(var metaElementIndex = 0; metaElementIndex < metaElements.length; metaElementIndex++) {
		if(metaElements[metaElementIndex].getAttribute("Name") == Dark_PageAttribute) {
			darkPage = false;
			
			darkPageString = metaElements[metaElementIndex].getAttribute("content");
			darkPageString = darkPageString.toLowerCase();
			
			if(darkPageString == "true") {
				darkPage = true;
			} else if(darkPageString != "false") {
				console.error("Dark page meta data value is not a boolean.");
			}
			
			return darkPage;
		}
	}
	
	return false;
}

function Dark_IsDarkModeActive () {
	if(window.location.protocol.toLowerCase() == "file:") {
		return true;
	}
	
	cookies = document.cookie.split(";");
	
	for(var cookieIndex = 0; cookieIndex < cookies.length; cookieIndex++) {
		cookie = cookies[cookieIndex].trimLeft();
		cookieEqualsIndex = cookie.indexOf("=");
		
		cookieKey = cookie.substring(0, cookieEqualsIndex);
		cookieKey = cookieKey.trim();
		
		if(cookieKey != Dark_ModeCookieKey) {
			continue;
		}
		
		cookieValue = cookie.substring(cookieEqualsIndex + 1, cookie.length);
		cookieValue = cookieValue.trim();
		
		cookieValue = cookieValue.toLowerCase();
		
		return cookieValue == "true" ? true : false;
	}
	
	return false;
}

function Dark_ChangeMode (darkEnabled) {
	if(darkEnabled) {
		darkElements = document.querySelectorAll("[" + Dark_ModeBehaviourAttribute + "]");
		
		for(var darkElementIndex = 0; darkElementIndex < darkElements.length; darkElementIndex++) {			
			behaviourAttributeValue = darkElements[darkElementIndex].getAttribute(Dark_ModeBehaviourAttribute);
			behaviourAttributeValue = behaviourAttributeValue.toLowerCase();
			
			if(behaviourAttributeValue == "hidden") {
				darkElements[darkElementIndex].style.display = "none";
			} else if(behaviourAttributeValue == "visible") {
				darkElements[darkElementIndex].style.display = null;
			} else if(behaviourAttributeValue != "none") {
				console.error("Dark element data value is not 'hidden', 'visible' or 'none'.");
			}
		}
	} else {
		darkElements = document.querySelectorAll("[" + Dark_ModeBehaviourAttribute + "]");
		
		for(var darkElementIndex = 0; darkElementIndex < darkElements.length; darkElementIndex++) {			
			behaviourAttributeValue = darkElements[darkElementIndex].getAttribute(Dark_ModeBehaviourAttribute);
			behaviourAttributeValue = behaviourAttributeValue.toLowerCase();
			
			if(behaviourAttributeValue == "hidden") {
				darkElements[darkElementIndex].style.display = null;
			} else if(behaviourAttributeValue == "visible") {
				darkElements[darkElementIndex].style.display = "none";
			} else if(behaviourAttributeValue != "none") {
				console.error("Dark element data value is not 'hidden', 'visible' or 'none'.");
			}
		}
	}
}

function Dark_AddModeCookie () {
	document.cookie = Dark_ModeCookieKey + " = true; expires = Tue, 31 Dec 2999 12:00:00 GMT; domain = .neonoceancreations.com";
}

function Dark_RemoveModeCookie () {
	document.cookie = Dark_ModeCookieKey + " = false; max-age = 0"
}

function Dark_Enable () {
	Dark_AddModeCookie();
	Dark_ChangeMode(true);
	
	enabledCheckbox = document.getElementById(Dark_EnabledCheckboxIdentifier);
	disableCheckbox = document.getElementById(Dark_DisableCheckboxdIdentifier);
	
	enabledCheckbox.style.display = null;
	disableCheckbox.style.display = "none";
}

function Dark_Disable () {
	Dark_RemoveModeCookie();
	Dark_ChangeMode(false);
	
	enabledCheckbox = document.getElementById(Dark_EnabledCheckboxIdentifier);
	disableCheckbox = document.getElementById(Dark_DisableCheckboxdIdentifier);
	
	enabledCheckbox.style.display = "none";
	disableCheckbox.style.display = null;
	
	if(Dark_IsPageDarkOnly()) {
		Dark_ShowPageDialog();
	}
}

function Dark_CheckboxCallback (checked) {
	if(checked) {
		Dark_ShowEnableDialog();
	} else {
		Dark_Disable();
	}
}

function Dark_ShowEnableDialog () {
	darkEnableDialog = document.getElementById(Dark_EnableDialogIdentifier);
	
	if(darkEnableDialog) {
		darkEnableDialog.style.display = null;
	} else {
		console.error("Couldn't find dark enable dialog for in this document.");
	}
}

function Dark_HideEnableDialog () {
	darkEnableDialog = document.getElementById(Dark_EnableDialogIdentifier);
	
	if(darkEnableDialog) {
		darkEnableDialog.style.display = "none";
	} else {
		console.error("Couldn't find dark enable dialog for in this document.");
	}
}

function Dark_EnableDialogCallback (response) {
	if(response) {
		Dark_Enable();
	}
	
	Dark_HideEnableDialog();
}

function Dark_ShowPageDialog () {
	darkPageDialog = document.getElementById(Dark_PageDialogIdentifier);
	
	if(darkPageDialog) {
		darkPageDialog.style.display = null;
	} else {
		console.error("Couldn't find dark page dialog for in this document.");
	}
}

function Dark_HidePageDialog () {
	darkPageDialog = document.getElementById(Dark_PageDialogIdentifier);
	
	if(darkPageDialog) {
		darkPageDialog.style.display = "none";
	} else {
		console.error("Couldn't find dark page dialog for in this document.");
	}
}

function Dark_PageDialogCallback () {
	Dark_Enable();
	
	Dark_HidePageDialog();
}

//window.addEventListener("load", Dark_OnPageLoad);