# encoding: utf-8
# Copyright 2009 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''
EKE Biomarkers: functional and documentation tests.
'''

from Testing import ZopeTestCase as ztc
import unittest, doctest, base

def test_suite():
	return unittest.TestSuite([
		ztc.ZopeDocFileSuite('README.txt', package='eke.biomarker',
			test_class=base.FunctionalBaseTestCase,
			optionflags=doctest.REPORT_ONLY_FIRST_FAILURE | doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS)
	])
	

if __name__ == '__main__':
	unittest.main(defaultTest='test_suite')
	
