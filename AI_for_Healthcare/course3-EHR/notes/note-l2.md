# EHR Data Security and Analysis

## resources
[Value of Medical Data on the Dark web](https://www.experian.com/blogs/ask-experian/heres-how-much-your-personal-information-is-selling-for-on-the-dark-web/)
[Hacker Hone their Techniques](https://www.healthcareitnews.com/news/healthcare-data-big-risk-hackers-innovate-and-hone-their-techniques)

## key concepts

### Patients, Providers & Data Users

#### providers:
These are entities/groups/individuals that provide care for patients. Providers can range in size from entire hospital networks to individual doctors and medical professionals. Some examples are:
- healthcare professionals treating you at a hospital
- in a doctor’s clinic
- dentist office

This interaction between a patient and a provider results in the production of an Electronic Health Record or EHR. Electronic health records can be used by data users, too.

#### payers
a group that consists of companies like healthcare insurance. Payers can also include entities such as the government for things like Medicaid and Medicare in the United States.

### data security

#### from patient
Data security is crucially important for many different reasons in healthcare, but here are a couple of very important reasons:
- Patients have a right to privacy and may not want to share their conditions and treatments with others.
- Medical data is far more valuable to hackers. Because of the detail and complexity of data in EHR, hackers can very easily impersonate a patient. You can learn more about this in the links below.

#### from provider
Medical professionals/organizations that are “providing” care to patients are under strict regulatory compliance laws. Your organization will handle the intricacies of how to interface with providers or if your organization is one, they have extensive training as part of the required HIPAA compliance. You'll learn more about HIPAA in a bit. To make sure organizations comply, there are some penalties and they can change periodically over time. Please check the HIPAA website to be up to date.

### Key Industry Regulations
Healthcare data security and privacy regulations are ubiquitous around the world. Most countries have regulations regarding data security and privacy around electronic health records with varying levels of complexity. However, for this course, we will focus on U.S. healthcare regulations.

#### United States:
- HIPAA: The Health Insurance Portability and Accountability Act is the key industry regulation that you should be familiar within the U.S.
HITECH: The Health Information Technology for Economic and Clinical Health Act is also important to note and this is really just an update to HIPAA that accounts for technology.
- HIPAA was passed in 1996 and then updated in 2009 under the HITECH act to evolve for digital technologies. While it might seem like EHR has been around for a while, it was only a little over a decade ago when the foundational legislation really was put in place that made the healthcare community start moving towards digitizing and putting their records in electronic format. Even now many systems are legacy systems that are built off of transcribed handwritten notes and other unstructured formats that organizations are spending large amounts of time to normalize and aggregate this info.

#### EU: European Union
- GDPR: The General Data Protection Regulation is generally considered more stringent than even HIPAA when it comes to protections for patients.
#### United Kingdom:
- DPA: The Data Protection Act really builds off of and add to GDPR

### PHI (Protected Health Information)
Probably one of the most important terms that you should be familiar with is PHI, which stands for protected health information. PHI is a part of HIPAA that protects the transmission of certain types of personally identifiable information such as name, address, and other info. Certain information in an electronic medical record is considered PHI and must comply with HIPAA standards around data security and privacy. This informs not only how you transmit and store data but also data usage rights and restrictions around building models for other purposes than the original use.

PHI by nature is identifiable information and can be used to easily identify a person. However, please note that omitting this information does not ensure that a person can not be identified.

### Covered Entities
a group of industry organizations defined by HIPAA to be one of three groups: health insurance plans, providers, or clearinghouses. You can see from the table the types of entities in each category.

These groups transmit protected health information and are subject to HIPAA regulations regarding these transmissions.

#### Other Covered Entities:

- Business Associates: A business associate is a person or entity that performs certain functions or activities that involve the use or disclosure of protected health information on behalf of, or provides services to, a covered entity.

Covered entities can disclose to BAs under Privacy Rule
- Only for a purpose allowed by the covered entity
- Safeguard data against misuse
- Comply with other requirements of the covered entity under HIPAA Privacy Rule

- Business Associates Agreement/Addendum (BAA): this is the contract between a covered entity and BA

### De-identifying a Dataset
 the removal of identifying fields like name, address from a dataset. De-Identification is done to reduce privacy risks to individuals and support the secondary use of data for research and such.

This is not something you should be doing on your own. HIPAA has two ways that you can use to de-identify a dataset:

- Expert Determination Method: done by a statistician that determines there is a small risk that an individual could be identified.

- Safe Harbor: the removal of 18 identifiers like name, zip code, etc.

Limited Latitude: Very limited scope of work. EHR Data can only be used for the purpose granted.

### Data Schema Analysis
- EDA: Exploratory Data Analysis

    EDA is a ste p in the data science process that is often overlooked for the modeling and evaluation phase that can be easier to quantify and benchmark.

    Reasons EDA is important:
    - EDA can enable you to discover features or data transformations/aggregations that might have data leakage. This can save a tremendous amount of time and prevent you from building a flawed model.
    - EDA can help you better translate and define modeling objectives and corresponding evaluation metrics from a machine learning/data science and business perspective.
    - EDA can help inform strategies for handling missing/null/zero valued data. This is a common issue that you will encounter with EHR data that you will have missing values and have to determine imputing strategies accordingly.
    - EDA can help to identify subsets of features to utilize for feature engineering and modeling along with appropriate feature transformations based off of type (e.g. categorical vs numerical features)

- CRISP-DM: This stands for “cross-industry standard process for data mining” and is a common framework used for data science projects and includes a series of steps from business understanding to deployment.

### Missing Data Classification
#### MCAR (Missing Completely at Random) 
This means that the data is missing due to something unrelated to the data and there is no systematic reason for the missing data. In other words, there is an equal probability that data is missing for all cases. This is often due to some instrumentation like a broken instrument or process issue where some of the data is randomly missing.Example: White cell value Data is missing because a testing machine was improperly calibrated.

#### MAR (Missing at Random)
this is the opposite case where there is some systematic relationship between data and the probability of missing data. For example, there might be some missing demographics choices in surveys. Example: Women could be less likely to give their weight on a survey.

#### MNAR (Missing Not at Random)
this usually means there is a relationship between a value in the dataset and the missing values. Example: Those with low education are not accounted for in a study.

Understanding why data is missing help with choosing the best imputing method to fill or drop the values in your dataset.

### High Cardinality
#### Cardinality
refers to the number of unique values that a feature has and is relevant to EHR datasets because there are code sets such as diagnosis codes in the order of tens of thousands of unique codes. This only applies to categorical features and the reason this is a problem is that it can increase dimensionality and makes training models much more difficult and time-consuming.

#### How do we define a field with high cardinality?

- Determine if it is a categorical feature.
- Determine if it has a high number of unique values. This can be a bit subjective but we can probably agree that for a field with 2 unique values would not have high cardinality whereas a field like diagnosis codes might have tens of thousands of unique values would have high cardinality.
- Use the nunique() method to return the number of unique values for the categorical categories above.

### Demographic Analysis
The reason that demographic analysis is so important, especially in healthcare, is that we need our clinical trials and machine learning models to be able to representative to general population. While this is not always completely possible given limited trials and very rare conditions it is something we need to strive for and identify as early as possible if there may be an issue.

If we don't have a properly representative demographic dataset, we wouldn't know how a drug or prediction might impact a certain age, race or gender which could lead to significant issues for those not represented.

When completing a demographic analysis, it can be helpful to group data into buckets or bins.


