Middleware Configuration
========================

The middleware configuration is done by environment variables (or using and .env file if your project uses python-dotenv).

The main variables are shown in the table below:

.. list-table::
   :header-rows: 1

   * - Name
     - Description
     - Values
     - Default
   * - TRANSACTION_MIDDLEWARE_LOG_LEVEL
     - Log level for the application
     - DEBUG, INFO, WARNING, ERROR, CRITICAL
     - INFO
   * - TRANSACTION_MIDDLEWARE_LOG_FORMAT
     - Log format
     - See python logger documentation
     - %(log_color)s%(levelname)-9s%(reset)s %(asctime)s %(name)s %(message)s
   * - TRANSACTION_MIDDLEWARE_DISABLED
     - Transaction middleware enabled/disabled
     - false, true
     - false
