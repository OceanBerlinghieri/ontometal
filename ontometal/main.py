import configparser
import os

from ontometal.entities.ontology_metadata import OntologyMetadata
from ontometal.repositories.resources.turtle_resource import TurtleResource
from ontometal.pipeline import Pipeline
from ontometal.services.class_builder import ClassBuilder
from ontometal.services.data_property_builder import DataPropertyBuilder
from ontometal.services.object_property_builder import ObjectPropertyBuilder
from ontometal.services.ontology_metadata_builder import OntologyMetadataBuilder


def _load_ontology_metadata() -> OntologyMetadata:
    working_dir = os.getcwd()
    config = configparser.ConfigParser()
    config.read(working_dir + "/config/ontology_config.ini")

    imports = [
        item.strip()
        for item in config.get("IMPORTS", "URIS").split(",")
        if item.strip()
    ]

    return OntologyMetadata(
        uri=config.get("ONTOMETAL", "URI"),
        version=config.get("ONTOMETAL", "VERSION"),
        version_info=config.get("ONTOMETAL", "VERSION_INFO"),
        creator=config.get("ONTOMETAL", "CREATOR"),
        created=config.get("ONTOMETAL", "CREATED"),
        contributor=config.get("ONTOMETAL", "CONTRIBUTOR"),
        publisher=config.get("ONTOMETAL", "PUBLISHER"),
        title=config.get("ONTOMETAL", "TITLE"),
        license=config.get("ONTOMETAL", "LICENSE"),
        comment=config.get("ONTOMETAL", "COMMENT"),
        preferred_namespace_prefix=config.get(
            "ONTOMETAL", "PREFERRED_NAMESPACE_PREFIX"
        ),
        preferred_namespace_uri=config.get("ONTOMETAL", "PREFERRED_NAMESPACE_URI"),
        imports=imports,
    )


def main():
    working_dir = os.getcwd()

    driver_config = configparser.ConfigParser()
    driver_config.read(working_dir + "/config/driver_config.ini")
    turtle_resource = TurtleResource(driver_config)

    ontology_metadata = _load_ontology_metadata()
    ontology_metadata_adder = OntologyMetadataBuilder(ontology_metadata)

    class_builder = ClassBuilder()
    object_property_builder = ObjectPropertyBuilder()
    data_property_builder = DataPropertyBuilder()

    pipeline = Pipeline()
    pipeline.run(
        turtle_resource,
        ontology_metadata_adder,
        class_builder,
        data_property_builder,
        object_property_builder,
    )


if __name__ == "__main__":
    main()
