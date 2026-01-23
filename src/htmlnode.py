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
		print(f"TAG: {self.tag} VALUE: {self.value}	CHILDREN: {self.children} PROPS: {self.props_to_html()}")

class ParentNode(HTMLNode):
	def __init__(self, tag, children, props=None):
		super().__init__(tag, value=None, children=children, props=props)

	def to_html(self):
		if self.tag == None:
			raise ValueError("missing tag")
		htmlToBuild = '<' + self.tag + '>'
		if self.children == None:
			raise ValueError("missing children")
		else:
			for child in self.children:
				child_html = child.to_html()
				htmlToBuild += child_html 
			htmlToBuild += "</" + self.tag + '>'
		return htmlToBuild
	
	def __repr__(self):
		print(f"TAG: {self.tag} CHILDREN: {self.children}	PROPS: `{self.props_to_html()}")
	
class LeafNode(HTMLNode):
	def __init__(self, tag, value, props=None):
		super().__init__(tag, value, children=None, props=props)

	def to_html(self):
		htmlToBuild = ""
		if self.value == None:
			raise ValueError("no value")
		if self.tag == None:
			return self.value
		if self.props_to_html() != "":
			htmlToBuild = '<' + self.tag + " " + self.props_to_html() + '>' + self.value + "</" + self.tag + '>'
			return htmlToBuild
		htmlToBuild = '<' + self.tag + '>' + self.value + "</" + self.tag + '>'
		return htmlToBuild
	
	def __repr__(self):
		print(f"TAG: {self.tag} VALUE: {self.value}	PROPS: {self.props_to_html()}")
	
	