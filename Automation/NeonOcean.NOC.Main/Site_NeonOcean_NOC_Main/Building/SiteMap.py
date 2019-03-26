import os
import pathlib
import sys
import typing
from xml.sax import saxutils

from Site_NeonOcean_NOC_Main import Paths, Site

def BuildSiteMap () -> bool:
	sitePaths = list()  # type: typing.List[str]

	if not os.path.exists(Paths.BuildPath):
		print("Site build path does not exist, this function should be run after everything has been built.", sys.stderr)
		return False

	buildPathObject = pathlib.Path(Paths.BuildPath)  # type: pathlib.Path
	for directoryRoot, directoryNames, fileNames in os.walk(Paths.BuildPath):  # type: str, typing.List[str], typing.List[str]
		directoryRootObject = pathlib.Path(directoryRoot)  # type: pathlib.Path

		if directoryRootObject == buildPathObject:
			directoryRelativePath = ""  # type: str
		else:
			directoryRelativePath = str(pathlib.Path(directoryRoot).relative_to(Paths.BuildPath))

		for fileName in fileNames:  # type: str
			fileExtension = os.path.splitext(fileName)[1].lower()  # type: str

			if fileExtension == ".html" or fileExtension == ".htm":
				filePath = os.path.join(directoryRelativePath, fileName)  # type: str

				if filePath in Site.GetCurrentSite().SitemapExcluded:
					continue

				sitePaths.append(filePath)

	if len(sitePaths) > 50000:
		print("Site map lists more than 50,000 pages", file = sys.stderr)

	# noinspection SpellCheckingInspection
	siteMapText = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n" \
				  "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\"" \
				  " xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"" \
				  " xsi:schemaLocation=\"http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd\">\n"

	for sitePath in sitePaths:
		siteURL = Site.GetCurrentSite().Domain + "/" + sitePath.replace("\\", "/")

		siteMapText += "\t<url>\n" \
					   "\t\t<loc>%s</loc>\n" \
					   "\t</url>\n" % saxutils.escape(siteURL)

	# noinspection SpellCheckingInspection
	siteMapText += "</urlset>"

	with open(os.path.join(Paths.BuildPath, "sitemap.xml"), "w+") as siteMapFile:
		siteMapFile.write(siteMapText)

	return True

BuildSiteMap()
