if __name__ == "__main__":
	import os
	import sys
	from importlib import util
		
	sys.path.append(os.path.join(os.path.dirname(__file__), "NeonOcean.NOC.Main"))
	Main = util.find_spec("Site_NeonOcean_NOC_Main.Main").loader.load_module()
		
	Main.BuildSite()