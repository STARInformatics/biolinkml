# Class: sequence variant


An allele that varies in its sequence from what is considered the reference allele at that locus.

URI: [biolink:SequenceVariant](https://w3id.org/biolink/vocab/SequenceVariant)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[OrganismTaxon]<in%20taxon(i)%200..*-%20\[SequenceVariant|id:identifier_type;has_biological_sequence:biological_sequence%20%3F;name(i):label_type%20%3F;category(i):iri_type%20*;node_property(i):string%20%3F;iri(i):iri_type%20%3F;synonym(i):label_type%20*;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;creation_date(i):date%20%3F;update_date(i):date%20%3F;has_chemical_formula(i):chemical_formula_value%20%3F;aggregate_statistic(i):string%20%3F;interbase_coordinate(i):string%20%3F],%20\[Gene]<has%20gene%200..*-%20\[SequenceVariant],%20\[GeneHasVariantThatContributesToDiseaseAssociation]-%20sequence%20variant%20qualifier%200..1>\[SequenceVariant],%20\[GenomicEntity]^-\[SequenceVariant])
## Inheritance

 *  is_a: [GenomicEntity](GenomicEntity.md) - an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)
## Children

## Used by

 *  **[GenotypeToVariantAssociation](GenotypeToVariantAssociation.md)** *[genotype to variant association.object](genotype_to_variant_association_object.md)*  <sub>REQ</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md)** *[sequence variant modulates treatment association.subject](sequence_variant_modulates_treatment_association_subject.md)*  <sub>REQ</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md)** *[sequence variant qualifier](sequence_variant_qualifier.md)*  <sub>OPT</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md)** *[variant to phenotypic feature association.subject](variant_to_phenotypic_feature_association_subject.md)*  <sub>REQ</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[VariantToPopulationAssociation](VariantToPopulationAssociation.md)** *[variant to population association.subject](variant_to_population_association_subject.md)*  <sub>REQ</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[VariantToThingAssociation](VariantToThingAssociation.md)** *[variant to thing association.subject](variant_to_thing_association_subject.md)*  <sub>REQ</sub>  **[SequenceVariant](SequenceVariant.md)**
## Fields

 * [affects abundance of](affects_abundance_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one changes the amount of the other within a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [affects activity of](affects_activity_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one changes the activity of the other within a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [affects degradation of](affects_degradation_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one impacts the rate of degradation of the other within a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [affects expression of](affects_expression_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one changes the level of expression of the other within a system of interest
    * range: [GenomicEntity](GenomicEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [affects folding of](affects_folding_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one changes the rate or quality of folding of the other
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [affects localization of](affects_localization_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one changes the localization of the other within a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [affects metabolic processing of](affects_metabolic_processing_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one impacts the metabolic processing of the other within a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [affects molecular modification of](affects_molecular_modification_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one leads changes in the molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [affects mutation rate of](affects_mutation_rate_of.md)  <sub>0..*</sub>
    * Description: holds between a molecular entity and a genomic entity where the action or effect of the molecular entity impacts the rate of mutation of the genomic entity within a system of interest
    * range: [GenomicEntity](GenomicEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [affects response to](affects_response_to.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one impacts the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [affects secretion of](affects_secretion_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one impacts the rate of secretion of the other out of a cell, gland, or organ
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [affects splicing of](affects_splicing_of.md)  <sub>0..*</sub>
    * Description: holds between a molecular entity and an mRNA where the action or effect of the molecular entity impacts the splicing of the mRNA
    * range: [Transcript](Transcript.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [affects stability of](affects_stability_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one impacts the stability of the other within a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [affects synthesis of](affects_synthesis_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one impacts the rate of chemical synthesis of the other
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [affects transport of](affects_transport_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one impacts the rate of transport of the other across some boundary in a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [affects uptake of](affects_uptake_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one impacts the rate of uptake of the other into of a cell, gland, or organ
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [biomarker for](biomarker_for.md)  <sub>0..*</sub>
    * Description: holds between a measurable molecular entity and a disease or phenotypic feature, where the entity is used as an indicator of the presence or state of the disease or feature.
    * range: [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>0..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [decreases abundance of](decreases_abundance_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one decreases the amount of the other within a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [decreases activity of](decreases_activity_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one decreases the activity of the other within a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [decreases degradation of](decreases_degradation_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one decreases the rate of degradation of the other within a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [decreases expression of](decreases_expression_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one decreases the level of expression of the other within a system of interest
    * range: [GenomicEntity](GenomicEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [decreases folding of](decreases_folding_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one decreases the rate or quality of folding of the other
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [decreases localization of](decreases_localization_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one decreases the proper localization of the other within a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [decreases metabolic processing of](decreases_metabolic_processing_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one decreases the rate of metabolic processing of the other within a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [decreases molecular modification of](decreases_molecular_modification_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one leads to decreased molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [decreases mutation rate of](decreases_mutation_rate_of.md)  <sub>0..*</sub>
    * Description: holds between a molecular entity and a genomic entity where the action or effect of the molecular entity decreases the rate of mutation of the genomic entity within a system of interest
    * range: [GenomicEntity](GenomicEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [decreases response to](decreases_response_to.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one decreases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [decreases secretion of](decreases_secretion_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one decreases the rate of secretion of the other out of a cell, gland, or organ
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [decreases splicing of](decreases_splicing_of.md)  <sub>0..*</sub>
    * Description: holds between a molecular entity and an mRNA where the action or effect of the molecular entity decreases the proper splicing of the mRNA
    * range: [Transcript](Transcript.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [decreases stability of](decreases_stability_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one decreases the stability of the other within a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [decreases synthesis of](decreases_synthesis_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one decreases the rate of chemical synthesis of the other
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [decreases transport of](decreases_transport_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one decreases the rate of transport of the other across some boundary in a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [decreases uptake of](decreases_uptake_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one decreases the rate of uptake of the other into of a cell, gland, or organ
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [description](description.md)  <sub>OPT</sub>
    * Description: a human-readable description of a thing
    * range: [NarrativeText](NarrativeText.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [full name](full_name.md)  <sub>OPT</sub>
    * Description: a long-form human readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [has gene](has_gene.md)  <sub>OPT</sub>
    * Description: connects and entity to a single gene
    * range: [Gene](Gene.md)
    * inherited from: [SequenceVariant](SequenceVariant.md)
 * [has phenotype](has_phenotype.md)  <sub>0..*</sub>
    * Description: holds between a biological entity and a phenotype, where a phenotype is construed broadly as any kind of quality of an organism part, a collection of these qualities, or a change in quality or qualities (e.g. abnormally increased temperature).
    * range: [PhenotypicFeature](PhenotypicFeature.md)
    * inherited from: [BiologicalEntity](BiologicalEntity.md)
    * in subsets: (translator_minimal)
 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects a thing to a class representing a taxon
    * range: [OrganismTaxon](OrganismTaxon.md)
    * inherited from: [ThingWithTaxon](ThingWithTaxon.md)
    * in subsets: (translator_minimal)
 * [increases abundance of](increases_abundance_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one increases the amount of the other within a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [increases activity of](increases_activity_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one increases the activity of the other within a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [increases degradation of](increases_degradation_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one increases the rate of degradation of the other within a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [increases expression of](increases_expression_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one increases the level of expression of the other within a system of interest
    * range: [GenomicEntity](GenomicEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [increases folding of](increases_folding_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one increases the rate or quality of folding of the other
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [increases localization of](increases_localization_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one increases the proper localization of the other within a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [increases metabolic processing of](increases_metabolic_processing_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one increases the rate of metabolic processing of the other within a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [increases molecular modification of](increases_molecular_modification_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one leads to increased molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [increases mutation rate of](increases_mutation_rate_of.md)  <sub>0..*</sub>
    * Description: holds between a molecular entity and a genomic entity where the action or effect of the molecular entity increases the rate of mutation of the genomic entity within a system of interest
    * range: [GenomicEntity](GenomicEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [increases response to](increases_response_to.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one increases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [increases secretion of](increases_secretion_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one increases the rate of secretion of the other out of a cell, gland, or organ
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [increases splicing of](increases_splicing_of.md)  <sub>0..*</sub>
    * Description: holds between a molecular entity and an mRNA where the action or effect of the molecular entity increases the proper splicing of the mRNA
    * range: [Transcript](Transcript.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [increases stability of](increases_stability_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one increases the stability of the other within a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [increases synthesis of](increases_synthesis_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one increases the rate of chemical synthesis of the other
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [increases transport of](increases_transport_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one increases the rate of transport of the other across some boundary in a system of interest
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [increases uptake of](increases_uptake_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one increases the rate of uptake of the other into of a cell, gland, or organ
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [interacts with](interacts_with.md)  <sub>0..*</sub>
    * Description: holds between any two entities that directly or indirectly interact with each other
    * range: [NamedThing](NamedThing.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [iri](iri.md)  <sub>OPT</sub>
    * Description: An IRI for the node. This is determined by the id using expansion rules.
    * range: [IriType](IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [molecularly interacts with](molecularly_interacts_with.md)  <sub>0..*</sub>
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>OPT</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [node property](node_property.md)  <sub>OPT</sub>
    * Description: A grouping for any property that holds between a node and a value
    * range: [String](String.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [regulates, entity to entity](regulates_entity_to_entity.md)  <sub>0..*</sub>
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [related to](related_to.md)  <sub>0..*</sub>
    * Description: A relationship that is asserted between two named things
    * range: [NamedThing](NamedThing.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [sequence variant.has biological sequence](sequence_variant_has_biological_sequence.md)  <sub>OPT</sub>
    * range: [BiologicalSequence](BiologicalSequence.md)
 * [sequence variant.has gene](sequence_variant_has_gene.md)  <sub>0..*</sub>
    * range: [Gene](Gene.md)
 * [sequence variant.id](sequence_variant_id.md)  <sub>REQ</sub>
    * range: [IdentifierType](IdentifierType.md)
 * [synonym](synonym.md)  <sub>0..*</sub>
    * Description: Alternate human-readable names for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [systematic synonym](systematic_synonym.md)  <sub>OPT</sub>
    * Description: more commonly used for gene symbols in yeast
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
