# Taipan REST Interface

This is a REST interface for [Taipan](https://github.com/dice-group/TAIPAN) CSV to RDF matching application.

# For Development
```
make build-dev
make run-dev
```

# For Production
```
make build
make run
```

You can also deploy docker container directly from Docker Hub.
```
docker run -p 80:5000 dice-group/taipan-rest
```

# Usage

To generate SML for a given CSV file, you need to submit CSV via POST request to /table/api/v1.0/generate_sml_mapping.
If your CSV use delimiter different from ',' (comma) or quotechar different from '"' (doublequote), you can set the headers "X-Delimiter" and "X-QuoteChar" to override defaults.
In case if your delimiter is a " " (space character), define it as a "space" (with a space keyword).

For the details please see [tests](./tests)
