function Tree(val, left, right) {
  this.left = left;
  this.right = right;
  this.val = val;
}

Tree.prototype[Symbol.iterator] = function* () {
  yield this.val;
  if (this.left) yield* this.left;
  if (this.right) yield* this.right;
};
var root = new Tree(1, new Tree(2, new Tree(3)), new Tree(4));
for (var e of root) {
  console.log(e);
}

Tree.prototype[Symbol.iterator] = function* () {
  const queue = [this];
  while (queue.length > 0) {
    const node = queue.shift(); // Dequeue the first node in the queue
    yield node.val;

    // Enqueue the left and right children if they exist
    if (node.left) queue.push(node.left);
    if (node.right) queue.push(node.right);
  }
};

for (var e of root) {
  console.log(e);
}
