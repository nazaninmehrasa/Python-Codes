from optparse import OptionParser


parser = OptionParser()
parser.add_option('-s', '--recompute_features', dest='s', action="store_true", default=False)
parser.add_option('-f', '--compute-db', dest='f', action="store_true", default=False)

(options, args) = parser.parse_args()
if not options.s:
    parser.error('Comment not provided...exiting')
    
else:
    parser.error('hello')
