import sys
from resource_management import *
class Master(Script):
  def install(self, env):
    print 'Install the Sample Srv Master';
  def stop(self, env):
    print 'Stop the Sample Srv Master';
  def start(self, env):
    print 'Start the Sample Srv Master';
     
  def status(self, env):
    print 'Status of the Sample Srv Master';
  def configure(self, env):
    print 'Configure the Sample Srv Master';
if __name__ == "__main__":
  Master().execute()
