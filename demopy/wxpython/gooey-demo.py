from gooey import Gooey, GooeyParser


@Gooey(program_name='Hello')
def main():
    parser = GooeyParser(description='A Demo')
    parser.add_argument('path', widget='FileChooser')
    parser.add_argument('date', widget='DateChooser')
    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    main()
