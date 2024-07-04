# Standard library imports
from dataclasses import dataclass


@dataclass
class DBCONSTANTS:
    """
    A data class holding constant values for configuring connections to an database.

    This class encapsulates essential parameters required for establishing a connection to
    an database, including server address, user credentials, port, service name,
    JDBC driver, and JDBC URL. The constants defined within this class can be used to
    configure database connections consistently across different modules.

    Note:
        This class is marked as frozen, ensuring that the defined constants remain
        immutable throughout the program.
    """

    SERVER = "servername"
    USERNAME =  "username"
    PASSWORD = "password"
    PORT = "port"

    # Driver and JDBC will be different for different databases, this is for oracle db as reference
    DRIVER = "oracle.jdbc.driver.OracleDriver"
    JDBCURL = f"jdbc:oracle:thin:@{SERVER}:{PORT}"
   
