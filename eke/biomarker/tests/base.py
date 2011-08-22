# encoding: utf-8
# Copyright 2008–2011 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''
Testing base code.
'''

from Products.Five import zcml
from Products.Five import fiveconfigure
from Testing import ZopeTestCase as ztc
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup
import eke.knowledge.tests.base as ekeKnowledgeBase
import eke.publications.tests.base as ekePublicationsBase
import eke.study.tests.base as ekeStudyBase
import eke.ecas.tests.base as ekeECASBase

# Traditional Products we have to load manually for test cases:
# (none at this time)

@onsetup
def setupEKESite():
    '''Set up additional products required.'''
    fiveconfigure.debug_mode = True
    import eke.biomarker
    zcml.load_config('configure.zcml', eke.biomarker)
    fiveconfigure.debug_mode = False
    ztc.installPackage('eke.knowledge')
    ztc.installPackage('eke.publications')
    ztc.installPackage('eke.study')
    ztc.installPackage('eke.ecas')
    ztc.installPackage('eke.biomarker')

setupEKESite()
ptc.setupPloneSite(products=['eke.biomarker'])

_biomarkerA = '''<?xml version='1.0' encoding='UTF-8'?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:bmdb="http://edrn.nci.nih.gov/rdf/rdfs/bmdb-1.0.0#">
    <bmdb:Biomarker rdf:about='http://edrn/bmdb/a1'>
        <bmdb:Title>Apogee 1</bmdb:Title>
        <bmdb:ShortName>A1</bmdb:ShortName>
        <bmdb:BiomarkerID>http://edrn/bmdb/a1</bmdb:BiomarkerID>
        <bmdb:URN>urn:edrn:bmdb:bm1</bmdb:URN>
        <bmdb:IsPanel>0</bmdb:IsPanel>
        <bmdb:Description>A sticky bio-marker.</bmdb:Description>
        <bmdb:QAState>Accepted</bmdb:QAState>
        <bmdb:Phase>3</bmdb:Phase>
        <bmdb:Security>Public</bmdb:Security>
        <bmdb:Type>Colloidal</bmdb:Type>
        <bmdb:Alias>Approach</bmdb:Alias>
        <bmdb:Alias>Advent</bmdb:Alias>
        <bmdb:Alias>Bigo</bmdb:Alias>
        <bmdb:memberOfPanel rdf:resource='http://edrn/bmdb/p1'/>
        <bmdb:AccessGrantedTo rdf:resource='ldap://edrn/groups/g1' />
        <bmdb:AssociatedDataset rdf:resource='urn:edrn:top-secret-data'/>
        <bmdb:indicatorForOrgan rdf:resource='http://edrn/bmdb/a1/o1' />
        <bmdb:hasBiomarkerStudyDatas>
            <bmdb:BiomarkerStudyData rdf:about='http://edrn/bmdb/a1/s1'>
                <bmdb:referencesStudy rdf:resource='http://swa.it/edrn/ps' />
            </bmdb:BiomarkerStudyData>
        </bmdb:hasBiomarkerStudyDatas>
        <bmdb:referencedInPublication rdf:resource='http://is.gd/pVKq' />
        <bmdb:referencesResource rdf:resource='http://yahoo.com/' />
    </bmdb:Biomarker>
    <bmdb:Biomarker rdf:about='http://edrn/bmdb/p1'>
        <bmdb:Title>Panel 1</bmdb:Title>
        <bmdb:ShortName>P1</bmdb:ShortName>
        <bmdb:BiomarkerID>http://edrn/bmdb/p1</bmdb:BiomarkerID>
        <bmdb:URN>urn:edrn:bmdb:p1</bmdb:URN>
        <bmdb:IsPanel>1</bmdb:IsPanel>
        <bmdb:Description>A very sticky panel.</bmdb:Description>
        <bmdb:QAState>Accepted</bmdb:QAState>
        <bmdb:Phase>4</bmdb:Phase>
        <bmdb:Security>Public</bmdb:Security>
        <bmdb:Type>Proteinesque</bmdb:Type>
        <bmdb:Alias>Group 1</bmdb:Alias>
        <bmdb:Alias>Composite 1</bmdb:Alias>
        <bmdb:hasBiomarker rdf:resource='http://edrn/bmdb/a1' />
    </bmdb:Biomarker>
</rdf:RDF>'''

_biomarkerOrganA = '''<?xml version='1.0' encoding='UTF-8'?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:bmdb="http://edrn.nci.nih.gov/rdf/rdfs/bmdb-1.0.0#">
    <bmdb:BiomarkerOrganData rdf:about="http://edrn/bmdb/a1/o1">
        <bmdb:URN>http://edrn/bmdb/a1/o1</bmdb:URN>
        <bmdb:Biomarker rdf:resource='http://edrn/bmdb/a1'/>
        <bmdb:Description>Action on the rectum is amazing.</bmdb:Description>
        <bmdb:PerformanceComment>The biomarker failed to perform as expected.</bmdb:PerformanceComment>
        <bmdb:Organ>Rectum</bmdb:Organ>
        <bmdb:Phase>1</bmdb:Phase>
        <bmdb:QAState>Accepted</bmdb:QAState>
        <bmdb:AccessGrantedTo rdf:resource='ldap://edrn/groups/g1'/>
        <bmdb:hasBiomarkerOrganStudyDatas>
            <rdf:Bag>
                <rdf:li rdf:resource='http://edrn/bmdb/a1/o1#s1'/>
            </rdf:Bag>
        </bmdb:hasBiomarkerOrganStudyDatas>
        <bmdb:referencedInPublication rdf:resource='http://is.gd/q6mS'/>
    </bmdb:BiomarkerOrganData>
    <bmdb:BiomarkerOrganStudyData rdf:about='http://edrn/bmdb/a1/o1#s1'>
        <bmdb:referencesStudy rdf:resource='http://swa.it/edrn/ps' />
        <bmdb:DecisionRule>A sample decision rule</bmdb:DecisionRule>
        <bmdb:SensitivityDatas>
            <rdf:Bag>
                <rdf:li rdf:resource='http://tumor.jpl.nasa.gov/bmdb/biomarkers/organs/19/40/sensitivity-data-0' />
                <rdf:li rdf:resource='http://tumor.jpl.nasa.gov/bmdb/biomarkers/organs/19/40/sensitivity-data-1' />
            </rdf:Bag>
        </bmdb:SensitivityDatas>
    </bmdb:BiomarkerOrganStudyData>
    <bmdb:SensitivityData rdf:about='http://tumor.jpl.nasa.gov/bmdb/biomarkers/organs/19/40/sensitivity-data-0'>
        <bmdb:SensSpecDetail>The first one</bmdb:SensSpecDetail>
        <bmdb:Sensitivity>1.0</bmdb:Sensitivity>
        <bmdb:Specificity>2.0</bmdb:Specificity>
        <bmdb:Prevalence>3.0</bmdb:Prevalence>
        <bmdb:NPV>4.0</bmdb:NPV>
        <bmdb:PPV>5.0</bmdb:PPV>
        <bmdb:SpecificAssayType>Sample specific assay type details</bmdb:SpecificAssayType>
    </bmdb:SensitivityData>
    <bmdb:SensitivityData rdf:about='http://tumor.jpl.nasa.gov/bmdb/biomarkers/organs/19/40/sensitivity-data-1'>
        <bmdb:SensSpecDetail>The second two</bmdb:SensSpecDetail>
        <bmdb:Sensitivity>6.0</bmdb:Sensitivity>
        <bmdb:Specificity>7.0</bmdb:Specificity>
        <bmdb:Prevalence>8.0</bmdb:Prevalence>
        <bmdb:NPV>9.0</bmdb:NPV>
        <bmdb:PPV>10.0</bmdb:PPV>
        <bmdb:SpecificAssayType>Sample specific assay type details</bmdb:SpecificAssayType>
    </bmdb:SensitivityData>
</rdf:RDF>'''

_biomarkerB = '''<?xml version='1.0' encoding='UTF-8'?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:bmdb="http://edrn.nci.nih.gov/rdf/rdfs/bmdb-1.0.0#">
    <bmdb:Biomarker rdf:about='http://edrn/bmdb/b1'>
        <bmdb:Title>Bile 1</bmdb:Title>
        <bmdb:ShortName>B1</bmdb:ShortName>
        <bmdb:BiomarkerID>http://edrn/bmdb/b1</bmdb:BiomarkerID>
        <bmdb:URN>urn:edrn:bmdb:bm2</bmdb:URN>
        <bmdb:IsPanel>0</bmdb:IsPanel>
        <bmdb:Description>A brown bio-marker.</bmdb:Description>
        <bmdb:QAState>Under Review</bmdb:QAState>
        <bmdb:Phase>3</bmdb:Phase>
        <bmdb:Security>Public</bmdb:Security>
        <bmdb:Alias>Ooze</bmdb:Alias>
        <bmdb:Type>Colloidal</bmdb:Type>
        <bmdb:AccessGrantedTo rdf:resource='ldap://edrn/groups/g1' />
        <bmdb:indicatorForOrgan rdf:resource='http://edrn/bmdb/a1/o1' />
        <bmdb:hasBiomarkerStudyDatas>
            <bmdb:BiomarkerStudyData rdf:about='http://edrn/bmdb/a1/s1'>
                <bmdb:referencesStudy rdf:resource='http://swa.it/edrn/ps' />
                <bmdb:DecisionRule>A sample decision rule</bmdb:DecisionRule>
            </bmdb:BiomarkerStudyData>
        </bmdb:hasBiomarkerStudyDatas>
        <bmdb:referencedInPublication rdf:resource='http://is.gd/pVKq' />
        <bmdb:referencesResource rdf:resource='http://yahoo.com/' />
    </bmdb:Biomarker>
</rdf:RDF>'''

_biomarkerOrganB = '''<?xml version='1.0' encoding='UTF-8'?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:bmdb="http://edrn.nci.nih.gov/rdf/rdfs/bmdb-1.0.0#">
    <bmdb:BiomarkerOrganData rdf:about="http://edrn/bmdb/b1/o1">
        <bmdb:URN>http://edrn/bmdb/b1/o1</bmdb:URN>
        <bmdb:Biomarker rdf:resource='http://edrn/bmdb/b1'/>
        <bmdb:Description>Action on the anus is amazing.</bmdb:Description>
        <bmdb:PerformanceComment>The biomarker failed to perform as expected.</bmdb:PerformanceComment>
        <bmdb:Organ>Anus</bmdb:Organ>
        <bmdb:Phase>2</bmdb:Phase>
        <bmdb:QAState>Under Review</bmdb:QAState>
        <bmdb:AccessGrantedTo rdf:resource='ldap://edrn/groups/g1'/>
        <bmdb:hasBiomarkerOrganStudyDatas/>
    </bmdb:BiomarkerOrganData>
</rdf:RDF>'''

_biomarkerC = '''<?xml version='1.0' encoding='UTF-8'?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:bmdb="http://edrn.nci.nih.gov/rdf/rdfs/bmdb-1.0.0#">
    <bmdb:Biomarker rdf:about='http://edrn/bmdb/msb'>
        <bmdb:Title>My Single Biomarker</bmdb:Title>
        <bmdb:ShortName>MSB</bmdb:ShortName>
        <bmdb:BiomarkerID>http://edrn/bmdb/msb</bmdb:BiomarkerID>
        <bmdb:URN>urn:edrn:bmdb:msb</bmdb:URN>
        <bmdb:IsPanel>0</bmdb:IsPanel>
        <bmdb:Description>A cloyingly sweet biomarker.</bmdb:Description>
        <bmdb:QAState>Accepted</bmdb:QAState>
        <bmdb:Phase>3</bmdb:Phase>
        <bmdb:Security>Public</bmdb:Security>
        <bmdb:Type>Colloidal</bmdb:Type>
        <bmdb:memberOfPanel rdf:resource='http://edrn/bmdb/mbp'/>
        <bmdb:AccessGrantedTo rdf:resource='ldap://edrn/groups/g1' />
        <bmdb:hasBiomarkerStudyDatas>
            <bmdb:BiomarkerStudyData rdf:about='http://edrn/bmdb/msb/s1'>
                <bmdb:referencesStudy rdf:resource='http://swa.it/edrn/ps' />
            </bmdb:BiomarkerStudyData>
        </bmdb:hasBiomarkerStudyDatas>
    </bmdb:Biomarker>
    <bmdb:Biomarker rdf:about='http://edrn/bmdb/mbp'>
        <bmdb:Title>My Biomarker P[anel]</bmdb:Title>
        <bmdb:ShortName>MBP</bmdb:ShortName>
        <bmdb:BiomarkerID>http://edrn/bmdb/mbp</bmdb:BiomarkerID>
        <bmdb:URN>urn:edrn:bmdb:mbp</bmdb:URN>
        <bmdb:IsPanel>1</bmdb:IsPanel>
        <bmdb:Description>A wood panel, very retro-chic.</bmdb:Description>
        <bmdb:QAState>Accepted</bmdb:QAState>
        <bmdb:Phase>4</bmdb:Phase>
        <bmdb:Security>Public</bmdb:Security>
        <bmdb:Type>Proteinesque</bmdb:Type>
        <bmdb:hasBiomarker rdf:resource='http://edrn/bmdb/msb' />
    </bmdb:Biomarker>
</rdf:RDF>'''

_biomarkerOrganC = '''<?xml version='1.0' encoding='UTF-8'?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"/>'''

def registerLocalTestData():
    ekeKnowledgeBase.registerLocalTestData()
    ekePublicationsBase.registerLocalTestData()
    ekeStudyBase.registerLocalTestData()
    ekeECASBase.registerLocalTestData()
    ekeKnowledgeBase.registerTestData('/biomarkers/a', _biomarkerA)
    ekeKnowledgeBase.registerTestData('/biomarkerorgans/a', _biomarkerOrganA)
    ekeKnowledgeBase.registerTestData('/biomarkers/b', _biomarkerB)
    ekeKnowledgeBase.registerTestData('/biomarkerorgans/b', _biomarkerOrganB)
    ekeKnowledgeBase.registerTestData('/biomarkers/c', _biomarkerC)
    ekeKnowledgeBase.registerTestData('/biomarkerorgans/c', _biomarkerOrganC)

class BaseTestCase(ekeKnowledgeBase.BaseTestCase):
    '''Base for tests in this package.'''
    def setUp(self):
        super(BaseTestCase, self).setUp()
        registerLocalTestData()
    
class FunctionalBaseTestCase(ekeKnowledgeBase.FunctionalBaseTestCase):
    '''Base class for functional (doc-)tests.'''
    def setUp(self):
        super(FunctionalBaseTestCase, self).setUp()
        registerLocalTestData()
    

