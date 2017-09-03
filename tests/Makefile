default: 
	for file in $(shell ls *.yaml) ; do \
		resttest.py http://localhost:80 $$file ; \
	done


subject_column_identification:
	resttest.py http://localhost:80 subject_column_identification.yaml

recommend_properties:
	resttest.py http://localhost:80 recommend_properties.yaml

generate_sml_mapping:
	resttest.py http://localhost:80 generate_sml_mapping.yaml

matthias_out_of_bounds_issue:
	resttest.py http://localhost:80 matthias_semicolon_out_of_bounds.yaml
