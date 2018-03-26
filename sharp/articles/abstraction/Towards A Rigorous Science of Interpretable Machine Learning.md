# Towards A Rigorous Science of Interpretable Machine Learning.md
The first evaluates interpretability in the context of an application: if the system is useful in either a practical application or a simplified version of it, then it must be somehow interpretable The second evaluates interpretability via a quantifiable proxy: a researcher might first
claim that some model class|e.g. sparse linear models, rule lists, gradient boosted trees|are
interpretable and then present algorithms to optimize within that class


To large extent, both evaluation approaches rely on some notion of \you’ll know it when you
see it." Should we be concerned about a lack of rigor? Yes and no: the notions of interpretability
above appear reasonable because they are reasonable: they meet the first test of having facevalidity on the correct test set of subjects: human beings. However, this basic notion leaves many
kinds of questions unanswerable: Are all models in all defined-to-be-interpretable model classes
equally interpretable? Quantifiable proxies such as sparsity may seem to allow for comparison, but
how does one think about comparing a model sparse in features to a model sparse in prototypes?
Moreover, do all applications have the same interpretability needs? If we are to move this field
forward|to compare methods and understand when methods may generalize|we need to formalize
these notions and make them evidence-based.

## 1 What is Interpretability?