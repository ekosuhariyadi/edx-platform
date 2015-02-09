from xmodule.modulestore.tests.django_utils import ModuleStoreTestCase
from xmodule.modulestore.tests.factories import CourseFactory, ItemFactory

from openedx.core.djangoapps.content.course_structures.models import generate_course_structure


class CourseStructureTests(ModuleStoreTestCase):
    def setUp(self, **kwargs):
        super(CourseStructureTests, self).setUp()
        self.course = CourseFactory.create()
        self.section = ItemFactory.create(parent=self.course, category='chapter', display_name='Test Section')

    def test_generate_course_structure(self):
        blocks = {}

        def add_block(block):
            children = block.get_children() if block.has_children else []

            blocks[unicode(block.location)] = {
                "usage_key": unicode(block.location),
                "block_type": block.category,
                "display_name": block.display_name,
                "graded": block.graded,
                "format": block.format,
                "children": [unicode(child.location) for child in children]
            }

            for child in children:
                add_block(child)

        add_block(self.course)

        expected = {
            'root': unicode(self.course.location),
            'blocks': blocks
        }

        self.maxDiff = None
        actual = generate_course_structure(self.course.id)
        self.assertDictEqual(actual, expected)
