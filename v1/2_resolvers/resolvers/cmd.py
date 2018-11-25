import subprocess
from sceptre.resolvers import Resolver

class CustomCmd(Resolver):

    def __init__(self, *args, **kwargs):
        super(CustomCmd, self).__init__(*args, **kwargs)

    def resolve(self):
        """
        resolve is the method called by Sceptre. It should carry out the work
        intended by this resolver. It should return a string to become the
        final value.

        self.argument is available from the base class and contains the
        argument defined in the sceptre config file (see below)

        The following attributes may be available from the base class:
        self.stack_config  (A dict of data from <stack_name>.yaml)
        self.environment_config  (A dict of data from config.yaml)
        self.connection_manager (A connection_manager)
        """
        output = (subprocess.check_output(self.argument.split(' '))
                           .decode("utf-8")
                           .strip())
        return output
