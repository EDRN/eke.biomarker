# encoding: utf-8
# Copyright 2009 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''EKE Biomarker: review listing implementation.'''

from eke.biomarker import ProjectMessageFactory as _
from eke.biomarker.config import PROJECTNAME
from eke.biomarker.interfaces import IReviewListing
from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from zope.interface import implements

ReviewListingSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((
    atapi.StringField(
        'accessGroup',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Access Group URI'),
            description=_(u'URI of the access group whose biomarkers should appear in the listing.'),
        ),
    ),
))

ReviewListingSchema['title'].storage = atapi.AnnotationStorage()
ReviewListingSchema['title'].widget.description = _(u'Name of this listing.')
ReviewListingSchema['description'].storage = atapi.AnnotationStorage()
ReviewListingSchema['description'].widget.description = _(u'A short summary of this review listing.')

finalizeATCTSchema(ReviewListingSchema, folderish=False, moveDiscussion=False)

class ReviewListing(base.ATCTContent):
    '''Study statistics.'''
    implements(IReviewListing)
    schema      = ReviewListingSchema
    portal_type = 'Review Listing'
    title       = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    accessGroup = atapi.ATFieldProperty('accessGroup')
    
atapi.registerType(ReviewListing, PROJECTNAME)
