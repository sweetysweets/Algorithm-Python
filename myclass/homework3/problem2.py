"""
KD树构造和查找
Description

对给定的点集合构造KD树，要求如下：将方差最大的维度作为当前的分割维度，将数据集在分割维度上排序后的中位数作为分割点。程序要检索给定点对应的最近的K个点的坐标。


Input

输入第一行为测试用例个数，后面为测试用例，每一个用例包含三行，第一行为点集合（点之间用逗号隔开，两个坐标用空格隔开），第二行为检索的点，第三行为K值。


Output

输出每一个用例的最近K个点，按照距离从小到大的顺序打印。


Sample Input 1

1
3 5,6 2,5 8,9 3,8 6,1 1,2 9
8.2 4.6
2
Sample Output 1

8 6,9 3
"""
from  sys import stdin
from time import time
from random import randint


class Node(object):
    def __init__(self):
        """Node class to build tree leaves.
        """
        self.father = None
        self.left = None
        self.right = None
        self.feature = None
        self.split = None


    def __str__(self):
        return "feature: %s, split: %s" % (str(self.feature), str(self.split))

    @property
    def brother(self):
        """Find the node's brother.
        Returns:
            node -- Brother node.
        """
        if not self.father:
            ret = None
        else:
            if self.father.left is self:
                ret = self.father.right
            else:
                ret = self.father.left
        return ret


class KDTree(object):
    def __init__(self):
        """KD Tree class to improve search efficiency in KNN.
        Attributes:
            root: the root node of KDTree.
        """
        self.root = Node()

    def __str__(self):
        """Show the relationship of each node in the KD Tree.
        Returns:
            str -- KDTree Nodes information.
        """
        ret = []
        i = 0
        que = [(self.root, -1)]
        while que:
            nd, idx_father = que.pop(0)
            ret.append("%d -> %d: %s" % (idx_father, i, str(nd)))
            if nd.left:
                que.append((nd.left, i))
            if nd.right:
                que.append((nd.right, i))
            i += 1
        return "\n".join(ret)

    def _get_median_idx(self, X, idxs, feature):
        """Calculate the median of a column of data.
        Arguments:
            X {list} -- 2d list object with int or float.
            idxs {list} -- 1D list with int.
            feature {int} -- Feature number.
            sorted_idxs_2d {list} -- 2D list with int.
        Returns:
            list -- The row index corresponding to the median of this column.
        """

        n = len(idxs)
        # Ignoring the number of column elements is odd and even.
        k = n // 2
        # Get all the indexes and elements of column j as tuples.
        col = map(lambda i: (i, X[i][feature]), idxs)
        # Sort the tuples by the elements' values
        # and get the corresponding indexes.
        sorted_idxs = map(lambda x: x[0], sorted(col, key=lambda x: x[1]))
        # Search the median value.
        median_idx = list(sorted_idxs)[k]
        return median_idx

    def _get_variance(self, X, idxs, feature):
        """Calculate the variance of a column of data.
        Arguments:
            X {list} -- 2d list object with int or float.
            idxs {list} -- 1D list with int.
            feature {int} -- Feature number.
        Returns:
            float -- variance
        """

        n = len(idxs)
        col_sum = col_sum_sqr = 0
        for idx in idxs:
            xi = X[idx][feature]
            col_sum += xi
            col_sum_sqr += xi ** 2
        # D(X) = E{[X-E(X)]^2} = E(X^2)-[E(X)]^2
        return col_sum_sqr / n - (col_sum / n) ** 2

    def _choose_feature(self, X, idxs):
        """Choose the feature which has maximum variance.
        Arguments:
            X {list} -- 2d list object with int or float.
            idxs {list} -- 1D list with int.
        Returns:
            feature number {int}
        """

        m = len(X[0])
        variances = map(lambda j: (
            j, self._get_variance(X, idxs, j)), range(m))
        return max(variances, key=lambda x: x[1])[0]

    def _split_feature(self, X, idxs, feature, median_idx):
        """Split indexes into two arrays according to split point.
        Arguments:
            X {list} -- 2d list object with int or float.
            idx {list} -- Indexes, 1d list object with int.
            feature {int} -- Feature number.
            median_idx {float} -- Median index of the feature.
        Returns:
            list -- [left idx, right idx]
        """

        idxs_split = [[], []]
        split_val = X[median_idx][feature]
        for idx in idxs:
            # Keep the split point in current node.
            if idx == median_idx:
                continue
            # Split
            xi = X[idx][feature]
            if xi < split_val:
                idxs_split[0].append(idx)
            else:
                idxs_split[1].append(idx)
        return idxs_split

    def build_tree(self, X, y):
        """Build a KD Tree. The data should be scaled so as to calculate variances.
        Arguments:
            X {list} -- 2d list object with int or float.
            y {list} -- 1d list object with int or float.
        """

        # Initialize with node, indexes
        nd = self.root
        idxs = range(len(X))
        que = [(nd, idxs)]
        while que:
            nd, idxs = que.pop(0)
            n = len(idxs)
            # Stop split if there is only one element in this node
            if n == 1:
                nd.split = (X[idxs[0]], y[idxs[0]])
                continue
            # Split
            feature = self._choose_feature(X, idxs)
            median_idx = self._get_median_idx(X, idxs, feature)
            idxs_left, idxs_right = self._split_feature(
                X, idxs, feature, median_idx)
            # Update properties of current node
            nd.feature = feature
            nd.split = (X[median_idx], y[median_idx])
            # Put children of current node in que
            if idxs_left != []:
                nd.left = Node()
                nd.left.father = nd
                que.append((nd.left, idxs_left))
            if idxs_right != []:
                nd.right = Node()
                nd.right.father = nd
                que.append((nd.right, idxs_right))

    def _search(self, Xi, nd):
        """Search Xi from the KDTree until Xi is at an leafnode.
        Arguments:
            Xi {list} -- 1d list with int or float.
        Returns:
            node -- Leafnode.
        """

        while nd.left or nd.right:
            if not nd.left:
                nd = nd.right
            elif not nd.right:
                nd = nd.left
            else:
                if Xi[nd.feature] < nd.split[0][nd.feature]:
                    nd = nd.left
                else:
                    nd = nd.right
        return nd

    def _get_eu_dist(self, Xi, nd):
        """Calculate euclidean distance between Xi and node.
        Arguments:
            Xi {list} -- 1d list with int or float.
            nd {node}
        Returns:
            float -- Euclidean distance.
        """

        X0 = nd.split[0]
        return get_euclidean_distance(Xi, X0)

    def _get_hyper_plane_dist(self, Xi, nd):
        """Calculate euclidean distance between Xi and hyper plane.
        Arguments:
            Xi {list} -- 1d list with int or float.
            nd {node}
        Returns:
            float -- Euclidean distance.
        """

        j = nd.feature
        X0 = nd.split[0]
        return abs(Xi[j] - X0[j])

    def nearest_neighbour_search(self, Xi):
        """Nearest neighbour search and backtracking.
        Arguments:
            Xi {list} -- 1d list with int or float.
        Returns:
            node -- The nearest node to Xi.
        """

        # The leaf node after searching Xi.
        dist_best = float("inf")
        nd_best = self._search(Xi, self.root)
        que = [(self.root, nd_best)]
        while que:
            nd_root, nd_cur = que.pop(0)
            # Calculate distance between Xi and root node
            dist = self._get_eu_dist(Xi, nd_root)
            # Update best node and distance.
            if dist < dist_best:
                dist_best, nd_best = dist, nd_root
            while nd_cur is not nd_root:
                # Calculate distance between Xi and current node
                dist = self._get_eu_dist(Xi, nd_cur)
                # Update best node, distance and visit flag.
                if dist < dist_best:
                    dist_best, nd_best = dist, nd_cur
                # If it's necessary to visit brother node.
                if nd_cur.brother and dist > \
                        self._get_hyper_plane_dist(Xi, nd_cur.father):
                    _nd_best = self._search(Xi, nd_cur.brother)
                    que.append((nd_cur.brother, _nd_best))
                # Back track.
                nd_cur = nd_cur.father

        return nd_best


def get_euclidean_distance( arr1, arr2):
    """Calculate the Euclidean distance of two vectors.
    Arguments:
        arr1 {list} -- 1d list object with int or float
        arr2 {list} -- 1d list object with int or float
    Returns:
        float -- Euclidean distance
    """

    return sum((x1 - x2) ** 2 for x1, x2 in zip(arr1, arr2)) ** 0.5

def gen_data(low, high, n_rows, n_cols=None):
    """Generate dataset randomly.
    Arguments:
        low {int} -- The minimum value of element generated.
        high {int} -- The maximum value of element generated.
        n_rows {int} -- Number of rows.
        n_cols {int} -- Number of columns.
    Returns:
        list -- 1d or 2d list with int
    """
    if n_cols is None:
        ret = [randint(low, high) for _ in range(n_rows)]
    else:
        ret = [[randint(low, high) for _ in range(n_cols)]
               for _ in range(n_rows)]
    return ret



def exhausted_search(X, Xi):
    """Linear search the nearest neighbour.
    Arguments:
        X {list} -- 2d list with int or float.
        Xi {list} -- 1d list with int or float.
    Returns:
        list -- 1d list with int or float.r.
    """

    dist_best = float('inf')
    row_best = None
    for row in X:
        dist = get_euclidean_distance(Xi, row)
        if dist < dist_best:
            dist_best = dist
            row_best = row
    return row_best


def main():
    print("Testing KD Tree...")
    test_times = 100
    run_time_1 = run_time_2 = 0
    for _ in range(test_times):
        # Generate dataset randomly
        low = 0
        high = 100
        n_rows = 1000
        n_cols = 2
        X = gen_data(low, high, n_rows, n_cols)
        y = gen_data(low, high, n_rows)
        Xi = gen_data(low, high, n_cols)

        # Build KD Tree
        tree = KDTree()
        tree.build_tree(X, y)

        # KD Tree Search
        start = time()
        nd = tree.nearest_neighbour_search(Xi)
        run_time_1 += time() - start
        ret1 = get_euclidean_distance(Xi, nd.split[0])

        # Exhausted search
        start = time()
        row = exhausted_search(X, Xi)
        run_time_2 += time() - start
        ret2 = get_euclidean_distance(Xi, row)

        # Compare result
        assert ret1 == ret2, "target:%s\nrestult1:%s\nrestult2:%s\ntree:\n%s" \
            % (Xi, nd, row, tree)
    print("%d tests passed!" % test_times)
    print("KD Tree Search %.2f s" % run_time_1)
    print("Exhausted search %.2f s" % run_time_2)


if __name__ == "__main__":
    main()
