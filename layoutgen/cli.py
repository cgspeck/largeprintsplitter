import argparse

from input_handler import load_image
from page_geometries import PageGeometry

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'image_file',
        type=argparse.FileType('rb'),
        help='Image to parse'
    )
    image_dimension_group = parser.add_mutually_exclusive_group(required=True)
    image_dimension_group.add_argument(
        '--width', type=int,
        help='Width of image in millimeters'
    )
    image_dimension_group.add_argument(
        '--height', type=int,
        help='Height of image in millimeters'
    )
    parser.add_argument(
        '--page_size',
        default='a3',
        help='Page size, e.g. a3, a4'
    )
    parser.add_argument(
        '--overlap',
        default=20,
        type=int,
        help='Print overlap in mm'
    )
    return parser

if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()

    input_image = load_image(args.image_file, args.width, args.height)
    page_geo = PageGeometry(args.page_size, portait=input_image.is_portrait())

    if input_image.fits_on_a_page(page_geo.max_printable_dimensions()):
        print('The image will fit on a single page')
    else:
        print('The image will not fit on a single page')

    crop_list = input_image.calculate_print_chunks(page_geo.max_printable_dimensions(), args.overlap)
    print(f'This will require {len(crop_list)} pages')
    input_image.chunk_and_annotate_image(crop_list)
