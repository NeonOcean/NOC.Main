Mod_TabButtonInactiveClass = "Mod_Tab_Button";
Mod_TabButtonActiveClass = "Mod_Tab_Button_Active";

Mod_TabButtonIdentifierPrefix = "Mod_";
Mod_TabButtonIdentifierSuffix = "_Tab_Button";

Mod_TabIdentifierPrefix = "Mod_";
Mod_TabIdentifierSuffix = "_Tab";

Mod_TabNames = [
	"Overview",
	"Gallery",
	"Files",
	"Requirements",
	"Issues",
	"Changes",
	"Development"
];

Mod_DefaultTab = "Overview";

function Mod_OnPageLoad () {
	defaultTabIdentifier = Mod_TabIdentifierPrefix + Mod_DefaultTab + Mod_TabIdentifierSuffix;
	
	if(document.getElementById(defaultTabIdentifier) == null) {
		return
	}
	
	Mod_OpenOverviewTab();
}

function Mod_EnabledTab (tabName) {
	tabButtonIdentifier = Mod_TabButtonIdentifierPrefix + tabName + Mod_TabButtonIdentifierSuffix;
	tabIdentifier = Mod_TabIdentifierPrefix + tabName + Mod_TabIdentifierSuffix;
	
	tab = document.getElementById(tabIdentifier);
	tabButton = document.getElementById(tabButtonIdentifier);
	
	if(tab != null && tabButton != null) {
		tab.style.display = null;
		tabButton.className = Mod_TabButtonActiveClass;
	} else {
		if(tab != null || tabButton != null) {
			console.warn("Tried to enable a tab named '" + tabName + "' but only the tab or tab button exists, not both or neither as expected.");
		}
	}
}

function Mod_DisableTab (tabName) {
	tabButtonIdentifier = Mod_TabButtonIdentifierPrefix + tabName + Mod_TabButtonIdentifierSuffix;
	tabIdentifier = Mod_TabIdentifierPrefix + tabName + Mod_TabIdentifierSuffix;
	
	tab = document.getElementById(tabIdentifier);
	tabButton = document.getElementById(tabButtonIdentifier);
	
	if(tab != null && tabButton != null) {
		tab.style.display = "none";
		tabButton.className = Mod_TabButtonInactiveClass;
	} else {
		if(tab != null || tabButton != null) {
			console.warn("Tried to enable a tab named '" + tabName + "' but only the tab or tab button exists, not both or neither as expected.");
		}
	}
}

function Mod_OpenTab (targetTabName) {
	Mod_EnabledTab(targetTabName);
	
	for(var tabNameIndex = 0; tabNameIndex < Mod_TabNames.length; tabNameIndex++) {		
		if(Mod_TabNames[tabNameIndex] == targetTabName) {
			continue;
		}
		
		Mod_DisableTab(Mod_TabNames[tabNameIndex]);
	}
}

function Mod_OpenOverviewTab () {
	Mod_OpenTab("Overview");
}

function Mod_OpenGalleryTab () {
	Mod_OpenTab("Gallery");
}

function Mod_OpenFilesTab () {
	Mod_OpenTab("Files");
}

function Mod_OpenRequirementsTab () {
	Mod_OpenTab("Requirements");
}

function Mod_OpenIssuesTab () {
	Mod_OpenTab("Issues");
}

function Mod_OpenChangesTab () {
	Mod_OpenTab("Changes");
}

function Mod_OpenDevelopmentTab () {
	Mod_OpenTab("Development");
}

window.addEventListener("load", Mod_OnPageLoad);