from twitter import Status


class StatusSerializer:
	def __init__(self, obj: Status, data=None):
		self.obj = obj
		self.data = self.to_representaion()

	def to_representaion(self):
		if isinstance(self.obj, list):
			return [x.AsDict() for x in self.obj]
		return self.obj.AsDict()
