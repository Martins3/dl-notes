## Introduction
> explain why nn works well

## One Hidden Layer Neural Networks
 A perceptron is a very simple neuron that fires if it exceeds a certain threshold and doesn’t fire if it doesn’t reach that threshold. A perceptron network gets binary (0 and 1) inputs and gives binary outputs.

## Word Embeddings
A word embedding W:words→Rn is a paramaterized function mapping words in some language to high-dimensional vectors (perhaps 200 to 500 dimensions)

W is initialized to have random vectors for each word. It learns to have meaningful vectors in order to perform some task.

> t-SNE https://lvdmaaten.github.io/tsne/

Word embeddings exhibit an even more remarkable property: analogies between words seem to be encoded in the difference vectors between words.

This seems to be a great strength of neural networks: they learn better ways to represent data, automatically. Representing data well, in turn, seems to be essential to success at many machine learning problems.

> 使用神经网络得到 R(W(w1), W(w2), ...) = valid or not 得到 W 具有一系列的好性质


## Shared Representations
The use of word representations… has become a key “secret sauce” for the success of many NLP systems in recent years, across tasks including named entity recognition, part-of-speech tagging, parsing, and semantic role labeling

This general tactic – learning a good representation on a task A and then using it on a task B – is one of the major tricks in the Deep Learning toolbox. It goes by different names depending on the details: pretraining, transfer learning, and multi-task learning. One of the great strengths of this approach is that it allows the representation to learn from more than one kind of data.

Instead of learning a way to represent one kind of data and using it to perform multiple kinds of tasks, we can learn a way to map multiple kinds of data into a single representation!

optimize for an additional property: words that we know are close translations should be close together.

## Recursive Neural Networks
These models are often called “recursive neural networks” because one often has the output of a module go into a module of the same type. They are also sometimes called “tree-structured neural networks.”

Recursive neural networks have had significant successes in a number of NLP tasks. For example, Socher et al. (2013c) uses a recursive neural network to predict sentence sentiment

One major goal has been to create a reversible sentence representation, a representation that one can reconstruct an actual sentence from, with roughly the same meaning




## Criticisms

## Conclusion
