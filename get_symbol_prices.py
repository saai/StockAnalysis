#!/usr/bin/env python2
import sys
import json
import os
from fetch_price import get_stock_year_price

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print 'get_symbol_prices.py [symbols file] [year] [output_dir]'
        sys.exit(1)
    sym_file = sys.argv[1]
    year = int(sys.argv[2])
    output = sys.argv[3]
    with open(sym_file, "r") as fp:
        for line in fp.readlines():
            sym =  line.strip()
            ret = get_stock_year_price(sym, year, year)
            json_output = json.dumps(ret, indent=4, sort_keys=True)
            output_filename = os.path.join(output, sym.upper() + ".json")
            output_fp = open(output_filename, "w")
            output_fp.write(json_output)
            output_fp.close()
            print "fetch " + sym.upper() + " successfully" 
 