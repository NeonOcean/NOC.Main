import os

AutomationPath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.normpath(__file__))))  # type: str
RootPath = os.path.dirname(AutomationPath)  # type: str

BuildPath = os.path.join(RootPath, "Build")  # type: str

DocumentsPath = os.path.join(RootPath, "Documents")  # type: str
DocumentsBuildPath = os.path.join(DocumentsPath, "Build")  # type: str
DocumentsConfigPath = os.path.join(DocumentsPath, "Config")  # type: str
DocumentsConfigDocumentsPath = os.path.join(DocumentsConfigPath, "Documents")  # type: str
DocumentsConfigTemplatesPath = os.path.join(DocumentsConfigPath, "Templates")  # type: str
DocumentsSourcesPath = os.path.join(DocumentsPath, "Sources")  # type: str
DocumentsSourcesIncludedPath = os.path.join(DocumentsPath, "Sources Included")  # type: str

ModsPath = os.path.join(RootPath, "Mods")  # type: str

TemplatesPath = os.path.join(RootPath, "Templates")  # type: str

LoosePath = os.path.join(RootPath, "Loose")  # type: str