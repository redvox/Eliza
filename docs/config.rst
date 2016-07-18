Config Loader
=============

Example Usage
-------------

.. code-block:: Python

    from eliza.config import ConfigLoader
    self.config_loader = ConfigLoader(use_vault=False)
    self.config = self.config_loader.load_config(path='resources/', environment=['default', 'develop'])

Load a config file
------------------

The config module can load config files in yaml format. Its possible to include vault secrets and environment variables as described below.

Config names can be passed as single name or as list of names. The file name pattern has to end with yaml.

Example: **<config_name>.yaml**

Every config in list will be loaded and merged to a single dictionary, where latter configs override previous ones.

Use Vault
---------

If you want to include vault secrets, include **<%= VAULT['secret/path'] %>** as key in your yaml file.

.. code-block:: yaml

    filename: default
    secret: <%= VAULT['secret/path'] %>


Use Environment Variables
-------------------------

If you want to include vault secrets, include **<%= ENV['variable_name'] %>** as key in your yaml file.

.. code-block:: yaml

    filename: default
    test_env: <%= ENV['HOME'] %>
