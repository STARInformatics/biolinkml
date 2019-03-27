# Auto generated from .yaml by pythongen.py version:
# Generation date:
# Schema: biolink model
#
# id: https://biolink.github.io/biolink-model/ontology/biolink.ttl
# description: Entity and association taxonomy and datamodel for life-sciences data
# license: https://creativecommons.org/publicdomain/zero/1.0/

from typing import Optional, List, Union, Dict
from dataclasses import dataclass
from biolinkml.utils.metamodelcore import empty_list, empty_dict
from biolinkml.utils.yamlutils import YAMLRoot
from biolinkml.utils.metamodelcore import Bool, NCName, URI, URIorCURIE, XSDDate, XSDDateTime, XSDTime

metamodel_version = "1.1.2"

inherited_slots: List[str] = []


# Types
class String(str):
    pass


class Integer(int):
    pass


class Boolean(Bool):
    """ A binary (true or false) value """
    pass


class Float(float):
    pass


class Double(float):
    pass


class Time(XSDTime):
    """ A time object represents a (local) time of day, independent of any particular day """
    pass


class Date(XSDDateTime):
    """ a date (year, month and day) in an idealized calendar """
    pass


class Datetime(XSDDate):
    pass


class Uriorcurie(URIorCURIE):
    """ a URI or a CURIE """
    pass


class Uri(URI):
    """ a complete URI """
    pass


class Ncname(NCName):
    """ Prefix part of CURIE """
    pass


class ChemicalFormulaValue(str):
    """ A chemical formula """
    pass


class IdentifierType(String):
    """ A string that is intended to uniquely identify a thing May be URI in full or compact (CURIE) form """
    pass


class IriType(Uri):
    """ An IRI """
    pass


class LabelType(String):
    """ A string that provides a human-readable name for a thing """
    pass


class NarrativeText(String):
    """ A string that provides a human-readable description of something """
    pass


class SymbolType(String):
    pass


class Frequency(String):
    pass


class PerecentageFrequencyValue(Double):
    pass


class Quotient(Double):
    pass


class Unit(String):
    pass


class TimeType(Time):
    pass


class BiologicalSequence(String):
    pass


# Class references
class AttributeId(IdentifierType):
    pass


class BiologicalSexId(AttributeId):
    pass


class PhenotypicSexId(BiologicalSexId):
    pass


class GenotypicSexId(BiologicalSexId):
    pass


class SeverityValueId(AttributeId):
    pass


class FrequencyValueId(AttributeId):
    pass


class ClinicalModifierId(AttributeId):
    pass


class OnsetId(AttributeId):
    pass


class NamedThingId(IdentifierType):
    pass


class BiologicalEntityId(NamedThingId):
    pass


class OntologyClassId(NamedThingId):
    pass


class RelationshipTypeId(OntologyClassId):
    pass


class GeneOntologyClassId(OntologyClassId):
    pass


class OrganismTaxonId(OntologyClassId):
    pass


class OrganismalEntityId(BiologicalEntityId):
    pass


class IndividualOrganismId(OrganismalEntityId):
    pass


class CaseId(IndividualOrganismId):
    pass


class PopulationOfIndividualOrganismsId(OrganismalEntityId):
    pass


class BiosampleId(OrganismalEntityId):
    pass


class DiseaseOrPhenotypicFeatureId(BiologicalEntityId):
    pass


class DiseaseId(DiseaseOrPhenotypicFeatureId):
    pass


class PhenotypicFeatureId(DiseaseOrPhenotypicFeatureId):
    pass


class EnvironmentId(BiologicalEntityId):
    pass


class InformationContentEntityId(NamedThingId):
    pass


class ConfidenceLevelId(InformationContentEntityId):
    pass


class EvidenceTypeId(InformationContentEntityId):
    pass


class PublicationId(InformationContentEntityId):
    pass


class AdministrativeEntityId(NamedThingId):
    pass


class ProviderId(AdministrativeEntityId):
    pass


class MolecularEntityId(BiologicalEntityId):
    pass


class ChemicalSubstanceId(MolecularEntityId):
    pass


class DrugId(ChemicalSubstanceId):
    pass


class MetaboliteId(ChemicalSubstanceId):
    pass


class AnatomicalEntityId(OrganismalEntityId):
    pass


class LifeStageId(OrganismalEntityId):
    pass


class PlanetaryEntityId(NamedThingId):
    pass


class EnvironmentalProcessId(PlanetaryEntityId):
    pass


class EnvironmentalFeatureId(PlanetaryEntityId):
    pass


class ClinicalEntityId(NamedThingId):
    pass


class ClinicalTrialId(ClinicalEntityId):
    pass


class ClinicalInterventionId(ClinicalEntityId):
    pass


class DeviceId(NamedThingId):
    pass


class GenomicEntityId(MolecularEntityId):
    pass


class GenomeId(GenomicEntityId):
    pass


class TranscriptId(GenomicEntityId):
    pass


class ExonId(GenomicEntityId):
    pass


class CodingSequenceId(GenomicEntityId):
    pass


class MacromolecularMachineId(GenomicEntityId):
    pass


class GeneOrGeneProductId(MacromolecularMachineId):
    pass


class GeneId(GeneOrGeneProductId):
    pass


class GeneProductId(GeneOrGeneProductId):
    pass


class ProteinId(GeneProductId):
    pass


class GeneProductIsoformId(GeneProductId):
    pass


class ProteinIsoformId(ProteinId):
    pass


class RNAProductId(GeneProductId):
    pass


class RNAProductIsoformId(RNAProductId):
    pass


class NoncodingRNAProductId(RNAProductId):
    pass


class MicroRNAId(NoncodingRNAProductId):
    pass


class MacromolecularComplexId(MacromolecularMachineId):
    pass


class GeneFamilyId(MolecularEntityId):
    pass


class ZygosityId(AttributeId):
    pass


class GenotypeId(GenomicEntityId):
    pass


class HaplotypeId(GenomicEntityId):
    pass


class SequenceVariantId(GenomicEntityId):
    pass


class DrugExposureId(EnvironmentId):
    pass


class TreatmentId(EnvironmentId):
    pass


class GeographicLocationId(PlanetaryEntityId):
    pass


class GeographicLocationAtTimeId(GeographicLocationId):
    pass


class AssociationId(IdentifierType):
    pass


class GenotypeToGenotypePartAssociationId(AssociationId):
    pass


class GenotypeToGeneAssociationId(AssociationId):
    pass


class GenotypeToVariantAssociationId(AssociationId):
    pass


class GeneToGeneAssociationId(AssociationId):
    pass


class GeneToGeneHomologyAssociationId(GeneToGeneAssociationId):
    pass


class PairwiseInteractionAssociationId(AssociationId):
    pass


class PairwiseGeneToGeneInteractionId(GeneToGeneAssociationId):
    pass


class CellLineToThingAssociationId(AssociationId):
    pass


class CellLineToDiseaseOrPhenotypicFeatureAssociationId(AssociationId):
    pass


class ChemicalToThingAssociationId(AssociationId):
    pass


class CaseToThingAssociationId(AssociationId):
    pass


class ChemicalToDiseaseOrPhenotypicFeatureAssociationId(AssociationId):
    pass


class ChemicalToPathwayAssociationId(AssociationId):
    pass


class ChemicalToGeneAssociationId(AssociationId):
    pass


class BiosampleToThingAssociationId(AssociationId):
    pass


class BiosampleToDiseaseOrPhenotypicFeatureAssociationId(AssociationId):
    pass


class EntityToPhenotypicFeatureAssociationId(AssociationId):
    pass


class DiseaseOrPhenotypicFeatureAssociationToThingAssociationId(AssociationId):
    pass


class DiseaseOrPhenotypicFeatureAssociationToLocationAssociationId(DiseaseOrPhenotypicFeatureAssociationToThingAssociationId):
    pass


class ThingToDiseaseOrPhenotypicFeatureAssociationId(AssociationId):
    pass


class DiseaseToThingAssociationId(AssociationId):
    pass


class GenotypeToPhenotypicFeatureAssociationId(AssociationId):
    pass


class EnvironmentToPhenotypicFeatureAssociationId(AssociationId):
    pass


class DiseaseToPhenotypicFeatureAssociationId(AssociationId):
    pass


class CaseToPhenotypicFeatureAssociationId(AssociationId):
    pass


class GeneToThingAssociationId(AssociationId):
    pass


class VariantToThingAssociationId(AssociationId):
    pass


class GeneToPhenotypicFeatureAssociationId(AssociationId):
    pass


class GeneToDiseaseAssociationId(AssociationId):
    pass


class VariantToPopulationAssociationId(AssociationId):
    pass


class PopulationToPopulationAssociationId(AssociationId):
    pass


class VariantToPhenotypicFeatureAssociationId(AssociationId):
    pass


class VariantToDiseaseAssociationId(AssociationId):
    pass


class GeneAsAModelOfDiseaseAssociationId(GeneToDiseaseAssociationId):
    pass


class GeneHasVariantThatContributesToDiseaseAssociationId(GeneToDiseaseAssociationId):
    pass


class GenotypeToThingAssociationId(AssociationId):
    pass


class GeneToExpressionSiteAssociationId(AssociationId):
    pass


class SequenceVariantModulatesTreatmentAssociationId(AssociationId):
    pass


class FunctionalAssociationId(AssociationId):
    pass


class MacromolecularMachineToMolecularActivityAssociationId(FunctionalAssociationId):
    pass


class MacromolecularMachineToBiologicalProcessAssociationId(FunctionalAssociationId):
    pass


class MacromolecularMachineToCellularComponentAssociationId(FunctionalAssociationId):
    pass


class GeneToGoTermAssociationId(FunctionalAssociationId):
    pass


class GenomicSequenceLocalizationId(AssociationId):
    pass


class SequenceFeatureRelationshipId(AssociationId):
    pass


class TranscriptToGeneRelationshipId(SequenceFeatureRelationshipId):
    pass


class GeneToGeneProductRelationshipId(SequenceFeatureRelationshipId):
    pass


class ExonToTranscriptRelationshipId(SequenceFeatureRelationshipId):
    pass


class GeneRegulatoryRelationshipId(AssociationId):
    pass


class AnatomicalEntityToAnatomicalEntityAssociationId(AssociationId):
    pass


class AnatomicalEntityToAnatomicalEntityPartOfAssociationId(AnatomicalEntityToAnatomicalEntityAssociationId):
    pass


class AnatomicalEntityToAnatomicalEntityOntogenicAssociationId(AnatomicalEntityToAnatomicalEntityAssociationId):
    pass


class OccurrentId(NamedThingId):
    pass


class BiologicalProcessOrActivityId(BiologicalEntityId):
    pass


class MolecularActivityId(BiologicalProcessOrActivityId):
    pass


class ActivityAndBehaviorId(OccurrentId):
    pass


class ProcedureId(OccurrentId):
    pass


class PhenomenonId(OccurrentId):
    pass


class BiologicalProcessId(BiologicalProcessOrActivityId):
    pass


class PathwayId(BiologicalProcessId):
    pass


class PhysiologicalProcessId(BiologicalProcessId):
    pass


class CellularComponentId(AnatomicalEntityId):
    pass


class CellId(AnatomicalEntityId):
    pass


class CellLineId(BiosampleId):
    pass


class GrossAnatomicalStructureId(AnatomicalEntityId):
    pass


@dataclass
class Attribute(YAMLRoot):
    """
    A property or characteristic of an entity
    """

    # === attribute ===
    id: Union[str, AttributeId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None
    subclass_of: List[Union[str, OntologyClassId]] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if not isinstance(self.id, AttributeId):
            self.id = AttributeId(self.id)
        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)
        self.category = [v if isinstance(v, IriType)
                         else IriType(v) for v in self.category]
        self.related_to = [v if isinstance(v, NamedThingId)
                           else NamedThingId(v) for v in self.related_to]
        self.interacts_with = [v if isinstance(v, NamedThingId)
                               else NamedThingId(v) for v in self.interacts_with]
        if self.iri is not None and not isinstance(self.iri, IriType):
            self.iri = IriType(self.iri)
        self.synonym = [v if isinstance(v, LabelType)
                        else LabelType(v) for v in self.synonym]
        if self.full_name is not None and not isinstance(self.full_name, LabelType):
            self.full_name = LabelType(self.full_name)
        if self.description is not None and not isinstance(self.description, NarrativeText):
            self.description = NarrativeText(self.description)
        if self.systematic_synonym is not None and not isinstance(self.systematic_synonym, LabelType):
            self.systematic_synonym = LabelType(self.systematic_synonym)
        self.subclass_of = [v if isinstance(v, OntologyClassId)
                            else OntologyClassId(v) for v in self.subclass_of]


@dataclass
class BiologicalSex(Attribute):

    # === attribute ===
    id: Union[str, BiologicalSexId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None
    subclass_of: List[Union[str, OntologyClassId]] = empty_list()

    # === biological sex ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, BiologicalSexId):
            self.id = BiologicalSexId(self.id)


@dataclass
class PhenotypicSex(BiologicalSex):
    """
    An attribute corresponding to the phenotypic sex of the individual, based upon the reproductive organs present.
    """

    # === attribute ===
    id: Union[str, PhenotypicSexId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None
    subclass_of: List[Union[str, OntologyClassId]] = empty_list()

    # === biological sex ===

    # === phenotypic sex ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, PhenotypicSexId):
            self.id = PhenotypicSexId(self.id)


@dataclass
class GenotypicSex(BiologicalSex):
    """
    An attribute corresponding to the genotypic sex of the individual, based upon genotypic composition of sex
    chromosomes.
    """

    # === attribute ===
    id: Union[str, GenotypicSexId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None
    subclass_of: List[Union[str, OntologyClassId]] = empty_list()

    # === biological sex ===

    # === genotypic sex ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GenotypicSexId):
            self.id = GenotypicSexId(self.id)


@dataclass
class SeverityValue(Attribute):
    """
    describes the severity of a phenotypic feature or disease
    """

    # === attribute ===
    id: Union[str, SeverityValueId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None
    subclass_of: List[Union[str, OntologyClassId]] = empty_list()

    # === severity value ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, SeverityValueId):
            self.id = SeverityValueId(self.id)


@dataclass
class FrequencyValue(Attribute):
    """
    describes the frequency of occurrence of an event or condition
    """

    # === attribute ===
    id: Union[str, FrequencyValueId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None
    subclass_of: List[Union[str, OntologyClassId]] = empty_list()

    # === frequency value ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, FrequencyValueId):
            self.id = FrequencyValueId(self.id)


@dataclass
class ClinicalModifier(Attribute):
    """
    Used to characterize and specify the phenotypic abnormalities defined in the Phenotypic abnormality subontology,
    with respect to severity, laterality, age of onset, and other aspects
    """

    # === attribute ===
    id: Union[str, ClinicalModifierId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None
    subclass_of: List[Union[str, OntologyClassId]] = empty_list()

    # === clinical modifier ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, ClinicalModifierId):
            self.id = ClinicalModifierId(self.id)


@dataclass
class Onset(Attribute):
    """
    The age group in which manifestations appear
    """

    # === attribute ===
    id: Union[str, OnsetId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None
    subclass_of: List[Union[str, OntologyClassId]] = empty_list()

    # === onset ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, OnsetId):
            self.id = OnsetId(self.id)


@dataclass
class NamedThing(YAMLRoot):
    """
    a databased entity or concept/class
    """

    # === named thing ===
    id: Union[str, NamedThingId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)
        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)
        self.category = [v if isinstance(v, IriType)
                         else IriType(v) for v in self.category]
        self.related_to = [v if isinstance(v, NamedThingId)
                           else NamedThingId(v) for v in self.related_to]
        self.interacts_with = [v if isinstance(v, NamedThingId)
                               else NamedThingId(v) for v in self.interacts_with]
        if self.iri is not None and not isinstance(self.iri, IriType):
            self.iri = IriType(self.iri)
        self.synonym = [v if isinstance(v, LabelType)
                        else LabelType(v) for v in self.synonym]
        if self.full_name is not None and not isinstance(self.full_name, LabelType):
            self.full_name = LabelType(self.full_name)
        if self.description is not None and not isinstance(self.description, NarrativeText):
            self.description = NarrativeText(self.description)
        if self.systematic_synonym is not None and not isinstance(self.systematic_synonym, LabelType):
            self.systematic_synonym = LabelType(self.systematic_synonym)


@dataclass
class BiologicalEntity(NamedThing):

    # === named thing ===
    id: Union[str, BiologicalEntityId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        self.has_phenotype = [v if isinstance(v, PhenotypicFeatureId)
                              else PhenotypicFeatureId(v) for v in self.has_phenotype]


@dataclass
class OntologyClass(NamedThing):
    """
    a concept or class in an ontology, vocabulary or thesaurus
    """

    # === named thing ===
    id: Union[str, OntologyClassId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === ontology class ===
    subclass_of: List[Union[str, OntologyClassId]] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, OntologyClassId):
            self.id = OntologyClassId(self.id)
        self.subclass_of = [v if isinstance(v, OntologyClassId)
                            else OntologyClassId(v) for v in self.subclass_of]


@dataclass
class RelationshipType(OntologyClass):
    """
    An OWL property used as an edge label
    """

    # === named thing ===
    id: Union[str, RelationshipTypeId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === ontology class ===
    subclass_of: List[Union[str, OntologyClassId]] = empty_list()

    # === relationship type ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, RelationshipTypeId):
            self.id = RelationshipTypeId(self.id)


@dataclass
class GeneOntologyClass(OntologyClass):
    """
    an ontology class that describes a functional aspect of a gene, gene prodoct or complex
    """

    # === named thing ===
    id: Union[str, GeneOntologyClassId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === ontology class ===
    subclass_of: List[Union[str, OntologyClassId]] = empty_list()

    # === gene ontology class ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GeneOntologyClassId):
            self.id = GeneOntologyClassId(self.id)


@dataclass
class OrganismTaxon(OntologyClass):

    # === named thing ===
    id: Union[str, OrganismTaxonId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === ontology class ===
    subclass_of: List[Union[str, OntologyClassId]] = empty_list()

    # === organism taxon ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, OrganismTaxonId):
            self.id = OrganismTaxonId(self.id)


@dataclass
class OrganismalEntity(BiologicalEntity):
    """
    A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding
    molecular entities
    """

    # === named thing ===
    id: Union[str, OrganismalEntityId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === organismal entity ===


@dataclass
class IndividualOrganism(OrganismalEntity):

    # === named thing ===
    id: Union[str, IndividualOrganismId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === organismal entity ===

    # === individual organism ===
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, IndividualOrganismId):
            self.id = IndividualOrganismId(self.id)
        self.in_taxon = [v if isinstance(v, OrganismTaxonId)
                         else OrganismTaxonId(v) for v in self.in_taxon]


@dataclass
class Case(IndividualOrganism):
    """
    An individual organism that has a patient role in some clinical context.
    """

    # === named thing ===
    id: Union[str, CaseId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === organismal entity ===

    # === individual organism ===
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    # === case ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, CaseId):
            self.id = CaseId(self.id)


@dataclass
class PopulationOfIndividualOrganisms(OrganismalEntity):
    """
    A collection of individuals from the same taxonomic class distinguished by one or more characteristics.
    Characteristics can include, but are not limited to, shared geographic location, genetics, phenotypes [Alliance
    for Genome Resources]
    """

    # === named thing ===
    id: Union[str, PopulationOfIndividualOrganismsId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === organismal entity ===

    # === population of individual organisms ===
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, PopulationOfIndividualOrganismsId):
            self.id = PopulationOfIndividualOrganismsId(self.id)
        self.in_taxon = [v if isinstance(v, OrganismTaxonId)
                         else OrganismTaxonId(v) for v in self.in_taxon]


@dataclass
class Biosample(OrganismalEntity):

    # === named thing ===
    id: Union[str, BiosampleId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === organismal entity ===

    # === biosample ===
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, BiosampleId):
            self.id = BiosampleId(self.id)
        self.in_taxon = [v if isinstance(v, OrganismTaxonId)
                         else OrganismTaxonId(v) for v in self.in_taxon]


@dataclass
class DiseaseOrPhenotypicFeature(BiologicalEntity):
    """
    Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these
    as distinct, others such as MESH conflate.
    """

    # === named thing ===
    id: Union[str, DiseaseOrPhenotypicFeatureId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === disease or phenotypic feature ===
    correlated_with: List[Union[str, MolecularEntityId]] = empty_list()
    has_biomarker: List[Union[str, MolecularEntityId]] = empty_list()
    treated_by: List[str] = empty_list()
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, DiseaseOrPhenotypicFeatureId):
            self.id = DiseaseOrPhenotypicFeatureId(self.id)
        self.correlated_with = [v if isinstance(v, MolecularEntityId)
                                else MolecularEntityId(v) for v in self.correlated_with]
        self.has_biomarker = [v if isinstance(v, MolecularEntityId)
                              else MolecularEntityId(v) for v in self.has_biomarker]
        self.in_taxon = [v if isinstance(v, OrganismTaxonId)
                         else OrganismTaxonId(v) for v in self.in_taxon]


@dataclass
class Disease(DiseaseOrPhenotypicFeature):

    # === named thing ===
    id: Union[str, DiseaseId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === disease or phenotypic feature ===
    correlated_with: List[Union[str, MolecularEntityId]] = empty_list()
    has_biomarker: List[Union[str, MolecularEntityId]] = empty_list()
    treated_by: List[str] = empty_list()
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    # === disease ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, DiseaseId):
            self.id = DiseaseId(self.id)


@dataclass
class PhenotypicFeature(DiseaseOrPhenotypicFeature):

    # === named thing ===
    id: Union[str, PhenotypicFeatureId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === disease or phenotypic feature ===
    correlated_with: List[Union[str, MolecularEntityId]] = empty_list()
    has_biomarker: List[Union[str, MolecularEntityId]] = empty_list()
    treated_by: List[str] = empty_list()
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    # === phenotypic feature ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, PhenotypicFeatureId):
            self.id = PhenotypicFeatureId(self.id)


@dataclass
class Environment(BiologicalEntity):
    """
    A feature of the environment of an organism that influences one or more phenotypic features of that organism,
    potentially mediated by genes
    """

    # === named thing ===
    id: Union[str, EnvironmentId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === environment ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, EnvironmentId):
            self.id = EnvironmentId(self.id)


@dataclass
class InformationContentEntity(NamedThing):
    """
    a piece of information that typically describes some piece of biology or is used as support.
    """

    # === named thing ===
    id: Union[str, InformationContentEntityId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === information content entity ===


@dataclass
class ConfidenceLevel(InformationContentEntity):
    """
    Level of confidence in a statement
    """

    # === named thing ===
    id: Union[str, ConfidenceLevelId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === information content entity ===

    # === confidence level ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, ConfidenceLevelId):
            self.id = ConfidenceLevelId(self.id)


@dataclass
class EvidenceType(InformationContentEntity):
    """
    Class of evidence that supports an association
    """

    # === named thing ===
    id: Union[str, EvidenceTypeId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === information content entity ===

    # === evidence type ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, EvidenceTypeId):
            self.id = EvidenceTypeId(self.id)


@dataclass
class Publication(InformationContentEntity):
    """
    Any published piece of information. Can refer to a whole publication, or to a part of it (e.g. a figure, figure
    legend, or section highlighted by NLP). The scope is intended to be general and include information published on
    the web as well as journals.
    """

    # === named thing ===
    id: Union[str, PublicationId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === information content entity ===

    # === publication ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, PublicationId):
            self.id = PublicationId(self.id)


@dataclass
class AdministrativeEntity(NamedThing):

    # === named thing ===
    id: Union[str, AdministrativeEntityId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === administrative entity ===


@dataclass
class Provider(AdministrativeEntity):
    """
    person, group, organization or project that provides a piece of information
    """

    # === named thing ===
    id: Union[str, ProviderId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === administrative entity ===

    # === provider ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, ProviderId):
            self.id = ProviderId(self.id)


@dataclass
class MolecularEntity(BiologicalEntity):
    """
    A gene, gene product, small molecule or macromolecule (including protein complex)
    """

    # === named thing ===
    id: Union[str, MolecularEntityId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === molecular entity ===
    molecularly_interacts_with: List[Union[str, MolecularEntityId]] = empty_list()
    affects_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    increases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    affects_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    increases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    decreases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    affects_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    regulates_entity_to_entity: List[Union[str, MolecularEntityId]] = empty_list()
    biomarker_for: List[Union[str, DiseaseOrPhenotypicFeatureId]] = empty_list()
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, MolecularEntityId):
            self.id = MolecularEntityId(self.id)
        self.molecularly_interacts_with = [v if isinstance(v, MolecularEntityId)
                                           else MolecularEntityId(v) for v in self.molecularly_interacts_with]
        self.affects_abundance_of = [v if isinstance(v, MolecularEntityId)
                                     else MolecularEntityId(v) for v in self.affects_abundance_of]
        self.increases_abundance_of = [v if isinstance(v, MolecularEntityId)
                                       else MolecularEntityId(v) for v in self.increases_abundance_of]
        self.decreases_abundance_of = [v if isinstance(v, MolecularEntityId)
                                       else MolecularEntityId(v) for v in self.decreases_abundance_of]
        self.affects_activity_of = [v if isinstance(v, MolecularEntityId)
                                    else MolecularEntityId(v) for v in self.affects_activity_of]
        self.increases_activity_of = [v if isinstance(v, MolecularEntityId)
                                      else MolecularEntityId(v) for v in self.increases_activity_of]
        self.decreases_activity_of = [v if isinstance(v, MolecularEntityId)
                                      else MolecularEntityId(v) for v in self.decreases_activity_of]
        self.affects_expression_of = [v if isinstance(v, GenomicEntityId)
                                      else GenomicEntityId(v) for v in self.affects_expression_of]
        self.increases_expression_of = [v if isinstance(v, GenomicEntityId)
                                        else GenomicEntityId(v) for v in self.increases_expression_of]
        self.decreases_expression_of = [v if isinstance(v, GenomicEntityId)
                                        else GenomicEntityId(v) for v in self.decreases_expression_of]
        self.affects_folding_of = [v if isinstance(v, MolecularEntityId)
                                   else MolecularEntityId(v) for v in self.affects_folding_of]
        self.increases_folding_of = [v if isinstance(v, MolecularEntityId)
                                     else MolecularEntityId(v) for v in self.increases_folding_of]
        self.decreases_folding_of = [v if isinstance(v, MolecularEntityId)
                                     else MolecularEntityId(v) for v in self.decreases_folding_of]
        self.affects_localization_of = [v if isinstance(v, MolecularEntityId)
                                        else MolecularEntityId(v) for v in self.affects_localization_of]
        self.increases_localization_of = [v if isinstance(v, MolecularEntityId)
                                          else MolecularEntityId(v) for v in self.increases_localization_of]
        self.decreases_localization_of = [v if isinstance(v, MolecularEntityId)
                                          else MolecularEntityId(v) for v in self.decreases_localization_of]
        self.affects_metabolic_processing_of = [v if isinstance(v, MolecularEntityId)
                                                else MolecularEntityId(v) for v in self.affects_metabolic_processing_of]
        self.increases_metabolic_processing_of = [v if isinstance(v, MolecularEntityId)
                                                  else MolecularEntityId(v) for v in self.increases_metabolic_processing_of]
        self.decreases_metabolic_processing_of = [v if isinstance(v, MolecularEntityId)
                                                  else MolecularEntityId(v) for v in self.decreases_metabolic_processing_of]
        self.affects_molecular_modification_of = [v if isinstance(v, MolecularEntityId)
                                                  else MolecularEntityId(v) for v in self.affects_molecular_modification_of]
        self.increases_molecular_modification_of = [v if isinstance(v, MolecularEntityId)
                                                    else MolecularEntityId(v) for v in self.increases_molecular_modification_of]
        self.decreases_molecular_modification_of = [v if isinstance(v, MolecularEntityId)
                                                    else MolecularEntityId(v) for v in self.decreases_molecular_modification_of]
        self.affects_synthesis_of = [v if isinstance(v, MolecularEntityId)
                                     else MolecularEntityId(v) for v in self.affects_synthesis_of]
        self.increases_synthesis_of = [v if isinstance(v, MolecularEntityId)
                                       else MolecularEntityId(v) for v in self.increases_synthesis_of]
        self.decreases_synthesis_of = [v if isinstance(v, MolecularEntityId)
                                       else MolecularEntityId(v) for v in self.decreases_synthesis_of]
        self.affects_degradation_of = [v if isinstance(v, MolecularEntityId)
                                       else MolecularEntityId(v) for v in self.affects_degradation_of]
        self.increases_degradation_of = [v if isinstance(v, MolecularEntityId)
                                         else MolecularEntityId(v) for v in self.increases_degradation_of]
        self.decreases_degradation_of = [v if isinstance(v, MolecularEntityId)
                                         else MolecularEntityId(v) for v in self.decreases_degradation_of]
        self.affects_mutation_rate_of = [v if isinstance(v, GenomicEntityId)
                                         else GenomicEntityId(v) for v in self.affects_mutation_rate_of]
        self.increases_mutation_rate_of = [v if isinstance(v, GenomicEntityId)
                                           else GenomicEntityId(v) for v in self.increases_mutation_rate_of]
        self.decreases_mutation_rate_of = [v if isinstance(v, GenomicEntityId)
                                           else GenomicEntityId(v) for v in self.decreases_mutation_rate_of]
        self.affects_response_to = [v if isinstance(v, MolecularEntityId)
                                    else MolecularEntityId(v) for v in self.affects_response_to]
        self.increases_response_to = [v if isinstance(v, MolecularEntityId)
                                      else MolecularEntityId(v) for v in self.increases_response_to]
        self.decreases_response_to = [v if isinstance(v, MolecularEntityId)
                                      else MolecularEntityId(v) for v in self.decreases_response_to]
        self.affects_splicing_of = [v if isinstance(v, TranscriptId)
                                    else TranscriptId(v) for v in self.affects_splicing_of]
        self.increases_splicing_of = [v if isinstance(v, TranscriptId)
                                      else TranscriptId(v) for v in self.increases_splicing_of]
        self.decreases_splicing_of = [v if isinstance(v, TranscriptId)
                                      else TranscriptId(v) for v in self.decreases_splicing_of]
        self.affects_stability_of = [v if isinstance(v, MolecularEntityId)
                                     else MolecularEntityId(v) for v in self.affects_stability_of]
        self.increases_stability_of = [v if isinstance(v, MolecularEntityId)
                                       else MolecularEntityId(v) for v in self.increases_stability_of]
        self.decreases_stability_of = [v if isinstance(v, MolecularEntityId)
                                       else MolecularEntityId(v) for v in self.decreases_stability_of]
        self.affects_transport_of = [v if isinstance(v, MolecularEntityId)
                                     else MolecularEntityId(v) for v in self.affects_transport_of]
        self.increases_transport_of = [v if isinstance(v, MolecularEntityId)
                                       else MolecularEntityId(v) for v in self.increases_transport_of]
        self.decreases_transport_of = [v if isinstance(v, MolecularEntityId)
                                       else MolecularEntityId(v) for v in self.decreases_transport_of]
        self.affects_secretion_of = [v if isinstance(v, MolecularEntityId)
                                     else MolecularEntityId(v) for v in self.affects_secretion_of]
        self.increases_secretion_of = [v if isinstance(v, MolecularEntityId)
                                       else MolecularEntityId(v) for v in self.increases_secretion_of]
        self.decreases_secretion_of = [v if isinstance(v, MolecularEntityId)
                                       else MolecularEntityId(v) for v in self.decreases_secretion_of]
        self.affects_uptake_of = [v if isinstance(v, MolecularEntityId)
                                  else MolecularEntityId(v) for v in self.affects_uptake_of]
        self.increases_uptake_of = [v if isinstance(v, MolecularEntityId)
                                    else MolecularEntityId(v) for v in self.increases_uptake_of]
        self.decreases_uptake_of = [v if isinstance(v, MolecularEntityId)
                                    else MolecularEntityId(v) for v in self.decreases_uptake_of]
        self.regulates_entity_to_entity = [v if isinstance(v, MolecularEntityId)
                                           else MolecularEntityId(v) for v in self.regulates_entity_to_entity]
        self.biomarker_for = [v if isinstance(v, DiseaseOrPhenotypicFeatureId)
                              else DiseaseOrPhenotypicFeatureId(v) for v in self.biomarker_for]
        self.in_taxon = [v if isinstance(v, OrganismTaxonId)
                         else OrganismTaxonId(v) for v in self.in_taxon]


@dataclass
class ChemicalSubstance(MolecularEntity):
    """
    May be a chemical entity or a formulation with a chemical entity as active ingredient, or a complex material with
    multiple chemical entities as part
    """

    # === named thing ===
    id: Union[str, ChemicalSubstanceId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === molecular entity ===
    molecularly_interacts_with: List[Union[str, MolecularEntityId]] = empty_list()
    affects_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    increases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    affects_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    increases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    decreases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    affects_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    regulates_entity_to_entity: List[Union[str, MolecularEntityId]] = empty_list()
    biomarker_for: List[Union[str, DiseaseOrPhenotypicFeatureId]] = empty_list()
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    # === chemical substance ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, ChemicalSubstanceId):
            self.id = ChemicalSubstanceId(self.id)


@dataclass
class Drug(ChemicalSubstance):
    """
    A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease
    """

    # === named thing ===
    id: Union[str, DrugId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === molecular entity ===
    molecularly_interacts_with: List[Union[str, MolecularEntityId]] = empty_list()
    affects_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    increases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    affects_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    increases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    decreases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    affects_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    regulates_entity_to_entity: List[Union[str, MolecularEntityId]] = empty_list()
    biomarker_for: List[Union[str, DiseaseOrPhenotypicFeatureId]] = empty_list()
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    # === chemical substance ===

    # === drug ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, DrugId):
            self.id = DrugId(self.id)


@dataclass
class Metabolite(ChemicalSubstance):
    """
    Any intermediate or product resulting from metabolism. Includes primary and secondary metabolites.
    """

    # === named thing ===
    id: Union[str, MetaboliteId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === molecular entity ===
    molecularly_interacts_with: List[Union[str, MolecularEntityId]] = empty_list()
    affects_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    increases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    affects_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    increases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    decreases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    affects_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    regulates_entity_to_entity: List[Union[str, MolecularEntityId]] = empty_list()
    biomarker_for: List[Union[str, DiseaseOrPhenotypicFeatureId]] = empty_list()
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    # === chemical substance ===

    # === metabolite ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, MetaboliteId):
            self.id = MetaboliteId(self.id)


@dataclass
class AnatomicalEntity(OrganismalEntity):
    """
    A subcellular location, cell type or gross anatomical part
    """

    # === named thing ===
    id: Union[str, AnatomicalEntityId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === organismal entity ===

    # === anatomical entity ===
    expresses: List[Union[str, GeneOrGeneProductId]] = empty_list()
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, AnatomicalEntityId):
            self.id = AnatomicalEntityId(self.id)
        self.expresses = [v if isinstance(v, GeneOrGeneProductId)
                          else GeneOrGeneProductId(v) for v in self.expresses]
        self.in_taxon = [v if isinstance(v, OrganismTaxonId)
                         else OrganismTaxonId(v) for v in self.in_taxon]


@dataclass
class LifeStage(OrganismalEntity):
    """
    A stage of development or growth of an organism, including post-natal adult stages
    """

    # === named thing ===
    id: Union[str, LifeStageId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === organismal entity ===

    # === life stage ===
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, LifeStageId):
            self.id = LifeStageId(self.id)
        self.in_taxon = [v if isinstance(v, OrganismTaxonId)
                         else OrganismTaxonId(v) for v in self.in_taxon]


@dataclass
class PlanetaryEntity(NamedThing):
    """
    Any entity or process that exists at the level of the whole planet
    """

    # === named thing ===
    id: Union[str, PlanetaryEntityId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === planetary entity ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, PlanetaryEntityId):
            self.id = PlanetaryEntityId(self.id)


@dataclass
class EnvironmentalProcess(PlanetaryEntity):

    # === named thing ===
    id: Union[str, EnvironmentalProcessId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === planetary entity ===

    # === environmental process ===
    regulates_process_to_process: List[Union[str, OccurrentId]] = empty_list()
    has_participant: List[str] = empty_list()
    has_input: List[str] = empty_list()
    precedes: List[Union[str, OccurrentId]] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, EnvironmentalProcessId):
            self.id = EnvironmentalProcessId(self.id)
        self.regulates_process_to_process = [v if isinstance(v, OccurrentId)
                                             else OccurrentId(v) for v in self.regulates_process_to_process]
        self.precedes = [v if isinstance(v, OccurrentId)
                         else OccurrentId(v) for v in self.precedes]


@dataclass
class EnvironmentalFeature(PlanetaryEntity):

    # === named thing ===
    id: Union[str, EnvironmentalFeatureId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === planetary entity ===

    # === environmental feature ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, EnvironmentalFeatureId):
            self.id = EnvironmentalFeatureId(self.id)


@dataclass
class ClinicalEntity(NamedThing):
    """
    Any entity or process that exists in the clinical domain and outside the biological realm. Diseases are placed
    under biological entities
    """

    # === named thing ===
    id: Union[str, ClinicalEntityId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === clinical entity ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, ClinicalEntityId):
            self.id = ClinicalEntityId(self.id)


@dataclass
class ClinicalTrial(ClinicalEntity):

    # === named thing ===
    id: Union[str, ClinicalTrialId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === clinical entity ===

    # === clinical trial ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, ClinicalTrialId):
            self.id = ClinicalTrialId(self.id)


@dataclass
class ClinicalIntervention(ClinicalEntity):

    # === named thing ===
    id: Union[str, ClinicalInterventionId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === clinical entity ===

    # === clinical intervention ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, ClinicalInterventionId):
            self.id = ClinicalInterventionId(self.id)


@dataclass
class Device(NamedThing):
    """
    A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment
    """

    # === named thing ===
    id: Union[str, DeviceId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === device ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, DeviceId):
            self.id = DeviceId(self.id)


@dataclass
class GenomicEntity(MolecularEntity):
    """
    an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is
    encoded in a genome (protein)
    """

    # === named thing ===
    id: Union[str, GenomicEntityId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === molecular entity ===
    molecularly_interacts_with: List[Union[str, MolecularEntityId]] = empty_list()
    affects_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    increases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    affects_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    increases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    decreases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    affects_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    regulates_entity_to_entity: List[Union[str, MolecularEntityId]] = empty_list()
    biomarker_for: List[Union[str, DiseaseOrPhenotypicFeatureId]] = empty_list()
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    # === genomic entity ===
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GenomicEntityId):
            self.id = GenomicEntityId(self.id)
        if self.has_biological_sequence is not None and not isinstance(self.has_biological_sequence, BiologicalSequence):
            self.has_biological_sequence = BiologicalSequence(self.has_biological_sequence)


@dataclass
class Genome(GenomicEntity):
    """
    A genome is the sum of genetic material within a cell or virion.
    """

    # === named thing ===
    id: Union[str, GenomeId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === molecular entity ===
    molecularly_interacts_with: List[Union[str, MolecularEntityId]] = empty_list()
    affects_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    increases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    affects_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    increases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    decreases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    affects_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    regulates_entity_to_entity: List[Union[str, MolecularEntityId]] = empty_list()
    biomarker_for: List[Union[str, DiseaseOrPhenotypicFeatureId]] = empty_list()
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    # === genomic entity ===
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    # === genome ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GenomeId):
            self.id = GenomeId(self.id)


@dataclass
class Transcript(GenomicEntity):
    """
    An RNA synthesized on a DNA or RNA template by an RNA polymerase
    """

    # === named thing ===
    id: Union[str, TranscriptId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === molecular entity ===
    molecularly_interacts_with: List[Union[str, MolecularEntityId]] = empty_list()
    affects_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    increases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    affects_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    increases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    decreases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    affects_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    regulates_entity_to_entity: List[Union[str, MolecularEntityId]] = empty_list()
    biomarker_for: List[Union[str, DiseaseOrPhenotypicFeatureId]] = empty_list()
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    # === genomic entity ===
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    # === transcript ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, TranscriptId):
            self.id = TranscriptId(self.id)


@dataclass
class Exon(GenomicEntity):
    """
    A region of the transcript sequence within a gene which is not removed from the primary RNA transcript by RNA
    splicing
    """

    # === named thing ===
    id: Union[str, ExonId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === molecular entity ===
    molecularly_interacts_with: List[Union[str, MolecularEntityId]] = empty_list()
    affects_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    increases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    affects_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    increases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    decreases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    affects_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    regulates_entity_to_entity: List[Union[str, MolecularEntityId]] = empty_list()
    biomarker_for: List[Union[str, DiseaseOrPhenotypicFeatureId]] = empty_list()
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    # === genomic entity ===
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    # === exon ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, ExonId):
            self.id = ExonId(self.id)


@dataclass
class CodingSequence(GenomicEntity):

    # === named thing ===
    id: Union[str, CodingSequenceId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === molecular entity ===
    molecularly_interacts_with: List[Union[str, MolecularEntityId]] = empty_list()
    affects_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    increases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    affects_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    increases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    decreases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    affects_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    regulates_entity_to_entity: List[Union[str, MolecularEntityId]] = empty_list()
    biomarker_for: List[Union[str, DiseaseOrPhenotypicFeatureId]] = empty_list()
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    # === genomic entity ===
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    # === coding sequence ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, CodingSequenceId):
            self.id = CodingSequenceId(self.id)


@dataclass
class MacromolecularMachine(GenomicEntity):
    """
    A union of gene, gene product, and macromolecular complex. These are the basic units of function in a cell. They
    either carry out individual biological activities, or they encode molecules which do this.
    """

    # === named thing ===
    id: Union[str, MacromolecularMachineId]
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === molecular entity ===
    molecularly_interacts_with: List[Union[str, MolecularEntityId]] = empty_list()
    affects_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    increases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    affects_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    increases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    decreases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    affects_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    regulates_entity_to_entity: List[Union[str, MolecularEntityId]] = empty_list()
    biomarker_for: List[Union[str, DiseaseOrPhenotypicFeatureId]] = empty_list()
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    # === genomic entity ===
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    # === macromolecular machine ===
    name: Optional[Union[str, SymbolType]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, MacromolecularMachineId):
            self.id = MacromolecularMachineId(self.id)
        if self.name is not None and not isinstance(self.name, SymbolType):
            self.name = SymbolType(self.name)


@dataclass
class GeneOrGeneProduct(MacromolecularMachine):
    """
    a union of genes or gene products. Frequently an identifier for one will be used as proxy for another
    """

    # === named thing ===
    id: Union[str, GeneOrGeneProductId]
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === molecular entity ===
    molecularly_interacts_with: List[Union[str, MolecularEntityId]] = empty_list()
    affects_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    increases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    affects_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    increases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    decreases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    affects_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    regulates_entity_to_entity: List[Union[str, MolecularEntityId]] = empty_list()
    biomarker_for: List[Union[str, DiseaseOrPhenotypicFeatureId]] = empty_list()
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    # === genomic entity ===
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    # === macromolecular machine ===
    name: Optional[Union[str, SymbolType]] = None

    # === gene or gene product ===
    in_pathway_with: List[Union[str, GeneOrGeneProductId]] = empty_list()
    in_complex_with: List[Union[str, GeneOrGeneProductId]] = empty_list()
    in_cell_population_with: List[Union[str, GeneOrGeneProductId]] = empty_list()
    expressed_in: List[Union[str, AnatomicalEntityId]] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GeneOrGeneProductId):
            self.id = GeneOrGeneProductId(self.id)
        self.in_pathway_with = [v if isinstance(v, GeneOrGeneProductId)
                                else GeneOrGeneProductId(v) for v in self.in_pathway_with]
        self.in_complex_with = [v if isinstance(v, GeneOrGeneProductId)
                                else GeneOrGeneProductId(v) for v in self.in_complex_with]
        self.in_cell_population_with = [v if isinstance(v, GeneOrGeneProductId)
                                        else GeneOrGeneProductId(v) for v in self.in_cell_population_with]
        self.expressed_in = [v if isinstance(v, AnatomicalEntityId)
                             else AnatomicalEntityId(v) for v in self.expressed_in]


@dataclass
class Gene(GeneOrGeneProduct):

    # === named thing ===
    id: Union[str, GeneId]
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === molecular entity ===
    molecularly_interacts_with: List[Union[str, MolecularEntityId]] = empty_list()
    affects_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    increases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    affects_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    increases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    decreases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    affects_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    regulates_entity_to_entity: List[Union[str, MolecularEntityId]] = empty_list()
    biomarker_for: List[Union[str, DiseaseOrPhenotypicFeatureId]] = empty_list()
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    # === genomic entity ===
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    # === macromolecular machine ===
    name: Optional[Union[str, SymbolType]] = None

    # === gene or gene product ===
    in_pathway_with: List[Union[str, GeneOrGeneProductId]] = empty_list()
    in_complex_with: List[Union[str, GeneOrGeneProductId]] = empty_list()
    in_cell_population_with: List[Union[str, GeneOrGeneProductId]] = empty_list()
    expressed_in: List[Union[str, AnatomicalEntityId]] = empty_list()

    # === gene ===
    genetically_interacts_with: List[Union[str, GeneId]] = empty_list()
    has_gene_product: List[Union[str, GeneProductId]] = empty_list()
    gene_associated_with_condition: List[Union[str, DiseaseOrPhenotypicFeatureId]] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GeneId):
            self.id = GeneId(self.id)
        self.genetically_interacts_with = [v if isinstance(v, GeneId)
                                           else GeneId(v) for v in self.genetically_interacts_with]
        self.has_gene_product = [v if isinstance(v, GeneProductId)
                                 else GeneProductId(v) for v in self.has_gene_product]
        self.gene_associated_with_condition = [v if isinstance(v, DiseaseOrPhenotypicFeatureId)
                                               else DiseaseOrPhenotypicFeatureId(v) for v in self.gene_associated_with_condition]


@dataclass
class GeneProduct(GeneOrGeneProduct):
    """
    The functional molecular product of a single gene. Gene products are either proteins or functional RNA molecules
    """

    # === named thing ===
    id: Union[str, GeneProductId]
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === molecular entity ===
    molecularly_interacts_with: List[Union[str, MolecularEntityId]] = empty_list()
    affects_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    increases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    affects_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    increases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    decreases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    affects_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    regulates_entity_to_entity: List[Union[str, MolecularEntityId]] = empty_list()
    biomarker_for: List[Union[str, DiseaseOrPhenotypicFeatureId]] = empty_list()
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    # === genomic entity ===
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    # === macromolecular machine ===
    name: Optional[Union[str, SymbolType]] = None

    # === gene or gene product ===
    in_pathway_with: List[Union[str, GeneOrGeneProductId]] = empty_list()
    in_complex_with: List[Union[str, GeneOrGeneProductId]] = empty_list()
    in_cell_population_with: List[Union[str, GeneOrGeneProductId]] = empty_list()
    expressed_in: List[Union[str, AnatomicalEntityId]] = empty_list()

    # === gene product ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GeneProductId):
            self.id = GeneProductId(self.id)


@dataclass
class Protein(GeneProduct):
    """
    A gene product that is composed of a chain of amino acid sequences and is produced by ribosome-mediated
    translation of mRNA
    """

    # === named thing ===
    id: Union[str, ProteinId]
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === molecular entity ===
    molecularly_interacts_with: List[Union[str, MolecularEntityId]] = empty_list()
    affects_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    increases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    affects_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    increases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    decreases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    affects_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    regulates_entity_to_entity: List[Union[str, MolecularEntityId]] = empty_list()
    biomarker_for: List[Union[str, DiseaseOrPhenotypicFeatureId]] = empty_list()
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    # === genomic entity ===
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    # === macromolecular machine ===
    name: Optional[Union[str, SymbolType]] = None

    # === gene or gene product ===
    in_pathway_with: List[Union[str, GeneOrGeneProductId]] = empty_list()
    in_complex_with: List[Union[str, GeneOrGeneProductId]] = empty_list()
    in_cell_population_with: List[Union[str, GeneOrGeneProductId]] = empty_list()
    expressed_in: List[Union[str, AnatomicalEntityId]] = empty_list()

    # === gene product ===

    # === protein ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, ProteinId):
            self.id = ProteinId(self.id)


@dataclass
class GeneProductIsoform(GeneProduct):
    """
    This is an abstract class that can be mixed in with different kinds of gene products to indicate that the gene
    product is intended to represent a specific isoform rather than a canonical or reference or generic product. The
    designation of canonical or reference may be arbitrary, or it may represent the superclass of all isoforms.
    """

    # === named thing ===
    id: Union[str, GeneProductIsoformId]
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === molecular entity ===
    molecularly_interacts_with: List[Union[str, MolecularEntityId]] = empty_list()
    affects_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    increases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    affects_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    increases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    decreases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    affects_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    regulates_entity_to_entity: List[Union[str, MolecularEntityId]] = empty_list()
    biomarker_for: List[Union[str, DiseaseOrPhenotypicFeatureId]] = empty_list()
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    # === genomic entity ===
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    # === macromolecular machine ===
    name: Optional[Union[str, SymbolType]] = None

    # === gene or gene product ===
    in_pathway_with: List[Union[str, GeneOrGeneProductId]] = empty_list()
    in_complex_with: List[Union[str, GeneOrGeneProductId]] = empty_list()
    in_cell_population_with: List[Union[str, GeneOrGeneProductId]] = empty_list()
    expressed_in: List[Union[str, AnatomicalEntityId]] = empty_list()

    # === gene product ===

    # === gene product isoform ===


@dataclass
class ProteinIsoform(Protein):
    """
    Represents a protein that is a specific isoform of the canonical or reference protein. See
    https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4114032/
    """

    # === named thing ===
    id: Union[str, ProteinIsoformId]
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === molecular entity ===
    molecularly_interacts_with: List[Union[str, MolecularEntityId]] = empty_list()
    affects_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    increases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    affects_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    increases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    decreases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    affects_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    regulates_entity_to_entity: List[Union[str, MolecularEntityId]] = empty_list()
    biomarker_for: List[Union[str, DiseaseOrPhenotypicFeatureId]] = empty_list()
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    # === genomic entity ===
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    # === macromolecular machine ===
    name: Optional[Union[str, SymbolType]] = None

    # === gene or gene product ===
    in_pathway_with: List[Union[str, GeneOrGeneProductId]] = empty_list()
    in_complex_with: List[Union[str, GeneOrGeneProductId]] = empty_list()
    in_cell_population_with: List[Union[str, GeneOrGeneProductId]] = empty_list()
    expressed_in: List[Union[str, AnatomicalEntityId]] = empty_list()

    # === gene product ===

    # === protein ===

    # === protein isoform ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, ProteinIsoformId):
            self.id = ProteinIsoformId(self.id)


@dataclass
class RNAProduct(GeneProduct):

    # === named thing ===
    id: Union[str, RNAProductId]
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === molecular entity ===
    molecularly_interacts_with: List[Union[str, MolecularEntityId]] = empty_list()
    affects_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    increases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    affects_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    increases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    decreases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    affects_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    regulates_entity_to_entity: List[Union[str, MolecularEntityId]] = empty_list()
    biomarker_for: List[Union[str, DiseaseOrPhenotypicFeatureId]] = empty_list()
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    # === genomic entity ===
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    # === macromolecular machine ===
    name: Optional[Union[str, SymbolType]] = None

    # === gene or gene product ===
    in_pathway_with: List[Union[str, GeneOrGeneProductId]] = empty_list()
    in_complex_with: List[Union[str, GeneOrGeneProductId]] = empty_list()
    in_cell_population_with: List[Union[str, GeneOrGeneProductId]] = empty_list()
    expressed_in: List[Union[str, AnatomicalEntityId]] = empty_list()

    # === gene product ===

    # === RNA product ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, RNAProductId):
            self.id = RNAProductId(self.id)


@dataclass
class RNAProductIsoform(RNAProduct):
    """
    Represents a protein that is a specific isoform of the canonical or reference RNA
    """

    # === named thing ===
    id: Union[str, RNAProductIsoformId]
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === molecular entity ===
    molecularly_interacts_with: List[Union[str, MolecularEntityId]] = empty_list()
    affects_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    increases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    affects_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    increases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    decreases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    affects_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    regulates_entity_to_entity: List[Union[str, MolecularEntityId]] = empty_list()
    biomarker_for: List[Union[str, DiseaseOrPhenotypicFeatureId]] = empty_list()
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    # === genomic entity ===
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    # === macromolecular machine ===
    name: Optional[Union[str, SymbolType]] = None

    # === gene or gene product ===
    in_pathway_with: List[Union[str, GeneOrGeneProductId]] = empty_list()
    in_complex_with: List[Union[str, GeneOrGeneProductId]] = empty_list()
    in_cell_population_with: List[Union[str, GeneOrGeneProductId]] = empty_list()
    expressed_in: List[Union[str, AnatomicalEntityId]] = empty_list()

    # === gene product ===

    # === RNA product ===

    # === RNA product isoform ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, RNAProductIsoformId):
            self.id = RNAProductIsoformId(self.id)


@dataclass
class NoncodingRNAProduct(RNAProduct):

    # === named thing ===
    id: Union[str, NoncodingRNAProductId]
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === molecular entity ===
    molecularly_interacts_with: List[Union[str, MolecularEntityId]] = empty_list()
    affects_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    increases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    affects_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    increases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    decreases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    affects_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    regulates_entity_to_entity: List[Union[str, MolecularEntityId]] = empty_list()
    biomarker_for: List[Union[str, DiseaseOrPhenotypicFeatureId]] = empty_list()
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    # === genomic entity ===
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    # === macromolecular machine ===
    name: Optional[Union[str, SymbolType]] = None

    # === gene or gene product ===
    in_pathway_with: List[Union[str, GeneOrGeneProductId]] = empty_list()
    in_complex_with: List[Union[str, GeneOrGeneProductId]] = empty_list()
    in_cell_population_with: List[Union[str, GeneOrGeneProductId]] = empty_list()
    expressed_in: List[Union[str, AnatomicalEntityId]] = empty_list()

    # === gene product ===

    # === RNA product ===

    # === noncoding RNA product ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, NoncodingRNAProductId):
            self.id = NoncodingRNAProductId(self.id)


@dataclass
class MicroRNA(NoncodingRNAProduct):

    # === named thing ===
    id: Union[str, MicroRNAId]
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === molecular entity ===
    molecularly_interacts_with: List[Union[str, MolecularEntityId]] = empty_list()
    affects_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    increases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    affects_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    increases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    decreases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    affects_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    regulates_entity_to_entity: List[Union[str, MolecularEntityId]] = empty_list()
    biomarker_for: List[Union[str, DiseaseOrPhenotypicFeatureId]] = empty_list()
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    # === genomic entity ===
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    # === macromolecular machine ===
    name: Optional[Union[str, SymbolType]] = None

    # === gene or gene product ===
    in_pathway_with: List[Union[str, GeneOrGeneProductId]] = empty_list()
    in_complex_with: List[Union[str, GeneOrGeneProductId]] = empty_list()
    in_cell_population_with: List[Union[str, GeneOrGeneProductId]] = empty_list()
    expressed_in: List[Union[str, AnatomicalEntityId]] = empty_list()

    # === gene product ===

    # === RNA product ===

    # === noncoding RNA product ===

    # === microRNA ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, MicroRNAId):
            self.id = MicroRNAId(self.id)


@dataclass
class MacromolecularComplex(MacromolecularMachine):

    # === named thing ===
    id: Union[str, MacromolecularComplexId]
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === molecular entity ===
    molecularly_interacts_with: List[Union[str, MolecularEntityId]] = empty_list()
    affects_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    increases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    affects_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    increases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    decreases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    affects_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    regulates_entity_to_entity: List[Union[str, MolecularEntityId]] = empty_list()
    biomarker_for: List[Union[str, DiseaseOrPhenotypicFeatureId]] = empty_list()
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    # === genomic entity ===
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    # === macromolecular machine ===
    name: Optional[Union[str, SymbolType]] = None

    # === macromolecular complex ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, MacromolecularComplexId):
            self.id = MacromolecularComplexId(self.id)


@dataclass
class GeneFamily(MolecularEntity):
    """
    any grouping of multiple genes or gene products related by common descent
    """

    # === named thing ===
    id: Union[str, GeneFamilyId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === molecular entity ===
    molecularly_interacts_with: List[Union[str, MolecularEntityId]] = empty_list()
    affects_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    increases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    affects_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    increases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    decreases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    affects_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    regulates_entity_to_entity: List[Union[str, MolecularEntityId]] = empty_list()
    biomarker_for: List[Union[str, DiseaseOrPhenotypicFeatureId]] = empty_list()
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    # === gene family ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GeneFamilyId):
            self.id = GeneFamilyId(self.id)


@dataclass
class Zygosity(Attribute):

    # === attribute ===
    id: Union[str, ZygosityId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None
    subclass_of: List[Union[str, OntologyClassId]] = empty_list()

    # === zygosity ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, ZygosityId):
            self.id = ZygosityId(self.id)


@dataclass
class Genotype(GenomicEntity):
    """
    An information content entity that describes a genome by specifying the total variation in genomic sequence and/or
    gene expression, relative to some extablished background
    """

    # === named thing ===
    id: Union[str, GenotypeId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === molecular entity ===
    molecularly_interacts_with: List[Union[str, MolecularEntityId]] = empty_list()
    affects_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    increases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    affects_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    increases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    decreases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    affects_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    regulates_entity_to_entity: List[Union[str, MolecularEntityId]] = empty_list()
    biomarker_for: List[Union[str, DiseaseOrPhenotypicFeatureId]] = empty_list()
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    # === genomic entity ===
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    # === genotype ===
    has_zygosity: Optional[Union[str, ZygosityId]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GenotypeId):
            self.id = GenotypeId(self.id)
        if self.has_zygosity is not None and not isinstance(self.has_zygosity, ZygosityId):
            self.has_zygosity = ZygosityId(self.has_zygosity)


@dataclass
class Haplotype(GenomicEntity):
    """
    A set of zero or more Alleles on a single instance of a Sequence[VMC]
    """

    # === named thing ===
    id: Union[str, HaplotypeId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === molecular entity ===
    molecularly_interacts_with: List[Union[str, MolecularEntityId]] = empty_list()
    affects_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    increases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    affects_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    increases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    decreases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    affects_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    regulates_entity_to_entity: List[Union[str, MolecularEntityId]] = empty_list()
    biomarker_for: List[Union[str, DiseaseOrPhenotypicFeatureId]] = empty_list()
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    # === genomic entity ===
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    # === haplotype ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, HaplotypeId):
            self.id = HaplotypeId(self.id)


@dataclass
class SequenceVariant(GenomicEntity):
    """
    An allele that varies in its sequence from what is considered the reference allele at that locus.
    """

    # === named thing ===
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === molecular entity ===
    molecularly_interacts_with: List[Union[str, MolecularEntityId]] = empty_list()
    affects_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_abundance_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_activity_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_expression_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_folding_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_localization_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_metabolic_processing_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_molecular_modification_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_synthesis_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_degradation_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    increases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    decreases_mutation_rate_of: List[Union[str, GenomicEntityId]] = empty_list()
    affects_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    increases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_response_to: List[Union[str, MolecularEntityId]] = empty_list()
    affects_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    increases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    decreases_splicing_of: List[Union[str, TranscriptId]] = empty_list()
    affects_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_stability_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_transport_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_secretion_of: List[Union[str, MolecularEntityId]] = empty_list()
    affects_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    increases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    decreases_uptake_of: List[Union[str, MolecularEntityId]] = empty_list()
    regulates_entity_to_entity: List[Union[str, MolecularEntityId]] = empty_list()
    biomarker_for: List[Union[str, DiseaseOrPhenotypicFeatureId]] = empty_list()
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    # === genomic entity ===

    # === sequence variant ===
    id: Union[str, SequenceVariantId] = None
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None
    has_gene: List[Union[str, GeneId]] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, SequenceVariantId):
            self.id = SequenceVariantId(self.id)
        if self.has_biological_sequence is not None and not isinstance(self.has_biological_sequence, BiologicalSequence):
            self.has_biological_sequence = BiologicalSequence(self.has_biological_sequence)
        self.has_gene = [v if isinstance(v, GeneId)
                         else GeneId(v) for v in self.has_gene]


@dataclass
class DrugExposure(Environment):
    """
    A drug exposure is an intake of a particular chemical substance
    """

    # === named thing ===
    id: Union[str, DrugExposureId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === environment ===

    # === drug exposure ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, DrugExposureId):
            self.id = DrugExposureId(self.id)


@dataclass
class Treatment(Environment):
    """
    A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures'
    """

    # === named thing ===
    id: Union[str, TreatmentId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === environment ===

    # === treatment ===
    treats: List[Union[str, DiseaseOrPhenotypicFeatureId]] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, TreatmentId):
            self.id = TreatmentId(self.id)
        self.treats = [v if isinstance(v, DiseaseOrPhenotypicFeatureId)
                       else DiseaseOrPhenotypicFeatureId(v) for v in self.treats]


@dataclass
class GeographicLocation(PlanetaryEntity):
    """
    a location that can be described in lat/long coordinates
    """

    # === named thing ===
    id: Union[str, GeographicLocationId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === planetary entity ===

    # === geographic location ===
    latitude: Optional[float] = None
    longitude: Optional[float] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GeographicLocationId):
            self.id = GeographicLocationId(self.id)


@dataclass
class GeographicLocationAtTime(GeographicLocation):
    """
    a location that can be described in lat/long coordinates, for a particular time
    """

    # === named thing ===
    id: Union[str, GeographicLocationAtTimeId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === planetary entity ===

    # === geographic location ===
    latitude: Optional[float] = None
    longitude: Optional[float] = None

    # === geographic location at time ===
    timepoint: Optional[Union[str, TimeType]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GeographicLocationAtTimeId):
            self.id = GeographicLocationAtTimeId(self.id)
        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)


@dataclass
class Association(YAMLRoot):
    """
    A typed association between two entities, supported by evidence
    """

    # === association ===
    id: Union[str, AssociationId]
    subject: Union[str, IriType]
    relation: Union[str, IriType]
    object: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    def _fix_elements(self):
        super()._fix_elements()
        if not isinstance(self.id, AssociationId):
            self.id = AssociationId(self.id)
        if not isinstance(self.subject, IriType):
            self.subject = IriType(self.subject)
        if not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if not isinstance(self.object, IriType):
            self.object = IriType(self.object)
        if self.association_type is not None and not isinstance(self.association_type, OntologyClassId):
            self.association_type = OntologyClassId(self.association_type)
        self.qualifiers = [v if isinstance(v, OntologyClassId)
                           else OntologyClassId(v) for v in self.qualifiers]
        self.publications = [v if isinstance(v, PublicationId)
                             else PublicationId(v) for v in self.publications]
        if self.provided_by is not None and not isinstance(self.provided_by, ProviderId):
            self.provided_by = ProviderId(self.provided_by)


@dataclass
class GenotypeToGenotypePartAssociation(Association):
    """
    Any association between one genotype and a genotypic entity that is a sub-component of it
    """

    # === association ===
    id: Union[str, GenotypeToGenotypePartAssociationId]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === genotype to genotype part association ===
    subject: Union[str, GenotypeId] = None
    relation: Union[str, IriType] = None
    object: Union[str, GenotypeId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GenotypeToGenotypePartAssociationId):
            self.id = GenotypeToGenotypePartAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if self.object is not None and not isinstance(self.object, GenotypeId):
            self.object = GenotypeId(self.object)


@dataclass
class GenotypeToGeneAssociation(Association):
    """
    Any association between a genotype and a gene. The genotype have have multiple variants in that gene or a single
    one. There is no assumption of cardinality
    """

    # === association ===
    id: Union[str, GenotypeToGeneAssociationId]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === genotype to gene association ===
    subject: Union[str, GenotypeId] = None
    relation: Union[str, IriType] = None
    object: Union[str, GeneId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GenotypeToGeneAssociationId):
            self.id = GenotypeToGeneAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)


@dataclass
class GenotypeToVariantAssociation(Association):
    """
    Any association between a genotype and a sequence variant.
    """

    # === association ===
    id: Union[str, GenotypeToVariantAssociationId]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === genotype to variant association ===
    subject: Union[str, GenotypeId] = None
    relation: Union[str, IriType] = None
    object: Union[str, SequenceVariantId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GenotypeToVariantAssociationId):
            self.id = GenotypeToVariantAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if self.object is not None and not isinstance(self.object, SequenceVariantId):
            self.object = SequenceVariantId(self.object)


@dataclass
class GeneToGeneAssociation(Association):
    """
    abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes
    homology and interaction.
    """

    # === association ===
    id: Union[str, GeneToGeneAssociationId]
    relation: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === gene to gene association ===
    subject: Union[str, GeneOrGeneProductId] = None
    object: Union[str, GeneOrGeneProductId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is not None and not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        if self.object is not None and not isinstance(self.object, GeneOrGeneProductId):
            self.object = GeneOrGeneProductId(self.object)


@dataclass
class GeneToGeneHomologyAssociation(GeneToGeneAssociation):
    """
    A homology association between two genes. May be orthology (in which case the species of subject and object should
    differ) or paralogy (in which case the species may be the same)
    """

    # === association ===
    id: Union[str, GeneToGeneHomologyAssociationId]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === gene to gene association ===
    subject: Union[str, GeneOrGeneProductId] = None
    object: Union[str, GeneOrGeneProductId] = None

    # === gene to gene homology association ===
    relation: Union[str, IriType] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GeneToGeneHomologyAssociationId):
            self.id = GeneToGeneHomologyAssociationId(self.id)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)


@dataclass
class PairwiseGeneToGeneInteraction(GeneToGeneAssociation):
    """
    An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between
    genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)
    """

    # === association ===
    id: Union[str, PairwiseGeneToGeneInteractionId]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === gene to gene association ===
    subject: Union[str, GeneOrGeneProductId] = None
    object: Union[str, GeneOrGeneProductId] = None

    # === pairwise gene to gene interaction ===
    relation: Union[str, IriType] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, PairwiseGeneToGeneInteractionId):
            self.id = PairwiseGeneToGeneInteractionId(self.id)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)


@dataclass
class CellLineToThingAssociation(Association):
    """
    An relationship between a cell line and another entity
    """

    # === association ===
    id: Union[str, CellLineToThingAssociationId]
    relation: Union[str, IriType]
    object: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === cell line to thing association ===
    subject: Union[str, CellLineId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is not None and not isinstance(self.subject, CellLineId):
            self.subject = CellLineId(self.subject)


@dataclass
class CellLineToDiseaseOrPhenotypicFeatureAssociation(Association):
    """
    An relationship between a cell line and a disease or a phenotype, where the cell line is derived from an
    individual with that disease or phenotype
    """

    # === association ===
    id: Union[str, CellLineToDiseaseOrPhenotypicFeatureAssociationId]
    relation: Union[str, IriType]
    object: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === cell line to disease or phenotypic feature association ===
    subject: Union[str, DiseaseOrPhenotypicFeatureId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, CellLineToDiseaseOrPhenotypicFeatureAssociationId):
            self.id = CellLineToDiseaseOrPhenotypicFeatureAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, DiseaseOrPhenotypicFeatureId):
            self.subject = DiseaseOrPhenotypicFeatureId(self.subject)


@dataclass
class ChemicalToThingAssociation(Association):
    """
    An interaction between a chemical entity and another entity
    """

    # === association ===
    id: Union[str, ChemicalToThingAssociationId]
    relation: Union[str, IriType]
    object: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === chemical to thing association ===
    subject: Union[str, ChemicalSubstanceId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is not None and not isinstance(self.subject, ChemicalSubstanceId):
            self.subject = ChemicalSubstanceId(self.subject)


@dataclass
class CaseToThingAssociation(Association):
    """
    An abstract association for use where the case is the subject
    """

    # === association ===
    id: Union[str, CaseToThingAssociationId]
    relation: Union[str, IriType]
    object: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === case to thing association ===
    subject: Union[str, CaseId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is not None and not isinstance(self.subject, CaseId):
            self.subject = CaseId(self.subject)


@dataclass
class ChemicalToDiseaseOrPhenotypicFeatureAssociation(Association):
    """
    An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise
    to or exacerbates the phenotype
    """

    # === association ===
    id: Union[str, ChemicalToDiseaseOrPhenotypicFeatureAssociationId]
    subject: Union[str, IriType]
    relation: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === chemical to disease or phenotypic feature association ===
    object: Union[str, DiseaseOrPhenotypicFeatureId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, ChemicalToDiseaseOrPhenotypicFeatureAssociationId):
            self.id = ChemicalToDiseaseOrPhenotypicFeatureAssociationId(self.id)
        if self.object is not None and not isinstance(self.object, DiseaseOrPhenotypicFeatureId):
            self.object = DiseaseOrPhenotypicFeatureId(self.object)


@dataclass
class ChemicalToPathwayAssociation(Association):
    """
    An interaction between a chemical entity and a biological process or pathway
    """

    # === association ===
    id: Union[str, ChemicalToPathwayAssociationId]
    subject: Union[str, IriType]
    relation: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === chemical to pathway association ===
    object: Union[str, PathwayId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, ChemicalToPathwayAssociationId):
            self.id = ChemicalToPathwayAssociationId(self.id)
        if self.object is not None and not isinstance(self.object, PathwayId):
            self.object = PathwayId(self.object)


@dataclass
class ChemicalToGeneAssociation(Association):
    """
    An interaction between a chemical entity and a gene or gene product
    """

    # === association ===
    id: Union[str, ChemicalToGeneAssociationId]
    subject: Union[str, IriType]
    relation: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === chemical to gene association ===
    object: Union[str, GeneOrGeneProductId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, ChemicalToGeneAssociationId):
            self.id = ChemicalToGeneAssociationId(self.id)
        if self.object is not None and not isinstance(self.object, GeneOrGeneProductId):
            self.object = GeneOrGeneProductId(self.object)


@dataclass
class BiosampleToThingAssociation(Association):
    """
    An association between a biosample and something
    """

    # === association ===
    id: Union[str, BiosampleToThingAssociationId]
    relation: Union[str, IriType]
    object: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === biosample to thing association ===
    subject: Union[str, BiosampleId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is not None and not isinstance(self.subject, BiosampleId):
            self.subject = BiosampleId(self.subject)


@dataclass
class BiosampleToDiseaseOrPhenotypicFeatureAssociation(Association):
    """
    An association between a biosample and a disease or phenotype
    """

    # === association ===
    id: Union[str, BiosampleToDiseaseOrPhenotypicFeatureAssociationId]
    subject: Union[str, IriType]
    relation: Union[str, IriType]
    object: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === biosample to disease or phenotypic feature association ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, BiosampleToDiseaseOrPhenotypicFeatureAssociationId):
            self.id = BiosampleToDiseaseOrPhenotypicFeatureAssociationId(self.id)


@dataclass
class EntityToPhenotypicFeatureAssociation(Association):

    # === association ===
    id: Union[str, EntityToPhenotypicFeatureAssociationId]
    subject: Union[str, IriType]
    relation: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === entity to phenotypic feature association ===
    object: Union[str, PhenotypicFeatureId] = None
    sex_qualifier: Optional[Union[str, BiologicalSexId]] = None
    frequency_qualifier: Optional[Union[str, FrequencyValueId]] = None
    severity_qualifier: Optional[Union[str, SeverityValueId]] = None
    onset_qualifier: Optional[Union[str, OnsetId]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.object is not None and not isinstance(self.object, PhenotypicFeatureId):
            self.object = PhenotypicFeatureId(self.object)
        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSexId):
            self.sex_qualifier = BiologicalSexId(self.sex_qualifier)
        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValueId):
            self.frequency_qualifier = FrequencyValueId(self.frequency_qualifier)
        if self.severity_qualifier is not None and not isinstance(self.severity_qualifier, SeverityValueId):
            self.severity_qualifier = SeverityValueId(self.severity_qualifier)
        if self.onset_qualifier is not None and not isinstance(self.onset_qualifier, OnsetId):
            self.onset_qualifier = OnsetId(self.onset_qualifier)


@dataclass
class DiseaseOrPhenotypicFeatureAssociationToThingAssociation(Association):

    # === association ===
    id: Union[str, DiseaseOrPhenotypicFeatureAssociationToThingAssociationId]
    relation: Union[str, IriType]
    object: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === disease or phenotypic feature association to thing association ===
    subject: Union[str, DiseaseOrPhenotypicFeatureId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is not None and not isinstance(self.subject, DiseaseOrPhenotypicFeatureId):
            self.subject = DiseaseOrPhenotypicFeatureId(self.subject)


@dataclass
class DiseaseOrPhenotypicFeatureAssociationToLocationAssociation(DiseaseOrPhenotypicFeatureAssociationToThingAssociation):
    """
    An association between either a disease or a phenotypic feature and an anatomical entity, where the
    disease/feature manifests in that site.
    """

    # === association ===
    id: Union[str, DiseaseOrPhenotypicFeatureAssociationToLocationAssociationId]
    relation: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === disease or phenotypic feature association to thing association ===
    subject: Union[str, DiseaseOrPhenotypicFeatureId] = None

    # === disease or phenotypic feature association to location association ===
    object: Union[str, AnatomicalEntityId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, DiseaseOrPhenotypicFeatureAssociationToLocationAssociationId):
            self.id = DiseaseOrPhenotypicFeatureAssociationToLocationAssociationId(self.id)
        if self.object is not None and not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)


@dataclass
class ThingToDiseaseOrPhenotypicFeatureAssociation(Association):

    # === association ===
    id: Union[str, ThingToDiseaseOrPhenotypicFeatureAssociationId]
    subject: Union[str, IriType]
    relation: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === thing to disease or phenotypic feature association ===
    object: Union[str, DiseaseOrPhenotypicFeatureId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.object is not None and not isinstance(self.object, DiseaseOrPhenotypicFeatureId):
            self.object = DiseaseOrPhenotypicFeatureId(self.object)


@dataclass
class DiseaseToThingAssociation(Association):

    # === association ===
    id: Union[str, DiseaseToThingAssociationId]
    relation: Union[str, IriType]
    object: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === disease to thing association ===
    subject: Union[str, DiseaseId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is not None and not isinstance(self.subject, DiseaseId):
            self.subject = DiseaseId(self.subject)


@dataclass
class GenotypeToPhenotypicFeatureAssociation(Association):
    """
    Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype,
    either in isolation or through environment
    """

    # === association ===
    id: Union[str, GenotypeToPhenotypicFeatureAssociationId]
    object: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === genotype to phenotypic feature association ===
    subject: Union[str, GenotypeId] = None
    relation: Union[str, IriType] = None
    sex_qualifier: Optional[Union[str, BiologicalSexId]] = None
    frequency_qualifier: Optional[Union[str, FrequencyValueId]] = None
    severity_qualifier: Optional[Union[str, SeverityValueId]] = None
    onset_qualifier: Optional[Union[str, OnsetId]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GenotypeToPhenotypicFeatureAssociationId):
            self.id = GenotypeToPhenotypicFeatureAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSexId):
            self.sex_qualifier = BiologicalSexId(self.sex_qualifier)
        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValueId):
            self.frequency_qualifier = FrequencyValueId(self.frequency_qualifier)
        if self.severity_qualifier is not None and not isinstance(self.severity_qualifier, SeverityValueId):
            self.severity_qualifier = SeverityValueId(self.severity_qualifier)
        if self.onset_qualifier is not None and not isinstance(self.onset_qualifier, OnsetId):
            self.onset_qualifier = OnsetId(self.onset_qualifier)


@dataclass
class EnvironmentToPhenotypicFeatureAssociation(Association):
    """
    Any association between an environment and a phenotypic feature, where being in the environment influences the
    phenotype
    """

    # === association ===
    id: Union[str, EnvironmentToPhenotypicFeatureAssociationId]
    relation: Union[str, IriType]
    object: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === environment to phenotypic feature association ===
    subject: Union[str, EnvironmentId] = None
    sex_qualifier: Optional[Union[str, BiologicalSexId]] = None
    frequency_qualifier: Optional[Union[str, FrequencyValueId]] = None
    severity_qualifier: Optional[Union[str, SeverityValueId]] = None
    onset_qualifier: Optional[Union[str, OnsetId]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, EnvironmentToPhenotypicFeatureAssociationId):
            self.id = EnvironmentToPhenotypicFeatureAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, EnvironmentId):
            self.subject = EnvironmentId(self.subject)
        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSexId):
            self.sex_qualifier = BiologicalSexId(self.sex_qualifier)
        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValueId):
            self.frequency_qualifier = FrequencyValueId(self.frequency_qualifier)
        if self.severity_qualifier is not None and not isinstance(self.severity_qualifier, SeverityValueId):
            self.severity_qualifier = SeverityValueId(self.severity_qualifier)
        if self.onset_qualifier is not None and not isinstance(self.onset_qualifier, OnsetId):
            self.onset_qualifier = OnsetId(self.onset_qualifier)


@dataclass
class DiseaseToPhenotypicFeatureAssociation(Association):
    """
    An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the
    disease in some way
    """

    # === association ===
    id: Union[str, DiseaseToPhenotypicFeatureAssociationId]
    subject: Union[str, IriType]
    relation: Union[str, IriType]
    object: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === disease to phenotypic feature association ===
    sex_qualifier: Optional[Union[str, BiologicalSexId]] = None
    frequency_qualifier: Optional[Union[str, FrequencyValueId]] = None
    severity_qualifier: Optional[Union[str, SeverityValueId]] = None
    onset_qualifier: Optional[Union[str, OnsetId]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, DiseaseToPhenotypicFeatureAssociationId):
            self.id = DiseaseToPhenotypicFeatureAssociationId(self.id)
        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSexId):
            self.sex_qualifier = BiologicalSexId(self.sex_qualifier)
        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValueId):
            self.frequency_qualifier = FrequencyValueId(self.frequency_qualifier)
        if self.severity_qualifier is not None and not isinstance(self.severity_qualifier, SeverityValueId):
            self.severity_qualifier = SeverityValueId(self.severity_qualifier)
        if self.onset_qualifier is not None and not isinstance(self.onset_qualifier, OnsetId):
            self.onset_qualifier = OnsetId(self.onset_qualifier)


@dataclass
class CaseToPhenotypicFeatureAssociation(Association):
    """
    An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or
    has had the phenotype
    """

    # === association ===
    id: Union[str, CaseToPhenotypicFeatureAssociationId]
    subject: Union[str, IriType]
    relation: Union[str, IriType]
    object: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === case to phenotypic feature association ===
    sex_qualifier: Optional[Union[str, BiologicalSexId]] = None
    frequency_qualifier: Optional[Union[str, FrequencyValueId]] = None
    severity_qualifier: Optional[Union[str, SeverityValueId]] = None
    onset_qualifier: Optional[Union[str, OnsetId]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, CaseToPhenotypicFeatureAssociationId):
            self.id = CaseToPhenotypicFeatureAssociationId(self.id)
        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSexId):
            self.sex_qualifier = BiologicalSexId(self.sex_qualifier)
        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValueId):
            self.frequency_qualifier = FrequencyValueId(self.frequency_qualifier)
        if self.severity_qualifier is not None and not isinstance(self.severity_qualifier, SeverityValueId):
            self.severity_qualifier = SeverityValueId(self.severity_qualifier)
        if self.onset_qualifier is not None and not isinstance(self.onset_qualifier, OnsetId):
            self.onset_qualifier = OnsetId(self.onset_qualifier)


@dataclass
class GeneToThingAssociation(Association):

    # === association ===
    id: Union[str, GeneToThingAssociationId]
    relation: Union[str, IriType]
    object: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === gene to thing association ===
    subject: Union[str, GeneOrGeneProductId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is not None and not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)


@dataclass
class GeneToPhenotypicFeatureAssociation(Association):

    # === association ===
    id: Union[str, GeneToPhenotypicFeatureAssociationId]
    relation: Union[str, IriType]
    object: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === gene to phenotypic feature association ===
    subject: Union[str, GeneOrGeneProductId] = None
    sex_qualifier: Optional[Union[str, BiologicalSexId]] = None
    frequency_qualifier: Optional[Union[str, FrequencyValueId]] = None
    severity_qualifier: Optional[Union[str, SeverityValueId]] = None
    onset_qualifier: Optional[Union[str, OnsetId]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GeneToPhenotypicFeatureAssociationId):
            self.id = GeneToPhenotypicFeatureAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSexId):
            self.sex_qualifier = BiologicalSexId(self.sex_qualifier)
        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValueId):
            self.frequency_qualifier = FrequencyValueId(self.frequency_qualifier)
        if self.severity_qualifier is not None and not isinstance(self.severity_qualifier, SeverityValueId):
            self.severity_qualifier = SeverityValueId(self.severity_qualifier)
        if self.onset_qualifier is not None and not isinstance(self.onset_qualifier, OnsetId):
            self.onset_qualifier = OnsetId(self.onset_qualifier)


@dataclass
class GeneToDiseaseAssociation(Association):

    # === association ===
    id: Union[str, GeneToDiseaseAssociationId]
    relation: Union[str, IriType]
    object: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === gene to disease association ===
    subject: Union[str, GeneOrGeneProductId] = None
    frequency_qualifier: Optional[Union[str, FrequencyValueId]] = None
    severity_qualifier: Optional[Union[str, SeverityValueId]] = None
    onset_qualifier: Optional[Union[str, OnsetId]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GeneToDiseaseAssociationId):
            self.id = GeneToDiseaseAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValueId):
            self.frequency_qualifier = FrequencyValueId(self.frequency_qualifier)
        if self.severity_qualifier is not None and not isinstance(self.severity_qualifier, SeverityValueId):
            self.severity_qualifier = SeverityValueId(self.severity_qualifier)
        if self.onset_qualifier is not None and not isinstance(self.onset_qualifier, OnsetId):
            self.onset_qualifier = OnsetId(self.onset_qualifier)


@dataclass
class VariantToPopulationAssociation(Association):
    """
    An association between a variant and a population, where the variant has particular frequency in the population
    """

    # === association ===
    id: Union[str, VariantToPopulationAssociationId]
    relation: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === variant to population association ===
    subject: Union[str, SequenceVariantId] = None
    object: Union[str, PopulationOfIndividualOrganismsId] = None
    has_count: Optional[int] = None
    has_total: Optional[int] = None
    has_quotient: Optional[float] = None
    has_percentage: Optional[float] = None
    frequency_qualifier: Optional[Union[str, FrequencyValueId]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, VariantToPopulationAssociationId):
            self.id = VariantToPopulationAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)
        if self.object is not None and not isinstance(self.object, PopulationOfIndividualOrganismsId):
            self.object = PopulationOfIndividualOrganismsId(self.object)
        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValueId):
            self.frequency_qualifier = FrequencyValueId(self.frequency_qualifier)


@dataclass
class PopulationToPopulationAssociation(Association):
    """
    An association between a two populations
    """

    # === association ===
    id: Union[str, PopulationToPopulationAssociationId]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === population to population association ===
    subject: Union[str, PopulationOfIndividualOrganismsId] = None
    relation: Union[str, IriType] = None
    object: Union[str, PopulationOfIndividualOrganismsId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, PopulationToPopulationAssociationId):
            self.id = PopulationToPopulationAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, PopulationOfIndividualOrganismsId):
            self.subject = PopulationOfIndividualOrganismsId(self.subject)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if self.object is not None and not isinstance(self.object, PopulationOfIndividualOrganismsId):
            self.object = PopulationOfIndividualOrganismsId(self.object)


@dataclass
class VariantToPhenotypicFeatureAssociation(Association):

    # === association ===
    id: Union[str, VariantToPhenotypicFeatureAssociationId]
    relation: Union[str, IriType]
    object: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === variant to phenotypic feature association ===
    subject: Union[str, SequenceVariantId] = None
    sex_qualifier: Optional[Union[str, BiologicalSexId]] = None
    frequency_qualifier: Optional[Union[str, FrequencyValueId]] = None
    severity_qualifier: Optional[Union[str, SeverityValueId]] = None
    onset_qualifier: Optional[Union[str, OnsetId]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, VariantToPhenotypicFeatureAssociationId):
            self.id = VariantToPhenotypicFeatureAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)
        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSexId):
            self.sex_qualifier = BiologicalSexId(self.sex_qualifier)
        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValueId):
            self.frequency_qualifier = FrequencyValueId(self.frequency_qualifier)
        if self.severity_qualifier is not None and not isinstance(self.severity_qualifier, SeverityValueId):
            self.severity_qualifier = SeverityValueId(self.severity_qualifier)
        if self.onset_qualifier is not None and not isinstance(self.onset_qualifier, OnsetId):
            self.onset_qualifier = OnsetId(self.onset_qualifier)


@dataclass
class VariantToDiseaseAssociation(Association):

    # === association ===
    id: Union[str, VariantToDiseaseAssociationId]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === variant to disease association ===
    subject: Union[str, IriType] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None
    frequency_qualifier: Optional[Union[str, FrequencyValueId]] = None
    severity_qualifier: Optional[Union[str, SeverityValueId]] = None
    onset_qualifier: Optional[Union[str, OnsetId]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, VariantToDiseaseAssociationId):
            self.id = VariantToDiseaseAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, IriType):
            self.subject = IriType(self.subject)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if self.object is not None and not isinstance(self.object, IriType):
            self.object = IriType(self.object)
        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValueId):
            self.frequency_qualifier = FrequencyValueId(self.frequency_qualifier)
        if self.severity_qualifier is not None and not isinstance(self.severity_qualifier, SeverityValueId):
            self.severity_qualifier = SeverityValueId(self.severity_qualifier)
        if self.onset_qualifier is not None and not isinstance(self.onset_qualifier, OnsetId):
            self.onset_qualifier = OnsetId(self.onset_qualifier)


@dataclass
class GeneAsAModelOfDiseaseAssociation(GeneToDiseaseAssociation):

    # === association ===
    id: Union[str, GeneAsAModelOfDiseaseAssociationId]
    relation: Union[str, IriType]
    object: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === gene to disease association ===
    frequency_qualifier: Optional[Union[str, FrequencyValueId]] = None
    severity_qualifier: Optional[Union[str, SeverityValueId]] = None
    onset_qualifier: Optional[Union[str, OnsetId]] = None

    # === gene as a model of disease association ===
    subject: Union[str, GeneOrGeneProductId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GeneAsAModelOfDiseaseAssociationId):
            self.id = GeneAsAModelOfDiseaseAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)


@dataclass
class GeneHasVariantThatContributesToDiseaseAssociation(GeneToDiseaseAssociation):

    # === association ===
    id: Union[str, GeneHasVariantThatContributesToDiseaseAssociationId]
    relation: Union[str, IriType]
    object: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === gene to disease association ===
    frequency_qualifier: Optional[Union[str, FrequencyValueId]] = None
    severity_qualifier: Optional[Union[str, SeverityValueId]] = None
    onset_qualifier: Optional[Union[str, OnsetId]] = None

    # === gene has variant that contributes to disease association ===
    subject: Union[str, GeneOrGeneProductId] = None
    sequence_variant_qualifier: Optional[Union[str, SequenceVariantId]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GeneHasVariantThatContributesToDiseaseAssociationId):
            self.id = GeneHasVariantThatContributesToDiseaseAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        if self.sequence_variant_qualifier is not None and not isinstance(self.sequence_variant_qualifier, SequenceVariantId):
            self.sequence_variant_qualifier = SequenceVariantId(self.sequence_variant_qualifier)


@dataclass
class GenotypeToThingAssociation(Association):

    # === association ===
    id: Union[str, GenotypeToThingAssociationId]
    relation: Union[str, IriType]
    object: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === genotype to thing association ===
    subject: Union[str, GenotypeId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is not None and not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)


@dataclass
class GeneToExpressionSiteAssociation(Association):
    """
    An association between a gene and an expression site, possibly qualified by stage/timing info.
    """

    # === association ===
    id: Union[str, GeneToExpressionSiteAssociationId]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === gene to expression site association ===
    subject: Union[str, GeneOrGeneProductId] = None
    relation: Union[str, IriType] = None
    object: Union[str, AnatomicalEntityId] = None
    stage_qualifier: Optional[Union[str, LifeStageId]] = None
    quantifier_qualifier: Optional[Union[str, OntologyClassId]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GeneToExpressionSiteAssociationId):
            self.id = GeneToExpressionSiteAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if self.object is not None and not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)
        if self.stage_qualifier is not None and not isinstance(self.stage_qualifier, LifeStageId):
            self.stage_qualifier = LifeStageId(self.stage_qualifier)
        if self.quantifier_qualifier is not None and not isinstance(self.quantifier_qualifier, OntologyClassId):
            self.quantifier_qualifier = OntologyClassId(self.quantifier_qualifier)


@dataclass
class SequenceVariantModulatesTreatmentAssociation(Association):
    """
    An association between a sequence variant and a treatment or health intervention. The treatment object itself
    encompasses both the disease and the drug used.
    """

    # === association ===
    id: Union[str, SequenceVariantModulatesTreatmentAssociationId]
    relation: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === sequence variant modulates treatment association ===
    subject: Union[str, SequenceVariantId] = None
    object: Union[str, TreatmentId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is not None and not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)
        if self.object is not None and not isinstance(self.object, TreatmentId):
            self.object = TreatmentId(self.object)


@dataclass
class FunctionalAssociation(Association):
    """
    An association between a macromolecular machine (gene, gene product or complex of gene products) and either a
    molecular activity, a biological process or a cellular location in which a function is executed
    """

    # === association ===
    id: Union[str, FunctionalAssociationId]
    relation: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === functional association ===
    subject: Union[str, MacromolecularMachineId] = None
    object: Union[str, GeneOntologyClassId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, FunctionalAssociationId):
            self.id = FunctionalAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, MacromolecularMachineId):
            self.subject = MacromolecularMachineId(self.subject)
        if self.object is not None and not isinstance(self.object, GeneOntologyClassId):
            self.object = GeneOntologyClassId(self.object)


@dataclass
class MacromolecularMachineToMolecularActivityAssociation(FunctionalAssociation):
    """
    A functional association between a macromolecular machine (gene, gene product or complex) and a molecular activity
    (as represented in the GO molecular function branch), where the entity carries out the activity, or contributes to
    its execution
    """

    # === association ===
    id: Union[str, MacromolecularMachineToMolecularActivityAssociationId]
    relation: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === functional association ===
    subject: Union[str, MacromolecularMachineId] = None

    # === macromolecular machine to molecular activity association ===
    object: Union[str, MolecularActivityId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, MacromolecularMachineToMolecularActivityAssociationId):
            self.id = MacromolecularMachineToMolecularActivityAssociationId(self.id)
        if self.object is not None and not isinstance(self.object, MolecularActivityId):
            self.object = MolecularActivityId(self.object)


@dataclass
class MacromolecularMachineToBiologicalProcessAssociation(FunctionalAssociation):
    """
    A functional association between a macromolecular machine (gene, gene product or complex) and a biological process
    or pathway (as represented in the GO biological process branch), where the entity carries out some part of the
    process, regulates it, or acts upstream of it
    """

    # === association ===
    id: Union[str, MacromolecularMachineToBiologicalProcessAssociationId]
    relation: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === functional association ===
    subject: Union[str, MacromolecularMachineId] = None

    # === macromolecular machine to biological process association ===
    object: Union[str, BiologicalProcessId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, MacromolecularMachineToBiologicalProcessAssociationId):
            self.id = MacromolecularMachineToBiologicalProcessAssociationId(self.id)
        if self.object is not None and not isinstance(self.object, BiologicalProcessId):
            self.object = BiologicalProcessId(self.object)


@dataclass
class MacromolecularMachineToCellularComponentAssociation(FunctionalAssociation):
    """
    A functional association between a macromolecular machine (gene, gene product or complex) and a cellular component
    (as represented in the GO cellular component branch), where the entity carries out its function in the cellular
    component
    """

    # === association ===
    id: Union[str, MacromolecularMachineToCellularComponentAssociationId]
    relation: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === functional association ===
    subject: Union[str, MacromolecularMachineId] = None

    # === macromolecular machine to cellular component association ===
    object: Union[str, CellularComponentId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, MacromolecularMachineToCellularComponentAssociationId):
            self.id = MacromolecularMachineToCellularComponentAssociationId(self.id)
        if self.object is not None and not isinstance(self.object, CellularComponentId):
            self.object = CellularComponentId(self.object)


@dataclass
class GeneToGoTermAssociation(FunctionalAssociation):

    # === association ===
    id: Union[str, GeneToGoTermAssociationId]
    relation: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === functional association ===

    # === gene to go term association ===
    subject: Union[str, MolecularEntityId] = None
    object: Union[str, GeneOntologyClassId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GeneToGoTermAssociationId):
            self.id = GeneToGoTermAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, MolecularEntityId):
            self.subject = MolecularEntityId(self.subject)
        if self.object is not None and not isinstance(self.object, GeneOntologyClassId):
            self.object = GeneOntologyClassId(self.object)


@dataclass
class GenomicSequenceLocalization(Association):
    """
    A relationship between a sequence feature and an entity it is localized to. The reference entity may be a
    chromosome, chromosome region or information entity such as a contig
    """

    # === association ===
    id: Union[str, GenomicSequenceLocalizationId]
    relation: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === genomic sequence localization ===
    subject: Union[str, GenomicEntityId] = None
    object: Union[str, GenomicEntityId] = None
    start_interbase_coordinate: Optional[str] = None
    end_interbase_coordinate: Optional[str] = None
    genome_build: Optional[str] = None
    phase: Optional[str] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GenomicSequenceLocalizationId):
            self.id = GenomicSequenceLocalizationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GenomicEntityId):
            self.subject = GenomicEntityId(self.subject)
        if self.object is not None and not isinstance(self.object, GenomicEntityId):
            self.object = GenomicEntityId(self.object)


@dataclass
class SequenceFeatureRelationship(Association):
    """
    For example, a particular exon is part of a particular transcript or gene
    """

    # === association ===
    id: Union[str, SequenceFeatureRelationshipId]
    relation: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === sequence feature relationship ===
    subject: Union[str, GenomicEntityId] = None
    object: Union[str, GenomicEntityId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, SequenceFeatureRelationshipId):
            self.id = SequenceFeatureRelationshipId(self.id)
        if self.subject is not None and not isinstance(self.subject, GenomicEntityId):
            self.subject = GenomicEntityId(self.subject)
        if self.object is not None and not isinstance(self.object, GenomicEntityId):
            self.object = GenomicEntityId(self.object)


@dataclass
class TranscriptToGeneRelationship(SequenceFeatureRelationship):
    """
    A gene is a collection of transcripts
    """

    # === association ===
    id: Union[str, TranscriptToGeneRelationshipId]
    relation: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === sequence feature relationship ===

    # === transcript to gene relationship ===
    subject: Union[str, TranscriptId] = None
    object: Union[str, GeneId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, TranscriptToGeneRelationshipId):
            self.id = TranscriptToGeneRelationshipId(self.id)
        if self.subject is not None and not isinstance(self.subject, TranscriptId):
            self.subject = TranscriptId(self.subject)
        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)


@dataclass
class GeneToGeneProductRelationship(SequenceFeatureRelationship):
    """
    A gene is transcribed and potentially translated to a gene product
    """

    # === association ===
    id: Union[str, GeneToGeneProductRelationshipId]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === sequence feature relationship ===

    # === gene to gene product relationship ===
    subject: Union[str, GeneId] = None
    relation: Union[str, IriType] = None
    object: Union[str, GeneProductId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GeneToGeneProductRelationshipId):
            self.id = GeneToGeneProductRelationshipId(self.id)
        if self.subject is not None and not isinstance(self.subject, GeneId):
            self.subject = GeneId(self.subject)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if self.object is not None and not isinstance(self.object, GeneProductId):
            self.object = GeneProductId(self.object)


@dataclass
class ExonToTranscriptRelationship(SequenceFeatureRelationship):
    """
    A transcript is formed from multiple exons
    """

    # === association ===
    id: Union[str, ExonToTranscriptRelationshipId]
    relation: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === sequence feature relationship ===

    # === exon to transcript relationship ===
    subject: Union[str, ExonId] = None
    object: Union[str, TranscriptId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, ExonToTranscriptRelationshipId):
            self.id = ExonToTranscriptRelationshipId(self.id)
        if self.subject is not None and not isinstance(self.subject, ExonId):
            self.subject = ExonId(self.subject)
        if self.object is not None and not isinstance(self.object, TranscriptId):
            self.object = TranscriptId(self.object)


@dataclass
class GeneRegulatoryRelationship(Association):
    """
    A regulatory relationship between two genes
    """

    # === association ===
    id: Union[str, GeneRegulatoryRelationshipId]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === gene regulatory relationship ===
    subject: Union[str, GeneOrGeneProductId] = None
    relation: Union[str, IriType] = None
    object: Union[str, GeneOrGeneProductId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GeneRegulatoryRelationshipId):
            self.id = GeneRegulatoryRelationshipId(self.id)
        if self.subject is not None and not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if self.object is not None and not isinstance(self.object, GeneOrGeneProductId):
            self.object = GeneOrGeneProductId(self.object)


@dataclass
class AnatomicalEntityToAnatomicalEntityAssociation(Association):

    # === association ===
    id: Union[str, AnatomicalEntityToAnatomicalEntityAssociationId]
    relation: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === anatomical entity to anatomical entity association ===
    subject: Union[str, AnatomicalEntityId] = None
    object: Union[str, AnatomicalEntityId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, AnatomicalEntityToAnatomicalEntityAssociationId):
            self.id = AnatomicalEntityToAnatomicalEntityAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, AnatomicalEntityId):
            self.subject = AnatomicalEntityId(self.subject)
        if self.object is not None and not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)


@dataclass
class AnatomicalEntityToAnatomicalEntityPartOfAssociation(AnatomicalEntityToAnatomicalEntityAssociation):
    """
    A relationship between two anatomical entities where the relationship is mereological, i.e the two entities are
    related by parthood. This includes relationships between cellular components and cells, between cells and tissues,
    tissues and whole organisms
    """

    # === association ===
    id: Union[str, AnatomicalEntityToAnatomicalEntityPartOfAssociationId]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === anatomical entity to anatomical entity association ===

    # === anatomical entity to anatomical entity part of association ===
    subject: Union[str, AnatomicalEntityId] = None
    relation: Union[str, IriType] = None
    object: Union[str, AnatomicalEntityId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, AnatomicalEntityToAnatomicalEntityPartOfAssociationId):
            self.id = AnatomicalEntityToAnatomicalEntityPartOfAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, AnatomicalEntityId):
            self.subject = AnatomicalEntityId(self.subject)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if self.object is not None and not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)


@dataclass
class AnatomicalEntityToAnatomicalEntityOntogenicAssociation(AnatomicalEntityToAnatomicalEntityAssociation):
    """
    A relationship between two anatomical entities where the relationship is ontogenic, i.e the two entities are
    related by development. A number of different relationship types can be used to specify the precise nature of the
    relationship
    """

    # === association ===
    id: Union[str, AnatomicalEntityToAnatomicalEntityOntogenicAssociationId]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    association_slot: Optional[str] = None

    # === anatomical entity to anatomical entity association ===

    # === anatomical entity to anatomical entity ontogenic association ===
    subject: Union[str, AnatomicalEntityId] = None
    relation: Union[str, IriType] = None
    object: Union[str, AnatomicalEntityId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, AnatomicalEntityToAnatomicalEntityOntogenicAssociationId):
            self.id = AnatomicalEntityToAnatomicalEntityOntogenicAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, AnatomicalEntityId):
            self.subject = AnatomicalEntityId(self.subject)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if self.object is not None and not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)


@dataclass
class Occurrent(NamedThing):
    """
    A processual entity
    """

    # === named thing ===
    id: Union[str, OccurrentId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === occurrent ===
    regulates_process_to_process: List[Union[str, OccurrentId]] = empty_list()
    has_participant: List[str] = empty_list()
    has_input: List[str] = empty_list()
    precedes: List[Union[str, OccurrentId]] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, OccurrentId):
            self.id = OccurrentId(self.id)
        self.regulates_process_to_process = [v if isinstance(v, OccurrentId)
                                             else OccurrentId(v) for v in self.regulates_process_to_process]
        self.precedes = [v if isinstance(v, OccurrentId)
                         else OccurrentId(v) for v in self.precedes]


@dataclass
class BiologicalProcessOrActivity(BiologicalEntity):
    """
    Either an individual molecular activity, or a collection of causally connected molecular activities
    """

    # === named thing ===
    id: Union[str, BiologicalProcessOrActivityId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === biological process or activity ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, BiologicalProcessOrActivityId):
            self.id = BiologicalProcessOrActivityId(self.id)


@dataclass
class MolecularActivity(BiologicalProcessOrActivity):
    """
    An execution of a molecular function carried out by a gene product or macromolecular complex.
    """

    # === named thing ===
    id: Union[str, MolecularActivityId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === biological process or activity ===

    # === molecular activity ===
    regulates_process_to_process: List[Union[str, OccurrentId]] = empty_list()
    has_participant: List[str] = empty_list()
    has_input: List[str] = empty_list()
    precedes: List[Union[str, OccurrentId]] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, MolecularActivityId):
            self.id = MolecularActivityId(self.id)
        self.regulates_process_to_process = [v if isinstance(v, OccurrentId)
                                             else OccurrentId(v) for v in self.regulates_process_to_process]
        self.precedes = [v if isinstance(v, OccurrentId)
                         else OccurrentId(v) for v in self.precedes]


@dataclass
class ActivityAndBehavior(Occurrent):
    """
    Activity or behavior of any independent integral living, organization or mechanical actor in the world
    """

    # === named thing ===
    id: Union[str, ActivityAndBehaviorId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === occurrent ===
    regulates_process_to_process: List[Union[str, OccurrentId]] = empty_list()
    has_participant: List[str] = empty_list()
    has_input: List[str] = empty_list()
    precedes: List[Union[str, OccurrentId]] = empty_list()

    # === activity and behavior ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, ActivityAndBehaviorId):
            self.id = ActivityAndBehaviorId(self.id)


@dataclass
class Procedure(Occurrent):
    """
    A series of actions conducted in a certain order or manner
    """

    # === named thing ===
    id: Union[str, ProcedureId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === occurrent ===
    regulates_process_to_process: List[Union[str, OccurrentId]] = empty_list()
    has_participant: List[str] = empty_list()
    has_input: List[str] = empty_list()
    precedes: List[Union[str, OccurrentId]] = empty_list()

    # === procedure ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, ProcedureId):
            self.id = ProcedureId(self.id)


@dataclass
class Phenomenon(Occurrent):
    """
    a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question
    """

    # === named thing ===
    id: Union[str, PhenomenonId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === occurrent ===
    regulates_process_to_process: List[Union[str, OccurrentId]] = empty_list()
    has_participant: List[str] = empty_list()
    has_input: List[str] = empty_list()
    precedes: List[Union[str, OccurrentId]] = empty_list()

    # === phenomenon ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, PhenomenonId):
            self.id = PhenomenonId(self.id)


@dataclass
class BiologicalProcess(BiologicalProcessOrActivity):
    """
    One or more causally connected executions of molecular functions
    """

    # === named thing ===
    id: Union[str, BiologicalProcessId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === biological process or activity ===

    # === biological process ===
    regulates_process_to_process: List[Union[str, OccurrentId]] = empty_list()
    has_participant: List[str] = empty_list()
    has_input: List[str] = empty_list()
    precedes: List[Union[str, OccurrentId]] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, BiologicalProcessId):
            self.id = BiologicalProcessId(self.id)
        self.regulates_process_to_process = [v if isinstance(v, OccurrentId)
                                             else OccurrentId(v) for v in self.regulates_process_to_process]
        self.precedes = [v if isinstance(v, OccurrentId)
                         else OccurrentId(v) for v in self.precedes]


@dataclass
class Pathway(BiologicalProcess):

    # === named thing ===
    id: Union[str, PathwayId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === biological process or activity ===

    # === biological process ===
    regulates_process_to_process: List[Union[str, OccurrentId]] = empty_list()
    has_participant: List[str] = empty_list()
    has_input: List[str] = empty_list()
    precedes: List[Union[str, OccurrentId]] = empty_list()

    # === pathway ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, PathwayId):
            self.id = PathwayId(self.id)


@dataclass
class PhysiologicalProcess(BiologicalProcess):

    # === named thing ===
    id: Union[str, PhysiologicalProcessId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === biological process or activity ===

    # === biological process ===
    regulates_process_to_process: List[Union[str, OccurrentId]] = empty_list()
    has_participant: List[str] = empty_list()
    has_input: List[str] = empty_list()
    precedes: List[Union[str, OccurrentId]] = empty_list()

    # === physiological process ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, PhysiologicalProcessId):
            self.id = PhysiologicalProcessId(self.id)


@dataclass
class CellularComponent(AnatomicalEntity):
    """
    A location in or around a cell
    """

    # === named thing ===
    id: Union[str, CellularComponentId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === organismal entity ===

    # === anatomical entity ===
    expresses: List[Union[str, GeneOrGeneProductId]] = empty_list()
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    # === cellular component ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, CellularComponentId):
            self.id = CellularComponentId(self.id)


@dataclass
class Cell(AnatomicalEntity):

    # === named thing ===
    id: Union[str, CellId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === organismal entity ===

    # === anatomical entity ===
    expresses: List[Union[str, GeneOrGeneProductId]] = empty_list()
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    # === cell ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, CellId):
            self.id = CellId(self.id)


@dataclass
class CellLine(Biosample):

    # === named thing ===
    id: Union[str, CellLineId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === organismal entity ===

    # === biosample ===
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    # === cell line ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, CellLineId):
            self.id = CellLineId(self.id)


@dataclass
class GrossAnatomicalStructure(AnatomicalEntity):

    # === named thing ===
    id: Union[str, GrossAnatomicalStructureId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()
    related_to: List[Union[str, NamedThingId]] = empty_list()
    interacts_with: List[Union[str, NamedThingId]] = empty_list()
    node_property: Optional[str] = None
    iri: Optional[Union[str, IriType]] = None
    synonym: List[Union[str, LabelType]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    systematic_synonym: Optional[Union[str, LabelType]] = None

    # === biological entity ===
    has_phenotype: List[Union[str, PhenotypicFeatureId]] = empty_list()

    # === organismal entity ===

    # === anatomical entity ===
    expresses: List[Union[str, GeneOrGeneProductId]] = empty_list()
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    # === gross anatomical structure ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GrossAnatomicalStructureId):
            self.id = GrossAnatomicalStructureId(self.id)