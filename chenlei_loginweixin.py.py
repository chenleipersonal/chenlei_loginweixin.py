Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============== RESTART: C:\Users\asus\chenlei_loginweixin.py.py ==============
█Getting uuid of QR code.
Downloading QR code.
Please scan the QR code to log in.
Please press confirm on your phone.
Loading the contact, this may take a little while.
--- Logging error ---
Traceback (most recent call last):
  File "C:\Users\asus\AppData\Local\Programs\Python\Python37\lib\logging\__init__.py", line 1037, in emit
    stream.write(msg + self.terminator)
  File "C:\Users\asus\AppData\Local\Programs\Python\Python37\lib\idlelib\run.py", line 362, in write
    return self.shell.write(s, self.tags)
  File "C:\Users\asus\AppData\Local\Programs\Python\Python37\lib\idlelib\rpc.py", line 608, in __call__
    value = self.sockio.remotecall(self.oid, self.name, args, kwargs)
  File "C:\Users\asus\AppData\Local\Programs\Python\Python37\lib\idlelib\rpc.py", line 220, in remotecall
    return self.asyncreturn(seq)
  File "C:\Users\asus\AppData\Local\Programs\Python\Python37\lib\idlelib\rpc.py", line 251, in asyncreturn
    return self.decoderesponse(response)
  File "C:\Users\asus\AppData\Local\Programs\Python\Python37\lib\idlelib\rpc.py", line 271, in decoderesponse
    raise what
UnicodeEncodeError: 'UCS-2' codec can't encode characters in position 27-27: Non-BMP character not supported in Tk
Call stack:
  File "<string>", line 1, in <module>
  File "C:\Users\asus\AppData\Local\Programs\Python\Python37\lib\idlelib\run.py", line 144, in main
    ret = method(*args, **kwargs)
  File "C:\Users\asus\AppData\Local\Programs\Python\Python37\lib\idlelib\run.py", line 474, in runcode
    exec(code, self.locals)
  File "C:\Users\asus\chenlei_loginweixin.py.py", line 3, in <module>
    itchat.login()
  File "C:\Users\asus\AppData\Local\Programs\Python\Python37\lib\site-packages\itchat\components\login.py", line 80, in login
    logger.info('Login successfully as %s' % self.storageClass.nickName)
Unable to print the message and arguments - possible formatting error.
Use the traceback above to help find the error.
318
男性好友：64.15%
女性好友： 29.25%
其他：6.92%
>>> 
