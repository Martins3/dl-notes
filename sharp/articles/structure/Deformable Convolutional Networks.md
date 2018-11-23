## Abstruct
 In
this work, we introduce two new modules to enhance the
transformation modeling capability of CNNs, namely, deformable convolution and deformable RoI pooling. Both
are based on the idea of augmenting the spatial sampling
locations in the modules with additional offsets and learning the offsets from the target tasks, without additional
supervision

## 1. Introduction
A key challenge in visual recognition is how to accommodate geometric variations or model geometric transformations in object scale, pose, viewpoint, and part deformation. In general, there are two ways. The first is to build the
training datasets with sufficient desired variations.
The second is to use transformation-invariant features and algorithms.

There are two drawbacks in above ways. First, the geometric transformations are assumed fixed and known. Such prior knowledge is used to augment the data, and design the
features and algorithms. This assumption prevents generalization to new tasks possessing unknown geometric transformations, which are not properly modeled. Second, handcrafted design of invariant features and algorithms could be
difficult or infeasible for overly complex transformations,
even when they are known.



In this work, we introduce two new modules that greatly
enhance CNNs’ capability of modeling geometric transfor
mations. The first is deformable convolution.
The second is deformable RoI pooling.



> The offsets are learned from the preceding feature maps, via additional
convolutional layers. Thus, the deformation is conditioned
on the input features in a local, dense, and adaptive manner. 看不懂啊 ？
> 个人的直觉告诉我，这一个东西为什么可以 learn , 而且为什么可以从preceding features maps


## 2. Deformable Convolutional Networks
The feature maps and convolution in CNNs are 3D. Both
deformable convolution and RoI pooling modules operate
on the 2D spatial domain. The operation remains the same
across the channel dimension. Without loss of generality,
the modules are described in 2D here for notation clarity.
Extension to 3D is straightforward

### 2.1. Deformable Convolution
