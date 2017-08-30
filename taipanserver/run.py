#!flask/bin/python
from flask import Flask
from flask import request, abort, jsonify

from taipan.generictable import GenericTable
from taipan.ml.subjectcolumn.scidentifier import SCIdentifier
from taipan.recommender.properties.lov import get_table_properties
from taipan.sml.taipantosml import TaipanToSML


app = Flask(__name__)

@app.route('/table/api/v1.0/identify_subject_column', methods=['POST'])
def identify_subject_column():
    if not request.data:
        abort(400)

    delimiter = ","
    quotechar = '"'
    if "X-Delimiter" in request.headers:
        delimiter = request.headers["X-Delimiter"]
        delimiter = " " if delimiter == "space" else delimiter
    if "X-QuoteChar" in request.headers:
        quotechar = request.headers["X-QuoteChar"]
    table_string = request.data.decode("utf-8")
    table = GenericTable(
        "stub",
        _id=None,
        csv_string=table_string,
        delimiter=delimiter,
        quotechar=quotechar
    )
    table.init()
    SCIDENTIFIER = SCIdentifier()
    subject_column = SCIDENTIFIER.identify_subject_column(table)
    return jsonify({'subject_column': subject_column}), 200


@app.route('/table/api/v1.0/recommend_properties', methods=['POST'])
def recommend_properties():
    if not request.data:
        abort(400)

    delimiter = ","
    quotechar = '"'
    if "X-Delimiter" in request.headers:
        delimiter = request.headers["X-Delimiter"]
        delimiter = " " if delimiter == "space" else delimiter
    if "X-QuoteChar" in request.headers:
        quotechar = request.headers["X-QuoteChar"]

    table_string = request.data.decode("utf-8")
    table = GenericTable(
        "stub",
        _id=None,
        csv_string=table_string,
        delimiter=delimiter,
        quotechar=quotechar
    )
    table.init()
    properties = get_table_properties(table)
    return jsonify(properties), 200


@app.route('/table/api/v1.0/generate_sml_mapping', methods=['POST'])
def generate_sml_mapping():
    if not request.data:
        abort(400)
    if not "X-Subject-Namespace" in request.headers:
        abort(400)

    delimiter = ","
    quotechar = '"'
    if "X-Delimiter" in request.headers:
        delimiter = request.headers["X-Delimiter"]
        delimiter = " " if delimiter == "space" else delimiter
    if "X-QuoteChar" in request.headers:
        quotechar = request.headers["X-QuoteChar"]

    subject_namespace = request.headers["X-Subject-Namespace"]
    table_string = request.data.decode("utf-8")
    table = GenericTable(
        "stub",
        _id=None,
        csv_string=table_string,
        delimiter=delimiter,
        quotechar=quotechar
    )
    table.init()
    sc_ident = SCIdentifier()
    subject_column = sc_ident.identify_subject_column(table)
    property_mappings = get_table_properties(table)
    sml_mapping = TaipanToSML(property_mappings, subject_namespace, subject_column[0])
    return sml_mapping.get_mapping(), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
