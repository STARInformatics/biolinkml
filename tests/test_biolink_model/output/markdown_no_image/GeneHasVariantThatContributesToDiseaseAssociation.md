
# Type: gene has variant that contributes to disease association




URI: [biolink:GeneHasVariantThatContributesToDiseaseAssociation](https://w3id.org/biolink/vocab/GeneHasVariantThatContributesToDiseaseAssociation)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SeverityValue],[SequenceVariant],[Publication],[OntologyClass],[Onset],[NamedThing],[GeneToDiseaseAssociation],[GeneOrGeneProduct],[GeneOrGeneProduct]<subject%201..1-%20[GeneHasVariantThatContributesToDiseaseAssociation&#124;predicate(i):predicate_type;relation(i):uriorcurie;negated(i):boolean%20%3F;type(i):string%20%3F;id(i):string;iri(i):iri_type%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[SequenceVariant]<sequence%20variant%20qualifier%200..1-%20[GeneHasVariantThatContributesToDiseaseAssociation],[GeneToDiseaseAssociation]^-[GeneHasVariantThatContributesToDiseaseAssociation],[FrequencyValue],[Attribute],[Association],[Agent])

## Parents

 *  is_a: [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md)

## Referenced by class


## Attributes


### Own

 * [gene has variant that contributes to disease association➞subject](gene_has_variant_that_contributes_to_disease_association_subject.md)  <sub>REQ</sub>
    * Description: A gene that has a role in modeling the disease. This may be a model organism ortholog of a known disease gene, or it may be a gene whose mutants recapitulate core features of the disease.
    * range: [GeneOrGeneProduct](GeneOrGeneProduct.md)
 * [sequence variant qualifier](sequence_variant_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in an association with the variant
    * range: [SequenceVariant](SequenceVariant.md)

### Inherited from gene to disease association:

 * [association➞category](association_category.md)  <sub>1..*</sub>
    * range: [Association](Association.md)
 * [association➞type](association_type.md)  <sub>OPT</sub>
    * Description: rdf:type of biolink:Association should be fixed at rdf:Statement
    * range: [String](types/String.md)
 * [description](description.md)  <sub>OPT</sub>
    * Description: a human-readable description of an entity
    * range: [NarrativeText](types/NarrativeText.md)
    * in subsets: (translator_minimal)
 * [has attribute](has_attribute.md)  <sub>0..*</sub>
    * Description: connects any entity to an attribute
    * range: [Attribute](Attribute.md)
    * in subsets: (samples)
 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [iri](iri.md)  <sub>OPT</sub>
    * Description: An IRI for an entity. This is determined by the id using expansion rules.
    * range: [IriType](types/IriType.md)
    * in subsets: (translator_minimal,samples)
 * [name](name.md)  <sub>OPT</sub>
    * Description: A human-readable name for an attribute or entity.
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal,samples)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](types/Boolean.md)
 * [object](object.md)  <sub>REQ</sub>
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)
 * [predicate](predicate.md)  <sub>REQ</sub>
    * Description: A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
    * range: [PredicateType](types/PredicateType.md)
 * [provided by](provided_by.md)  <sub>0..*</sub>
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Agent](Agent.md)
 * [publications](publications.md)  <sub>0..*</sub>
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)
 * [qualifiers](qualifiers.md)  <sub>0..*</sub>
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: The relation which describes an association between a subject and an object in a more granular manner. Usually this is a term from Relation Ontology, but it can be any edge CURIE.
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [source](source.md)  <sub>OPT</sub>
    * Description: a lightweight analog to the association class 'has provider' slot, which is the string name, or the authoritative (i.e. database) namespace, designating the origin of the entity to which the slot belongs.
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)
