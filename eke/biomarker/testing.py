# encoding: utf-8
# Copyright 2011 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

from eke.knowledge.testing import EKE_KNOWLEDGE_FIXTURE
from eke.publications.testing import EKE_PUBLICATIONS_FIXTURE
from eke.site.testing import EKE_SITE_FIXTURE
from eke.study.testing import EKE_STUDY_FIXTURE
from plone.app.testing import PloneSandboxLayer, IntegrationTesting, FunctionalTesting
from plone.testing import z2

class EKEBiomarker(PloneSandboxLayer):
    defaultBases = (EKE_STUDY_FIXTURE, EKE_SITE_FIXTURE, EKE_PUBLICATIONS_FIXTURE, EKE_KNOWLEDGE_FIXTURE)
    def setUpZope(self, app, configurationContext):
        import eke.biomarker
        self.loadZCML(package=eke.biomarker)
        z2.installProduct(app, 'eke.biomarker')
        import eke.biomarker.tests.base
        eke.biomarker.tests.base.registerLocalTestData()
    def setUpPloneSite(self, portal):
        self.applyProfile(portal, 'eke.biomarker:default')
    def teatDownZope(self, app):
        z2.uninstallProduct(app, 'eke.biomarker')

EKE_BIOMARKER_FIXTURE = EKEBiomarker()
EKE_BIOMARKER_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EKE_BIOMARKER_FIXTURE,),
    name='EKEBiomarker:Integration',
)
EKE_BIOMARKER_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(EKE_BIOMARKER_FIXTURE,),
    name='EKEBiomarker:Functional',
)
