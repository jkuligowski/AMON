import argparse

from microMetabPred.parse_KEGG import get_from_kegg_flat_file, parse_organism

if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', '--input', help="KEGG organism flat file",
                        required=True)
    parser.add_argument('-o', '--output', help="Output file of new line separated list of KOs from genome",
                        required=True)

    args = parser.parse_args()

    kegg_org_file_loc = args.input
    output_file = args.output

    org_records = get_from_kegg_flat_file(kegg_org_file_loc, parser=parse_organism)
    # for org_record in org_records:
    kos = [org_record['ORTHOLOGY'][0] for org_record in org_records if 'ORTHOLOGY' in org_record]

    with open(output_file, 'w') as f:
        f.write('%s\n' % '\n'.join(kos))