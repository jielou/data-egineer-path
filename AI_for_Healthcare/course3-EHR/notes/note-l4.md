# EHR Transformations & Feature Engineering

## resources
[google nature paper](https://www.nature.com/articles/s41746-018-0029-1)
## key concepts

### EHR Dataset levels

#### Line Level
A denormalized or disaggregated representation of all the things that might happen in a medical visit or encounter.

Think of a visit to the doctor for bronchitis. Your line-level data entries could be:
- A diagnosis code of bronchitis
- A medication code for a cough suppressant
- A procedure code for a test for bronchitis and a line could be a diagnosis or medication that was prescribed. Another line could include information on a lab test that the doctor ordered for informing the diagnosis.

#### Encounter Level
Also known as the visit level, which is the aggregated information from the previously mentioned line level for one encounter. This information can be collapsed into a single row or arrays.

Using the example above, the encounter level for that visit would include the diagnosis code of bronchitis, medication code for a cough suppressant, and the procedure code for a test for bronchitis in one array or list.

#### Longitudinal Level
Also known as the patient level view. This level aggregates the patient history and can show how the culmination of visits/encounter lead to some clinical impact.

Continuing with our example above if the patient contracts bronchitis often, over a series of years, we might gain some insights into a possible autoimmune disease or know exactly what to prescribe the patient when they start seeing symptoms.

### encounter

> An interaction between a patient and healthcare provider(s) for the purpose of providing healthcare service(s) or assessing the health status of a patient. [source](https://www.hl7.org/fhir/encounter-definitions.html)

The definition of an encounter commonly used for EHR records comes from the Health Level Seven International (HL7), the organization that sets the international standards for healthcare data. As the definition states, it is essentially an interaction between a patient and a healthcare professional(s). It usually refers to doctors visits and hospital stays.

### Data Leakage
Inadvertently sharing data between test and training datasets.

#### Representative Splitting
Having accurate labels and demographics in your data splits that reflect the real world. A major challenge for most machine learning problems is a generalization and building a dataset that is representative. Common errors that can occur include:

- Non-representative distribution of your label across the splits
- Non-representative demographics
Example: Only female patients in training and male in testing

This would introduce some unintended biases and issues in your model for procedures that are gender-specific.

#### Testing and Validating Dataset Splitting
It is important to have some ways to assess whether you have split your data right.

Here are a few ways to do this.

1. Assess to make sure that a single patient's data is not in more than one partition to avoid possible data leakage.
2. Check that the total number of unique patients across the splits is equal to the total number of unique patients in the original dataset. This ensures no patient information lost in the splitting and that the counts are correct.
3. Check that the total number of rows in original dataset should be equal to the sum of rows across all three dataset partitions.

`len(original_df) == len(train_df) + len(val_df) + len(test_df)` should evaluate to True.

### ETL with TensorFlow Dataset API Key Points
TF Dataset API: tf.data.Dataset

1. Process your input data in a distributed format.
2. It can be batched and processed in parallel on GPU/TPUs.
3. API builds iterators to batch process and prevents memory loss

**Important Note**: TF Dataset API cannot accept mixed data types. You may need to remove or convert null values.