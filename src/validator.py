"""Validator Class"""

from datetime import datetime
from sys import exc_info


class Validator:
    """
    Class for performing validation operations on json input file

    Attributes
    ----------
        logger: logger object

    Methods:
    -------
        validate: Executes the validation methods validate_msg_keys and validate_msg_keys_datatype
        validate_msg_keys: Performs validation of input message schema keys with predefined schema keys to filter if any key is missing
        validate_msg_keys_datatype : Performs validation of input message's datatype with predefined schema keys datatypes
    """
    def __init__(self, logger):
        self.logger = logger

        self.schema_string_fields = {
            "id": str,
            "anonymous_id": str,
            "context_library_name": str,
            "context_library_version": str, 
            "context_app_version": str,
            "context_device_manufacturer": str,
            "context_device_model": str,
            "context_device_type": str,
            "context_locale": str,
            "context_os_name": str,
            "context_timezone": str,
            "event": str,
            "event_text": str,
            "user_id": (int, str),
            "context_network_carrier": str,
            "context_device_token": (str, None.__class__),
            "context_traits_taxfix_language": str
        }

        self.schema_boolean_fields = {
            "context_device_ad_tracking_enabled": bool,
            "context_network_wifi": bool,
        }

        self.schema_datetime_fields = {
            "received_at": datetime,
            "sent_at": datetime,
            "timestamp": datetime,
        }

        self.schema_utc_datetime_fields = {
            "original_timestamp": datetime
        }


    def validate(self, msg):
        """
        Executes the validation methods validate_msg_keys and validate_msg_keys_datatype
        """
        try:
            self.validate_msg_keys(msg=msg)
            
            self.validate_msg_keys_datatype(msg=msg)

        except Exception as ex:
            self.logger.error(ex, exc_info=True)


    def validate_msg_keys(self, msg):
        """
        Performs validation of input message keys with predefined schema keys 
        to filter if any key is missing in incoming message record
        """
        try:
            keys =  set(self.schema_string_fields.keys()).union(
                    set(self.schema_boolean_fields.keys()),
                    set(self.schema_datetime_fields.keys())) - set(msg.keys())

            if len(keys) > 0:
                self.logger.info(f"Missing fields {keys}")

        except Exception as ex:
            self.logger.error(ex, exc_info=True)


    def validate_msg_keys_datatype(self, msg):
        """
        Performs datatype validation for input message keys with predefined datatypes of schema keys
        """
        try:
            for _key in msg.keys():

                if _key in self.schema_string_fields.keys():

                    if not isinstance(msg[_key], self.schema_string_fields[_key]):
                        self.logger.info(f'Datatype not same as in schema for {_key}')
                
                if _key in self.schema_boolean_fields.keys():
                    if not isinstance(msg[_key], self.schema_boolean_fields[_key]):
                        self.logger.info(f'Datatype not same as in schema for {_key}')

                if _key in self.schema_datetime_fields.keys():
                    try:
                        value = datetime.strptime(msg[_key], "%Y-%m-%d %H:%M:%S.%f")
                        if not isinstance(value, self.schema_datetime_fields[_key]):
                            self.logger.info(f'Datatype not same as in schema for {_key}')
                    except Exception as ex:
                        self.logger.info(f'Datatype not same as in schema for {_key}')

                if _key in self.schema_utc_datetime_fields.keys():
                    try:
                        value = datetime.strptime(msg[_key], "%Y-%m-%dT%H:%M:%S.%f%z")
                        if not isinstance(value, self.schema_utc_datetime_fields[_key]):
                            self.logger.info(f'Datatype not same as in schema for {_key}')
                    except Exception as ex:
                        self.logger.info(f'Datatype not same as in schema for {_key}')

        except Exception as ex:
            self.logger.error(ex, exc_info=True)
