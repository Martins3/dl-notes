##  Abstract
We introduce a novel visualization technique that
gives insight into the function of intermediate feature layers and the operation of the classifier. Used in a diagnostic role, these visualizations allow
us to find model architectures that outperform Krizhevsky et al. on the
ImageNet classification benchmark. We also perform an ablation study
to discover the performance contribution from different model layers. We
show our ImageNet model generalizes well to other datasets: when the
softmax classifier is retrained, it convincingly beats the current state-of-the-art results on Caltech-101 and Caltech-256 datasets.

## 1 Introduction
In this paper we introduce a visualization
technique that reveals the input stimuli that excite individual feature maps at
any layer in the model.

It also allows us to observe the evolution of features
during training and to diagnose potential problems with the model.

The visualization technique we propose uses a multi-layered Deconvolutional Network
(deconvnet), as proposed by Zeiler et al. [29], to project the feature activations
back to the input pixel space.

 We also perform a sensitivity analysis of the classifier output by occluding portions of the input image, revealing which parts of
the scene are important for classification.

Using these tools, we start with the architecture of Krizhevsky et al. [18] and
explore different architectures, discovering ones that outperform their results
on ImageNet. We then explore the generalization ability of the model to other
datasets, just retraining the softmax classifier on top. As such, this is a form
of supervised pre-training, which contrasts with the unsupervised pre-training
methods popularized by Hinton et al. [13] and others [1,26]
technique that reveals the input stimuli that excite individual feature maps at
any layer in the model.


### 1.1 Related Work
Visualization:

[8] find the
optimal stimulus for each unit by performing gradient descent in image space
to maximize the unit’s activation. This requires a careful initialization and does
not give any information about the unit’s invariances. Motivated by the latter’s
short-coming, [19] (extending an idea by [2]) show how the Hessian of a given
unit may be computed numerically around the optimal response, giving some
insight into invariances. The problem is that for higher layers, the invariances are
extremely complex so are poorly captured by a simple quadratic approximation.
Our approach, by contrast, provides a non-parametric view of invariance, show
ing which patterns from the training set activate the feature map. Our approach
is similar to contemporary work by Simonyan et al. [23] who demonstrate how
saliency maps can be obtained from a convnet by projecting back from the fully
connected layers of the network, instead of the convolutional features that we
use. Girshick et al. [10] show visualizations that identify patches within a dataset
that are responsible for strong activations at higher layers in the model. Our vi
sualizations differ in that they are not just crops of input images, but rather
top-down projections that reveal structures within each patch that stimulate a
particular feature map.
Feature Generalization: Our demonstration of the generalization ability of
convnet features is also explored in concurrent work by Donahue et al. [7] and
Girshick et al. [10]. They use the convnet features to obtain state-of-the-art
performance on Caltech-101 and the Sun scenes dataset in the former case, and
for object detection on the PASCAL VOC dataset, in the latter.

## 2 Approach

> [29]

### 2.1 visualizations with Deconvnet
Understanding the operation of a convnet requires interpreting the feature activity in
intermediate layers.

We present a novel way to map these activities back to the
input pixel space, showing what input pattern originally caused a given activation
in the feature maps. We perform this mapping with a Deconvolutional Network
(deconvnet) Zeiler et al. [29].

 A deconvnet can be thought of as a convnet model
that uses the same components (filtering, pooling) but in reverse, so instead of
mapping pixels to features does the opposite. __In Zeiler et al. [29], deconvnets were
proposed as a way of performing unsupervised learning__.

 Here, they are not used
in any learning capacity, just as a probe of an already trained convnet.
To examine a convnet, a deconvnet is attached to each of its layers, as illustrated in Fig. 1(top), providing a continuous path back to image pixels.

To start,
an input image is presented to the convnet and features computed throughout
the layers. To examine a given convnet activation, we set all other activations in
the layer to zero and pass the feature maps as input to the attached deconvnet
layer. Then we successively (i) unpool, (ii) rectify and (iii) filter to reconstruct
the activity in the layer beneath that gave rise to the chosen activation. This is
then repeated until input pixel space is reached.


Unpooling: In the convnet, the max pooling operation is non-invertible, however we can obtain an approximate inverse by recording the locations of the
maxima within each pooling region in a set of switch variables. In the deconvnet, the unpooling operation uses these switches to place the reconstructions
from the layer above into appropriate locations, preserving the structure of the
stimulus. See Fig. 1(bottom) for an illustration of the procedure.
Rectification: The convnet uses relu non-linearities, which rectify the feature maps thus ensuring the feature maps are always positive. To obtain valid


feature reconstructions at each layer (which also should be positive), we pass the
reconstructed signal through a relu non-linearity1.
Filtering: The convnet uses learned filters to convolve the feature maps from
the previous layer. To approximately invert this, the deconvnet uses transposed
versions of the same filters (as other autoencoder models, such as RBMs), but
applied to the rectified maps, not the output of the layer beneath. In practice
this means flipping each filter vertically and horizontally.
Note that we do not use any contrast normalization operations when in this
reconstruction path. Projecting down from higher layers uses the switch settings
generated by the max pooling in the convnet on the way up. As these switch
settings are peculiar to a given input image, the reconstruction obtained from a
single activation thus resembles a small piece of the original input image, with
structures weighted according to their contribution toward to the feature activation. Since the model is trained discriminatively, they implicitly show which
parts of the input image are discriminative. Note that these projections are not
samples from the model, since there is no generative process involved. The whole
procedure is similar to backpropping a single strong activation (rather than the
usual gradients), i.e. computing ∂X ∂h n , where h is the element of the feature map
with the strong activation and Xn is the input image. However, it differs in
that (i) the the relu is imposed independently and (ii) contrast normalization
operations are not used. A general shortcoming of our approach is that it only
visualizes a single activation, not the joint activity present in a layer. Nevertheless, as we show in Fig. 6, these visualizations are accurate representations of
the input pattern that stimulates the given feature map in the model: when the
parts of the original input image corresponding to the pattern are occluded, we
see a distinct drop in activity within the feature map
