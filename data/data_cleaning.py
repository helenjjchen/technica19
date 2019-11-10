import pandas as pd

__name__ = '__main__'

if __name__ == '__main__':
    csv_sat = 'sat2012.csv'
    csv_ap = 'ap2012.csv'
    sat = pd.read_csv(csv_sat)
    ap = pd.read_csv(csv_ap)
    scores = pd.merge(sat, ap, on=['DBN','SCHOOL NAME'])

    csv_enrollment = 'enrollment.csv'
    enrollment = pd.read_csv(csv_enrollment, usecols=['DBN', 'schoolyear',
        'grade9', 'grade10', 'grade11', 'grade12', 'ell_num', 'ell_percent',
        'sped_num', 'sped_percent', 'asian_num', 'asian_per',
        'black_num', 'black_per', 'white_num', 'white_per',
        'hispanic_num', 'hispanic_per', 'male_num', 'male_per',
        'female_num', 'female_per'])
    enrollment = enrollment[enrollment['schoolyear']==20112012]

    demographics = pd.merge(scores, enrollment, on='DBN')

    csv_location = 'location.csv'
    location = pd.read_csv(csv_location, usecols=['ATS SYSTEM CODE',
        'PRIMARY_ADDRESS_LINE_1', 'X_COORDINATE', 'Y_COORDINATE',
        'COMMUNITY_DISTRICT', 'COUNCIL_DISTRICT', 'CENSUS_TRACT',
        'BOROUGH_BLOCK_LOT', 'NTA', 'NTA_NAME', 'Location 1'])

    location['ATS SYSTEM CODE'] = location['ATS SYSTEM CODE'].str.replace(' ', '')

    schools = pd.merge(demographics, location, left_on='DBN',
        right_on='ATS SYSTEM CODE')

    csv_trees = 'trees2015.csv'
    trees = pd.read_csv(csv_trees, usecols=['tree_id', 'status', 'address',
        'postcode', 'community board', 'borough', 'cncldist', 'nta', 'nta_name',
        'boro_ct', 'latitude', 'longitude', 'x_sp', 'y_sp', 'council district',
        'census tract'])

    schools.to_csv('nyc_schools.csv', index=False)
    trees.to_csv('nyc_trees.csv', index=False)
