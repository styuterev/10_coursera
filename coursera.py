import lxml
import urllib.request
import argparse
import logging


def get_courses_xml(courses_page):
    with urllib.request.urlopen(courses_page) as response:
        logger.info('Getting course list from URL: {}'.format(courses_page))
        courses_xml = response.read()
        logger.debug('Courses XML:\n {}'.format(courses_xml))
        return courses_xml


def get_course_urls(courses_xml):
    pass


def get_course_info(course_slug):
    pass


def output_courses_info_to_xlsx(filepath):
    pass


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('courses_page', type=str,
                        help='URL of XML document with list of courses.')
    return parser.parse_args()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    arguments = parse_arguments()
    get_courses_xml(arguments.courses_page)
