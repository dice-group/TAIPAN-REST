#!flask/bin/python
from flask import Flask
from flask import request, abort, jsonify

from taipan.generictable import GenericTable
from taipan.ml.subjectcolumn.scidentifier import SCIdentifier
from taipan.recommender.properties.lov import get_table_properties

app = Flask(__name__)

@app.route('/table/api/v1.0/identify_subject_column', methods=['POST'])
def identify_subject_column():
    if not request.data:
        abort(400)
    table_string = request.data.decode("utf-8")
    table = GenericTable("stub", _id=None, csv_string=table_string)
    table.init()
    SCIDENTIFIER = SCIdentifier()
    #Returns nothing, needs tuning!
    subject_column = SCIDENTIFIER.identify_subject_column(table)
    return jsonify({'subject_column': subject_column}), 200


@app.route('/table/api/v1.0/recommend_properties', methods=['POST'])
def recommend_properties():
    if not request.data:
        abort(400)
    table_string = request.data.decode("utf-8")
    table = GenericTable("stub", _id=None, csv_string=table_string)
    table.init()
    properties = get_table_properties(table)
    print(properties)
    return jsonify(properties), 200



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
