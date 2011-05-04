# encoding: utf-8
# Copyright 2009 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''
EKE Biomarker: test the setup of this package.
'''

import unittest
from eke.biomarker.tests.base import BaseTestCase
from Products.CMFCore.utils import getToolByName

class TestSetup(BaseTestCase):
    '''Unit tests the setup of this package.'''
    def testCatalogIndexes(self):
        '''Check if indexes are properly installed.'''
        catalog = getToolByName(self.portal, 'portal_catalog')
        indexes = catalog.indexes()
        for i in ('biomarkerType', 'indicatedBodySystems', 'accessGroups'):
            self.failUnless(i in indexes)
    def testCatalogMetadata(self):
        '''Check if indexed metadata schema are properly installed.'''
        catalog = getToolByName(self.portal, 'portal_catalog')
        metadata = catalog.schema()
        for i in ('biomarkerType', 'indicatedBodySystems'):
            self.failUnless(i in metadata)
    def testTypes(self):
        '''Make sure our types are available.'''
        types = getToolByName(self.portal, 'portal_types').objectIds()
        for i in (
            'Biomarker Folder', 'Elemental Biomarker', 'Biomarker Panel', 'Biomarker Body System', 'Body System Study',
            'Study Statistics'
        ):
            self.failUnless(i in types)
    def testTypesNotSearched(self):
        '''Ensure our "structural" types aren't searched by default.'''
        notSearched = self.portal.portal_properties.site_properties.getProperty('types_not_searched')
        for i in ('Biomarker Body System', 'Body System Study', 'Study Statistics'):
            self.failUnless(i in notSearched)
    def testForWideURLField(self):
        '''Ensure fields for URLs are extra wide.'''
        from eke.biomarker.content.biomarkerfolder import BiomarkerFolderSchema
        self.failUnless(BiomarkerFolderSchema['bmoDataSource'].widget.size >= 60)

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite
    
