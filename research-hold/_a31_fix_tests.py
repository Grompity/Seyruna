import ast
ts = open("tests.py").read()

# --- T168 de-pinned: the seam-cap FAMILY is what the bound-law weighs ----
old = '           and set(tr["keys"]) == {"GRADE_MAXTOK", "AUDIT_MAXTOK", "SYNTH_MAXTOK"}'
assert ts.count(old) == 1
ts = ts.replace(old, '           and {"GRADE_MAXTOK", "AUDIT_MAXTOK",\n'
                    '                   "SYNTH_MAXTOK"} <= set(tr["keys"])\n'
                    '           and all(k.endswith("_MAXTOK") for k in tr["keys"])', 1)

old = '       "is the global word); the config carries the three seam words and "'
assert ts.count(old) == 1
NEW = ('       "is the global word); the charter carries the seam-cap family '
       '(three A29 "\n'
       '       "words; A31\'s lap added a fourth to the family - the bound-law "\n'
       '       "weighs ALL of them, never one era\'s count) and "')
ts = ts.replace(old, NEW, 1)

# --- T172: the APPLIED moment must be OBSERVED, not assumed -------------
old = '    _old31, _prior31 = loop.apply_word(_p31, "GENERAL_MAXTOK", 1024)\n    _back31 = loop.restore_bytes(_p31, _prior31)'
assert ts.count(old) == 1
ts = ts.replace(old, '    _old31, _prior31 = loop.apply_word(_p31, "GENERAL_MAXTOK", 1024)\n'
                     '    _mid31 = loop.read_cfg(_p31)          # the word WHILE applied\n'
                     '    _back31 = loop.restore_bytes(_p31, _prior31)', 1)

old = '    "apply": (_old31, _back31.get("GENERAL_MAXTOK")),\n    "restored-exact": _exact,'
assert ts.count(old) == 1
ts = ts.replace(old, '    "apply": (_old31, _mid31.get("GENERAL_MAXTOK"),\n'
                     '              _back31.get("GENERAL_MAXTOK")),\n'
                     '    "restored-exact": _exact,', 1)

old = ('           and tr["apply"][0] is None and tr["apply"][1] == 1024\n'
       '           and tr["restored-exact"])')
assert ts.count(old) == 1
ts = ts.replace(old, ('           and tr["apply"][0] is None and tr["apply"][1] == 1024\n'
                      '           and tr["apply"][2] is None\n'
                      '           and tr["restored-exact"])'), 1)

old = ('       "one-key write hands back the old word (None when it was absent) "\n'
       '       "and a RESTORE returns the EXACT prior bytes')
assert ts.count(old) == 1
ts = ts.replace(old, ('       "one-key write hands back the old word (None when it was absent), "\n'
                      '       "the APPLIED charter carries the new one, the RESTORED charter has "\n'
                      '       "it GONE again (both moments read - the restore\'s absence IS the "\n'
                      '       "restore WORKING), and a RESTORE returns the EXACT prior bytes'), 1)

open("tests.py", "w").write(ts)
ast.parse(ts)
print("amendments applied")
