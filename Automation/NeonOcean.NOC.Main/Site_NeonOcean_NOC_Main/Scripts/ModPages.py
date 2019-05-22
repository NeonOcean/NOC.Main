import os
import sys
import typing

from Site_NeonOcean_NOC_Main import Mods, Paths
from Site_NeonOcean_NOC_Main.Tools import Formatting

try:
	import markdown
except Exception as e:
	markdown = None
	print("Failed to import markdown \n" + str(e), file = sys.stderr)

_documentationURL = "https://doc.mods.neonoceancreations.com"  # type: str
_distributionURL = "https://dist.mods.neonoceancreations.com"  # type: str

class FormattingDict(dict):
	def __missing__ (self, key):
		return "{" + key + "}"

ModPageFormattingTemplate = {
	"Namespace": lambda modConfig: modConfig.Namespace,
	"Name": lambda modConfig: modConfig.Name,
	"BannerURL": lambda modConfig: modConfig.BannerURL,
	"DocumentationURL": lambda modConfig: _documentationURL + "/s4/" + modConfig.Mod.GetName().lower() if modConfig.Mod.GetName() is not None else _documentationURL,
	"Version": lambda modConfig: modConfig.Mod.ReleaseLatest.Version,
	"UpdateDate": lambda modConfig: modConfig.Mod.ReleaseLatest.ReleaseDateObject.strftime("%B %d, %Y"),
	"GameVersion": lambda modConfig: modConfig.Mod.ReleaseLatest.GameVersion,

	"OverviewTab": lambda modConfig: _GetOverviewTabText(modConfig),
	"FilesTab": lambda modConfig: _GetFilesTabText(modConfig),
	"RequirementsTab": lambda modConfig: _GetRequirementsTabText(modConfig),
	"IssuesTab": lambda modConfig: _GetIssuesTabText(modConfig),
	"ChangesTab": lambda modConfig: _GetChangesTabText(modConfig),
	"DevelopmentTab": lambda modConfig: _GetDevelopmentTabText(modConfig)
}  # type: typing.Dict[str, typing.Callable[[Mods.ModConfig], typing.Any]]

OverviewTabFormattingTemplate = {
	"DocumentationURL": lambda modConfig: _documentationURL + "/s4/" + modConfig.Mod.GetName().lower() if modConfig.Mod.GetName() is not None else _documentationURL,
}  # type: typing.Dict[str, typing.Callable[[Mods.ModConfig], typing.Any]]

FilesTabFormattingTemplate = {
	"InstallerURL": lambda modConfig: _distributionURL + "/mods/" + modConfig.Namespace.lower() + "/installer",
	"FilesURL": lambda modConfig: _distributionURL + "/mods/" + modConfig.Namespace.lower() + "/files",
	"FilesInstallationGuideURL": lambda modConfig: _documentationURL + "/s4/" + modConfig.Mod.GetName().lower() + "/installation" if modConfig.Mod.GetName() is not None else _documentationURL,

	"SourcesURL": lambda modConfig: _distributionURL + "/mods/" + modConfig.Namespace.lower() + "/sources",
	
	"DownloadIndexURL": lambda modConfig: _distributionURL + "/mods/" + modConfig.Namespace.lower()
}  # type: typing.Dict[str, typing.Callable[[Mods.ModConfig], typing.Any]]

RequirementsTabFormattingTemplate = {

}  # type: typing.Dict[str, typing.Callable[[Mods.ModConfig], typing.Any]]

IssuesTabFormattingTemplate = {
	"BugReportingGuideURL": lambda modConfig: _documentationURL + "/s4/" + modConfig.Mod.GetName().lower() + "/reporting-bugs" if modConfig.Mod.GetName() is not None else _documentationURL,
}  # type: typing.Dict[str, typing.Callable[[Mods.ModConfig], typing.Any]]

ChangesTabFormattingTemplate = {
	"Changes": lambda modConfig: _GetChangesText(modConfig)
}  # type: typing.Dict[str, typing.Callable[[Mods.ModConfig], typing.Any]]

DevelopmentTabFormattingTemplate = {
	"Plans": lambda modConfig: _GetPlansText(modConfig)
}  # type: typing.Dict[str, typing.Callable[[Mods.ModConfig], typing.Any]]

def GetModPageText (modNamespace: str) -> str:
	modConfig = Mods.GetModConfig(modNamespace)  # type: Mods.ModConfig

	with open(os.path.join(Paths.TemplatesPath, "ModPage.html")) as modPageTemplateFile:
		modPageTemplate = modPageTemplateFile.read()  # type: str

	modPageFormatting = FormattingDict()  # type: typing.Dict[str, typing.Any]

	for formattingKey, formattingValueLambda in ModPageFormattingTemplate.items():  # type: str, typing.Callable[[Mods.ModConfig], typing.Any]
		modPageFormatting[formattingKey] = formattingValueLambda(modConfig)

	return Formatting.FormatDictionary(modPageTemplate, modPageFormatting)

def _GetOverviewTabText (modConfig: Mods.ModConfig) -> str:
	with open(os.path.join(Paths.DocumentsSourcesPath, modConfig.OverviewTabSource)) as overviewTabTemplateFile:
		overviewTabTemplate = overviewTabTemplateFile.read()  # type: str

	overviewTabFormatting = FormattingDict()  # type: typing.Dict[str, typing.Any]

	for formattingKey, formattingValueLambda in OverviewTabFormattingTemplate.items():  # type: str, typing.Callable[[Mods.ModConfig], typing.Any]
		overviewTabFormatting[formattingKey] = formattingValueLambda(modConfig)

	return Formatting.FormatDictionary(overviewTabTemplate, overviewTabFormatting)

def _GetFilesTabText (modConfig: Mods.ModConfig) -> str:
	with open(os.path.join(Paths.DocumentsSourcesPath, modConfig.FilesTabSource)) as filesTabTemplateFile:
		filesTabTemplate = filesTabTemplateFile.read()  # type: str

	filesTabFormatting = FormattingDict()  # type: typing.Dict[str, typing.Any]

	for formattingKey, formattingValueLambda in FilesTabFormattingTemplate.items():  # type: str, typing.Callable[[Mods.ModConfig], typing.Any]
		filesTabFormatting[formattingKey] = formattingValueLambda(modConfig)

	return Formatting.FormatDictionary(filesTabTemplate, filesTabFormatting)

def _GetRequirementsTabText (modConfig: Mods.ModConfig) -> str:
	with open(os.path.join(Paths.DocumentsSourcesPath, modConfig.RequirementsTabSource)) as requirementsTabTemplateFile:
		requirementsTabTemplate = requirementsTabTemplateFile.read()  # type: str

	requirementsTabFormatting = FormattingDict()  # type: typing.Dict[str, typing.Any]

	for formattingKey, formattingValueLambda in RequirementsTabFormattingTemplate.items():  # type: str, typing.Callable[[Mods.ModConfig], typing.Any]
		requirementsTabFormatting[formattingKey] = formattingValueLambda(modConfig)

	return Formatting.FormatDictionary(requirementsTabTemplate, requirementsTabFormatting)

def _GetIssuesTabText (modConfig: Mods.ModConfig) -> str:
	with open(os.path.join(Paths.DocumentsSourcesPath, modConfig.IssuesTabSource)) as issuesTabTemplateFile:
		issuesTabTemplate = issuesTabTemplateFile.read()  # type: str

	issuesTabFormatting = FormattingDict()  # type: typing.Dict[str, typing.Any]

	for formattingKey, formattingValueLambda in IssuesTabFormattingTemplate.items():  # type: str, typing.Callable[[Mods.ModConfig], typing.Any]
		issuesTabFormatting[formattingKey] = formattingValueLambda(modConfig)

	return Formatting.FormatDictionary(issuesTabTemplate, issuesTabFormatting)

def _GetChangesTabText (modConfig: Mods.ModConfig) -> str:
	with open(os.path.join(Paths.DocumentsSourcesPath, modConfig.ChangesTabSource)) as changesTabTemplateFile:
		changesTabTemplate = changesTabTemplateFile.read()  # type: str

	changesTabFormatting = FormattingDict()  # type: typing.Dict[str, typing.Any]

	for formattingKey, formattingValueLambda in ChangesTabFormattingTemplate.items():  # type: str, typing.Callable[[Mods.ModConfig], typing.Any]
		changesTabFormatting[formattingKey] = formattingValueLambda(modConfig)

	return Formatting.FormatDictionary(changesTabTemplate, changesTabFormatting)

def _GetChangesText (modConfig: Mods.ModConfig) -> str:
	if markdown is None:
		return ""

	changesFilePath = modConfig.Mod.GetChangesFilePath()  # type: typing.Optional[str]

	if changesFilePath is None:
		return ""

	with open(changesFilePath) as changesFile:
		changes = changesFile.read()  # type: str

	return markdown.markdown(changes, output_format = 'html5')

def _GetDevelopmentTabText (modConfig: Mods.ModConfig) -> str:
	with open(os.path.join(Paths.DocumentsSourcesPath, modConfig.DevelopmentTabSource)) as developmentTabTemplateFile:
		developmentTabTemplate = developmentTabTemplateFile.read()  # type: str

	developmentTabFormatting = FormattingDict()  # type: typing.Dict[str, typing.Any]

	for formattingKey, formattingValueLambda in DevelopmentTabFormattingTemplate.items():  # type: str, typing.Callable[[Mods.ModConfig], typing.Any]
		developmentTabFormatting[formattingKey] = formattingValueLambda(modConfig)

	return Formatting.FormatDictionary(developmentTabTemplate, developmentTabFormatting)

def _GetPlansText (modConfig: Mods.ModConfig) -> str:
	if markdown is None:
		return ""

	plansFilePath = modConfig.Mod.GetPlansFilePath()  # type: typing.Optional[str]

	if plansFilePath is None:
		return ""

	with open(plansFilePath) as plansFile:
		plans = plansFile.read()  # type: str

	return markdown.markdown(plans, output_format = 'html5')