class State:
    def __init__(self, name, abbreviation, zip_code, fips_code):
        self.name = name
        self.abbreviation = abbreviation
        self.zip_code = zip_code
        self.fips_code = fips_code

    def get_name(self):
        return self.name
    
    def get_a_name(self):
        return self.abbreviation
    
    def get_zip(self):
        return self.zip_code
    
    def get_fip(self):
        return self.fips_code

states = [
    State("Alabama", "AL", "36104", "01101"),
    State("Alaska", "AK", "99501", "02020"),
    State("Arizona", "AZ", "85004", "04013"),
    State("Arkansas", "AR", "72201", "05125"),
    State("California", "CA", "90014", "06037"),
    State("Colorado", "CO", "80202", "08031"),
    State("Connecticut", "CT", "06103", "09003"),
    State("Delaware", "DE", "19801", "10003"),
    State("Florida", "FL", "32801", "12095"),
    State("Georgia", "GA", "30303", "13121"),
    State("Hawaii", "HI", "96813", "15003"),
    State("Idaho", "ID", "83702", "16001"),
    State("Illinois", "IL", "60603", "17031"),
    State("Indiana", "IN", "46204", "18097"),
    State("Iowa", "IA", "50309", "19153"),
    State("Kansas", "KS", "66603", "20191"),
    State("Kentucky", "KY", "40202", "21111"),
    State("Louisiana", "LA", "70112", "22071"),
    State("Maine", "ME", "04330", "23025"),
    State("Maryland", "MD", "21201", "24510"),
    State("Massachusetts", "MA", "02116", "25025"),
    State("Michigan", "MI", "48226", "26163"),
    State("Minnesota", "MN", "55101", "27123"),
    State("Mississippi", "MS", "39201", "28127"),
    State("Missouri", "MO", "63101", "29189"),
    State("Montana", "MT", "59601", "30049"),
    State("Nebraska", "NE", "68508", "31109"),
    State("Nevada", "NV", "89101", "32003"),
    State("New Hampshire", "NH", "03301", "33013"),
    State("New Jersey", "NJ", "08608", "34021"),
    State("New Mexico", "NM", "87501", "35049"),
    State("New York", "NY", "10001", "36061"),
    State("North Carolina", "NC", "27601", "37183"),
    State("North Dakota", "ND", "58501", "38007"),
    State("Ohio", "OH", "43215", "39049"),
    State("Oklahoma", "OK", "73102", "40109"),
    State("Oregon", "OR", "97204", "41051"),
    State("Pennsylvania", "PA", "19102", "42101"),
    State("Rhode Island", "RI", "02903", "44007"),
    State("South Carolina", "SC", "29201", "45079"),
    State("South Dakota", "SD", "57104", "46099"),
    State("Tennessee", "TN", "37203", "47157"),
    State("Texas", "TX", "78701", "48453"),
    State("Utah", "UT", "84101", "49035"),
    State("Vermont", "VT", "05602", "50023"),
    State("Virginia", "VA", "23219", "51760"),
    State("Washington", "WA", "98104", "53033"),
    State("West Virginia", "WV", "25301", "54055"),
    State("Wisconsin", "WI", "53703", "55079"),
    State("Wyoming", "WY", "82001", "56021"),
]