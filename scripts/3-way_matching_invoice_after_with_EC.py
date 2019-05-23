import os
from pathlib import Path
from pprint import pprint

from conformance_checking.rule_base import Rule_Checker
from util import import_xes_log

working_dir = Path("C:/Users/Simon.Remy/ownCloud/Projects/BPI19/BPI19 - Logs")

os.chdir(working_dir)
print('changed directory to: %s' % os.getcwd())

log_file = Path("3-way invoice after GR/with EC/Invoice after GR (with EC).xes")

log = import_xes_log(log_file, '{http://www.xes-standard.org}')
print('length: %s' % len(log))
print(log[0])

rc = Rule_Checker()

print('####### order rules ########')
res = rc.check_order(log, 'Record Service Entry Sheet', 'Record Invoice Receipt')
pprint(res)

res = rc.check_order(log, 'Record Goods Receipt', 'Record Invoice Receipt')
pprint(res)

res = rc.check_order(log, 'SRM: Change was Transmitted', 'Create Purchase Order Item')
pprint(res)

print('####### response rules ########')
res = rc.check_response(log, 'Record Goods Receipt', 'Record Invoice Receipt')
pprint(res)

res = rc.check_response(log, 'Record Invoice Receipt', 'Clear Invoice')
pprint(res)

res = rc.check_response(log, 'Record Invoice Receipt', 'Clear Invoice', True)
pprint(res)

print('####### precedence rules ########')
res = rc.check_precedence(log, 'Vendor creates invoice', 'Record Invoice Receipt', True)
pprint(res)

res = rc.check_precedence(log, 'Create Purchase Order Item', 'Vendor creates invoice', True)
pprint(res)

print('####### cardinality rules ########')
res = rc.check_cardinality(log, 'Clear Invoice', 1, 1)
pprint(res)

res = rc.check_cardinality(log, 'Create Purchase Order Item', 1, 1)
pprint(res)

res = rc.check_cardinality(log, 'Vendor creates invoice', 1, 1)
pprint(res)

res = rc.check_cardinality(log, 'Record Invoice Receipt', 1, 1)
pprint(res)

res = rc.check_cardinality(log, 'Record Goods Receipt', 1, 1)
pprint(res)