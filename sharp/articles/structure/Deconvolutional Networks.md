<!-- cvpr 2010 -->
# Deconvolutional Networks

## Abstract
Building robust low and mid-level image representations, beyond edge primitives, is a long-standing goal in
vision.
> beyond edge primitives

Many existing feature detectors spatially pool edge
information which destroys cues such as edge intersections,
parallelism and symmetry.
> spatially pool edge information 什么意思， 为什么会 destory cues

We present a learning framework where features that capture these mid-level cues spontaneously emerge from image data. Our approach is based
on the convolutional decomposition of images under a sparsity constraint and is totally unsupervised. By building a
hierarchy of such decompositions we can learn rich feature
sets that are a robust image representation for both the analysis and synthesis of images.
> decomposition 此处的含义是 ？
> unsupervised, 难道还是需要学习的 如何 decomposition

## 1. Introduction
In this paper we propose Deconvolutional Networks, a framework that permits the unsupervised construction of hierarchical image representations.
> hierarchical 体现在于何处 ？

These representations can
be used for both low-level tasks such as denoising, as well as providing features for object recognition.
> denoising

Each level of the hierarchy groups information from the level beneath to
form more complex features that exist over a larger scale in the image.
Our grouping mechanism is sparsity: by encouraging parsimonious(吝啬的 过于节俭的) representations at each level of the
hierarchy, features naturally assemble into more complex structures.
> 文章如何证明 hierarchy 的结构 逐渐形成一个 more complex feature
> parsimonious representation
> naturally assemble into : how naturally assemble

However, as we demonstrate, sparsity itself is
not enough – it must be deployed within the correct architecture to have the desired effect. We adopt a convolutional approach since it provides stable latent representations at each level which preserve locality and thus facilitate the grouping behavior. Using the same parameters for
learning each layer, our Deconvolutional Network (DN) can
automatically extract rich features that correspond to midlevel concepts such as edge junctions, parallel lines, curves
and basic geometric elements, such as rectangles. Remarkably, some of them look very similar to the mid-level tokens
posited by Marr in his primal sketch theory [18] (see Fig. 1).



Convolutional networks are a bottom-up approach where the input signal is subjected to multiple layers of convolutions, non-linearities and sub-sampling.
By contrast, each layer in our Deconvolutional Network is top-down; it seeks to generate the input signal by a sum
over convolutions of the feature maps (as opposed to the input) with learned filters. Given an input and a set of
filters, inferring the feature map activations requires solving
a multi-component deconvolution problem that is computationally challenging.
In response, we use a range of tools from low-level vision, such as sparse image priors and efficient algorithms for image deblurring. Correspondingly, our paper is an attempt to link high-level object recognition with low-level tasks like image deblurring through a unified
architecture.
