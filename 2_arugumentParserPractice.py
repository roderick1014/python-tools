from argparse import ArgumentParser


def display_config(args):
    print(vars(args))       # vars() function returns all attributes in the class in a dict() :).


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--epoch', help='num of epochs.', type = int, default=9999)
    parser.add_argument('--batch_size', help='size of each batch.', type=int, default=5)
    parser.add_argument('--nonsense', help = 'dont care', type = str, default='hahaha')

    args = parser.parse_args()
    display_config(args)

    # print('epoch: ', args.epoch)
    # print('batch_size: ', args.batch_size)
    # print(args.nonsense)