#Parameters
###n_components : int, optional (default: 2)
Dimension of the embedded space.

###perplexity : float, optional (default: 30)
The perplexity is related to the number of nearest neighbors that is used in other manifold learning algorithms. Larger datasets usually require a larger perplexity. Consider selecting a value between 5 and 50. The choice is not extremely critical since t-SNE is quite insensitive to this parameter.

###early_exaggeration : float, optional (default: 4.0)
Controls how tight natural clusters in the original space are in the embedded space and how much space will be between them. For larger values, the space between natural clusters will be larger in the embedded space. Again, the choice of this parameter is not very critical. If the cost function increases during initial optimization, the early exaggeration factor or the learning rate might be too high.

###learning_rate : float, optional (default: 1000)
The learning rate can be a critical parameter. It should be between 100 and 1000. If the cost function increases during initial optimization, the early exaggeration factor or the learning rate might be too high. If the cost function gets stuck in a bad local minimum increasing the learning rate helps sometimes.

###n_iter : int, optional (default: 1000)
Maximum number of iterations for the optimization. Should be at least 200.

###n_iter_without_progress : int, optional (default: 30)
Only used if method=’exact’ Maximum number of iterations without progress before we abort the optimization. If method=’barnes_hut’ this parameter is fixed to a value of 30 and cannot be changed.
New in version 0.17: parameter n_iter_without_progress to control stopping criteria.

###min_grad_norm : float, optional (default: 1e-7)
Only used if method=’exact’ If the gradient norm is below this threshold, the optimization will be aborted. If method=’barnes_hut’ this parameter is fixed to a value of 1e-3 and cannot be changed.

###metric : string or callable, optional
The metric to use when calculating distance between instances in a feature array. If metric is a string, it must be one of the options allowed by scipy.spatial.distance.pdist for its metric parameter, or a metric listed in pairwise.PAIRWISE_DISTANCE_FUNCTIONS. If metric is “precomputed”, X is assumed to be a distance matrix. Alternatively, if metric is a callable function, it is called on each pair of instances (rows) and the resulting value recorded. The callable should take two arrays from X as input and return a value indicating the distance between them. The default is “euclidean” which is interpreted as squared euclidean distance.

###init : string or numpy array, optional (default: “random”)
Initialization of embedding. Possible options are ‘random’, ‘pca’, and a numpy array of shape (n_samples, n_components). PCA initialization cannot be used with precomputed distances and is usually more globally stable than random initialization.

###verbose : int, optional (default: 0)
Verbosity level.

###random_state : int or RandomState instance or None (default)
Pseudo Random Number generator seed control. If None, use the numpy.random singleton. Note that different initializations might result in different local minima of the cost function.

###method : string (default: ‘barnes_hut’)
By default the gradient calculation algorithm uses Barnes-Hut approximation running in O(NlogN) time. method=’exact’ will run on the slower, but exact, algorithm in O(N^2) time. The exact algorithm should be used when nearest-neighbor errors need to be better than 3%. However, the exact method cannot scale to millions of examples.
New in version 0.17: Approximate optimization method via the Barnes-Hut.

###angle : float (default: 0.5)
Only used if method=’barnes_hut’ This is the trade-off between speed and accuracy for Barnes-Hut T-SNE. ‘angle’ is the angular size (referred to as theta in [3]) of a distant node as measured from a point. If this size is below ‘angle’ then it is used as a summary node of all points contained within it. This method is not very sensitive to changes in this parameter in the range of 0.2 - 0.8. Angle less than 0.2 has quickly increasing computation time and angle greater 0.8 has quickly increasing error.n_components

#Attributes
###embedding_ : array-like, shape (n_samples, n_components)
Stores the embedding vectors.
###kl_divergence_ : float
Kullback-Leibler divergence after optimization.

---