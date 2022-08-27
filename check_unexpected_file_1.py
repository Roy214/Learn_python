import glob
import re

flag = False
pat = '^domain_realm_*'
accepted_filename = ['/var/lib/sss/pubconf/krb5.include.d/krb5_libdefaults',
                     '/var/lib/sss/pubconf/krb5.include.d/localauth_plugin']
for name in glob.glob("/var/lib/sss/pubconf/krb5.include.d/*"):
    # print("Files inside directory",name)
    flag = False
    if not re.match(pat, name.split("/")[-1]):
        for file_name in accepted_filename:
            # print(accepted files, " ", file_name)
            if name == file_name:
                flag = True
                break
    else:
        flag = True

    if not flag:
        print("Unexpected files present")
        break
if flag:
    print("No unexpected file found")

