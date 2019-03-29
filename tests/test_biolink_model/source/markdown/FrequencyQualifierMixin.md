# Class: frequency qualifier mixin


Qualifier for freqency type associations

URI: [https://biolink.github.io/biolink-model/ontology/biolink.ttl/FrequencyQualifierMixin](https://biolink.github.io/biolink-model/ontology/biolink.ttl/FrequencyQualifierMixin)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[FrequencyValue]<frequency%20qualifier%200..1-%20\[FrequencyQualifierMixin],%20\[VariantToPopulationAssociation]uses%20-.->\[FrequencyQualifierMixin],%20\[FrequencyQualifierMixin]^-\[EntityToFeatureOrDiseaseQualifiers])
## Inheritance

## Children

 * [EntityToFeatureOrDiseaseQualifiers](EntityToFeatureOrDiseaseQualifiers.md) - Qualifiers for entity to disease or phenotype associations
 * [VariantToPopulationAssociation](VariantToPopulationAssociation.md) (mixin)  - An association between a variant and a population, where the variant has particular frequency in the population
## Used by

## Fields

 * [frequency qualifier](frequency_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject
    * range: [FrequencyValue](FrequencyValue.md)
