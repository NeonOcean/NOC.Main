import os
import typing

from Site_NeonOcean_NOC_Main import Mods, Paths
from Site_NeonOcean_NOC_Main.Tools import Formatting

ModsListEntryFormattingTemplate = {
	"Name": lambda modConfig: modConfig.Name,
	
	"PageURL": lambda modConfig: modConfig.PageURL,
	"PreviewURL": lambda modConfig: modConfig.PreviewURL,
	"Version": lambda modConfig: modConfig.Mod.ReleaseLatest.Version,
	"UpdateDate": lambda modConfig: modConfig.Mod.ReleaseLatest.ReleaseDateObject.strftime("%B %d, %Y"),

	"Description": lambda modConfig: modConfig.Description
}  # type: typing.Dict[str, typing.Callable[[Mods.ModConfig], typing.Any]]

def GetModListText (gameIdentifier: typing.Optional[str] = None) -> str:
	if gameIdentifier is None:
		modConfigs = Mods.GetAllModConfigs()  # type: typing.List[Mods.ModConfig]
	else:
		modConfigs = Mods.GetGameModConfigs(gameIdentifier)  # type: typing.List[Mods.ModConfig]

	with open(os.path.join(Paths.TemplatesPath, "ModList.html")) as modListTemplateFile:
		modListTemplate = modListTemplateFile.read()  # type: str

	with open(os.path.join(Paths.TemplatesPath, "ModListEntry.html")) as modListEntryTemplateFile:
		modListEntryTemplate = modListEntryTemplateFile.read()  # type: str

	modList = ""  # type: str

	for modConfig in modConfigs:  # type: Mods.ModConfig
		modListEntryFormatting = dict()  # type: typing.Dict[str, str]

		for formattingKey, formattingValueLambda in ModsListEntryFormattingTemplate.items():  # type: str, typing.Callable[[Mods.ModConfig], typing.Any]
			modListEntryFormatting[formattingKey] = formattingValueLambda(modConfig)

		if modList == "":
			modList = Formatting.FormatDictionary(modListEntryTemplate, modListEntryFormatting)
		else:
			modList += "\n" + Formatting.FormatDictionary(modListEntryTemplate, modListEntryFormatting)
		
	return Formatting.FormatDictionary(modListTemplate, { "ModList": modList })