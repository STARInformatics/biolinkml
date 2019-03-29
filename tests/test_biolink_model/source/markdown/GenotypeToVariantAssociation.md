# Class: genotype to variant association


Any association between a genotype and a sequence variant.

URI: [https://biolink.github.io/biolink-model/ontology/biolink.ttl/GenotypeToVariantAssociation](https://biolink.github.io/biolink-model/ontology/biolink.ttl/GenotypeToVariantAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Provider]<provided%20by(i)%200..1-%20\[GenotypeToVariantAssociation|relation:iri_type;id(i):identifier_type;negated(i):boolean%20%3F;association_slot(i):string%20%3F],%20\[Publication]<publications(i)%200..*-%20\[GenotypeToVariantAssociation],%20\[OntologyClass]<qualifiers(i)%200..*-%20\[GenotypeToVariantAssociation],%20\[OntologyClass]<association%20type(i)%200..1-%20\[GenotypeToVariantAssociation],%20\[SequenceVariant]<object%201..1-%20\[GenotypeToVariantAssociation],%20\[Genotype]<subject%201..1-%20\[GenotypeToVariantAssociation],%20\[Association]^-\[GenotypeToVariantAssociation])
## Inheritance

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence
## Children

## Used by

## Fields

 * [association slot](association_slot.md)  <sub>OPT</sub>
    * Description: any slot that relates an association to another entity
    * range: [String](String.md)
    * inherited from: [Association](Association.md)
 * [association type](association_type.md)  <sub>OPT</sub>
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [OntologyClass](OntologyClass.md)
    * inherited from: [Association](Association.md)
 * [association.id](association_id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an association
    * range: [IdentifierType](IdentifierType.md)
    * inherited from: [Association](Association.md)
    * in subsets: (translator_minimal)
 * [genotype to variant association.object](genotype_to_variant_association_object.md)  <sub>REQ</sub>
    * range: [SequenceVariant](SequenceVariant.md)
 * [genotype to variant association.relation](genotype_to_variant_association_relation.md)  <sub>REQ</sub>
    * range: [IriType](IriType.md)
 * [genotype to variant association.subject](genotype_to_variant_association_subject.md)  <sub>REQ</sub>
    * range: [Genotype](Genotype.md)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](Boolean.md)
    * inherited from: [Association](Association.md)
 * [provided by](provided_by.md)  <sub>OPT</sub>
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Provider](Provider.md)
    * inherited from: [Association](Association.md)
 * [publications](publications.md)  <sub>0..*</sub>
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)
    * inherited from: [Association](Association.md)
 * [qualifiers](qualifiers.md)  <sub>0..*</sub>
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)
    * inherited from: [Association](Association.md)
