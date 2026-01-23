class HTMLNode:
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props
		
	def to_html(self):
		raise NotImplementedError

	def props_to_html(self):
		stringToBuild = ""
		if self.props == None:
			return ""
		for prop, value in self.props.items():
			toAdd = prop + '=' + '"' + value + '"' + " "
			stringToBuild += toAdd
		
		stringToBuild = stringToBuild[:-1] #TODO: removes final extra space, probably a more elegant way to write
		return stringToBuild

	def __repr__(self):
		print(f"TAG: {self.tag} 	VALUE: {self.value}	CHILDREN: {self.children}	PROPS: {self.props_to_html()}")