package armory.logicnode;

class ReadJsonNode extends LogicNode {

	var data: Dynamic;

	public function new(tree: LogicTree) {
		super(tree);
	}

	override function run(from: Int) {
		// Relative or absolute path to file
		var file: String = inputs[1].get();

		// Whether to use the cache
		var useCache: Bool = inputs[2].get();

		// Load the file asynchronously
		if (!useCache && iron.data.Data.cachedBlobs.get(file) != null) iron.data.Data.cachedBlobs.remove(file);
		iron.data.Data.getBlob(file, function(b: kha.Blob) {
			data = haxe.Json.parse(b.toString());
			if (!useCache) iron.data.Data.cachedBlobs.remove(file);
			runOutput(0);
		});

		if (data == null) runOutput(1);
	}

	override function get(from: Int): Dynamic {
		return data;
	}
}
