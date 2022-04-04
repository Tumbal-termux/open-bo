import os
if __name__ == "__main__":
   try:
       __import__("bo").infoo()
   except Exception as e:
       exit(str(e))
