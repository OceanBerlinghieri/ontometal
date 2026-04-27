from rdf_conversion.pipeline import Pipeline
from rdf_conversion.repository.country_repository_impl import CountryRepositoryImpl
from rdf_conversion.repository.resource.csv_resource import CSVResource
from rdf_conversion.repository.resource.turtle_resource import TurtleResource

if __name__ == "__main__":
    csv_resource = CSVResource()
    turtle_resource = TurtleResource()
    country_repository = CountryRepositoryImpl(resource=csv_resource)

    pipeline = Pipeline(
        country_repository=country_repository,
        turtle_resource=turtle_resource,
    )
    pipeline.run()
