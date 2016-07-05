Config Loader
=============

Example Usage
-------------

.. code-block:: Python

    from eliza.config import ConfigLoader
    self.config_loader = ConfigLoader(use_vault=False)
    self.config = self.config_loader.load_config(path='resources/', environment='develop')

Load a config file
------------------

The config module can load config files in yaml format. Its possible to include vault secrets and environment variables as described below.

Loading a config consits of two steps, first **default.yaml** will be loaded, then **<environment>.yaml**.

Keys in the environment file will override the default config.

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
