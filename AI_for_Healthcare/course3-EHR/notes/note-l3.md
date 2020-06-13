# EHR Code Sets

## resources
[IDC10-CM Sepsis Codes](https://www.icd10data.com/ICD10CM/Codes/A00-B99/A30-A49/A41-/A41)
[CDC ICD10-CM Lookup Tool](https://icd10cmtool.cdc.gov/?fy=FY2019)
[ccs website](https://www.hcup-us.ahrq.gov/toolssoftware/ccs10/ccs10.jsp#download)
## key concepts

### medical encounter

An interaction between a patient and healthcare provider(s) for the purpose of providing healthcare service(s) or assessing the health status of a patient.

This could also be online in today's world. During each encounter, one or more codes are generated about your encounter.

1. It is important to note that medical records often go through a process from a written note or some other unstructured input to a structured medical code that is standardized but can be very specific. There is a whole industry of medical coders that take this unstructured information and “code” it to medical code standards and into EHR records.

2. Another piece of information that is relevant to industry codes is whether the encounter occurred in an inpatient or outpatient setting.

    - Inpatient usually refers to hospitalization.
    - Outpatient refers to visits and encounters like visits with your primary care physician or specialists like a cardiologist but do not require hospitalization.
    - Outpatient can also refer to ambulatory care.

It is important to work with subject-matter experts who know the domain and processes at a much deeper level. There are a lot of intricacies and details in healthcare that require you to work deeply with SMEs to understand the context better.


### diagnosis codes
#### What is a diagnosis?
Let’s imagine that you see a doctor and you have some symptoms such as coughing and a stomach ache and then your doctor magically comes up with a diagnosis. As we will learn later this diagnosis is a key piece of information that connects so much of the encounter experience together.

#### ICD10 (International Classification of Diseases 10)

- Also known as ICD10
- Standard developed by WHO: World Health Organization and in 10th revision

#### ICD10-CM (International Classification of Diseases 10 - Clinical Modification)
Diagnosis code standard used in the U.S.

- Maintained by U.S. CDC
- Contains a wide variety of diseases and conditions
- Used for Medical claims, disease epidemic, and mortality tracking

#### ICD9 to 10
The U.S. had been using ICD9 since 1979 until it adopted ICD10 in October of 2014. The US lagged a bit behind the rest of the world who had adopted ICD10 much earlier. The reason for the changes from ICD9 to ICD10 is that the code set was not robust enough to meet future healthcare needs.

Important Changes:

- 14,025 codes => 69,823 codes
- Up to 7 characters
- Created a much higher level of detail
    - Included things like laterality or side of injury

#### ICD10- CM Code Structure

**[ XXX ]**.XXX X

The first part is the category of the diagnosis and it is the first three characters and could be an S code like the injury category. There are 21 different categories and these range from the disease of the respiratory system to injury, poisoning, and certain other consequences of external causes.

XXX.**[ XXX ]**X

The Second is the etiology, anatomic site, and manifestation part which can be up to 3 more characters and is essentially the cause for a condition or disease or the location of the condition.

XXX.XXX **[ X ]**

Finally, the third part is the extension which is the last character and can be tricky b/c it can often be null or has an X placeholder. It is often used with injury-related codes referring to the episode of care.

### encounter with diagnosis
- it can take several encounters for a patient to receive a diagnosis, and therefore a diagnosis code. There may be an initial appointment, some follow-up testing, and then another appointment before a diagnosis is determined. This is very common. This means that there may not be diagnosis codes for every encounter.
- a diagnosis code should never be repeated in the same encounter.
- a diagnosis would carry across different encounters as the patient is being treated for that diagnosis.

### Diagnosis Code Prioritization

- Primary Diagnosis Code: The code that takes up the most resources to treat.
- Principal Diagnosis Code: The diagnosis that is found after hospitalization to be the one that is chiefly responsible.

This can be an important distinction since the admitting diagnosis code can widely differ from the final, Principal Diagnosis. For the most part, these terms interchangeably but it's good to be aware of the differences and the need to dig into the details when necessary.

- Secondary Diagnosis Codes: The other diagnosis codes listed on an encounter.
For example, if a patient were to have a knee replacement surgery but had type 2 diabetes as a prior condition, the secondary diagnosis code of type 2 diabetes would be included in the medical record.

#### Note: 
- Secondary diagnoses codes can include many additional codes
- the primary diagnosis is the first, while the principal is the main cause or most severe

### procedure codes
the categorization of the medical codes during an encounter. It's important to note if a procedure is inpatient or outpatient.

#### ICD10 PCS: Procedure Coding Systems
- Only for Inpatient
- 72,000+ codes as of 2019
- Focus on medical and surgical

code structure:
- 7 alphanumeric characters [A-Z, 0-9]
- 1st character is the Section
    - Reference Section codes categories in the table above
- Subsequent characters relate to the Section and give:
    - Body System
    - Body Part
    - Approach
    - Device used for a procedure

example:

027004Z. This is a Heart Surgery code that relates to:

- Dilation of Coronary Artery
- One Site with Drug-eluting Intraluminal Device
- Open Approach

You can see the breakdown in the image above. In the table, you can see that this code starts with 0, which is the Medical category. If you look over the link [PCS Procedure Code System](https://www.cms.gov/Medicare/Coding/ICD10/Downloads/2014-pcs-procedure-coding-system.pdf), you can further see where the rest of the code breaks down.

- 0 = Medical
- 2 = Heart and Great Vessels
- 7 = Dilation
- 0 = Coronary Artery, One Site
- 0 = Open Approach
- 4 = Drug-eluting Intraluminal Device
- Z = No Qualifier
#### CPT: Current Procedural Terminology
- Outpatient focused but can apply to physician visits in ambulatory settings
- 10,000+ codes as of 2019
- Focus on professional services by physician

code structure:
- Up to 5 numbers
- 3 Categories
    - Category 1: Billable codes
        - 10 sections largely split along biological systems which are broken out in the image above
    - Category 2:
        - Five digits that end in F
        - Non-billable
        - Performance measure focused on physicals and patient history
    - Category 3:
        - Services and procedures using emerging technology
#### HCPCS: Healthcare Common Procedure Coding System
- Inpatient and outpatient
- Has 3 levels
    - L1: CPT Codes
    - L2: Non-physician services
        - DME: Durable Medical Equipment
        - Ambulatory Services
        - Dental
    - L3: Medicare/Medicaid related

### medication codes

#### NDC (National Drug Code)
- since 1972
- maintained by FDAA

#### NDC Code Structure
- 10- to 11-digit code
    - multiple configurations

- 3 Parts
    - Labeler: Drug manufacturer
    - Product code: the actual drug details
    - Package code: form and size of medication

### CCS - Clinical Classifications Software

As mentioned earlier, there is a tremendous challenge of taking the 77K+ ICD10 PCS codes and categorizing them into meaningful categories at scale. This is where a government-industry partnership called the Healthcare Cost and Utilization Project (HCUP) created a categorization system called clinical classifications software or CCS. It can be used to map diagnosis or procedure codes from ICD code sets. It has single or multi-level options for mapping these codes.

#### Single Level Categories
- Mutually exclusive categories
- 285 categories for diagnoses
- 231 categories for procedures

As an example using single-level codes:

- Operations on the cardiovascular system are codes 43-63
- Heart valve procedures is code 43.

#### Other Categorization Systems
- MS- DRG- Medicare Severity-Diagnosis Related Group
    - Group payment based on the principal diagnosis
    - Up to 25 secondary dx
    - Up to 25 procedures during a visit/encounter
- SNOMED CT- Systematized Nomenclature of Medicine—Clinical Terms
    - License to use
    - Helpful for making the EHR records interoperable