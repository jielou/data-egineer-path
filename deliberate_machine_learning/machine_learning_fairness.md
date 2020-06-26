# machine learning fairness

## resources

[A Survey on Bias and Fairness in Machine Learning](https://arxiv.org/abs/1908.09635)
[Attacking discrimination with smarter machine learning](https://research.google.com/bigpicture/attacking-discrimination-in-ml/)
[Equality of Opportunity in Supervised Learning](https://arxiv.org/abs/1610.02413)
[The Measure and Mismeasure of Fairness: A Critical Review of Fair Machine Learning](https://arxiv.org/abs/1808.00023)
[Mitigating Unwanted Biases with Adversarial Learning](https://arxiv.org/abs/1801.07593)
[AI Explainability Whitepaper](https://storage.googleapis.com/cloud-ai-whitepapers/AI%20Explainability%20Whitepaper.pdf)
## what is fairness and discrimination
Broadly, fairness is the absence of any prejudice or favoritism towards an individual or a group based on their intrinsic or acquired traits in the context of decision-making

### direct discrimination
Direct discrimination happens when protected attributes of individuals explicitly result in non-favorable outcomes toward them

### Indirect Discrimination. 
In Indirect discrimination, individuals appear to be treated based on seemingly neutral and non-protected attributes; however, protected groups or individuals
still get to be treated unjustly as a result of implicit effects from their protected attributes

## definitions of fairness

### equalized odds
This means that the probability of a person in the positive class being correctly assigned a positive outcome and the probability of a person in a negative class being incorrectly assigned a positive outcome should both be the same for the protected and unprotected (male and female) group members

### equal opportunity
This means that the probability of a person in a positive class being assigned to a positive outcome should be equal for both protected and unprotected (female and male) group members. In other words, the equal opportunity definition states that the protected and unprotected groups should have equal true positive rates.

### demographic parity
The likelihood of a positive outcome should be the same regardless of whether the person is in the protected (e.g., female) group.

### fairness through awareness
any two individuals who are similar with respect to a similarity (inverse distance) metric defined for a particular task should receive a similar outcome.

### Fairness Through Unawareness
An algorithm is fair as long as any protected attributes A are not explicitly used in the decision-making process

### Treatment Equality
Treatment equality is achieved when the ratio of false negatives and false positives is the same for both protected group categories

### 


## tools in detecting unfairness

- SAVRY: tool used in risk assessment frameworks
- Aequitas: let users test models with regards to several bias and fairness
- AI Fairness 360: from IBM

## types of bias
### historical bias
the already existing bias and socio-technical issues in the world and can seep into from the data generation process even given a perfect sampling and feature selection

### Representation Bias. 
happens from the way we define and sample from a population

### Measurement Bias. 
happens from the way we choose, utilize, and measure a particular feature

### Evaluation Bias
Evaluation bias happens during model evaluation

### Aggregation Bias. 
Aggregation bias happens when false conclusions are drawn for a subgroup based on observing other different subgroups or generally when false assumptions about a population affect the model’s outcome and definition

### Population bias 
arises when statistics, demographics, representatives, and
user characteristics are different in the user population represented in the dataset or platform from the original target population

### Simpson’s Paradox. 
Simpson’s paradox can bias the analysis of heterogeneous data that is composed of subgroups or individuals with different behaviors. According to Simpson’s paradox, a trend, association, or characteristic observed in underlying subgroups may be quite
different from association or characteristic observed when these subgroups are aggregated.

### Algorithmic Bias. 
Algorithmic bias is when the bias is not present in the input data and is added purely by the algorithm