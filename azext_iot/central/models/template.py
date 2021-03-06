# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


class Template:
    def __init__(self, template: dict):
        self.raw_template = template
        try:
            self.id = template.get("id")
            self.name = template.get("displayName")
            self.interfaces = self._extract_interfaces(template)
            self.schema_names = self._extract_schema_names(self.interfaces)
        except:
            raise CLIError("Could not parse iot central device template.")

    def get_schema(self, telemetry_name, interface_name=""):
        # interface_name has been specified, do a pointed lookup
        if interface_name:
            interface = self.interfaces.get(interface_name, {})
            return interface.get(telemetry_name)

        # find first matching telemetry_name in any interface
        for interface in self.interfaces.values():
            schema = interface.get(telemetry_name)
            if schema:
                return schema

        # not found
        return None

    def _extract_interfaces(self, template: dict) -> dict:
        try:
            dcm = template.get("capabilityModel", {})
            interfaces = dcm.get("implements", {})
            return {
                interface["name"]: self._extract_schemas(interface)
                for interface in interfaces
            }
        except Exception:
            details = "Unable to extract device schema from template '{}'.".format(
                self.id
            )
            raise CLIError(details)

    def _extract_schemas(self, interface: dict) -> dict:
        return {schema["name"]: schema for schema in interface["schema"]["contents"]}

    def _extract_schema_names(self, interfaces: dict) -> dict:
        return {
            interface_name: list(interface_schemas.keys())
            for interface_name, interface_schemas in interfaces.items()
        }
