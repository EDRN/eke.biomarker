# encoding: utf-8
# Copyright 2009 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''Biomarker folder.'''

from eke.biomarker import ProjectMessageFactory as _
from eke.biomarker.config import PROJECTNAME
from eke.biomarker.interfaces import IBiomarkerFolder
from Products.Archetypes import atapi
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from zope.interface import implements
from eke.knowledge.content import knowledgefolder

BiomarkerFolderSchema = knowledgefolder.KnowledgeFolderSchema.copy() + atapi.Schema((
    atapi.StringField(
        'bmoDataSource',
        required=False,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Biomarker-Organ RDF Data Source'),
            description=_(u'URL to a source of RDF data that supplements the RDF data source with biomarker-organ data.'),
            size=60,
        ),
    ),
))

finalizeATCTSchema(BiomarkerFolderSchema, folderish=True, moveDiscussion=False)

class BiomarkerFolder(knowledgefolder.KnowledgeFolder):
    '''Biomarker folder which contains biomarkers.'''
    implements(IBiomarkerFolder)
    portal_type               = 'Biomarker Folder'
    _at_rename_after_creation = True
    schema                    = BiomarkerFolderSchema
    bmoDataSource             = atapi.ATFieldProperty('bmoDataSource')

atapi.registerType(BiomarkerFolder, PROJECTNAME)
