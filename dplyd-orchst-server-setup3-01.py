import  re
################################################################################################
# 12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012 #
################################################################################################
_ba01 = open ("/etc/systemd/system/user@.service.d/delegate.conf", "r").read ().strip ()
if re.search (r'\[Service\]' , _ba01) == None: _ba01 = _ba01 + "\n[Service]\n"
_ba01 =_ba01.strip ()
_ba01 =_ba01 = _ba01 + "\n"
open ("/etc/systemd/system/user@.service.d/delegate.conf", "w").write ( _ba01 )
