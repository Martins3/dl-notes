1. Informally, we define the __bias__ of a model to be the expected
generalization error even if we were to fit it to a very (say, infinitely) large
training set.
2. By fitting these “spurious” patterns in the training set, we might again
obtain a model with large generalization error. In this case, we say the model
has large __variance__


a few questions:
1. First, can we make formal the bias/variance tradeoff that
was just discussed?
2.
  1. Second, in machine learning it’s really generalization error that we care about, but most learning algorithms fit their models to the training set.   
  2. Why should doing well on the training set tell us
anything about generalization error?     
  3. Specifically, can we relate error on the training set to generalization error?
3.  Third and finally, are there conditions under which we can actually prove that learning algorithms will work well?
