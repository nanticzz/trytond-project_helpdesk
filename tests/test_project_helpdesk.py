# This file is part of the project_helpdesk module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class ProjectHelpdeskTestCase(ModuleTestCase):
    'Test Project Helpdesk module'
    module = 'project_helpdesk'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        ProjectHelpdeskTestCase))
    return suite