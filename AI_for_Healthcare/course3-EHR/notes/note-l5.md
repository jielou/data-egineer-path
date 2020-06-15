# Building, Evaluating & Interpreting Models

## resources
[Tensorflow Regression with Probabilistic Layers Tutorial](https://blog.tensorflow.org/2019/03/regression-with-probabilistic-layers-in.html)
[LIME](https://arxiv.org/pdf/1602.04938.pdf)
[Shapley values](https://github.com/slundberg/shap)
[Shapley values explanations](https://www.analyticsvidhya.com/blog/2019/11/shapley-value-machine-learning-interpretability-game-theory/)


## key concepts

### biases

#### Unintended biases
a bias that is not intentional and often is not even apparent to the creator of a model

Unintended biases represent the unconscious or unintentional biases that come with the AI models that we are building. Becoming more aware of these biases and how they impact different groups is key.

#### Aequitas
- Developed by University of Chicago Data Science for Social Good
- Addresses concerns about unintended bias unfairly affecting certain groups
- Definitions and metrics for unintended bias in predictive models

### uncertainty

#### Aleatoric
- Statistical Uncertainty - a natural, random process
- Known Unknowns

Aleatoric uncertainty is otherwise known as statistical uncertainty and is known unknowns. This type of uncertainty is inherent, and just a part of the stochasticity that naturally exists. An example is rolling a dice, which will have an element of randomness always to it.

#### Epistemic
- Systematic Uncertainty - lack of measurement, knowledge
- Unknown Unknowns

Epistemic uncertainty is also known as systemic uncertainty and is unknown unknowns. This type of uncertainty can be improved by adding parameters/features that might measure something in more detail or provide more knowledge.

### Model Agnostic
methods that can be used on deep learning models or traditional ml models A few methods we can use for interpreting deep learning models that are also model agnostic include:

#### LIME or Local Interpretable Model-Agnostic Explanations
- Can scale to large datasets
- Can be difficult to find the right kernel
- Can have unstable interpretations

#### Shapley Values
Shapley values are based on game theory and provide the marginal contributions of features by taking the permutations of different features and then the differences between the prediction output. You can learn more about these in the links below.
- A method that measures the marginal contributions of features
- Can be computationally expensive