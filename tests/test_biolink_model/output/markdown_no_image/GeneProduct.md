
# Type: gene product


The functional molecular product of a single gene. Gene products are either proteins or functional RNA molecules

URI: [biolink:GeneProduct](https://w3id.org/biolink/vocab/GeneProduct)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Transcript],[Protein],[OrganismTaxon],[NamedThing],[GeneToGeneProductRelationship],[GeneToGeneProductRelationship]-%20object%201..1>[GeneProduct&#124;synonym:label_type%20*;xref:iri_type%20*;name(i):symbol_type%20%3F;has_biological_sequence(i):biological_sequence%20%3F;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[GeneProduct]^-[Transcript],[GeneProduct]^-[Protein],[GeneProduct]^-[RNAProduct],[GeneOrGeneProduct]^-[GeneProduct],[GeneOrGeneProduct],[Gene],[Attribute],[Agent],[RNAProduct])

## Parents

 *  is_a: [GeneOrGeneProduct](GeneOrGeneProduct.md) - a union of genes or gene products. Frequently an identifier for one will be used as proxy for another

## Children

 * [RNAProduct](RNAProduct.md)
 * [Protein](Protein.md) - A gene product that is composed of a chain of amino acid sequences and is produced by ribosome-mediated translation of mRNA
 * [Transcript](Transcript.md) - An RNA synthesized on a DNA or RNA template by an RNA polymerase

## Referenced by class

 *  **[GeneToGeneProductRelationship](GeneToGeneProductRelationship.md)** *[gene to gene product relationship➞object](gene_to_gene_product_relationship_object.md)*  <sub>REQ</sub>  **[GeneProduct](GeneProduct.md)**
 *  **[Gene](Gene.md)** *[has gene product](has_gene_product.md)*  <sub>0..*</sub>  **[GeneProduct](GeneProduct.md)**

## Attributes


### Own

 * [synonym](synonym.md)  <sub>0..*</sub>
    * Description: Alternate human-readable names for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)
 * [xref](xref.md)  <sub>0..*</sub>
    * Description: Alternate CURIEs for a thing
    * range: [IriType](types/IriType.md)
    * in subsets: (translator_minimal)

### Inherited from gene or gene product:

 * [description](description.md)  <sub>OPT</sub>
    * Description: a human-readable description of an entity
    * range: [NarrativeText](types/NarrativeText.md)
    * in subsets: (translator_minimal)
 * [has attribute](has_attribute.md)  <sub>0..*</sub>
    * Description: connects any entity to an attribute
    * range: [Attribute](Attribute.md)
    * in subsets: (samples)
 * [has biological sequence](has_biological_sequence.md)  <sub>OPT</sub>
    * Description: connects a genomic feature to its sequence
    * range: [BiologicalSequence](types/BiologicalSequence.md)
 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [iri](iri.md)  <sub>OPT</sub>
    * Description: An IRI for an entity. This is determined by the id using expansion rules.
    * range: [IriType](types/IriType.md)
    * in subsets: (translator_minimal,samples)
 * [macromolecular machine➞name](macromolecular_machine_name.md)  <sub>OPT</sub>
    * Description: genes are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name
    * range: [SymbolType](types/SymbolType.md)
 * [named thing➞category](named_thing_category.md)  <sub>1..*</sub>
    * range: [NamedThing](NamedThing.md)
 * [provided by](provided_by.md)  <sub>0..*</sub>
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Agent](Agent.md)
 * [source](source.md)  <sub>OPT</sub>
    * Description: a lightweight analog to the association class 'has provider' slot, which is the string name, or the authoritative (i.e. database) namespace, designating the origin of the entity to which the slot belongs.
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)
 * [type](type.md)  <sub>OPT</sub>
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | WIKIDATA:Q424689 |
|  | | GENO:0000907 |
|  | | NCIT:C26548 |

