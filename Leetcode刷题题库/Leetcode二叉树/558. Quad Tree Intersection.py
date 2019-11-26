# 四叉树是树的数据，其中每个内部节点正好有四个孩子：topLeft，topRight，bottomLeft和bottomRight。四叉树通常用于通过将
# 二维空间递归细分为四个象限或区域来划分二维空间。我们想在我们的四叉树中存储对/错信息。四叉树用于表示N * N布尔网格。
# 对于每个节点，它将细分为四个子节点，直到它表示的区域中的值都相同为止。每个节点还有另外两个布尔属性：isLeaf和val。
# isLeaf当且仅当节点是叶节点时才为true。val叶节点的属性包含其表示的区域的值。
# 注意：
# 双方A并B 表示大小的网格N * N。
# N 保证是2的幂。
# 如果您想了解有关四叉树的更多信息，可以参考其wiki。
# 逻辑或运算的定义如下：如果A is true，或B is true，或，则“ A或B”为true both A and B are true。
