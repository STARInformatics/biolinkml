# Class: genomic sequence localization


A relationship between a sequence feature and an entity it is localized to. The reference entity may be a chromosome, chromosome region or information entity such as a contig

URI: [https://w3id.org/biolink/biolink-model/GenomicSequenceLocalization](https://w3id.org/biolink/biolink-model/GenomicSequenceLocalization)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Provider]<provided%20by(i)%200..1-%20\[GenomicSequenceLocalization|start_interbase_coordinate:string%20%3F;end_interbase_coordinate:string%20%3F;genome_build:string%20%3F;phase:string%20%3F;id(i):identifier_type;relation(i):iri_type;negated(i):boolean%20%3F;association_slot(i):string%20%3F],%20\[Publication]<publications(i)%200..*-%20\[GenomicSequenceLocalization],%20\[OntologyClass]<qualifiers(i)%200..*-%20\[GenomicSequenceLocalization],%20\[OntologyClass]<association%20type(i)%200..1-%20\[GenomicSequenceLocalization],%20\[GenomicEntity]<object%201..1-%20\[GenomicSequenceLocalization],%20\[GenomicEntity]<subject%201..1-%20\[GenomicSequenceLocalization],%20\[Association]^-\[GenomicSequenceLocalization])
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
 * [end interbase coordinate](end_interbase_coordinate.md)  <sub>OPT</sub>
    * range: [String](String.md)
 * [genome build](genome_build.md)  <sub>OPT</sub>
    * Description: TODO
    * range: [String](String.md)
 * [genomic sequence localization.object](genomic_sequence_localization_object.md)  <sub>REQ</sub>
    * range: [GenomicEntity](GenomicEntity.md)
 * [genomic sequence localization.subject](genomic_sequence_localization_subject.md)  <sub>REQ</sub>
    * range: [GenomicEntity](GenomicEntity.md)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](Boolean.md)
    * inherited from: [Association](Association.md)
 * [phase](phase.md)  <sub>OPT</sub>
    * Description: TODO
    * range: [String](String.md)
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
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: the relationship type by which a subject is connected to an object in an association
    * range: [IriType](IriType.md)
    * inherited from: [Association](Association.md)
 * [start interbase coordinate](start_interbase_coordinate.md)  <sub>OPT</sub>
    * range: [String](String.md)
