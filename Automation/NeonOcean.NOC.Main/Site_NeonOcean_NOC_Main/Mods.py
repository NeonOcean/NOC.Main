import json
import os
import typing
from importlib import util

from Site_NeonOcean_NOC_Main import Paths
from Site_NeonOcean_NOC_Main.Tools import Types

_modConfigs = list()  # type: typing.List[ModConfig]

_showedWarning = False  # type: bool

class ModConfig:
	Namespace: str
	Name: str
	PageURL: str
	BannerURL: str
	PreviewURL: str
	GameIdentifier: str

	Description: str

	OverviewTabSource: str
	FilesTabSource: str
	RequirementsTabSource: str
	IssuesTabSource: str
	ChangesTabSource: str
	DevelopmentTabSource: str

	Attributes = {
		"Namespace": str,
		"Name": str,
		"PageURL": str,
		"BannerURL": str,
		"PreviewURL": str,
		"GameIdentifier": str,

		"Description": str,

		"OverviewTabSource": str,
		"FilesTabSource": str,
		"RequirementsTabSource": str,
		"IssuesTabSource": str,
		"ChangesTabSource": str,
		"DevelopmentTabSource": str
	}

	def __init__ (self, modFilePath: str):
		self.LoadModDictionary(modFilePath)

		from Automation import Mods

		self.Mod = Mods.GetMod(self.Namespace)  # type: Mods.Mod

	def LoadModDictionary (self, modFilePath: str):
		modFileName = os.path.split(modFilePath)[1]  # type: str

		try:
			with open(modFilePath) as modFile:
				modDictionary = json.JSONDecoder().decode(modFile.read())  # type: dict
		except Exception as e:
			raise Exception("Failed to load mod file at '" + modFilePath + "'.") from e

		for attributeName, attributeType in self.Attributes.items():  # type: str, type
			attributeValue = modDictionary.get(attributeName)

			if attributeValue is None:
				raise Exception("Missing attribute '" + attributeName + "' from the mod file at '" + modFilePath + "'.")

			if type(attributeValue) != attributeType:
				raise Exception("Attribute '" + attributeName + "' in the mod file '" + modFileName +  "' is the wrong type. We expected the type '" + Types.GetFullName(attributeType) + " but got '" + Types.GetFullName(attributeValue) + "'.")

			setattr(self, attributeName, attributeValue)

def GetModConfig (namespace: str) -> ModConfig:
	for mod in _modConfigs:  # type: ModConfig
		if mod.Namespace == namespace:
			return mod

	raise Exception("Missing mod config '" + namespace + "'.")

def GetGameModConfigs (gameIdentifier: str) -> typing.List[ModConfig]:
	gameMods = list()

	for mod in _modConfigs:  # type: ModConfig
		if mod.GameIdentifier == gameIdentifier:
			gameMods.append(mod)

	return gameMods

def GetAllModConfigs () -> typing.List[ModConfig]:
	return list(_modConfigs)

def _Setup ():
	automationModule = util.find_spec("Automation")

	if automationModule is None and not _showedWarning:
		print("Failed to load mods. Environment automation modules are not loaded.")
		return ""

	for directoryRoot, directoryNames, fileNames in os.walk(Paths.ModsPath):  # type: str, typing.List[str], typing.List[str]
		for fileName in fileNames:  # type: str
			if os.path.splitext(fileName)[1] == ".json":
				modFilePath = os.path.join(directoryRoot, fileName)  # type: str

				_modConfigs.append(ModConfig(modFilePath))

_Setup()